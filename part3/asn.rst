.. _part3/asn:

###############
ASN.1, DER, PEM
###############

-----
ASN.1
-----

wikipedia:

"Abstract Syntax Notation One (ASN.1) is a standard interface description language for defining data structures that can be serialized and deserialized in a cross-platform way. It is broadly used in telecommunications and computer networking, and especially in cryptography."

example:

::

    FooProtocol DEFINITIONS ::= BEGIN

        FooQuestion ::= SEQUENCE {
            trackingNumber INTEGER,
            question       IA5String
        }
    
        FooAnswer ::= SEQUENCE {
            questionNumber INTEGER,
            answer         BOOLEAN
        }

    END

---
DER
---

Any particular example must be encoded.  So there are a variety of codecs or encoding and decoding rules including the very common:  DER, distinguished encoding rules.

example:

::

    FooProtocol DEFINITIONS ::= BEGIN
    
        FooQuestion ::= SEQUENCE {
            trackingNumber INTEGER(0..199),
            question       IA5String
        }
    
        FooAnswer ::= SEQUENCE {
            questionNumber INTEGER(10..20),
            answer         BOOLEAN
        }
    
        FooHistory ::= SEQUENCE {
            questions SEQUENCE(SIZE(0..10)) OF FooQuestion,
            answers   SEQUENCE(SIZE(1..10)) OF FooAnswer,
            anArray   SEQUENCE(SIZE(100))  OF INTEGER(0..1000),
            ...
        }
    
    END

The DER version of an RSA key will contain binary data.  As a result, another format is very common, namely

---
PEM
---

The PEM format is often used to encapsulate DER-encoded ASN.1 certificates and keys in an ASCII-only format. The PEM version of a DER message consists of the base64 encoding of the DER message, preceded by "-----BEGIN FOO-----" and followed by "-----END FOO-----," where "FOO" may indicate "CERTIFICATE," "PUBLIC KEY," "PRIVATE KEY" or many other types of content.

----------

------
Parser
------

OpenSSL has an ASN.1 parser.  But it doesn't seem to work on OpenSSH keys.  And in any case, it's not real informative:

::

    > openssl genpkey -algorithm rsa > kf
    ..............................................+++
    .................+++
    > openssl asn1parse -inform pem -in kf
        0:d=0  hl=4 l=1213 cons: SEQUENCE          
        4:d=1  hl=2 l=   1 prim: INTEGER           :00
        7:d=1  hl=2 l=  13 cons: SEQUENCE          
        9:d=2  hl=2 l=   9 prim: OBJECT            :rsaEncryption
       20:d=2  hl=2 l=   0 prim: NULL              
       22:d=1  hl=4 l=1191 prim: OCTET STRING      [HEX DUMP]:308204A3