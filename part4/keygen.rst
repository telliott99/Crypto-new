.. _part3/keygen:

##############
Key generation
##############

-------
OpenSSH
-------

Probably the most common way to generate RSA keys is to use the ``ssh-keygen`` utility:

.. code-block:: bash

    ssh-keygen
    
Common flags include:

- ``[-b bits]``
- ``[-t dsa | ecdsa | ed25519 | rsa]``
- ``[-N new_passphrase]``
- ``[-f output_keyfile]``

The defaults are 2048 bits and RSA.  It will prompt for a passphrase (which can be empty ``""``) and for an output file path, which is suggested to be ``.ssh/id_rsa`` plus the same with ``.pub``.

--------
Examples
--------

::

    > ssh-keygen -N "" -f kf
    Generating public/private rsa key pair.
    Your identification has been saved in kf.
    Your public key has been saved in kf.pub.
    The key fingerprint is:
    SHA256:Qom284Cw07VyzyAPJ3CZds+ssIFXF44XHN2HL/qBx/U telliott@newmini.local
    The key's randomart image is:
    +---[RSA 2048]----+
    |     .+o . .     |
    |   o +.+. o .    |
    |o = B *    o     |
    | O * X    . o    |
    |+ @ O = S+ o .   |
    | o % O .o +   E  |
    |  . o +  o .     |
    |          .      |
    |                 |
    +----[SHA256]-----+

**kf**

::

    -----BEGIN OPENSSH PRIVATE KEY-----
    ..
    
**kf.pub**

::

    ssh-rsa
    ..

This private key said to be OpenSSH format, but it is really already PKCS1.

------
Export
------

- ``-e`` This option will read a private or public OpenSSH key file and print to stdout a public key in one of the formats specified by the ``-m`` option. The default export format is “RFC4716”.

::

    ---- BEGIN SSH2 PUBLIC KEY ----

To get PKCS1

::

    ssh-keygen -f kf.pub -e -m pem

will convert the public key in file ``key.pub`` into PKCS1 format, and print it to standard out.  

::

    -----BEGIN RSA PUBLIC KEY-----

Using the ``-e -m`` flags:

::

    ssh-keygen -f kf.pub -e -m pem > kf.pub.pem

saves the new key.

None of these is read by ``openssl rsa``.

------
Import
------

- ``-i`` This option will read an unencrypted private (or public) key file in the format specified by the -m option and print an OpenSSH compatible private (or public) key to stdout.

Only this one worked so far:

::

    ssh-keygen -i -f kf.pub.pem -m pem

RFC4716 is supposed to work.  

