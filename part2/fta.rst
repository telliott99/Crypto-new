#################################
Fundamental Theorem of Arithmetic
#################################

--------------
Euclid's lemma
--------------

Every natural number *n*, every positive integer greater than *1*, is either prime or it is the product of two smaller natural numbers *a* and *b*

But the same is true of *a* and *b* in turn.

Therefore, every number is the product of the prime factors of *a* times the prime factors of *b*.  

If a given prime *p* divides *n* then either *p* divides *a* or *p* divides *b* or both.

-----
Proof
-----

The proof is by induction.  

Assume the lemma is true for all numbers between *1* and *n* (e.g. it is certainly true for :math:`n < 13`).  If *n* is prime there is nothing to prove and we move to *n + 1*.  

If *n* is not prime, then there exist integers *a* and *b* (with :math:`1 < a \le b < n`) such that :math:`n = a \times b`.

By the induction hypothesis, since *a < n* and *b < n*, *a* has prime factors :math:`p_1 p_2 \dots` and *b* has prime factors :math:`q_1 q_2 \dots` so

.. math::

    n = ab = p_1 p_2 \dots q_1 q_2 \dots

This shows that there exists a prime factorization of *n*.

----------
Uniqueness
----------

To show that the prime factorization is unique suppose that *n* is the smallest integer for which there exist two different factorizations:

.. math::

    n = p_1 p_2 \dots = q_1 q_2 \dots
    
Pick the first factor :math:`p_1`.  Since :math:`p_1` divides :math:`n = q_1 q_2 \dots`, by Euclid's lemma, it must divide some particular :math:`q_j`.  Rearrange the :math:`q` so that :math:`q_j` is first.

But since :math:`p_1` divides :math:`q_1` and both are prime, it follows that :math:`p_1 = q_1`. 

Now continue the same process with all the factors :math:`p_i`.

As wikipedia says now:

    This can be done for each of the *m* :math:`p_i`'s, showing that :math:`m \le n` and every :math:`p_i` is some :math:`q_j`. Applying the same argument with the p and q reversed shows :math:`n \le m` (hence :math:`m = n`) and every :math:`q_j` is a :math:`p_i`.
    
-----
Hardy
-----

Hardy and Wright (*Theory of Numbers*, sect. 2:11) have a second proof, which is given here (almost) verbatim:

Let us call numbers which can be factored into primes in more than one way, *abnormal*, and let *n* be the smallest abnormal number.

**Different factorization**

The same prime *P* cannot appear in two different factorizations of *n*, for, if it did, *n/P* would be abnormal and yet :math:`n/P < n`, the smallest abnormal number.

Thus, we have that

.. math::

    n = p_1 p_2 \dots = q_1 q_2 \dots
    
where the *p* and *q* are primes, and no *p* is a *q* and no *q* is a *p*.

If there exist abnormal numbers with two such factorizations, they must be completely different.

**Contradiction**

We may take :math:`p_1` to be the least *p*.  Since *n* is composite, :math:`p_1^2 \le n`.

The same is true for :math:`q_1` and (since :math:`p_1 \ne q_1`, we have that :math:`p_1 q_1 < n`)

Hence, if :math:`N = n - p_1 q_1`, we have :math:`0 < N < n` and also that *N* is not abnormal.

Now :math:`p_1 | n` and since :math:`N = n - p_1 q_1`, so :math:`p_1 | N`.

Similarly :math:`q_1 | N`.  Hence :math:`p_1` and :math:`q_1` both appear in the unique factorizations of both *N* and :math:`p_1 q_1`.

From this it follows that :math:`p_1 q_1 | n` and hence :math:`q_1 = n/p_1`.  But :math:`n/p_1` is less than *n* and has the unique prime factorization :math:`p_2 p_3 \dots`.

Since :math:`q_1` is not a *p*, this is impossible.  Hence there cannot be any abnormal numbers and this is the fundamental theorem.









