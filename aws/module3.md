# Module 3 - Computing

## AWS Elastic Compute Cloud (EC2)
This is just like your traditional on-prem server. It can support web hosting, applications, databases, authentication, and anything else your would run on a server.

#### Instance Types
t2.large, c5.xlarge, p3.2xlarge, m5.large
- m is the family name
- 5 is the generation number
- large is the size

The coefficient in front of the size describes how much larger. For example an m5.2xlarge is twice as large (and performant) than m5.xlarge. An m5.10xlarge is 10x as large and has 10x the performance of an m5.xlarge.

#### Dedicated Instances and Hosts
- Default - Your instance runs on shared hardware.
- Dedicated Instance - EC2 instances that run in a VPC on hardware which is dedicated to a single customer. They are physically isolated at the host hardware level from other instances. Only accessible by your AWS account, but does not run on specific hardware.
- Dedicated Host - A physical server with EC2 instances that is fully dedicated for your use. Only accessible by your AWS account *and* on a specific piece of hardware of your choosing.

#### Amazon Machine Images (AMIs)

You can launch an AWS EC2 with an Amazon Machine Image (AMI). You must specify one AMI to launch an EC2 instance, and you may launch multiple EC2 instances from one AMI. This may be useful if you want multiple web servers behind a load balancer, for example.

Where to get an AMI?
- Pre-Built - There are a bunch of pre-built AMIs offered by amazon that you can quickly select and run from the 'main menu'
- Marketplace - Digital catalog (for purchase) with thousands of software solutions listed. They are good for specific use-cases.
- Create your own
- Community AMIs - use at your own risk

Amazon's "security group" is virtual firewalling, probably among other things. By default, all AMIs have all ports open, and you manage the firewalling virtually through AWS. If you use firewalls on the machines, they will still get applied, just after the AWS Security Group gets applied.

#### User Data script
This is a script that you can configure when you launch a new EC2 instance, that only runs once. You can use it to update and install software, call home to your config management tool, start httpd and run the web server, or whatever you need it to do.

## AWS Elastic Block Store (EBS)
EBS Storage is directly attached to an EC2 instance, so it provides low latency (compared to S3 for example). They can also be used to back up AMIs and then stored in S3.
EBS persists through shutdowns and provides a way to back up data.

Instance storage is ephemeral. This is physically on a hard drive that is attached to the EC2 instance, and will not persist through shutdown.

## Shared File Systems (EFS/FSx)
- EFS - Linux NFSv4 file system - shared across zones, regions, VPCs, accounts

- FSx - Windows NTFS file system - shared across zones only

EBS attaches only to one instance, so this isn't an option.

S3 doesn't have a true file system. If you make a small change to a file, you have to re-upload the whole file.
