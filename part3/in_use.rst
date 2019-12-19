.. _part2/in_use:

#########################
Encrypting and decrypting
#########################

Asymmetric coding and decoding:
-------------------------------

::

    echo "hello world" > p.txt
    openssl genpkey -algorithm rsa > kf.private.pem
    openssl rsa -in kf.private.pem -pubout -out kf.public.pem
    openssl rsautl -encrypt -in p.txt -out c.txt -pubin -inkey kf.public.pem
    openssl rsautl -decrypt -in c.txt -inkey kf.private.pem

output:

::

    hello world

Notice:  we must generate the public key in a second step, and then provide the correct key files for encryption and decryption.

or 

::

    openssl rsautl -sign -in p.txt -out c.txt -inkey kf.private.pem
    openssl rsautl -verify -in c.txt -pubin -inkey kf.public.pem

with the same output

--------------------
Symmetric encryption
--------------------

Using random data

::

    echo "hello world" > p.txt
    openssl rand 250 > key
    openssl enc -aes-256-cbc -salt -in p.txt -out c.txt -pass file:./key
    openssl enc -d -aes-256-cbc -in c.txt -out m.txt -pass file:./key
    cat m.txt

output:

::

    hello world
