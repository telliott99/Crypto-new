.. _part3/genrsa:

##############
OpenSSL genrsa
##############

------
genrsa
------

``openssl`` has a utility for generating a private key, called ``genrsa``:

.. code-block:: bash

    openssl genrsa -out kf

::

    -----BEGIN RSA PRIVATE KEY-----
    ..

Encryption is optional.  The default public exponent is 65537.  

The man page says ``numbits`` is how to specify size, but this doesn't work.
    
The output is PKCS1.  There is no option for outputting a different format.  However, there is another utility ``openssl rsa`` that can interconvert different formats.

Also, this method does not generate a public key file, you have to do that separately.
