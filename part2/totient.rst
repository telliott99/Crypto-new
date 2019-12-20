###############
Euler's totient
###############

---
Phi
---

Euler's totient function is symbolized by ``phi(n)``.  

Phi gives the count of how many numbers in the set

.. math::

    \{ 1, 2, 3 \dots , n-1 \}
    
that is

.. math::

    a \in \mathbb{N} \ | \ a < n

share no common factors with ``n`` other than ``1``, i.e. that have a gcd with ``n`` equal to 1.  We include ``1`` in the count.

If ``n`` is prime, this is easy.  

For a prime ``p``, the only number that evenly divides ``p`` is ``1`` (and ``1`` always has a gcd of ``1`` with another integer), so the count of numbers less than ``p`` that have gcd ``= 1`` is ``p - 1``.

Otherwise, it gets harder.  

The fundamental theorem of arithmetic says that any number ``n`` has a *unique* prime factorization.

There is another theorem that says that if we have the prime factors of ``n``:

.. math::

    n = p_1 \cdot p_2 \cdot p_3 \dots
    
then

.. math::

    phi(n) = phi(p_1) \cdot phi(p_2) \cdot phi(p_3) \dots

This is true not just for primes, but for any two coprime factors of ``n``.  

That explains why we were able to write (in deriving an RSA key), that since ``n = p * q``:

.. math::

    phi(n) = (p-1)(q-1)

So if

.. math::

    phi(n) = phi(p_1) \ phi(p_2) \ phi(p_3) \dots
    
We can multiply and divide by the prime product equal to ``n`` and obtain

.. math::

    phi(n) = \frac{p_1 \ p_2 \dots}{p_1 \ p_2 \dots} (p_1 - 1) \ (p_2 - 1) \ \dots
    
    phi(n) = n(p_1 - 1/p_1)(p_2 - 1/p_2) \ \dots

I found a nice write-up of this here:

http://www.claysturner.com/dsp/totient.pdf

In the write-up he sketches a proof of the last line above, and you can follow it backward to what we were given:

.. math::

    phi(n) = phi(p_1) \cdot phi(p_2) \cdot phi(p_3) \dots

-------
Example
-------

Consider ``n = 30``.

If we run Euclid's algorithm on ``1 < m < 30``:

>>> from gcd import gcd
>>> for i in range(2,30):
...     if gcd(30,i) == 1:
...          print(i)
... 
7
11
13
17
19
23
29
>>> 

The set we seek is ``{ 1, 7, 11, 13, 17, 19, 23, 29 }``.

These are the numbers that are not included in the Venn circles:

.. image:: /_static/fermat-30.png
   :scale: 75 %

The prime factors of ``30`` are ``2``, ``3`` and ``5``.  

We can divide :math:`1 \le m \le n` into several sets:

- ``n``
- prime factors of ``n``:  ``2``, ``3`` or ``5``

plus

- gcd equal to a single prime factor
- gcd equal to a product of prime factors

and last

- 1
- prime, not a factor of ``n``

What we are trying to count is the last group.

Let

- A be the set of integers that 2 divides into evenly, including ``n``
- B be the set .. 3 
- C be the set .. 5

We want to find the count or size of the set of all the numbers that are not in A, B or C (the numbers listed along the bottom of the figure).

This is

::

    sizeof ~(A U B U C)
    
where ``~`` symbolizes the complement of the set, those elements not in the given set, and ``U`` is set union.

There is a famous theorem in set theory that says: 

::

    ~(A U B U C) = ~A ^ ~B ^ ~C

``^`` is set intersection.

so we write that we want is the size of the right-hand side.

-----------
Probability
-----------

It is somewhat surprising, but we can easily calculate the probability that a number is in the set ``~A``.  

Consider the set including ``2`` and all its multiples.  The probability that a number ``<= 30`` is contained in the complement of that set is ``1 - 1/2``, times ``30``.  Similarly, for ``~B``, the probability is ``1 - 1/3`` times ``30`` and so on.

The total probability is the product of the individual probabilities.

And that total probability, times ``n``, is equal to the count.

Thus

::

    phi(30) = sizeof (~A ^ ~B ^ ~C)
    = 30·(1 - 1/2) * (1 - 1/3) * (1 - 1/5)
    
And generalizing

::

    phi(n) = n * (1 - 1/p_1) * (1 - 1/p_2) \dots
    
which is what we needed to prove.  This can be rewritten as

::

    phi(n) = (p_1 - 1) * (p_2 - 1) \dots

