# AWS Foundations

## Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password.

tags: Identity and Access Management

* Load credentials report.
* Find users in credential report with:

     | Field            | Value              |
     |------------------|--------------------|
     | password_enabled | true,not_supported |
     | mfa_active       | false              |

## Ensure Single Sign-On (SSO) is enabled and integrated with CFPB's Okta Identity-as-a-Service (IDaaS).


tags: Account Management

* Add test step details here!


## Avoid the use of the "root" account.

tags: Identity and Access Management

* Add test step details here!


## Ensure credentials unused for 90 days or greater are disabled.

tags: Identity and Access Management

* Add test step details here!


## Ensure access keys are rotated every 90 days or less.

tags: Identity and Access Management

* Add test step details here!


## Ensure IAM password policy requires at least one uppercase letter.

tags: Identity and Access Management

* Managed Config Rule "IAM_PASSWORD_POLICY" must be enabled
* Managed Config Rule "IAM_PASSWORD_POLICY" parameters must "contain":

     | Parameter                  | Value |
     |----------------------------|-------|
     | RequireUppercaseCharacters | true  |


## Ensure IAM password policy require at least one lowercase letter.

tags: Identity and Access Management

* Managed Config Rule "IAM_PASSWORD_POLICY" must be enabled
* Managed Config Rule "IAM_PASSWORD_POLICY" parameters must "contain":

     | Parameter                  | Value |
     |----------------------------|-------|
     | RequireLowercaseCharacters | true  |


## Ensure IAM password policy require at least one symbol.

tags: Identity and Access Management

* Managed Config Rule "IAM_PASSWORD_POLICY" must be enabled
* Managed Config Rule "IAM_PASSWORD_POLICY" parameters must "contain":

     | Parameter                  | Value |
     |----------------------------|-------|
     | RequireSymbols             | true  |


## Ensure IAM password policy require at least one number.

tags: Identity and Access Management

* Managed Config Rule "IAM_PASSWORD_POLICY" must be enabled
* Managed Config Rule "IAM_PASSWORD_POLICY" parameters must "contain":

     | Parameter                  | Value |
     |----------------------------|-------|
     | RequireNumbers             | true  |


## Ensure IAM password policy requires minimum length of 14 or greater.

tags: Identity and Access Management

* Managed Config Rule "IAM_PASSWORD_POLICY" must be enabled
* Managed Config Rule "IAM_PASSWORD_POLICY" parameters must "contain":

     | Parameter                  | Value |
     |----------------------------|-------|
     | MinimumPasswordLength      | 14    |


## Ensure IAM password policy prevents password reuse.

tags: Identity and Access Management

* Managed Config Rule "IAM_PASSWORD_POLICY" must be enabled
* Managed Config Rule "IAM_PASSWORD_POLICY" parameters must "contain":

     | Parameter                  | Value |
     |----------------------------|-------|
     | PasswordReusePrevention    | 24    |


## Ensure IAM password policy expires passwords within 90 days or less.

tags: Identity and Access Management

* Managed Config Rule "IAM_PASSWORD_POLICY" must be enabled
* Managed Config Rule "IAM_PASSWORD_POLICY" parameters must "contain":

     | Parameter                  | Value |
     |----------------------------|-------|
     | MaxPasswordAge             | 90    |


## Ensure no root account access key exists.

tags: Identity and Access Management

* Managed Config Rule "IAM_ROOT_ACCESS_KEY_CHECK" must be enabled


## Ensure security questions are registered in the AWS account.

tags: Identity and Access Management

* Add test step details here!


## Ensure IAM policies are attached only to groups or roles.

tags: Identity and Access Management

* Add test step details here!


## Ensure contact details are up to date.

tags: Identity and Access Management

* Add test step details here!


## Ensure Security contact information is registered. 

tags: Identity and Access Management

* Add test step details here!


## Ensure IAM instance roles are used for AWS resource access from instances. 

tags: Identity and Access Management

* Add test step details here!


## Ensure a support role has been created to manage incidents with AWS Support.

tags: Identity and Access Management

* Add test step details here!


## Do not setup access keys during initial user setup for all IAM users that have a console password. 

tags: Identity and Access Management

* Add test step details here!


## Ensure IAM policies that allow full "*:*" administrative privileges are not created.

tags: Identity and Access Management

* Add test step details here!


## Ensure CloudTrail is enabled in all regions.

tags: Logging

* Add test step details here!


## Ensure CloudTrail log file validation is enabled.

tags: Logging

* Add test step details here!


## Ensure the S3 bucket used to store CloudTrail logs is not publicly accessible.

tags: Logging

* Add test step details here!


## Ensure CloudTrail trails are integrated with CloudWatch Logs.

tags: Logging

* Add test step details here!


## Ensure AWS Config is enabled in all regions.

tags: Logging

* Add test step details here!


## Ensure S3 bucket access logging is enabled on the CloudTrail S3 bucket.

tags: Logging

* Add test step details here!


## Ensure CloudTrail logs are encrypted at rest using KMS CMKs.

tags: Logging

* Add test step details here!


## Ensure rotation for customer created CMKs is enabled.

tags: Logging

* Add test step details here!


## Ensure VPC flow logging is enabled in all VPCs. 

tags: Logging

* Add test step details here!


## Ensure a log metric filter and alarm exist for unauthorized API calls.

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for Management Console sign-in without MFA.

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for usage of "root" account . 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for IAM policy changes. 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for CloudTrail configuration changes. 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for AWS Management Console authentication failures. 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for disabling or scheduled deletion of customer created CMKs. 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for S3 bucket policy changes. 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for AWS Config configuration changes. 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for security group changes. 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for changes to Network Access Control Lists (NACL). 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for changes to network gateways. 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for route table changes. 

tags: Monitoring

* Add test step details here!


## Ensure a log metric filter and alarm exist for VPC changes. 

tags: Monitoring

* Add test step details here!


## Ensure no security groups allow ingress from 0.0.0.0/0 to port 22. 

tags: Networking

* Add test step details here!


## Ensure no security groups allow ingress from 0.0.0.0/0 to port 3389. 

tags: Networking

* Add test step details here!


## Ensure the default security group of every VPC restricts all traffic. 

tags: Networking

* Add test step details here!


## Ensure routing tables for VPC peering are "least access".

tags: Networking

* Add test step details here!


## All logs shall be forwarded to CFPB's Security Information and Event Management (SIEM) server.

tags: Audit and Accountability

* Add test step details here!


## Logging must be enabled according to CFPB policy, in order to audit the following:
a. identity of each user and device accessing or attempting to access an information system; 
b. time and date of the access and the logoff; and
c. activities that might modify, bypass, or negate information security safeguards. 
d. all remote connections.
e. security-relevant actions associated with processing based on a risk assessment and mission/business needs.

tags: Audit and Accountability

* Add test step details here!


## All privileged users identified as administrators must be documented and delegated a selected IAM role.

tags: Account Management


* Add test step details here!


## All Identity-based policies (IAM policies) shall be documented and approved by the system owner.

tags: Audit and Accountability


* Add test step details here!


## User- or group-based permissions policies shall not be used for any IAM policy (role-based permissions policies should be used).

tags: Access Control


* Add test step details here!


## Ensure that data backup is performed at required intervals in accordance with CFPB policy

tags: Backup and Recovery

* Add test step details here!


## Ensure the Bureau's IT contingency planningis applied where applicable. 

tags: Contingency Planning

* Add test step details here!

