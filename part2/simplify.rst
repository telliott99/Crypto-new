.. _part2/simplify:

################
RSA calculations
################

In the theory of RSA encryption and decryption, we choose two primes *p* and *q* and compute their product *n = pq*, as well as Euler’s totient *φ(n) = (p-1)(q-1)*.

We pick a public exponent *e*, which is co-prime to *φ(n)*, and the usual choice is ``65537 = 0x101 = 0b1 00000000 00000001``.

We must also find *d* such that it is the multiplicative modular inverse of *e*:

.. math::

    d = e^{-1} \ mod \ φ(n)

This is done using the extended Euclidean algorithm for gcd (greatest common divisor).  The above equation is equivalent to:

.. math::

    e \cdot d = 1 \ mod \ φ(n)

With these definitions, it can be shown that

.. math::

    (m^e)^d = (m^d)^e = m \ mod \ n

This is the basis of asymmetric encryption and decryption.

It makes life easy if *e* has very few binary ones, which explains the choice we made above.  However, *d* is determined from *e* and *φ(n)*, and computing

.. math::

   x^d \ mod \ n

is hard.  (``x`` is either the plaintext message or its encryption with the public key).

---------
Shortcuts
---------

The Chinese Remainder Theorem tells us that for each ``x`` in the range ``[1..n-1]`` there is a unique pair or tuple ``(x mod p-1, x mod q-1)``.

Some smart guy figured out that, not only is the result uniquely identified by that tuple, but it can be calculated from it.

So, just as with ``φ(n)``, we calculate the multiplicative modular inverse of *e* with *(p-1)* and *(q-1)*.  These are called 

.. math::

    dP = e^{-1} \ mod \ (p-1)

.. math::

    dQ = e^{-1} \ mod \ (q-1)

Note that

.. math::

    dP \cdot e = 1 \ mod \ (p-1)

.. math::

    dQ \cdot e = 1 \ mod \ (e-1)

We also need the inverse of *q* with respect to *p*

.. math::

    qInv = q^{-1} \ mod \ p

To do the calculation, first find

.. math::

    x_1 = x^{dP} \ mod \ p

.. math::

    x_2 = x^{dQ} \ mod \ q

Then

.. math::

    x = x_2 + h \cdot q

where

.. math::

    h = (x_1 - x_2) \cdot qInv \ mod \ p

-------
Example
-------

It's nice to find a worked out example that tests for errors:

https://www.di-mgt.com.au/crt_rsa.html

Suppose

::

    p = 137
    q = 131
    n = 17947
    φ = 16680
    e = 3

Compute *d* using ``mod.py`` (and then just check it):

::

    d = 11787

So then

.. math::

    dP = e^{-1} \ mod \ (p-1)
    
.. math::

    dP = e^{-1} \ mod \ (q-1)
    

::

    dP = 91
    dQ = 87

and finally

.. math::

    qInv = q^{-1} \ mod \ p

::

    qInv = 114

Having chosen a message with value ``m = 513``, to encrypt:

.. math::

    c = (m^e) \ mod \ n

::

    m = 513
    c = 513^3 mod 17947 = 8363

-----------
Calculation
-----------

Decrypt by

::

    8363^11787 mod 17947 = 513

The intermediate exponentiation result ``8363^11787`` has ``46233`` digits.  It goes pretty quickly on my computer, but still..


The shortcut is as follows:

.. math::

    m_1 = c^{dP} \ mod p

::

    m1 = 8363^91 \ mod 137 = 102

Here, the exponentiation result has 357 digits.

.. math::

    m_2 = c^{dQ} \ mod q

::

    m2 = 8363^87 \ mod 131 = 120

Since ``m2 > m1`` the difference is negative, therefore add an extra ``p``:

::

    m1 - m2 = -18;  + 137 = 119

Multiply by ``qInv``:

:: 

    h = qInv.(m1-m2) mod p = 114 x 119 mod 137 = 3

So the result is

::

    m = m2 + h.q = 120 + 3(131) = 513

It works!

