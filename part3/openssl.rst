.. _part3/openssl:

#######
OpenSSL
#######

As we said last time, standard key formats include:

- OPENSSH PRIVATE (OpenSSH format)
- RSA PRIVATE/PUBLIC KEY (PKCS1)
- PRIVATE/PUBLIC KEY (PKCS8, may be ENCRYPTED)
- SSH2 PRIVATE/PUBLIC KEY (RFC4716)

All of these are PEM-encoded save the OpenSSH Public key, which doesn't meet the standard first line "BEGIN XXX".

And, also we said that:

::

    ssh-keygen -N "" -f kf

gives a new key in OpenSSH format.

``ssh-keygen`` can convert to other formats with ``-e -m``, but only the public keys.

----------  

**OpenSSL** can also be used to generate RSA keys.

::

    openssl genpkey -algorithm rsa -out kf.pem

which has the first line:

::

    -----BEGIN PRIVATE KEY-----

This is PKCS8.  Other options include size and text output (including the modulus and so on).

::

    -pkeyopt rsa_keygen_bits:2048
    -text

Using ``-text``with ``genpkey``

::

    > openssl genpkey -algorithm rsa -text      
    .............................+++
    .................+++
    -----BEGIN PRIVATE KEY-----
    MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDML5loXhr+lCXN
    ..
    -----END PRIVATE KEY-----
    Private-Key: (2048 bit)
    modulus:
        00:cc:2f:99:68:5e:1a:fe:94:25:cd:b0:85:19:69:
        ..      
    publicExponent: 65537 (0x10001)
    privateExponent: ..
    prime1: ..
    prime2: ..
    exponent1: ..
    exponent2: ..
    coefficient: ..

Can we use ``-text`` to get these values for a pre-existing key?  When I run

::

    openssl rsa -text -in kf.pem

where there is an existing key ``kf.pem``, I get output, but it looks different,  Output:

::

    > openssl rsa -text -in kf.pem
    Private-Key: (2048 bit)
    ..
    -----BEGIN RSA PRIVATE KEY-----
    ..

What's going on is that ``openssl rsa`` has read the PKCS8 format and reformatted as PKCS1, and that's why the base64 sections don't match.

However, it will not read the OpenSSH formatted private key.


