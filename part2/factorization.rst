#############
Factorization
#############

If *p* is a prime and

.. math::

    p|ab

then either :math:`p|a` or :math:`p|b` (or both).

Note that this is not necessarily true for non-primes.  For example, :math:`6 \cdot 10 = 60 | 4` but neither :math:`6 | 4` nor :math:`10 | 4`.  This happens because *2* is a prime factor of both *6* and *10*, generating a factor of *4* in the product.

----------------------
Proof of Factorization
----------------------

Now, suppose *p* is prime and and :math:`p | ab` but :math:`p \not| a` and :math:`p \not| b`.  The symbol :math:`\not|` looks a little funny but it simply means "does not evenly divide".

Then Bezout says that there exist integers such that

.. math::

    ah + pk = 1

.. math::

    bH + pK = 1
    
so

.. math::

    1 = (ah + pk)(bH + pK)
    
.. math::

    1 = ahbH + ahpK + pkbH + p^2kK
    
.. math::

    1 = ab(hH) + p(ahK + kbH + pkK)
    
Since :math:`p | ab`, *p* divides the right hand side.

But this means that :math:`p | 1`.  But this is absurd.  

Therefore, it is not true that :math:`p \not| a` and :math:`p \not| b`, so *p* divides at least one of *a* and *b*.

----------------------
Multiplicative inverse
----------------------

*a* is the multiplicative inverse of *b* (mod *n*) if

.. math::

     ab = 1 \ mod \ n

Obviously, *a* and *b* must be coprime to *n*.

If *p* is prime, then **every**  :math:`1 < a < p` has a multiplicative inverse (mod *p*).


----------------
Wilson's theorem
----------------

Let *p* be prime.  Then

.. math::

    (p-1)! = -1 \ mod \ p

-----
Proof
-----

If *p* is prime, then :math:`x < p` may be its own multiplicative inverse. 

.. math::

    x^2 = 1 \ mod \ p 

However, this happens only if

.. math::

    x^2 - 1 = 0 \ mod \ p 

.. math::

    (x - 1)(x + 1) = 0 \ mod \ p

That is, :math:`x - 1 = 0` mod *p* or :math:`x + 1 = 0`, mod *p*.

But the only numbers in ``[1..p]`` for which this can be true are *1* and *p-1*.  No other number can be its own multiplicative inverse.

And *that* means that for every factor in the product 

.. math::

    (p-1)! = 1 \times 2 \dots \times (p-1)

For nearly all the factors in the factorial the multiplicative inverse is also present, and the pair then contribute only *1* to the product (mod *p*).

The exceptions *1* and *(p-1)* are their own inverses.  The result follows.

    


