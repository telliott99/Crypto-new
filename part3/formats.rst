.. _part3/formats:

###############
RSA key formats
###############

There are a number of different RSA key formats that you might run into.

- ``OPENSSH PRIVATE`` (OpenSSH format)
- ``RSA PRIVATE/PUBLIC KEY`` (PKCS1)
- ``PRIVATE/PUBLIC KEY`` (PKCS8, may be ENCRYPTED)
- ``SSH2 PRIVATE/PUBLIC KEY`` (RFC4716)

So far as I know, despite contrary OpenSSH usage, these are all technically PEM format (i.e. base64-encoded, with a first line BEGIN XXX), except the OpenSSH public key which starts ssh-rsa.

Even though it's base64-encoded the first public key "ssh-rsa" is not PEM format because it doesn't have the "BEGIN XXX" part.

And they can be distinguished by the first line.

-------
OpenSSH
-------

::

    ssh-keygen -f kf

- -----BEGIN OPENSSH PRIVATE KEY-----
- ssh-rsa

The first is the first line of the private key, and the second is the public one.  The private key is a propietary format.

According to the man pages for ``keygen``:

These are "keys for use by SSH protocol version 2...For keys stored in the newer OpenSSH format, there is also a comment field in the key file that is only for convenience to the user to help identify the key."

So this suggests there is an older and a newer OpenSSH format.

SSH v. 2 is described in RFC4253.  Docs here:  https://tools.ietf.org/html/rfc4253#section-6.6

Discussion:  https://blog.oddbit.com/post/2011-05-08-converting-openssh-public-keys/

Regardless of format, the ``openssl`` utility will not read them.

::

    openssl rsa -text -in kf

Output:

::

    unable to load Private Key

-----
PKCS1
-----

::

    ssh-keygen -f kf.pub -e -m pem

convert an OpenSSH public key to PKCS1 format:

- -----BEGIN RSA PUBLIC KEY-----

which is officially PKCS #1.  

(Often called PKCS1, because of some technical restriction on the ``#`` symbol).

According to the internet, a PKCS1 public key looks like this:

::

    RSAPublicKey ::= SEQUENCE {
        modulus           INTEGER,  -- n
        publicExponent    INTEGER   -- e
    }

According to the man page for ``ssh-keygen``, in the section on the flag -m key_format, there are three supported formats:

- RFC4716
- PKCS8 (PEM PKCS8 public key)
- PEM (PEM public key)

The last is PKCS1 which we saw above.

-----
PKCS8
-----

::

    > ssh-keygen -f kf.pub -e -m pkcs8
    -----BEGIN PUBLIC KEY-----

-------
RFC4716
-------

One description of the RFC4716 format is [here](https://tools.ietf.org/html/rfc4716).  A distinguishing characteristic is

::

    ---- BEGIN SSH2 PUBLIC KEY ----


- says:  BEGIN/END SSH2 PUBLIC KEY
- there are four dashes plus a space
- may be preceded by Comment: and Subject lines
- line length is 70 (required <= 72 bytes)
- line termination character can be native
- the key data is base64-encoded
