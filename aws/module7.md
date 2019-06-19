# Module 7 - Identity and Access Management (IAM)

When you first create an AWS account, you have one user. The AWS account root user. This user has full access to all AWS services and all account settings.

AWS recommends using not using the AWS root account for day-to-day activities. You should create an IAM "admin" user, then lock away the root account credentials where they are seldom used or accessed. Then you should use the admin user to create other IAM users with less and less privileges based on business purpose. Even this IAM "admin" user should probably not be used for "day-to-day" activities.

## IAM Principals
A principal is an entity that can take some action on AWS. This could be an AWS IAM user, an AWS service (like EC2), a SAML provider, or an Identity Provider (IdP).

Instead of using IAM to create users and provision access, you can use an external IdP to do this, and then manage that IdP within IAM. If you have a separate IdP or something that's already configured/convenient, this can be an easy way to port your own IAM to the cloud.

## IAM Users
IAM Users are not separate accounts. They are separate principals within your account.

When an IAM user is created it has nothing other than metadata. It has no credentials for someone to use for login. It has no permissions to perform any kind of action. After you create an IAM user, you must first assign it credentials before anyone can log in, and then assign permissions to that user so it can do things.

## IAM Policies
An IAM Policy is an entity that, when attached to an identity or resource, defines the permissions of that other entity. AWS evaluates policies when a principal makes a request (attempts to take some action).

IAM Policies only control access to AWS services, and *they have no visibility beyond that*. If you need access control at the OS layer, you will need to use LDAP, SAML, or something that provides OS-level access control.

When AWS evaluates permission for a principal, it first checks to see if there is an explicity 'deny' rule for the action. If there is no explicit deny, then it checks for an explicit 'allow'. If there is no explicit allow, then access is denied.

#### Types of Policies
Identity-based policies - policies that you write and attach to an identity. These are like user permissions. They define what kind of access the identity has, and what kind of actions they can perform.

Resource-based polices - policies that you write and attach to a resource. These are like ACLs for a specific object. They define who can access the object and how they can interact with it. We have already seen a resource-based policy with the S3 storage we used before.

Managed policies - policies that you can attach to multiple principals. There are 'AWS managed' and 'customer managed' policies.

Inline policies - Policies that you write and directly attach to a single principal or resource. All resource-based policies are inline.

## IAM Roles
IAM Roles are a defined set of permissions that are required for a user to access a resource or service. They are one way to allow a user to temporarily change their access. They eliminate the need to create multiple accounts for a single user.

A user or entity can assume a role. When a user assumes a role, that user's existing permissions are temporarily forgotten until the role is 'unassumed'. AWS Services (like EC2) can assume a role at run-time.

There are two parts to an IAM role.
1. Trust policy - this defines which entities can assume the role.
2. Access policy - the permissions associated with a role.

The principal can also be an IAM group, or an external IAM role for an account which you do not own. This mean you can easily use IAM roles in conjunction with an external IdP (your own corporate IdP, or 3rd parties, for example). When the external user authenticates, the AWS IAM role assigns them temporary credentials based on their access.

## Amazon Cognito

Cognito is a fully managed authentication, authorization, and access management service.
