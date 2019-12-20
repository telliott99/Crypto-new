.. _part4/digest:

####################
OpenSSH fingerprints
####################

-------
Digests
-------

::

    > echo "hello" > x.txt
    > md5 < x.txt
    b1946ac92492d2347c6235b4d2611184
    > openssl dgst -sha1 < x.txt
    f572d396fae9206628714fb2ce00f72e94f2258f
    > openssl dgst -sha256 < x.txt
    5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03

::

    > echo "hello" | md5
    b1946ac92492d2347c6235b4d2611184
    > echo "hallo" | md5
    aee97cb3ad288ef0add6c6b5b5fae48a

Quick to compute, sensitive to subtle changes, impossible to craft a different set of data with the same hash (though this is changing, which is why SHA256 is now recommended).

--------------
Fingerprinting
--------------

The ``ssh-keygen`` utility can print a fingerprint for an OpenSSH key.

This is simply the hash of the binary data in the public key.  It makes it easier to compare the data in the public key on a server with what you have on the client at home.

You can either input the public key, or the program will find the public key data embedded in the private key.

The command line flag is:

- ``-l`` fingerprint

as in 

::

    ssh-keygen -lf kf

which outputs something like:

::

    2048 SHA256:Qom284Cw07VyzyAPJ3CZds+ssIFXF44XHN2HL/qBx/U telliott@newmini.local (RSA)

To get MD5 you just do

- ``-E``

::

    > ssh-keygen -l -f kf -E md5   
    2048 MD5:bd:9d:45:95:9f:a3:8f:88:20:93:40:76:66:9e:77:8b telliott@newmini.local (RSA)

------------
Confirmation
------------

I want to confirm that this is doing what I think it is.  While it is simple enough to cut and paste the base64 data of the public key, as in:

::

    echo ''

then paste the data in betweenca the quotes, and hit return:

::

    AAAAB3Nz..lg3EH32T

A better way if you're going to do this a lot is to use ``awk``.

::

    
    awk '{ print $2 }' kf.pub

which gives the same thing.  Then pipe that to

::

    | base64 -d | openssl dgst -sha256 -binary | base64

That is, do

::

    awk '{ print $2 }' kf.pub \
    | base64 -d | openssl dgst -sha256 -binary | base64

with output:

::

    Qom284Cw07VyzyAPJ3CZds+ssIFXF44XHN2HL/qBx/U=

or more simply:

::

    > awk '{ print $2 }' kf.pub \
    | base64 -d | md5        

with output:

::

    bd9d45959fa38f8820934076669e778b

And that's a match.