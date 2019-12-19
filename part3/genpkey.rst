.. _part3/genpkey:

###############
OpenSSL genpkey
###############

``openssl`` has another utility for generating keys called ``genrsa``:

.. code-block:: bash

    openssl genpkey -out kf2

"The genpkey command generates private keys.  The use of this program is encouraged over the algorithm specific utilities because additional algorithm options can be used."

- ``-algorithm alg`` e.g. rsa
- ``-out`` file to write
- ``-pkeyopt opt:value`` like ``rsa_keygen_bits:2048``
- ``-text``

--------
Examples
--------

::

    openssl genpkey -algorithm rsa > kf.private.pem

gives a PKCS8 formatted key in ``kf.private.pem``.

::

    -----BEGIN PRIVATE KEY-----

::

    openssl genpkey -algorithm rsa -text

prints the whole thing including the formatted key, but also the modulus, etc.  PKCS8