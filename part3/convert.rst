.. _part3/convert:

###############
Key conversions
###############

--------------
OpenSSH export
--------------

Start by generating a new OpenSSH private key:

::

    ssh-keygen -N "" -f kf.openssh
    -----BEGIN OPENSSH PRIVATE KEY-----

which generates both private and public keys.

To generate/convert a *public key* from the OpenSSH private key

- in SSH2 format (RFC4716)

::

    ssh-keygen -f kf.openssh -e
    ---- BEGIN SSH2 PUBLIC KEY ----

- in PEM (that is, PKCS1) format

::

    ssh-keygen -f kf.openssh -e -m pem
    -----BEGIN RSA PUBLIC KEY-----

- in PKCS8 format

::

    ssh-keygen -f kf.openssh -e -m pkcs8
    -----BEGIN PUBLIC KEY-----

------------

However, the OpenSSH private key is another matter.  One suggested solution is ``putty``.  

https://federicofr.wordpress.com/2019/01/02/how-to-convert-openssh-private-keys-to-rsa-pem/

I got ``putty`` from Homebrew.

::

    puttygen kf.openssh -O private-openssh -o kf.pkcs1
    -----BEGIN RSA PRIVATE KEY----

---------------
PKCS1 to/from 8
---------------

1 -> 8

::

    openssl pkcs8 -topk8 -inform PEM -outform PEM \ 
    -nocrypt -in kf.pkcs1 -out kf.pkcs8
    -----BEGIN PRIVATE KEY-----

The ``-topk8`` flag means "read traditional format private key and write PKCS8."

One can verify the same info in the pkcs1 and pkcs8 versions with 

::

    openssl rsa -text -in kf.pkcs1
    openssl rsa -text -in kf.pkcs8

8 -> 1

Also, the latter outputs PKCS1 format(even starting from PKCS8) as well as the modulus, etc.

Although the above won't read an OpenSSH key, because of the data length markers, it's easy to find the pieces in the OpenSSH key.  So for example, I find

- OpenSSH, first part of the modulus

::

    b70ca0491e6c4b48615b89a23c84158bd629546c916f872e

- openssl rsa output:

::

    Private-Key: (2048 bit)
    modulus:
    00:b7:0c:a0:49:1e:6c:4b:48:61:5b:89:a2:3c:84:
    15:8b:d6:29:54:6c:91:6f:87:2e:67:c7:41:6f:d2:

That looks like it all matches up.

--------------
OpenSSH import
--------------

::

    ssh-keygen -i -f kf -m pkcs8
                        pem


Chokes on the ones I tried.


