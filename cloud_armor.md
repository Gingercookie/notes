# Google Cloud Armor

# Overview
Google Cloud Armor uses policies to match traffic. These are very similar to regular network firewall tables / rules, i.e. the first matching rule is applied, and the rest are ignored. 0 is highest priority and 2147483647 is the lowest priority.

Cloud Armor Premium Tier is preconfigured to apply the ModSecurity Core Rule Set (ModSec CRS) 3.0.2, but even these rules can be tuned to match your specific use case.
There are no pre-configured rules in the Standard Tier.

Cloud Armor affects traffic on external load balancers, so as to stop bad traffic as far away from your resources as possible.
In addition to blocking malicious traffic via security policies, all external load balancers automatically get volumetric protection (DDoS attacks).

#### Requirements for Security Policies
* The load balancer must be external `HTTPS`
* The backend service's load balancing scheme must be `EXTERNAL`
* The backend service's protocol must be one of `HTTP`, `HTTPS`, or `HTTP/2`

#### Weirdness Processing POST requests

Of all the HTTP methods, Google Cloud Armor will only look at and evaluate the body of `HTTP POST` requests.
The `evaluatePreconfiguredExpr()` method is used to evalute the body.
Cloud Armor will decode and evaluate the first 8KB of the body, and then stop.
Content-Type/Content-Encoding such as JSON, XML, Gzip, etc. are not supported.

When processing HTTP POST requests, the header is received and processed first.
If the header is allowed, the header & body are then processed separately.
The body may then be denied afterwards, which would cause the header to be sent through to the backend service (on the initial processing), but the body of the request would be blocked.



# Useful commands

`gcloud compute security-policies ...`

# Links and other resources

[Main Product Page](https://cloud.google.com/armor)
