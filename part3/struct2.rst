.. _part3/struct2:

########################
RSA key structure: PKCS1
########################

-----
PKCS1
-----

We're going to dissect a PKCS1 key.  Luckily, I discovered how to convert an OpenSSH *private* key to PKCS1:

::

    puttygen kf.openssh -O private-openssh -o kf.pkcs1


So we'll paste the base64 data into the following:

::

    echo "" | base64 -d | xxd -p

::

    308204a20201000282010100b70ca0491e6c4b48615b89a23c84158bd629
    546c916f872e67c7416fd2f1cbf050d4a7821cf277ded2954e89474d2753
    4f0a121103a1bb5b9471acaaebb95c1b3e744617a498a8a91b612c89dd2c
    8ff9528cd33ea1c05ca58cab86e5f9050f1ffca8e8bbc4815b4b810c3792
    2237c788a7dfdb55748f2e3511e95567105b070a963f112f0328f84d4985
    b021b5a6d85eeb3cb0a08d1282cfb4796ef3943d4ebb03b6b95aab38a8da
    9b097607b7ac128b496a9e8a81b0d8d0d4fe3db60b902c50fa74a12a810c
    c77fbe18124a6aaa3cacd7b829d048183f7e36ce77117a3a04f43476feb7
    82e4e79ae65a3ab4a5508806d58286ddcbcbdb6c96dc2da0d02d988f0203
    010001028201003c9e32ca6407cada7a5b3cf5fc0265bc3c3ccd97728633
    871b98f1c39d60b37faed4ed6ffa34159c35b27a229df91fe7c7c9f6f7a9
    733abf76263adf1356fbf88db325af18b3f14ea721840557b8352984bbdc
    0ce6b5f43862a03ef9138128641860bb49cb26675c56acfc0e29c4bd1035
    3fbdbbcbf0ca858a9bf1cb42b0526110ae4b03152c555d06ff2bd318477c
    45a2caf77672e732a79209602e669f6ebc5492f5f8a103c72b24b6c203d4
    211e4b84cded77155968df361b86ced780a66b7c2fe7943e395ed8b11cc8
    adad61e784f62b41559bc4bd23cb25af347e98c75c3564d553de6984482f
    47fd875eee244c5edfc0449333a526fe4d6fbf542886a902818100e075ab
    32affcb508cba928cc1e7e53727435793f4033dda2949d6325ebab8617de
    ff0b306127237ccb9357cee094177f2242dac37d0619ef89ffa9dcfc43bd
    3b25233e13713b107ba7fdceb2331499fe032b7771ce48e25af2c70e3887
    5600b0f3f76dcdc25d91226ccf7f22370801c8d1844536d0a7c193345e4b
    05807f40fd02818100d0c55520133f638f4582f171c7de06036b1e8b8667
    a964ae3e26bbb9c2f85196485637f75e2cd6612c6c78f2682e23bc1b57b8
    f5f17e490ee82379a53ff31b52b70bb998e8fe1cdbc4fa864810b60d0ba4
    4a8d88718076cf7d6eb91d4b7bf7d792a16f3d7af726e402372cc528849e
    cb6e5a4bbed6865db0a0246d3e41c08b7b02818010f0907508d7178a8c64
    3dd1f9d32ad50e7422ac655a04b60a653e605442e3a1d59085f5a6bf5f6c
    41a8e30d97e1554ca0f74eaf463639aadc4d51327e4f566eaa44d8a07b01
    2c2348f05cb3122bd1db5bbde20bd2b7a96d97b8f217ce0eed8a6d3f1528
    5c2cd79133890d5d35ae030476db76a5c66582b46b555a7015dc84b90281
    800b826580002fa57077979172015fc71b1723b6f370f190c05e62ca44a2
    7008276dd37b00632bbba1ddce1918dc0f771edeaf065e60b2e29a34c807
    e3c953c0b4ddac82cde0426a1adf90242902ead66b46e2694d155cccb001
    ad41fd50750423d94c97125f9e1281cd717741634b7469a8aac7b43ca569
    b2dc114608819d78d3028180402f0f3ac4ad8b61c36d6e6e0893c5476006
    dc2d54395ba58bf31f43731733bcca0c148bc2f9129bf49949b74859850b
    e47193617999f3465a86aea1ccc67fd79c0d075cbafd1d1a0c3ff52eb807
    63a392e0af024a3c3c6cb81eb57aa5b26f5e0edb1571e1038d8742e823cd
    d54473a0e8291851612162f8da943bc3a12b5430

Now we can search for the byte strings we found in the previous chapter.

I easily find *n*, *e*, *d*, *p* and *q*

::

    308204a2020100
                  02820101
    ----------------------00b70ca0491e6c4b48615b89a23c84158bd629  n
    546c916f872e67c7416fd2f1cbf050d4a7821cf277ded2954e89474d2753
    4f0a121103a1bb5b9471acaaebb95c1b3e744617a498a8a91b612c89dd2c
    8ff9528cd33ea1c05ca58cab86e5f9050f1ffca8e8bbc4815b4b810c3792
    2237c788a7dfdb55748f2e3511e95567105b070a963f112f0328f84d4985
    b021b5a6d85eeb3cb0a08d1282cfb4796ef3943d4ebb03b6b95aab38a8da
    9b097607b7ac128b496a9e8a81b0d8d0d4fe3db60b902c50fa74a12a810c
    c77fbe18124a6aaa3cacd7b829d048183f7e36ce77117a3a04f43476feb7
    82e4e79ae65a3ab4a5508806d58286ddcbcbdb6c96dc2da0d02d988f
    ........................................................0203
    010001                                                        e
    ....................................................02820100. d
    ..............3c9e32ca6407cada7a5b3cf5fc0265bc3c3ccd97728633
    871b98f1c39d60b37faed4ed6ffa34159c35b27a229df91fe7c7c9f6f7a9
    733abf76263adf1356fbf88db325af18b3f14ea721840557b8352984bbdc
    0ce6b5f43862a03ef9138128641860bb49cb26675c56acfc0e29c4bd1035
    3fbdbbcbf0ca858a9bf1cb42b0526110ae4b03152c555d06ff2bd318477c
    45a2caf77672e732a79209602e669f6ebc5492f5f8a103c72b24b6c203d4
    211e4b84cded77155968df361b86ced780a66b7c2fe7943e395ed8b11cc8
    adad61e784f62b41559bc4bd23cb25af347e98c75c3564d553de6984482f
    47fd875eee244c5edfc0449333a526fe4d6fbf542886a9
    ..............................................028181
    ....................................................00e075ab  p
    32affcb508cba928cc1e7e53727435793f4033dda2949d6325ebab8617de
    ff0b306127237ccb9357cee094177f2242dac37d0619ef89ffa9dcfc43bd
    3b25233e13713b107ba7fdceb2331499fe032b7771ce48e25af2c70e3887
    5600b0f3f76dcdc25d91226ccf7f22370801c8d1844536d0a7c193345e4b
    05807f40fd
    ..........028181
    ................00d0c55520133f638f4582f171c7de06036b1e8b8667  q
    a964ae3e26bbb9c2f85196485637f75e2cd6612c6c78f2682e23bc1b57b8
    f5f17e490ee82379a53ff31b52b70bb998e8fe1cdbc4fa864810b60d0ba4
    4a8d88718076cf7d6eb91d4b7bf7d792a16f3d7af726e402372cc528849e
    cb6e5a4bbed6865db0a0246d3e41c08b7b
    ..................................028180
    ........................................10f0907508d7178a8c64
    3dd1f9d32ad50e7422ac655a04b60a653e605442e3a1d59085f5a6bf5f6c
    41a8e30d97e1554ca0f74eaf463639aadc4d51327e4f566eaa44d8a07b01
    2c2348f05cb3122bd1db5bbde20bd2b7a96d97b8f217ce0eed8a6d3f1528
    5c2cd79133890d5d35ae030476db76a5c66582b46b555a7015dc84b9
    ........................................................0281
    80
    ..0b826580002fa57077979172015fc71b1723b6f370f190c05e62ca44a2
    7008276dd37b00632bbba1ddce1918dc0f771edeaf065e60b2e29a34c807
    e3c953c0b4ddac82cde0426a1adf90242902ead66b46e2694d155cccb001
    ad41fd50750423d94c97125f9e1281cd717741634b7469a8aac7b43ca569
    b2dc114608819d78d3
    ..................028180
    ........................402f0f3ac4ad8b61c36d6e6e0893c5476006 ?
    dc2d54395ba58bf31f43731733bcca0c148bc2f9129bf49949b74859850b
    e47193617999f3465a86aea1ccc67fd79c0d075cbafd1d1a0c3ff52eb807
    63a392e0af024a3c3c6cb81eb57aa5b26f5e0edb1571e1038d8742e823cd
    d54473a0e8291851612162f8da943bc3a12b5430


Each is preceded by a value like

- 02820 + 101
- 02 + 03
- 0281 + 81
- 0281 + 81
- 0281 + 80
- 0281 + 80

There is a header, but no footer.

Using this clue, I divide up the unknown region.  Having done that, we can compare with what the rsa tool gives us.  (I couldn't load PKCS1, but did get PKCS8 to work).

::

    modulus:
        00:b7:0c:a0:49:1e:6c:4b:48:61:5b:89:a2:3c:84:
        15:8b:d6:29:54:6c:91:6f:87:2e:67:c7:41:6f:d2:
        f1:cb:f0:50:d4:a7:82:1c:f2:77:de:d2:95:4e:89:
        47:4d:27:53:4f:0a:12:11:03:a1:bb:5b:94:71:ac:
        aa:eb:b9:5c:1b:3e:74:46:17:a4:98:a8:a9:1b:61:
        2c:89:dd:2c:8f:f9:52:8c:d3:3e:a1:c0:5c:a5:8c:
        ab:86:e5:f9:05:0f:1f:fc:a8:e8:bb:c4:81:5b:4b:
        81:0c:37:92:22:37:c7:88:a7:df:db:55:74:8f:2e:
        35:11:e9:55:67:10:5b:07:0a:96:3f:11:2f:03:28:
        f8:4d:49:85:b0:21:b5:a6:d8:5e:eb:3c:b0:a0:8d:
        12:82:cf:b4:79:6e:f3:94:3d:4e:bb:03:b6:b9:5a:
        ab:38:a8:da:9b:09:76:07:b7:ac:12:8b:49:6a:9e:
        8a:81:b0:d8:d0:d4:fe:3d:b6:0b:90:2c:50:fa:74:
        a1:2a:81:0c:c7:7f:be:18:12:4a:6a:aa:3c:ac:d7:
        b8:29:d0:48:18:3f:7e:36:ce:77:11:7a:3a:04:f4:
        34:76:fe:b7:82:e4:e7:9a:e6:5a:3a:b4:a5:50:88:
        06:d5:82:86:dd:cb:cb:db:6c:96:dc:2d:a0:d0:2d:
        98:8f
    publicExponent: 65537 (0x10001)
    privateExponent:
        3c:9e:32:ca:64:07:ca:da:7a:5b:3c:f5:fc:02:65:
        bc:3c:3c:cd:97:72:86:33:87:1b:98:f1:c3:9d:60:
        b3:7f:ae:d4:ed:6f:fa:34:15:9c:35:b2:7a:22:9d:
        f9:1f:e7:c7:c9:f6:f7:a9:73:3a:bf:76:26:3a:df:
        13:56:fb:f8:8d:b3:25:af:18:b3:f1:4e:a7:21:84:
        05:57:b8:35:29:84:bb:dc:0c:e6:b5:f4:38:62:a0:
        3e:f9:13:81:28:64:18:60:bb:49:cb:26:67:5c:56:
        ac:fc:0e:29:c4:bd:10:35:3f:bd:bb:cb:f0:ca:85:
        8a:9b:f1:cb:42:b0:52:61:10:ae:4b:03:15:2c:55:
        5d:06:ff:2b:d3:18:47:7c:45:a2:ca:f7:76:72:e7:
        32:a7:92:09:60:2e:66:9f:6e:bc:54:92:f5:f8:a1:
        03:c7:2b:24:b6:c2:03:d4:21:1e:4b:84:cd:ed:77:
        15:59:68:df:36:1b:86:ce:d7:80:a6:6b:7c:2f:e7:
        94:3e:39:5e:d8:b1:1c:c8:ad:ad:61:e7:84:f6:2b:
        41:55:9b:c4:bd:23:cb:25:af:34:7e:98:c7:5c:35:
        64:d5:53:de:69:84:48:2f:47:fd:87:5e:ee:24:4c:
        5e:df:c0:44:93:33:a5:26:fe:4d:6f:bf:54:28:86:
        a9
    prime1:
        00:e0:75:ab:32:af:fc:b5:08:cb:a9:28:cc:1e:7e:
        53:72:74:35:79:3f:40:33:dd:a2:94:9d:63:25:eb:
        ab:86:17:de:ff:0b:30:61:27:23:7c:cb:93:57:ce:
        e0:94:17:7f:22:42:da:c3:7d:06:19:ef:89:ff:a9:
        dc:fc:43:bd:3b:25:23:3e:13:71:3b:10:7b:a7:fd:
        ce:b2:33:14:99:fe:03:2b:77:71:ce:48:e2:5a:f2:
        c7:0e:38:87:56:00:b0:f3:f7:6d:cd:c2:5d:91:22:
        6c:cf:7f:22:37:08:01:c8:d1:84:45:36:d0:a7:c1:
        93:34:5e:4b:05:80:7f:40:fd
    prime2:
        00:d0:c5:55:20:13:3f:63:8f:45:82:f1:71:c7:de:
        06:03:6b:1e:8b:86:67:a9:64:ae:3e:26:bb:b9:c2:
        f8:51:96:48:56:37:f7:5e:2c:d6:61:2c:6c:78:f2:
        68:2e:23:bc:1b:57:b8:f5:f1:7e:49:0e:e8:23:79:
        a5:3f:f3:1b:52:b7:0b:b9:98:e8:fe:1c:db:c4:fa:
        86:48:10:b6:0d:0b:a4:4a:8d:88:71:80:76:cf:7d:
        6e:b9:1d:4b:7b:f7:d7:92:a1:6f:3d:7a:f7:26:e4:
        02:37:2c:c5:28:84:9e:cb:6e:5a:4b:be:d6:86:5d:
        b0:a0:24:6d:3e:41:c0:8b:7b
    exponent1:
        10:f0:90:75:08:d7:17:8a:8c:64:3d:d1:f9:d3:2a:
        d5:0e:74:22:ac:65:5a:04:b6:0a:65:3e:60:54:42:
        e3:a1:d5:90:85:f5:a6:bf:5f:6c:41:a8:e3:0d:97:
        e1:55:4c:a0:f7:4e:af:46:36:39:aa:dc:4d:51:32:
        7e:4f:56:6e:aa:44:d8:a0:7b:01:2c:23:48:f0:5c:
        b3:12:2b:d1:db:5b:bd:e2:0b:d2:b7:a9:6d:97:b8:
        f2:17:ce:0e:ed:8a:6d:3f:15:28:5c:2c:d7:91:33:
        89:0d:5d:35:ae:03:04:76:db:76:a5:c6:65:82:b4:
        6b:55:5a:70:15:dc:84:b9
    exponent2:
        0b:82:65:80:00:2f:a5:70:77:97:91:72:01:5f:c7:
        1b:17:23:b6:f3:70:f1:90:c0:5e:62:ca:44:a2:70:
        08:27:6d:d3:7b:00:63:2b:bb:a1:dd:ce:19:18:dc:
        0f:77:1e:de:af:06:5e:60:b2:e2:9a:34:c8:07:e3:
        c9:53:c0:b4:dd:ac:82:cd:e0:42:6a:1a:df:90:24:
        29:02:ea:d6:6b:46:e2:69:4d:15:5c:cc:b0:01:ad:
        41:fd:50:75:04:23:d9:4c:97:12:5f:9e:12:81:cd:
        71:77:41:63:4b:74:69:a8:aa:c7:b4:3c:a5:69:b2:
        dc:11:46:08:81:9d:78:d3
    coefficient:
        40:2f:0f:3a:c4:ad:8b:61:c3:6d:6e:6e:08:93:c5:
        47:60:06:dc:2d:54:39:5b:a5:8b:f3:1f:43:73:17:
        33:bc:ca:0c:14:8b:c2:f9:12:9b:f4:99:49:b7:48:
        59:85:0b:e4:71:93:61:79:99:f3:46:5a:86:ae:a1:
        cc:c6:7f:d7:9c:0d:07:5c:ba:fd:1d:1a:0c:3f:f5:
        2e:b8:07:63:a3:92:e0:af:02:4a:3c:3c:6c:b8:1e:
        b5:7a:a5:b2:6f:5e:0e:db:15:71:e1:03:8d:87:42:
        e8:23:cd:d5:44:73:a0:e8:29:18:51:61:21:62:f8:
        da:94:3b:c3:a1:2b:54:30


So these other values are called the exponents (1 & 2) and the coefficient.

Here is a reference:

https://www.di-mgt.com.au/crt_rsa.html

``exponent1`` is the inverse of ``e`` mod ``(p-1)`` and ``exponent2`` is the inverse of ``e`` mod ``(q-1)`` while the ``coefficient`` is the inverse of ``q`` mod ``p``.

I pasted in the values and checked that the results of calculation match the values given in the hex output above.  

We'll explore what these do in another chapter.  Basically the answer is that computing the mod with ``phi`` can be done faster if you know ``p`` and ``q`` and something called the Chinese Remainder Theorem.

