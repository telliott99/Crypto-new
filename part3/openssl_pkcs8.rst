.. _part3/openssl_pkcs8:

####################
OpenSSL:  read PKCS8
####################

We used 

::

    > openssl genpkey -algorithm rsa

and ended up with a PKCS8 formatted key in ``kf.pem``.  We want to read this key and extract the data, and compare that with what we get with the ``openssl rsa`` utility.  Let's do that part first.

::

    > openssl rsa -text -in kf.pem

What we get is text formatted as hex bytes with ':' separators.

::

    Private-Key: (2048 bit)
    modulus:
        00:f4:26:20:6d:d6:08:fb:03:3a:cb:2c:8e:f1:52:
        52:b2:20:39:d4:85:2d:33:33:52:ad:f2:36:85:92:
        af:77:e2:9e:46:cb:78:aa:79:f9:df:4c:d8:51:bb:
        c3:86:e3:ea:f7:81:98:bc:a8:00:39:0f:92:57:49:
        32:7b:fc:61:d1:0b:ac:25:f1:8b:b3:ed:70:72:f2:
        7e:8a:47:99:28:aa:20:d5:11:88:0e:c8:34:e4:ef:
        e7:d7:4e:04:4d:e0:3b:c6:e9:dc:55:60:27:d1:11:
        ac:06:55:60:c3:07:84:ec:41:8b:09:ed:0c:e4:18:
        36:b7:a8:b1:b2:05:c7:75:69:69:2a:25:3d:3f:ff:
        db:4c:17:94:19:ba:7c:aa:0c:01:9e:bc:a7:5f:53:
        59:15:3a:4c:41:9d:4b:80:1b:6d:5e:23:cd:72:76:
        19:8d:d4:f6:76:f1:a2:c4:a5:07:52:2f:88:68:cd:
        4f:65:ac:37:f2:1f:09:f7:73:71:3f:3c:79:2a:c1:
        91:83:23:4e:b8:02:d2:8c:ed:26:67:9f:92:dd:d9:
        49:04:37:59:63:9f:bc:0b:e0:fd:cd:dc:10:92:fe:
        e2:de:bc:6f:a7:9f:52:7b:74:3f:10:82:63:6c:90:
        cf:a8:c7:06:c1:96:39:f1:c6:fc:5b:fa:87:c2:4f:
        29:15
    publicExponent: 65537 (0x10001)
    privateExponent:
        00:af:b9:a9:69:a4:bd:fd:fd:0b:1a:25:4e:14:ff:
        4d:aa:0b:6b:d4:3c:ae:95:c5:80:e2:d6:0c:cc:03:
        11:ec:55:dd:d9:d2:a5:5c:fe:42:0c:a8:c0:a1:c3:
        65:2d:f7:69:ad:0f:48:21:b1:41:c7:d0:1f:62:57:
        ba:d0:66:8c:f8:eb:4f:d2:57:92:57:c4:b4:44:e7:
        a8:90:5a:8c:30:2a:93:4b:08:3d:47:76:6e:2b:c1:
        48:bb:3c:d9:f8:3b:46:8b:1a:d3:8d:57:92:10:f6:
        89:3c:5d:c3:31:5c:7e:1d:95:e7:3f:13:b1:4d:92:
        e7:ff:34:9a:01:2a:0b:af:c2:f1:1d:9c:5b:06:ff:
        b2:38:4e:30:34:86:5e:4d:e9:74:cf:31:fa:98:e4:
        9e:60:dd:4a:01:e8:50:ab:d8:d3:77:0c:a9:ba:e3:
        10:40:6d:19:d5:23:82:51:f2:24:04:b2:d7:0c:b7:
        2d:00:a3:e6:20:9d:4d:4e:f5:ed:91:e6:33:06:6d:
        cf:eb:d8:cb:7c:5e:82:d7:ff:1d:61:0f:85:2f:8f:
        1e:8f:55:3c:bf:2b:e8:b5:d4:d4:b6:30:f9:4a:6a:
        e7:85:19:ac:8b:41:d6:fb:75:63:33:00:55:95:e2:
        29:62:53:2b:6b:81:1b:3e:ef:3d:0d:69:12:19:15:
        04:c1
    prime1:
        00:fa:b8:d0:8e:d6:34:c0:c9:2e:ea:33:b7:8b:9b:
        31:5c:b8:d9:48:31:4b:ea:52:13:f3:50:18:8a:d1:
        d8:18:a3:2b:52:04:4e:7c:0d:3d:32:d2:0f:c8:eb:
        88:f1:66:f5:bb:60:a2:62:29:86:5b:82:67:44:bd:
        bf:4a:76:bf:fc:58:9c:8c:91:51:54:a1:4f:dc:ab:
        44:df:b8:d5:42:78:8f:6b:c6:31:6e:71:d2:d5:57:
        6e:5a:93:a3:af:7e:ae:28:87:4e:0d:02:e3:3f:c5:
        c0:52:b9:29:34:f3:e3:dc:f9:ae:55:5c:19:07:a0:
        d8:86:aa:13:33:d2:5b:a0:6d
    prime2:
        00:f9:49:e3:90:88:e3:1e:1d:70:aa:7d:d9:97:c7:
        88:09:df:5f:0c:26:6c:a4:84:10:ea:8c:52:57:85:
        d8:17:fa:ac:95:91:ed:28:89:dd:af:c4:b8:bc:d3:
        95:14:4e:cf:52:2f:49:1a:74:88:08:d9:81:ec:20:
        41:20:00:07:7e:8b:16:62:bf:f3:90:5c:65:18:78:
        b7:b6:e2:20:63:43:f9:90:24:2e:14:14:90:37:12:
        6a:9d:00:98:9d:e3:86:21:b5:21:60:27:1d:77:ca:
        13:0e:dd:e6:c8:c6:96:ea:e8:dc:3f:15:e6:ec:bd:
        4f:42:4b:c9:00:e3:c9:d2:49
    exponent1:
        3a:54:6a:f9:00:2e:cf:b7:3e:79:f0:44:40:6f:7f:
        a1:71:c3:e3:3e:cc:c9:9c:04:d6:33:89:32:2a:b5:
        da:ad:83:73:96:5a:e8:13:70:6c:75:60:84:be:ff:
        62:22:31:03:41:ed:25:67:41:c1:e2:69:c2:1d:5e:
        f6:a4:ff:ef:66:72:2d:65:d5:85:19:ee:69:89:53:
        01:b5:8f:af:e2:3a:83:b9:5d:60:b3:8c:78:63:d9:
        e1:aa:bd:87:23:b2:c2:ed:0f:a4:89:4a:73:58:bf:
        70:bf:71:2d:c7:9b:f8:9a:02:0c:0b:dc:2a:e1:29:
        de:d2:8c:9b:1e:d2:80:55
    exponent2:
        70:47:b5:75:8e:12:2d:a8:38:ec:b1:8e:65:ec:7a:
        fb:67:5e:5a:0c:9c:76:64:fd:71:87:0e:37:59:93:
        81:09:68:de:5d:41:a2:36:a6:60:da:8c:12:90:81:
        df:09:b8:1b:5e:2c:e0:fb:87:a1:e4:c5:bd:e2:b1:
        32:86:90:d9:90:2f:de:fe:71:e7:9d:95:f3:35:bc:
        19:65:34:0d:41:ba:90:0f:9b:a9:73:b1:98:fc:74:
        84:8e:96:2e:d7:21:bc:e0:e6:4d:76:90:b1:39:94:
        e7:e7:4e:61:34:01:19:81:14:62:5d:ad:0b:08:21:
        40:cc:fd:95:a7:03:69:f1
    coefficient:
        5a:2c:5d:98:80:58:04:ac:a7:6f:b2:a6:e5:c9:26:
        96:86:c3:06:75:18:50:14:b4:bd:25:65:c0:2c:32:
        06:3c:8c:b3:da:94:2b:63:d6:34:15:20:7a:64:87:
        4f:a1:5f:ec:9f:c8:96:17:ca:7e:1f:8f:aa:79:bf:
        df:f0:a8:fb:78:e7:71:62:0c:50:19:fb:26:02:e0:
        d2:cc:51:2f:9f:64:f4:d4:be:f0:a1:f3:53:e9:b1:
        bf:e6:83:2d:10:e8:2e:d1:a2:d6:d8:f5:9f:1d:72:
        a0:4f:c3:75:48:73:07:8e:08:cc:df:ac:15:72:66:
        1b:05:6c:ac:bd:e5:30:cc
    writing RSA key
    -----BEGIN RSA PRIVATE KEY-----
    ...


I wrote a little Python:

.. code-block:: python

    import sys
    s = sys.argv[1]

    def f(s):
        s = s.replace(' ', '')
        s = s.replace(':', '')
        s = s.replace('\n', '')
        print int(s,16)

    f(s)

which I invoke from the command line, pasting the hex

::

    python decode.py '00:... '

**modulus**

::

    > python decode.py '00:f4:26:20:6d:d6:08:fb:03:3a:cb:2c:8e:f1:52:
        52:b2:20:39:d4:85:2d:33:33:52:ad:f2:36:85:92:
        af:77:e2:9e:46:cb:78:aa:79:f9:df:4c:d8:51:bb:
        c3:86:e3:ea:f7:81:98:bc:a8:00:39:0f:92:57:49:
        32:7b:fc:61:d1:0b:ac:25:f1:8b:b3:ed:70:72:f2:
        7e:8a:47:99:28:aa:20:d5:11:88:0e:c8:34:e4:ef:
        e7:d7:4e:04:4d:e0:3b:c6:e9:dc:55:60:27:d1:11:
        ac:06:55:60:c3:07:84:ec:41:8b:09:ed:0c:e4:18:
        36:b7:a8:b1:b2:05:c7:75:69:69:2a:25:3d:3f:ff:
        db:4c:17:94:19:ba:7c:aa:0c:01:9e:bc:a7:5f:53:
        59:15:3a:4c:41:9d:4b:80:1b:6d:5e:23:cd:72:76:
        19:8d:d4:f6:76:f1:a2:c4:a5:07:52:2f:88:68:cd:
        4f:65:ac:37:f2:1f:09:f7:73:71:3f:3c:79:2a:c1:
        91:83:23:4e:b8:02:d2:8c:ed:26:67:9f:92:dd:d9:
        49:04:37:59:63:9f:bc:0b:e0:fd:cd:dc:10:92:fe:
        e2:de:bc:6f:a7:9f:52:7b:74:3f:10:82:63:6c:90:
        cf:a8:c7:06:c1:96:39:f1:c6:fc:5b:fa:87:c2:4f:
        29:15'
    308209..447061
    >

Here, and further on, I have deleted the internal part of the decimal output.

**prime1**

::

    > python decode.py '00:fa:b8:d0:8e:d6:34:c0:c9:2e:ea:33:b7:8b:9b:
        31:5c:b8:d9:48:31:4b:ea:52:13:f3:50:18:8a:d1:
        d8:18:a3:2b:52:04:4e:7c:0d:3d:32:d2:0f:c8:eb:
        88:f1:66:f5:bb:60:a2:62:29:86:5b:82:67:44:bd:
        bf:4a:76:bf:fc:58:9c:8c:91:51:54:a1:4f:dc:ab:
        44:df:b8:d5:42:78:8f:6b:c6:31:6e:71:d2:d5:57:
        6e:5a:93:a3:af:7e:ae:28:87:4e:0d:02:e3:3f:c5:
        c0:52:b9:29:34:f3:e3:dc:f9:ae:55:5c:19:07:a0:
        d8:86:aa:13:33:d2:5b:a0:6d'
    176062..413933
    >


**prime2**

::

    > python decode.py '00:f9:49:e3:90:88:e3:1e:1d:70:aa:7d:d9:97:c7:
        88:09:df:5f:0c:26:6c:a4:84:10:ea:8c:52:57:85:
        d8:17:fa:ac:95:91:ed:28:89:dd:af:c4:b8:bc:d3:
        95:14:4e:cf:52:2f:49:1a:74:88:08:d9:81:ec:20:
        41:20:00:07:7e:8b:16:62:bf:f3:90:5c:65:18:78:
        b7:b6:e2:20:63:43:f9:90:24:2e:14:14:90:37:12:
        6a:9d:00:98:9d:e3:86:21:b5:21:60:27:1d:77:ca:
        13:0e:dd:e6:c8:c6:96:ea:e8:dc:3f:15:e6:ec:bd:
        4f:42:4b:c9:00:e3:c9:d2:49'
    175056..689417
    >

Check that the multiplication works.  It does!

>>> 1760629..413933 * 175056..689417
308209..447061L

*e* is:

::

    publicExponent: 65537 (0x10001)
    
**private exponent**

::

    > python decode.py '00:af:b9:a9:69:a4:bd:fd:fd:0b:1a:25:4e:14:ff:
        4d:aa:0b:6b:d4:3c:ae:95:c5:80:e2:d6:0c:cc:03:
        11:ec:55:dd:d9:d2:a5:5c:fe:42:0c:a8:c0:a1:c3:
        65:2d:f7:69:ad:0f:48:21:b1:41:c7:d0:1f:62:57:
        ba:d0:66:8c:f8:eb:4f:d2:57:92:57:c4:b4:44:e7:
        a8:90:5a:8c:30:2a:93:4b:08:3d:47:76:6e:2b:c1:
        48:bb:3c:d9:f8:3b:46:8b:1a:d3:8d:57:92:10:f6:
        89:3c:5d:c3:31:5c:7e:1d:95:e7:3f:13:b1:4d:92:
        e7:ff:34:9a:01:2a:0b:af:c2:f1:1d:9c:5b:06:ff:
        b2:38:4e:30:34:86:5e:4d:e9:74:cf:31:fa:98:e4:
        9e:60:dd:4a:01:e8:50:ab:d8:d3:77:0c:a9:ba:e3:
        10:40:6d:19:d5:23:82:51:f2:24:04:b2:d7:0c:b7:
        2d:00:a3:e6:20:9d:4d:4e:f5:ed:91:e6:33:06:6d:
        cf:eb:d8:cb:7c:5e:82:d7:ff:1d:61:0f:85:2f:8f:
        1e:8f:55:3c:bf:2b:e8:b5:d4:d4:b6:30:f9:4a:6a:
        e7:85:19:ac:8b:41:d6:fb:75:63:33:00:55:95:e2:
        29:62:53:2b:6b:81:1b:3e:ef:3d:0d:69:12:19:15:
        04:c1'
    221832..747393
    >


Now I check that the math works:

>>> e = 65537
>>> d = 221832..747393
>>> n = 308209..447061
>>> m = 18096537
>>> 
>>> c = pow(m,e,n)
>>> pow(c,d,n)
18096537L
>>> 

Looks good.  I could check the derivation of the private exponent but I won't bother.  

In the next part, we want to decode the data in the private key manually.

