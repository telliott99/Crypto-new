.. _part2/simplify:

################
RSA calculations
################

In the theory of RSA encryption and decryption, we choose two primes *p* and *q* and compute their product *n = pq*, as well as Euler’s totient *phi(n) = (p-1)(q-1)*.

We pick a public exponent *e*, which is co-prime to *phi(n)*, and the usual choice is ``65537 = 0x101 = 0b1 00000000 00000001``.

We must also find *d* such that it is the multiplicative modular inverse of *e*:

.. code-block:: python

    d = e^{-1} % phi(n)

This is done using the extended Euclidean algorithm for gcd (greatest common divisor).  The above equation is equivalent to:

.. code-block:: python

    e \cdot d = 1 % phi(n)

With these definitions, it can be shown that

.. code-block:: python

    (m^e)^d = (m^d)^e = m % n

This is the basis of asymmetric encryption and decryption.

It makes life easy if *e* has very few binary ones, which explains the choice we made above.  However, *d* is determined from *e* and *phi(n)*, and computing

.. code-block:: python

   x^d % n

is hard.  (``x`` is either the plaintext message or its encryption with the public key).

---------
Shortcuts
---------

The Chinese Remainder Theorem tells us that for each ``x`` in the range ``[1..n-1]`` there is a unique pair or tuple ``(x mod p-1, x mod q-1)``.

Some smart guy figured out that, not only is the result uniquely identified by that tuple, but it can be calculated from it.

So, just as with ``phi(n)``, we calculate the multiplicative modular inverse of *e* with *(p-1)* and *(q-1)*.  These are called 

.. code-block:: python

    dP = e^{-1} % (p-1)

.. code-block:: python

    dQ = e^{-1} % (q-1)

Note that

.. code-block:: python

    dP \cdot e = 1 % (p-1)

.. code-block:: python

    dQ \cdot e = 1 % (e-1)

We also need the inverse of *q* with respect to *p*

.. code-block:: python

    qInv = q^{-1} % p

To do the calculation, first find

.. code-block:: python

    x_1 = x^{dP} % p

.. code-block:: python

    x_2 = x^{dQ} % q

Then

.. code-block:: python

    x = x_2 + h \cdot q

where

.. code-block:: python

    h = (x_1 - x_2) \cdot qInv % p

-------
Example
-------

It's nice to find a worked out example that tests for errors:

https://www.di-mgt.com.au/crt_rsa.html

Suppose

.. code-block:: python

    p = 137
    q = 131
    n = 17947
    phi = 16680
    e = 3

Compute *d* using ``mod.py`` (and then just check it):

.. code-block:: python

    d = 11787

So then

.. code-block:: python

    dP = e^{-1} % (p-1)
    
.. code-block:: python

    dP = e^{-1} % (q-1)
    

.. code-block:: python

    dP = 91
    dQ = 87

and finally

.. code-block:: python

    qInv = q^{-1} % p

.. code-block:: python

    qInv = 114

Having chosen a message with value ``m = 513``, to encrypt:

.. code-block:: python

    c = (m^e) % n

.. code-block:: python

    m = 513
    c = 513^3 mod 17947 = 8363

-----------
Calculation
-----------

Decrypt by

.. code-block:: python

    8363^11787 % 17947 = 513

The intermediate exponentiation result ``8363^11787`` has ``46233`` digits.  It goes pretty quickly on my computer, but still..


The shortcut is as follows:

.. code-block:: python

    m_1 = c^{dP} % p

.. code-block:: python

    m1 = 8363^91 % 137 = 102

Here, the exponentiation result has 357 digits.

.. code-block:: python

    m_2 = c^{dQ} % q

.. code-block:: python

    m2 = 8363^87 % 131 = 120

Since ``m2 > m1`` the difference is negative, therefore add an extra ``p``:

.. code-block:: python

    m1 - m2 = -18;  + 137 = 119

Multiply by ``qInv``:

.. code-block:: python 

    h = qInv * (m1-m2) % p = 114 * 119 % 137 = 3

So the result is

.. code-block:: python

    m = m2 + h * q = 120 + (3) * 131 = 513

It works!

