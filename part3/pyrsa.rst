.. _part3/pyrsa:

#################
Python RSA module
#################

https://stuvel.eu/python-rsa-doc

-------
Example
-------

::

    > openssl genrsa -out kf.pem 512
    Generating RSA private key, 512 bit long modulus
    ..........++++++++++++
    .........++++++++++++
    e is 65537 (0x10001)
    > pyrsa-priv2pub -i kf.pem -o kf.pub.pem
    Reading private key from kf.pem in PEM format
    Writing public key to kf.pub.pem in PEM format
    > echo "hello world" > x.txt

::
    > pyrsa-encrypt -i x.txt -o c.bin kf.pub.pem
    Reading public key from kf.pub.pem
    Reading input from x.txt
    Encrypting
    Writing output to c.bin
    > openssl rsautl -in c.bin -inkey kf.pem -decrypt
    hello world
    > 
