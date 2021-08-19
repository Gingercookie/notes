## Cross Site Request Forgery (CSRF)

Cross Site Request Forgery (CSRF) is an exploit that executes unwanted actions
on a user's behalf, without their knowledge.

This works by an attacker generating a malicious HTTP request and tricks the
victim into accidentally submitting this request. The malicious request will
inherit the identity (and thus permissions) of the victim user and execute
as a normal request from the user.

Typically, the attacker is not able to directly view the response of the
request, so the malicious requests are state-changing (POST). The usual
example is to order something, send money from victim's bank, change the
victim's password... Anything that changes state really.

#### How to Perform
1. Wait for an user to be authenticated to the target website
2. Send a malicious link to the user
    www.bank.com/transfers&action=send&target=1234578&amt=9999
   but disguise the link as something benign
   <a href=<malicious link> cute dog pictures!/>
3. When the user clicks the link, a request will be sent from their
    browser, using the already authenticated session they had open. The
    link will be processed as if coming from a legitimate request.

Another, trickier, way to present the malicious URL to a victim is to
include a 0x0 pixel image in an email, website, etc and embed the URL
within the src property of the image. The browser or email client will
automatically attempt to download the image from the indicated source,
and the user will never even realize what's happening.

#### How to defend against CSRF
1. Confirmation

    The simplest way to defend against this kind of attack is to ask for user
    confirmation on all state-changing actions (or at least the ones that may
    have severe consequences). This way, when the server gets the rogue HTTP
    request, it will send a confirmation response before doing any actual
    processing.

2. CSRF Token

    Another way to mitigate these attacks is to append a unique identifier
    to the HTTP request. This identifier should be a hidden form field on the
    web page itself and randomly generated from a PRNG. The attacker would
    thus have no knowledge of the hidden identifier, and the request would
    be seen as a fake. No further action is taken.

    CSRF Token Implementation Checks
    1. Form submission fails without token
    2. New token for each form  
    3. Random token each time
    4. Token not in URL
    5. Check generating algorithm if not standard
