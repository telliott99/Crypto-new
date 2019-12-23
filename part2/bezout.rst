#################
Bezout's Identity
#################

There is a preliminary result that we will need.

-----------------------
Quotient Remainder Rule
-----------------------

    Given integers :math:`a \in \mathbb{Z}` and :math:`b \in \mathbb{N_1}`, there are unique integers *q* and *r* such that (i) a = qb + r, and (ii) :math:`0 \le r < b`.

The proof of this is surprisingly long-winded and I will not bother with it.  Although the definition above doesn't require it, we suppose that *a > 0* and *b > 0* and :math:`b < a`.

Rewrite:

.. math::

    a - qb = r

We see that zero or more copies of *b* can be subtracted from *a* while the result remains :math:`\ge 0`.  If *r = 0* then we say that *b* divides *a*, :math:`b|a`.

In any event, the theorem says that *q* and *b* exist with :math:`0 \le r < b`.  We use that below.

Suppose that *a < 0* (and ecall that *b > 0*).  Then *q < 0*, and we add *q* copies of *b*, sufficient to be in the correct range :math:`[0..b)`.

The remainder of :math:`-2 / 3` is *1*.

------
Bezout
------

    Let *a* and *b* be integers with greatest common divisor *d*. Then, there exist non-zero integers *x* and *y* such that 

.. math::

    ax + by = d

--------
Examples
--------

Suppose :math:`a = 6` and :math:`b = 10`.  Then, :math:`d = 2` and so we want 

.. math::

    6x + 10y = 2
    
Obviously, either :math:`x < 0` or :math:`y < 0`.  One solution is :math:`x = 2, y = -1`.  Another one is :math:`x = -3, y = 2`.

More generally, the integers of the form :math:`ax + by` are exactly the multiples of *d*.

Corollary:

    *x* and *y* are coprime if and only if there exist integers *a* and *b* such that

.. math::

    ax + by = 1

That is, if the the gcd *(x,y) = 1*, we can find *a* and *b* with this property.  For example, if :math:`a = 6` and :math:`b = 5` then we can find

.. math::

    6x + 5y = 1
    
A simple solution is :math:`x = 1, y = -1`.

An application is that if

.. math::

    6x + 5y = 1

.. math::

    6x = 1 - 5y
    
then (mod *y*):

.. math::

    6x = 1
    
That is, *x* is the multiplicative inverse of *x* mod *y*.

-----
Proof
-----

This proof is a bit challenging at the critical step.  We follow `Aitken <https://public.csusm.edu/aitken_html/m422/Handout1.pdf>`_.  Another source is `Hefferon <http://joshua.smcvt.edu/numbertheory/book.pdf>`_.  

Restatement:

- let *a* and *b* be integers, not both zero
- form a linear combination :math:`sa + tb`
- there is a least positive such combination with value *d*
- there is also a greatest common divisor or :math:`gcd(ab) = g`
- the theorem says that :math:`g = d`

-----

D1.  A common divisor of *a* and *b* is an integer that divides both *a* and *b*.

D2.  A linear combination is :math:`sa + tb`, such that :math:`s,t \in \mathbb{Z}`

P3.  Let *d* be a common divisor of :math:`a,b`, then :math:`d \ | \ sa + tb`.

Proof: we have *a = dk* and *b =dl* for some integer *k* and *l* so

.. math::

    sa + tb = s(dk) + t(dl) = d(sk + tl)

P4.  If *a* and *b* are both non-zero, then the GCD exists.

Proof:  Suppose :math:`a \ne 0` and *S* is the set of common divisors.  :math:`1 \in S`.
    
- *S* is not empty since :math:`1 \in S`
- the maximum element of *S* is :math:`|a|`
- Therefore *S* has a maximum *d* and :math:`d \ge 1`

P5.  There is a *least* positive integer combination :math:`sa + tb`.

Proof:  For convenience suppose :math:`a \ne 0`.  Let *S* be the set of positive linear combinations.

- clearly, :math:`|a| \in S`
- S is not empty
- S has a minimum

Here is the tricky part.

-----
Lemma
-----

If :math:`a \ne 0` and :math:`b \ne 0`, then the least positive linear combination of *a* and *b* is a common divisor of *a* and *b*.

Proof:  let :math:`m = sa + tb` be the least positive linear combination of *a* and *b*.

Using the Quotient Remainder Rule write :math:`a = qm + r`.  So

.. math::

    r = a - qm

.. math::

    r = a - q(sa + tb)

.. math::

    r = a(1 - qs) - qtb

The quotient rule defines :math:`0 \le r < m`.

- r is non-negative
- *r* is a linear combination (above)
- but *m* is the smallest positive linear combination

Therefore :math:`r = 0`.

Since *r = 0*, *a = qm* and therefore :math:`m|a`.  

Similarly, :math:`m|b`.  *m* is a common divisor of *a* and *b*.

-------
Theorem
-------

T7.  (Bezout's Identity).  If *a* and *b* are not both zero, then the least positive linear combination of *a* and *b* is equal to their greatest common divisor.

Proof:  let *m* be the least positive linear combination, and let *g* be the GCD.

- :math:`g|m` by Proposition 3, which means that :math:`g \le m`
- by the lemma, *m* is a common divisor
- the greatest common divisor is *g*, so :math:`g < m` cannot be true

Therefore, :math:`g = m`.



