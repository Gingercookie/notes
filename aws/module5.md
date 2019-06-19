# Module 5 - Networking Part 1

## Virtual Private Cloud (VPC)
Private network space in the cloud. Allows for logical isolation for workloads (dev/qa environments, for example). Each VPC allows for it's own access controls and security settings.

Tenancy is shared by default but can be dedicated.

You specify a CIDR block for private IPs that you use for internal addressing. IPv6 CIDR block is optional (assigned to you), but must have IPv4 CIDR block.

A VPC is unique to your account. One account can own many VPCs, however.

For a small org, a single VPC may be enough, or a single AWS account with multiple VPCs. For larger orgs, it is common to see multiple AWS accounts, each owning one or more VPCs. This allows for greater separation of duties (Delivery team owns "prod" account/VPCs and SWE owns the "dev" account/VPCs)

There is a soft limit of 5 VPCs per region, per account, but you can request more.

## Subnets
It seems like the way these are used is functionally very similar to on-prem VLANs.
You can carve up your VPC into multiple subnets. Each subnet will reside on a single availability zone.
Amazon reserves the first four and the last IP address in each subnet block you create.

#### Public Subnets
A 'public subnet' is a subnet that is routable over the internet. There doesn't even have to be anything deployed to that subnet.

In order to have a public subnet, you need to have a routing table entry that routes to an internet gateway to support public inbound/outbound connections.

Unless this condition is met, everything else is a private subnet.

#### Protected Subnets
In certain circumstances where data is extremely sensitive and cannot be connected directly or indirectly to the internet, that subnet may be designated 'protected'.

## Gateways

#### Internet Gateway
Gateways allow communication between your VPC and the internet. It is horizontally scaled, highly redundant and available device. It scales automatically, so we don't have to worry about it.

In a route table, you assign the gateway as the target to allow for internet connections.

The gateway also provides NAT for instances that have public IPv4 addresses.

#### NAT Gateway
- Enable instances in a private subnet to initiate outbound traffic to the internet
- Prevent private instances from receiving inbound traffic from the internet.

This NAT gateway must then route to the internet gateway to allow this. Because of this, you have to deploy one of these on a public subnet.

## Network Security

#### Security Groups
AWS Firewalls.

By default, a security group allows inbound connections from any other machine on the same security group, and outbound connections anywhere.

#### Routing Tables
A route table is a set of rules, called routes that are used to determine where traffic can be directed. They look like firewalls.

When you create a VPC, it automatically has a main route table that allows all local traffic. Meaning, all things in the VPC can talk to all other things within the same VPC.

#### Network Access Control Lists (NACLs)
By default, there is just one rule that allows all traffic.
