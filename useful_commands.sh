# Sed replace things
grep title custom_roles.tf | cut -d '"' -f 2 | while read i; do new=$(echo $i  | sed -e "s/\([A-Z][a-z]\)/_\1/g" -e "s/__/_/g" -e "s/-/_/g"| tr "[A-Z]" "[a-z]") ; echo "$i > $new"; sed -i -e "s/$i/$new/g" custom_roles.tf | grep -E "$i|$new"; done

#####################
## Gcloud commands ##
#####################


###############
## Terraform ##
###############
# Show just the "change" lines in a terraform plan
grep -e "^.*#.*\([^blue]\|green\).*\(created\|destroyed\|replaced\|updated\)" tf_output

###########################################
## Import all project-level custom roles ##
###########################################
project=${project}
dir=modules/$project/iam
module=module.redacted

# Loop import of custom roles

# List all custom roles and write into a file called "custom_roles_out"
gcloud iam roles list --project=${project} --format="value(name)" > custom_roles_out

# Create defintion stubs for all custom roles in "custom_roles.tf". These will be blown up and replaced when copying from tf state show
cat custom_roles_out | while read role; do echo -e "resource \"google_project_iam_custom_role\" \"$(basename $role | tr '.' '_')\" {\n\n}\n"; done > $dir/custom_roles.tf

# Loop through each role and do a tf import of that resource, then copy the "tf state show" of those resources into "custom_roles.tf"
cat custom_roles_out | while read role; do terraform import $module.google_project_iam_custom_role.$(basename $role | tr '.' '_') "${project} $role"; done
cat custom_roles_out | while read role; do tf state show -no-color $module.google_project_iam_custom_role.$(basename $role | tr '.' '_'); done > $dir/custom_roles.tf
rm custom_roles_out

#######################################
## Import all project-level bindings ##
#######################################

# Get all project-level roles (excluding inherited) and write to "roles_out"
gcloud projects get-iam-policy ${project} --format=json | jq '.bindings[].role' -r > roles_out

# For each role in roles_out, create a binding resource definition in a file
# called "project_bindings.tf", replacing "." with "-" in role name
cat roles_out | while read role; do echo -e "resource \"google_project_iam_binding\" \"$(basename $role | tr '.' '_')\" {\n\n}\n"; done > $dir/project_bindings.tf

# For each role in roles_out, do a terraform import of that role,
# replacing "." with "-" in role name
cat roles_out | while read role; do terraform import $module.google_project_iam_binding.$(basename $role | tr '.' '_') "${project} $role"; done

# Copy contents of tf state show into the project_bindings.tf file.
# Should be a better way to do this without recreating file, but it works???
cat roles_out | while read role; do binding=$(basename $role | tr '.' '_'); tf state show -no-color $module.google_project_iam_binding.$binding; done > $dir/project_bindings.tf
rm roles_out

########################################################################
## Show firewall rules for all projects with source range = 0.0.0.0/0 ##
########################################################################
for p in $(gcloud projects list --format="value(projectId)" | grep -vE "^sys-"); do
  echo "[[$p]]" ;
  timeout 5 gcloud compute firewall-rules list --format="table(
                name,
                allowed[].map().firewall_rule().list():label=ALLOW
            )" --filter="sourceRanges=(0.0.0.0/0)";
  echo
done

## View shieldedInstanceConfig for each instance template
for i in $(gcloud compute instance-templates list --format="value(name)"); do echo "Config for template $i"; gcloud compute instance-templates describe $i --format=json| jq '.properties.shieldedInstanceConfig'; done;
