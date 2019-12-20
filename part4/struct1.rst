.. _part3/struct1:

###########################
RSA key structure:  OpenSSH
###########################

-------
OpenSSH
-------

We're going to look at key structure, starting with an OpenSSH key.

One way to decode the data in a key is to just enter this command in Terminal (with no return yet):

::

    echo "" | base64 -d | hexdump

and then paste the whole base64 data string between the quotation marks.  

In the case of the OpenSSH public key that I have in ``kf.pub`` (with first line ``ssh-rsa``), I obtain:

::

    0000000 00 00 00 07 73 73 68 2d 72 73 61 00 00 00 03 01
    0000010 00 01 00 00 01 01 00 cc 41 ed ca f6 cc ad a8 c5
    ..

I found the answer to getting continous hex:

::

    echo "" | base64 -d | xxd -p

::
    
    000000077373682d727361000000030100010000010100b70ca0491e6c4b
    48615b89a23c84158bd629546c916f872e67c7416fd2f1cbf050d4a7821c
    f277ded2954e89474d27534f0a121103a1bb5b9471acaaebb95c1b3e7446
    17a498a8a91b612c89dd2c8ff9528cd33ea1c05ca58cab86e5f9050f1ffc
    a8e8bbc4815b4b810c37922237c788a7dfdb55748f2e3511e95567105b07
    0a963f112f0328f84d4985b021b5a6d85eeb3cb0a08d1282cfb4796ef394
    3d4ebb03b6b95aab38a8da9b097607b7ac128b496a9e8a81b0d8d0d4fe3d
    b60b902c50fa74a12a810cc77fbe18124a6aaa3cacd7b829d048183f7e36
    ce77117a3a04f43476feb782e4e79ae65a3ab4a5508806d58286ddcbcbdb
    6c96dc2da0d02d988f                           

The first part is a 32-bit int which says the length of the following data section is 7 bytes, followed by those 7 bytes, which is ASCII for ssh-rsa (run hexdump with -C to see this):

::

    00 00 00 07
                73 73 68 2d 72 73 61

then another 32-bit int for the following data section of 3 bytes

::

    00 00 00 03
                01 00 01

this is 65537 in hex:  ``1 * 16**4 + 1``.

Then another 32-bit int:

::

    00 00 01 01

which says the following data section is 257 bytes.  

If we strip off the leading null, that's the length that we should have for a 2048 bit key.

::

    ..............................................b70ca0491e6c4b
    48615b89a23c84158bd629546c916f872e67c7416fd2f1cbf050d4a7821c
    f277ded2954e89474d27534f0a121103a1bb5b9471acaaebb95c1b3e7446
    17a498a8a91b612c89dd2c8ff9528cd33ea1c05ca58cab86e5f9050f1ffc
    a8e8bbc4815b4b810c37922237c788a7dfdb55748f2e3511e95567105b07
    0a963f112f0328f84d4985b021b5a6d85eeb3cb0a08d1282cfb4796ef394
    3d4ebb03b6b95aab38a8da9b097607b7ac128b496a9e8a81b0d8d0d4fe3d
    b60b902c50fa74a12a810cc77fbe18124a6aaa3cacd7b829d048183f7e36
    ce77117a3a04f43476feb782e4e79ae65a3ab4a5508806d58286ddcbcbdb
    6c96dc2da0d02d988f 

We can use the script ``decode.py`` from before, just paste in the relevant bytes (in quotes), obtaining (I have broken the lines)

::

    231078359784953640556250936100765278034044456796567803307879
    741903952616004667698467445611485962430664366862543283853578
    114440818626659592152360008282153539987046965902690291423105
    853129532115344940489982148622824657938803130717168030363186
    452392494555837804339938659537931611124829371134569636259862
    608973210794911874003357425470781233434251847210990719978682
    756380369293842875814280516186706300902649573228547539514910
    305327885065850259588188003492877601723927652894332863523652
    475636717690954561480395722140304918026021402089792935224691
    290319419331992767287916398917302730494421618111767072007753
    15718739157948559
    
We will refer to this number as 231..559.  I have also pasted the original output into the Python interpreter and assigned it to the variable *n*.

Now, of course, we want to check this against the private key.

---------------

Again,

::

    echo "" | base64 -d | xxd -p
    
::

    6f70656e7373682d6b65792d763100000000046e6f6e65000000046e6f6e
    65000000000000000100000117000000077373682d727361000000030100
    010000010100b70ca0491e6c4b48615b89a23c84158bd629546c916f872e
    67c7416fd2f1cbf050d4a7821cf277ded2954e89474d27534f0a121103a1
    bb5b9471acaaebb95c1b3e744617a498a8a91b612c89dd2c8ff9528cd33e
    a1c05ca58cab86e5f9050f1ffca8e8bbc4815b4b810c37922237c788a7df
    db55748f2e3511e95567105b070a963f112f0328f84d4985b021b5a6d85e
    eb3cb0a08d1282cfb4796ef3943d4ebb03b6b95aab38a8da9b097607b7ac
    128b496a9e8a81b0d8d0d4fe3db60b902c50fa74a12a810cc77fbe18124a
    6aaa3cacd7b829d048183f7e36ce77117a3a04f43476feb782e4e79ae65a
    3ab4a5508806d58286ddcbcbdb6c96dc2da0d02d988f000003d06002a68f
    6002a68f000000077373682d7273610000010100b70ca0491e6c4b48615b
    89a23c84158bd629546c916f872e67c7416fd2f1cbf050d4a7821cf277de
    d2954e89474d27534f0a121103a1bb5b9471acaaebb95c1b3e744617a498
    a8a91b612c89dd2c8ff9528cd33ea1c05ca58cab86e5f9050f1ffca8e8bb
    c4815b4b810c37922237c788a7dfdb55748f2e3511e95567105b070a963f
    112f0328f84d4985b021b5a6d85eeb3cb0a08d1282cfb4796ef3943d4ebb
    03b6b95aab38a8da9b097607b7ac128b496a9e8a81b0d8d0d4fe3db60b90
    2c50fa74a12a810cc77fbe18124a6aaa3cacd7b829d048183f7e36ce7711
    7a3a04f43476feb782e4e79ae65a3ab4a5508806d58286ddcbcbdb6c96dc
    2da0d02d988f00000003010001000001003c9e32ca6407cada7a5b3cf5fc
    0265bc3c3ccd97728633871b98f1c39d60b37faed4ed6ffa34159c35b27a
    229df91fe7c7c9f6f7a9733abf76263adf1356fbf88db325af18b3f14ea7
    21840557b8352984bbdc0ce6b5f43862a03ef9138128641860bb49cb2667
    5c56acfc0e29c4bd10353fbdbbcbf0ca858a9bf1cb42b0526110ae4b0315
    2c555d06ff2bd318477c45a2caf77672e732a79209602e669f6ebc5492f5
    f8a103c72b24b6c203d4211e4b84cded77155968df361b86ced780a66b7c
    2fe7943e395ed8b11cc8adad61e784f62b41559bc4bd23cb25af347e98c7
    5c3564d553de6984482f47fd875eee244c5edfc0449333a526fe4d6fbf54
    2886a900000080402f0f3ac4ad8b61c36d6e6e0893c5476006dc2d54395b
    a58bf31f43731733bcca0c148bc2f9129bf49949b74859850be471936179
    99f3465a86aea1ccc67fd79c0d075cbafd1d1a0c3ff52eb80763a392e0af
    024a3c3c6cb81eb57aa5b26f5e0edb1571e1038d8742e823cdd54473a0e8
    291851612162f8da943bc3a12b54300000008100e075ab32affcb508cba9
    28cc1e7e53727435793f4033dda2949d6325ebab8617deff0b306127237c
    cb9357cee094177f2242dac37d0619ef89ffa9dcfc43bd3b25233e13713b
    107ba7fdceb2331499fe032b7771ce48e25af2c70e38875600b0f3f76dcd
    c25d91226ccf7f22370801c8d1844536d0a7c193345e4b05807f40fd0000
    008100d0c55520133f638f4582f171c7de06036b1e8b8667a964ae3e26bb
    b9c2f85196485637f75e2cd6612c6c78f2682e23bc1b57b8f5f17e490ee8
    2379a53ff31b52b70bb998e8fe1cdbc4fa864810b60d0ba44a8d88718076
    cf7d6eb91d4b7bf7d792a16f3d7af726e402372cc528849ecb6e5a4bbed6
    865db0a0246d3e41c08b7b0000001674656c6c696f7474406e65776d696e
    692e6c6f63616c0102030405


First, a header that includes 73-73-68-2d (ssh-) but not 72-73-61(rsa):

::

    6f70656e7373682d6b65792d7631

size and data block of unknown function (conserved across different keys)

::

    ............................00000000046e6f6e65

repeated

::

    ..............................................000000046e6f6e
    65

Something I haven't yet identified:

::

    ..000000000000000100000117

ssh-rsa (this is the public key):

::

    ..........................00000007
    ..................................7373682d727361

*e* = 65537:

::

    ................................................00000003
    ........................................................0100
    01

The size and data for *n*, the modulus:

::

    ..00000101
    ..........00b70ca0491e6c4b48615b89a23c84158bd629546c916f872e
    67c7416fd2f1cbf050d4a7821cf277ded2954e89474d27534f0a121103a1
    bb5b9471acaaebb95c1b3e744617a498a8a91b612c89dd2c8ff9528cd33e
    a1c05ca58cab86e5f9050f1ffca8e8bbc4815b4b810c37922237c788a7df
    db55748f2e3511e95567105b070a963f112f0328f84d4985b021b5a6d85e
    eb3cb0a08d1282cfb4796ef3943d4ebb03b6b95aab38a8da9b097607b7ac
    128b496a9e8a81b0d8d0d4fe3db60b902c50fa74a12a810cc77fbe18124a
    6aaa3cacd7b829d048183f7e36ce77117a3a04f43476feb782e4e79ae65a
    3ab4a5508806d58286ddcbcbdb6c96dc2da0d02d988f

Stuff of unknown function

::

    ............................................000003d06002a68f
    6002a68f

Size and data block that says ssh-rsa

::

    ........00000007
    ................7373682d727361

The modulus data, repeated

::

    ................................00000101
    ........................................b70ca0491e6c4b48615b
    89a23c84158bd629546c916f872e67c7416fd2f1cbf050d4a7821cf277de
    d2954e89474d27534f0a121103a1bb5b9471acaaebb95c1b3e744617a498
    a8a91b612c89dd2c8ff9528cd33ea1c05ca58cab86e5f9050f1ffca8e8bb
    c4815b4b810c37922237c788a7dfdb55748f2e3511e95567105b070a963f
    112f0328f84d4985b021b5a6d85eeb3cb0a08d1282cfb4796ef3943d4ebb
    03b6b95aab38a8da9b097607b7ac128b496a9e8a81b0d8d0d4fe3db60b90
    2c50fa74a12a810cc77fbe18124a6aaa3cacd7b829d048183f7e36ce7711
    7a3a04f43476feb782e4e79ae65a3ab4a5508806d58286ddcbcbdb6c96dc
    2da0d02d988f

*e*, repeated:

::

    ............00000003
    ....................010001

----------------

And now, the new stuff.  First, a candidate for the private exponent:

::

    ..........................00000100
    ..................................3c9e32ca6407cada7a5b3cf5fc
    0265bc3c3ccd97728633871b98f1c39d60b37faed4ed6ffa34159c35b27a
    229df91fe7c7c9f6f7a9733abf76263adf1356fbf88db325af18b3f14ea7
    21840557b8352984bbdc0ce6b5f43862a03ef9138128641860bb49cb2667
    5c56acfc0e29c4bd10353fbdbbcbf0ca858a9bf1cb42b0526110ae4b0315
    2c555d06ff2bd318477c45a2caf77672e732a79209602e669f6ebc5492f5
    f8a103c72b24b6c203d4211e4b84cded77155968df361b86ced780a66b7c
    2fe7943e395ed8b11cc8adad61e784f62b41559bc4bd23cb25af347e98c7
    5c3564d553de6984482f47fd875eee244c5edfc0449333a526fe4d6fbf54
    2886a9

something that turns out not to be either of our primes:

::

    ......00000080
    ..............402f0f3ac4ad8b61c36d6e6e0893c5476006dc2d54395b
    a58bf31f43731733bcca0c148bc2f9129bf49949b74859850be471936179
    99f3465a86aea1ccc67fd79c0d075cbafd1d1a0c3ff52eb80763a392e0af
    024a3c3c6cb81eb57aa5b26f5e0edb1571e1038d8742e823cdd54473a0e8
    291851612162f8da943bc3a12b5430

prime1 aka *p*:

::

    ..............................00000081
    ......................................00e075ab32affcb508cba9
    28cc1e7e53727435793f4033dda2949d6325ebab8617deff0b306127237c
    cb9357cee094177f2242dac37d0619ef89ffa9dcfc43bd3b25233e13713b
    107ba7fdceb2331499fe032b7771ce48e25af2c70e38875600b0f3f76dcd
    c25d91226ccf7f22370801c8d1844536d0a7c193345e4b05807f40fd

prime2 aka *q*:

::

                                                            0000
    0081
    ....00d0c55520133f638f4582f171c7de06036b1e8b8667a964ae3e26bb
    b9c2f85196485637f75e2cd6612c6c78f2682e23bc1b57b8f5f17e490ee8
    2379a53ff31b52b70bb998e8fe1cdbc4fa864810b60d0ba44a8d88718076
    cf7d6eb91d4b7bf7d792a16f3d7af726e402372cc528849ecb6e5a4bbed6
    865db0a0246d3e41c08b7b

followed by 22 bytes of data

::

    ......................0000001674656c6c696f7474406e65776d696e
    692e6c6f63616c01

and finally:

::

    ................01020304
    
-------------

In the first part, we obtained this for the modulus *n*:

::

    231..559

So to do the check I copied values from above for *p* and *q* and then ran ``python decode.py`` on each one and then pasted into the interpreter to check the multiplication.

The 81-byte value labeled "something?" was a candidate for prime1, but it turns out the next two values are prime1 and prime2

::

    00e075.. = 157..677
    00d0c5.. = 146..667

The product of these two *is* equal to the modulus.


>>> p*q==n
True


So if ``3c9e..`` is *d* equal to ``765..577``, then we can paste the full decimal output in and
check ``(d*e)%phi(n) = 1``

>>> phi = (p-1)*(q-1)
>>> e = 65537
>>> d*e % phi
1L

Yay!

There are some extra bits and pieces including "something?", but this has all checked out pretty nicely.

OpenSSL has a parsing tool but it throws an error with this key:

::

    > openssl asn1parse -inform pem -in kf
    0:d=0  hl=2 l= 112 cons: appl [ 15 ]       
    2:d=1  hl=2 l= 110 cons: appl [ 5 ]        
    Error in encoding..

------------

I compared two different new OpenSSH private keys.

The base64 was the same, which after decoding with the ``echo "" | base64 -d | xxd -p`` command gives:

:: 

    6f70656e7373682d6b65792d763100000000046e6f6e65000000046e6f6e
    65000000000000000100000117000000077373682d727361000000030100
    010000010100aecbc2f5a910ad6a95aeb169ca853d58127c

Notice that with the ``0000010100ae`` on the third line, we are into the modulus.  So the header data is constant, and then the first digits of the moduli are also the same.


