# Pentest Team DEFCON presentation
## RFID

## Magstripes in cards
The magnetic stripe on your card is the same as a cassette, and is a record of
a clip of audio.

Samsung pay works for card readers that don't support electronic cards, because
the app is actually replaying the magnetic field of the card, directly into
the space around the reader.

## CMD & CTRL
#### Graffiti website (retail store)
- Make an account, upload pictures, make them private or public.
- Vuln existed to view other users' private pictures and make them public.
- Able to upload a shell, but not able to actually use the shell. haha.

#### Financial website

## Exploiting CI and Automated Build systems

## Automation and Commoditization of infosec
- Many security jobs are at risk of being automated, or done for really cheap
- Continue to educate yourself, not

## Containerization (Docker & Kubernetes)
- A couple people went to this workshop and it turned out to be pretty bad, so
they just left.
- It was very basic, and consisted mainly of creating a container and spinning
it up.

## A new era of SSRF
- Server-side request forgery
- Bypasses the firewall and it reaches the intranet
- Therefore, able to compromise internal services

Vulnerabilities exist within different URL parsing libraries, because they all
do it differently. You can craft malicious URLs because the libraries do not
conform to the RFC perfectly.

You are especially vulnerable to this if you use different parsing libraries
within one project.

cURL is vulnerable to some things, which is too bad, because it's very common.

Example: `http://127.0.0.1:11211#@google.com/`
The parser could say yes this is valid, because the request is coming from
google.com. However, if you use cURL to grab the resource, it will fetch the
localhost resource instead.

Lesson learned: use the same standards and same parsing libaries consistently
within an application.

## Phone System Testing and Other Fun Tricks
There are a lot of different protocols and codecs, and if you want to attempt
this, you should be familiar with a handful of them, because they do differ.

The meat of the risk here is "Security Misconfiguration and Sensitive Data
Exposure". Basically, you can get internal confidential data leaked by spoofing
internal phones.

## Lockpicking village CTF
5 different levels of lockpicking, but alex forgot to bring his whole set of
picks

## Edge Cases in Web Hacking (NVisium)
#### Server-side template injection
- The ability to manipulate the structure of a template through the unsafe
inclusion of user-input.
- Use {{ 8*8 }} in a user-input field to see if the server evaluates that
expression. If it does, it's vulnerable and you can access different config
variables, classes, and some level of remote control.

#### Serialization Vulnerabilities
Serialization by itself is not a security concern, but the implementation
often introduces vulns.

Python deserialization lib "Pickle" is very unsafe.

## Breaking the x86 Instruction Set Architecture
We do so much security review and audit process for software, but we don't do
any of this for hardware.. Why?

Instructions can be either one byte, or 15 bytes. So there are roughly
1.3*10^36 possible x86 instructions.

## Crypto & Privacy Village CTF
I participated in this! It was fun.

## Demystifying Kernel Exploitation by Abusing GDI Objects
