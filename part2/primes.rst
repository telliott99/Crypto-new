###############
Infinite primes
###############

We don't need this, but it is probably the most famous proof about primes.

----------------
Euclid's theorem
----------------

There is an infinite number of primes.

-----
Proof
-----

We suppose that there is not an infinite number of primes.

Then, there is a finite number of primes, and at least in principle, we could write all the primes in increasing order as a product:

.. math ::

    P = 2 \cdot 3 \cdot 5 \dots p_{max}

Now add *P + 1*.  

It is clear that none of the primes in our list can divide *P + 1* evenly.  

If one did then it would also have to evenly divide the difference :math:`(P + 1) - P = 1`, which is impossible.

So then one of two things is true:

- *P+1* is prime
- another prime, not in our list, divides *P+1*

In any case, our list does not include all the primes.