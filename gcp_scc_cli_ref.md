Initial settings
```
PROJECT=gcp-project
ORG=$(gcloud organizations list --uri | cut -d / -f 6)
```

Issues in the SCC with "Ignore" flag set *will* be shown. Without setting any filters, the results you get in the CLI should be consistent with the GUI / Console view.

List all active findings by severity
```
FILTER='severity="CRITICAL" AND state="ACTIVE"'

gcloud scc findings list ${ORG} \
  --filter="${FILTER}" \
  --format=json |
  jq '.[].finding.category' |
  sort | uniq -c | sort -r
```


Useful fields to jq filter within response

```
[].finding.category
[].finding.severity
[].finding.sourceProperties.Container_Name
[].finding.sourceProperties.Container_Image_Uri
```

I typically define my filter and pull it into a jq_json.json file, then cat that file with my additional JQ filters so that I'm not making a huge number of requests, and just searching the output after the fact.

cat jq_json.json | jq '.[] | {
  Category: .finding.category,
  Severity: .finding.severity,
  Container: .finding.sourceProperties.Container_Name,
  Image: .finding.sourceProperties.Container_Image_Uri,
  Created: .finding.createTime}'
