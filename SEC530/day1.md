# Day 1

### Course Goals
* Design, build, harden network, infra, and apps
* Architect to reduce scope and severity of incidents

10 year's experience to be "good" at this.

People with little experience / just coming out of college see everything as an app, and ignore the rest. That is, they only see layer 7, everything else is just magic.

OSI model is a collective imaginary idea used to talk about abstract things. Cellular engineer and home network engineer have different layer 3 but they both have *a* layer 3.

Compliance can be a hindrance to security where they are only trying to pass their "checklist" or get "clean scans".

### Flat networks
Offers little or no internal filtering on Layers 2 (data link), 3 (network), and 4 (transport). Flat networks allow pivot points to the entire rest of the network.
* Simply separating systems on VLANs is not enough. They are a good idea, but they also need filtering in between them
* ACLs, firewalls, etc.. must be in place as well


### Case Study : NotPetya
NotPetya is part of a family of malware based on the (allegedly) leaked NSA hacking tool called ETERNALBLUE. Check out the link on OneNote page (Wired article) about Maersk.
* Targeted Windows Server Message Block (SMB, port 445) and was patched (before the 0-day announced)
* After entering via SMB, start using Mimikatz to steal creds and move laterally
* On a flat network, this will take out *everything*

### Failed Mindsets
* The LAN is secure
* The All-Prevent defense
* PCI Compliance == Security
* We always did it this way
* "Shiny-box Syndrome"


### Red/Blue Asymmetries
Look for things that are *easy* for Blue team to implement, and make the Red team's objective *much harder* .
* Private VLANs - restrict client to client communication

### Goal : Identifying the unknown unknowns
* Known : Things we already know
* Known Unknown : Things we know that we don't know
* Unknown unknown : Things we aren't even remotely aware of


### Layer 2 and 3 for as many hours
ZZzzzzzz....

CAM

VLAN Trunking?

A lab about reading pcaps

Zach stole a private key...

Don't use Telnet

Bro/Zeek... NetFlow...

# Quotes
> "One goal, one message"

> "Architecture is meant to communicate a future state"

> "Think *RED* act *BLUE*"

# Impressions
* This guy really likes to talk about VLANs and VLAN filtering
* He doesn't really "tell" you what he's talking about, he just talks about it. He doesn't stick to the slides either. This makes it hard to follow along and take notes, but it makes it easy to listen to.
