.. _part2/math:

################
Math of RSA keys
################

**Overview**

We're exploring public-key cryptography. One first generates a pair of keys called the public key and a corresponding private (i.e. secret) key. 

These have a symmetry property, such that if either one is used to encrypt a message, then the other one can be used to decrypt the ciphertext and recover the plaintext.

Suppose that Alice generates a public/private key pair and then distributes the public key in such a way that Bob is certain that he really knows Alice’s public key.

Bob can encrypt a message with Alice's public key and send it to Alice with the knowledge that only Alice can decrypt it using her private key. 

Alternatively, Alice can encrypt a message with her private key and send it to Bob. Successful decryption with Alice’s public key proves that the message is from Alice.

The process of encryption and decryption is computationally expensive, and only short messages should be exchanged by this method. Such a message would typically consist of yet another key which can be used to encode the main message by a different protocol.

**Two primes**

Key generation starts with two prime numbers, *p* and *q*. 

For a first example, I obtained two such numbers from a `list <http://primes.utm.edu/lists>`_ of primes (near the 50 millionth prime):

The prime numbers for real-world use are much larger than this.

Python code:

.. code-block:: python

    p = 961748941
    q = 982451653
    n = p*q
    
If you paste the lines above into the Python interpreter, you should be able to query the value of *n* like this:

>>> n
944871836856449473
>>> len(bin(n))
62
>>>

This means we can securely encode not more than about 62 bits. 

A note on notation:  standard mathematics uses these two symbols for multiplication and exponentiation:

.. math::

    a \times b

.. math::

    a^e

We'll be using Python a lot, so we'll use the Python notation.  Multiplication is ``a * b`` and exponentiation is ``a ** e``.  The remainder from division, or modulus operator, is ``a % b``.

**Phi**

We're going to find three other numbers in order to use this method, one is called *phi* or sometimes  *phi(n)* since it depends on the numbers *p* and *q*.  We wouldn't mind using the Greek letter phi, but it's not part of ASCII and the LaTeX to PDF typesetter doesn't support it.

The other two values are called the exponents.  The *exponent of the private key*, *d*, depends on phi.  

We also need to choose *e*, the *exponent of the public key*.

.. code-block:: python

    phi = (p-1)*(q-1)

>>> phi 
944871834912248880
>>>

Now choose *e* such that:  

.. math::

    1 < e < phi

with the requirement that *e* should be coprime to phi, (they should have no common factor other than 1).

While we could factor phi, the easiest way to do this is to pick a prime number like 

.. math::

    e = 2^{16} + 1 = 65537
    
Note that 65537 is `10000001` in binary.

I also confirmed that *e* is on a list of primes:

http://primes.utm.edu/lists/small/10000.txt

To test tha phi and *e* are coprime, we show that the prime number *e* is not a factor of phi, i.e. that there is a remainder when dividing:

>>> phi
944871834912248880
>>> e = 2**16 + 1
>>> e
65537
>>> phi % e
42186
>>>

The public key is then (*n*, *e*).

Actually, in practice, there is little variation in *e*.  It is typically the same value as used here, 65537.  According to Laurens Van Houtven's *Crpto 101*:

https://www.crypto101.io

*e* is either 65537 or 3, and this is because there are very few binary ``1``'s in these numbers (only two single digits ``1``), and as a result the exponentiation which we will compute *a lot*

``m**e``

is much more efficient.

65537 in binary is ``10000 0000 0000 0001``.  Thus to obtain ``m^e``, just left-shift *m* by 16 and add that to the original value of *m* that we started with. 

The private key consists of *n* plus another number *d* which is computed from phi and so, as we said, requires knowledge of *p* and *q*. 

That is why the process of breaking this method of encryption is described as being the same as the problem of finding two primes that can factor a large number:  *n*, the product of the primes *p* and *q*. *n* is known from the public key.

**Encryption**

The encryption function we will use is

.. math::

    c = m^e mod \ n

.. code-block:: python

    m = 920321254041092
    e = 65537
    n = 944871836856449473
    x = m**e
    
>>> len(str(x))
980692
>>> c = x % n
>>> c
448344912451359241L
>>>

The number *c* is our ciphertext. (The L on the end signifies a Python long, a type of number).

:math:`x = m^e` is a very large number!  Its decimal representation has nearly one million digits.

It is much more efficient to do the mod operation at the same time as the exponentiation. The Python built-in function ``pow`` allows that as an option:

>>> pow(m,e,n)
448344912451359241L
>>>

**Decryption**

We still need one more number to decode the encrypted text. This number is called *d*, the *exponent of the private key*. 

The private key is (*d*, *n*), although just the *d* part is actually secret. Finding *d* is the tricky part of the whole operation, but it only needs to be computed once for a given key pair.

*d* is called the modular multiplicative inverse of *e* (mod *(n)*). 

What this means is that we want *d* such that

``d × e = 1 (mod phi(n))``

Substituting the known values for *e* and *phi(n)*

``d × 65537 = 1 (mod 944871834912248880)``

Without worrying about the details, the method for doing this is the extended Euclidean algorithm for greatest common divisor.  Given two numbers *a* and *b*, the egcd gives us *x* and *y* such that

.. math::

    ax + my = gcd(a,m)

So if the gcd is equal to 1 (and *e* and *phi* have been chosen with this in mind), then 

.. math::

    ax - 1 = (-y)m

that is,

.. math::

    ax = 1 \ (mod \ m)

Thus, *x* is the multiplicative inverse of *a*, mod *m*.

`Here is <https://planetcalc.com/3311/>`_ an online calculator.  It appears to give the wrong answer!

I found an implementation for computing *d* `here <http://stackoverflow.com/questions/4798654>`_.  We'll talk about this more in a separate chapter.

.. code-block:: python

    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b \% a, a)
            return (g, x - (b // a) * y, y)

.. code-block:: python

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception("modular inverse does not exist")
        else:
            return x % m
            
It is easy to show that this code does work. I saved it in a file ``mod.py``. Let’s try it out:

.. code-block:: python

    from mod import modinv
    e = 65537
    phi = 944871834912248880
    d = modinv(e,phi)

Output:

>>> d
8578341116816273
>>> d*e % phi
1L
>>>

So, having found *d*, now we are finally ready to decrypt:

.. code-block:: python

    c = 448344912451359241
    n = 944871836856449473
    d = 8578341116816273
    p = pow(c,d,n)

>>> p 
920321254041092L
>>>

Recall

>>> m
920321254041092

We have successfully generated a key pair, and used it to encrypt and decrypt a simple message. Now we need to show that we can also encrypt with private key, and decrypt with public one:

.. code-block:: python

    m = 920321254041092
    d = 8578341116816273
    n = 944871836856449473
    c = pow(m,d,n)
    
>>> c
461000660869754451L
e = 65537
p = pow(c,e,n)
>>> p
920321254041092L

We have again recovered our plaintext message: *p* is equal to *m*.
