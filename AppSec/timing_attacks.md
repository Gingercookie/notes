# Timing Side-Channel Attacks

This whole attack is based on the way that strings are compared in php's
`memcmp()` and `is_identical()` functions,
which are used virtually everywhere to compare strings (for hashes,
secrets, passwords, etc...).

### `is_identical()`

This function compares the string lengths. If the two strings are different
lengths, it exists immediately. This means that it does more work to compare
strings of the same length than it does to compare string of different lengths.
Great, using a sample size of about 50,000 queries, we have confidence in the
length of the secret.

Once it compares our strings and finds two that have the same length, the
function continues and makes a call to `memcmp()`...

### `memcmp()`

The function compares character by character, and exits the function as soon as
it finds a character that does not match. This means that if we try every
letter of our alphabet (key-space), then one of those characters will match
and proceed to look at the second character, taking more time than any other.
Once we have determined what the first character is, we do this all over again
to find the 2nd, 3rd, ... nth character of the secret, up to our previously
determined length. After some time, the secret will be found.  

### How to Mitigate
Simply by comparing every character in the
strings (even if you know early on that they are not equal), each comparison
call will take the same amount of time, making the attack useless.

You can also mitigate these attacks by limiting the amount of queries in a
given timeframe. The attack requires a huge amount of calls (and queries) to
be made to leak information, so if you stop the amount of calls that can be
made, then you don't leak the information. However, if someone has direct access
to query your database, this will not be effective. 

Because the entire existence of these functions is to make the comparison calls
quicker (and the reason why this attacks works), we will have to trade off
some performance here for security.
