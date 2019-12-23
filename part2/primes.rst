######
Primes
######

All the numbers in this document are integers.  Most of them are the positive integers or counting numbers:  :math:`1,\ 2,\ 3 \dots`.

The number *d* divides the number *n* if there is a *k* such that 

.. math::

    n = d k 

We say that *d* is a factor of *n*, *n* is evenly divisible by *d*, or *n* is a multiple of *d*.

As you know, prime numbers have only two factors, themselves and *1*, since :math:`1 \cdot n = n` is true for any number.

Primes can be enumerated by a number of algorithms, one of the most famous is called the `Sieve of Eratosthenes <https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>`_.

Numbers that are not prime are called composite.  Two composite numbers or one such number and a prime number may be coprime:  we say this if they have no factors in common.  We may say that their **greatest common divisor** or *gcd*, is equal to *1*.

The number *1* is neither prime, nor composite.

Consider two different numbers, both having *p* as a prime factor.

.. math::

    n = jp \\

    m = kp

The difference :math:`n - m = p(j-k)` is also divisible by *p*.

Probably the most famous theorem about primes is this:

----------------
Infinite theorem
----------------

The theorem, in Euclid, is that there exists an infinite number of primes.

-----
Proof
-----

We suppose the opposite, that there is not an infinite number of primes.

At least in principle, we can write all the primes in increasing order as a product:

.. math ::

    2 \cdot 3 \cdot 5 \dots p_{max} = P

Now add *P + 1*. 

It is clear that none of the primes in our list can divide ::math:`P + 1` evenly.  

If one did then it would also have to evenly divide the difference :math:`(P + 1) - P = 1`, which is impossible.

So then one of two things is true:

- *P+1* is prime
- another prime, not in our list, divides *P+1*

In any case, this list does not include all the primes.

-------------------
Prime factorization
-------------------

Every number can be decomposed into a set of prime factors:

.. math::

    n = p_1 \cdot p_2 \dots

There is only one such decomposition.

This is called the **fundamental theorem of arithmetic**, and we will prove it next.

Two numbers are **coprime** if they do not share any prime factors.  As we'll see, there is an algorithm from Euclid for determining the greatest common divisor of two factors.  If the gcd(*a,b*) is equal to *1*, then they are coprime.

--------
Notation
--------

If *a* divides *n* evenly with no remainder, write

.. math::

    a | n
