.. count:

#############################
Derivation of Euler's totient
#############################

Euler's totient function is symbolized by ``phi(n)``.  

It gives the count of how many numbers in the set ``1..n-1`` have a gcd with ``n`` equal to ``1`` (thus, it includes ``1``).  For a prime number ``p``, ``phi((p) = p-1``.

We will sketch a proof to show that if ``n`` has a prime factorization

.. math::

    n = p_1 \cdot p_2 \dots

then

.. math::
    
    phi(n) = n(p_1 - 1/p_1)(p_2 - 1/p_2) \ \dots

I found a nice write-up of this here:

http://www.claysturner.com/dsp/totient.pdf

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

We can divide ``1 <= m <= n`` into several categories:

- 1
- ``n``
- prime factor of ``n``

plus

- gcd equal to a single prime factor:  ``2``, ``3`` or ``5``
- gcd equal to any multiple of prime factors
- prime, not a factor of ``n``

Now, what we are trying to count is the last line plus ``1``, but what we will count are all the prime factors plus every number in this set 

- gcd equal to a single prime factor:  ``2``, ``3`` or ``5``

We must not double-count:

- gcd equal to any multiple of prime factors

plus ``n``, and then subtract that from ``30``.

Let

- A be the set of integers that 2 divides into evenly, plus ``n``
- B be the set .. 3 
- C be the set .. 5

We want to find the count or size of the set of all the numbers that are not in A, B or C (the numbers listed along the bottom of the figure).

This is

::

    sizeof ~(A U B U C)
    
where ``~`` symbolizes the complement of the set, those elements not in the given set.

There is a famous theorem in set theory that says: 

::

    ~(A U B U C) = ~A ^ ~B ^ ~C

so we write that we want

::

    sizeof ~A ^ ~B ^ ~C

(where ``^`` is an ASCII symbol close enough to "intersection.")
    
-----------
Probability
-----------

It is somewhat surprising, but we can calculate ``~A``.  Consider the set including ``2`` and all its multiples.  The probability that a number ``<= 30`` is contained in the complement of that set is ``1 - 1/2``, times ``30``.  Similarly, for ``~B``, the probability is ``1 - 1/3`` times ``30`` and so on.

The total probability is the product of the individual probabilities.

And that total probability, times ``n``, is equal to the count.

Thus

::

    phi(30) = sizeof (~A ^ ~B ^ ~C)
    = 30·(1 - 1/2)(1 - 1/3)(1 - 1/5)
    
And generalizing

::

    phi(n) = n·(1 - 1/p_1)(1 - 1/p_2) \dots
    
which is what we needed to prove.  This can be rewritten as

::

    phi(n) = (p_1 - 1)(p_2 - 1) \dots

    







