.. _part3/rsa:

###########
OpenSSL rsa
###########

- derive a public key from a private key
- print a key's components in hex
- change from base64 (PEM) to binary (DER)

::

    openssl rsa -in kf

Some flags:

- ``-modulus`` print the modulus (only)``
- ``-out file``
- ``-outform der | net | pem``
- ``-pubin`` read a public key
- ``-pubout`` output a public key
- ``-text`` print the private key components in plain text

--------
Examples
--------

::

     openssl rsa -in kf -pubout -out kf.pub

Output a public key PKCS8.

::

    > openssl rsa -in kf -pubout             
    writing RSA key
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA10R1rteU0JcuA74UEUoy



Print key components:

::

     openssl rsa -in kf -text

Output

::

    Private-Key: (2048 bit)
    modulus:
    00:d7:44:75:ae:d7:94:d0:97:2e:03:be:14:11:4a:
    ..

This utility will not read any of the OpenSSH keys, private or public, PKCS1 or not.