## JOSE and JWT
_TL;DR - JWT is bad for sessions; okay for one-time use auth._


Let's start off with a couple of definitions
- _JOSE - Javascript Object Signing and Encryption_
- _JWT - JSON Web Token_
- _JWS - JSON Web Signatures_
- _JWE - JSON Web Encryption_

Most people are complaining about the use of JWTs, but let's be clear. JWTs are
a _type_ of JOSE, since they are Javascript Objects (JSON).

#### Forging Tokens (round 1)
Part of the RFC defines a "none" algorithm to be used for an _unsecured JWS_.
An unsecured JWS should only be used in a scenario where integrity protection
is not required. Implementations should not accept unsecured JWSs by default
as valid.
Unfortunately, the "none" algorithm is one of two algorithms that is considered
mandatory to implement - the other algorithm is HS256 (this is a symmetric key
scheme, and will be important in a minute).

_However_, some JWT libraries treat JWT's with the alg set to "none" as a valid
token without actually verifying anything. This allows an attacker to forge
a JWT, with `"alg": "none"` and `signature = ""`, and the implementation may
treat it as a valid token.

_How to mitigate_

- Explicitly check for and deny tokens with the "none" algorithm set. This may
have to be outside of your JWT library.
- If you expect a signed token (you should), attempt to verify the token like
normal. If it fails verification (because there is no signed part of the
token), throw away the token.

#### Forging Tokens (round 2)
Conveniently, the JWT spec has allowed us to use either symmetric or asymmetric
keys to sign our tokens. Also conveniently for hackers, they have allowed us
to specify the signing algorithm with the "alg" claim.
For asymmetric schemes, the private key is used to sign and the public key to
verify. For symmetric schemes, the same key is used for both.

Now, imagine a scenario where a token-issuing server creates and signs tokens
with a set of asymmetric keys. Because we are required by the RFC to implement
HS256 (same key signs and verifies). The attacker can then forge a token and
use the server's public key to sign it, but claim that the algorithm used to
sign was HS256. That shouldn't work right ? But here's the catch...

_If a server is expecting an RSA signed token, but actually receives
an HMAC'ed token, it will think the public key is actually the HMAC secret key._

Thus, the default implementation of RSA JWTs is vulnerable to token forgery.

_How to mitigate_

The server should know what kind of signature to expect (and thus which key to
use to verify the token). The `verify(...)` method of your JWT library should
include an argument to specify what kind of algorithm was expected. If the
algorithm doesn't match what you expect, throw away the token.

If your library doesn't support this, then you can decode and verify that the
"alg" claim in the token is what you expect before you verify, and trust, the
token.

If you need to use multiple keys (for compatibility), use a separate key for
each algorithm, and set the "key ID" field appropriately. You can then decode
and check both the "algorithm" and "keyid" claims to make sure they are what
you expected.

#### Insecurity of JWE Algorithms
- RSA with PKCS #1v1.5 Padding

    This has been vulnerable since 1998.
- RSA with OAEP Padding

    Likely secure, but does not have a complete mathematical proof.
- ECDH-ES

    Vulnerable to invalid curve attacks. This could be mitigated trough the
    use of secure elliptic curves, but would become non-compliant with the RFC.
- AES-GCM

    ?
