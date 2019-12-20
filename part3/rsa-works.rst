.. rsa-works:

#############
Why RSA works
#############
phi
I found a nice write-up of this here:

http://www.claysturner.com/dsp/totient.pdf

We'll attempt a high-level sketch of how/why RSA works here.  At some point in the future, perhaps I'll fill in the details.

---------------
Euler's Totient
---------------

Euler's totient function is symbolized by ``phi(n)``.  It gives the count of how many numbers in the set

.. math::

    \{ 1, 2, 3 \dots , n-1 \}
    
that is

.. math::

    a \in \mathbb{N} \ | \ a < n

share no common factors with ``n`` other than ``1``, i.e. that have a gcd with ``n`` equal to 1.  We then also include ``1`` in the count.

If ``n`` is prime, this is easy.  

For a prime ``p``, ``phi(p) = p - 1``.  

The only number that evenly divides ``p`` is ``1`` (and ``1`` always has a gcd of ``1`` with another integer), so the count of numbers less than ``p`` that have gcd ``= 1`` is ``p - 1``.

Otherwise, it gets harder.  The fundamental theorem of arithmetic says that any number ``n`` has a *unique* prime factorization.

There is another theorem that says that if we have the prime factors of ``n``:

.. math::

    n = p_1 \cdot p_2 \cdot p_3 \dots
    
then

.. math::

    phi(n) = phi(p_1) \cdot phi(p_2) \cdot phi(p_3) \dots

This is true not just for primes, but for any two coprime factors of ``n``.  This explains why we were able to write (in deriving an RSA key), that since ``n = p * q``:

.. math::

    phi(n) = (p-1)(q-1)

So if

.. math::

    phi(n) = phi(p_1) \ phi(p_2) \ phi(p_3) \dots
    
We can multiply and divide by the prime product equal to ``n`` and obtain

.. math::

    phi(n) = \frac{p_1 \ p_2 \dots}{p_1 \ p_2 \dots} (p_1 - 1) \ (p_2 - 1) \ \dots
    
    phi(n) = n(p_1 - 1/p_1)(p_2 - 1/p_2) \ \dots
    
In the write-up he sketches a proof of the last line above, and you can follow it backward to what we were given:

.. math::

    phi(n) = phi(p_1) \cdot phi(p_2) \cdot phi(p_3) \dots

-----------------------
Fermat's Little Theorem
-----------------------

This theorem says that for any integer ``a`` and prime ``p``:

.. math::

    a^p := a \ (mod \ p)
    
where ``:=`` means "defined to be equal".

We can rewrite this as

.. math::

    a^{p-1} = 1 \ (mod \ p)
    
Euler proved this theorem (Fermat did not) and he extended it by showing that it is true, not just for ``p`` prime, but for any ``b`` coprime to a.  Since we'll actually be using ``n`` (as defined before), let's stick with that:

.. math::

    a^{phi(n)} = 1 \ (mod \ n)

--------
Our goal
--------

What we're looking for here is a function that has an inverse, where

.. math::

    (m^e)^d = (m^d)^e = m
    
Always, mod ``n``.

Go back to Euler's extension of Fermat's little theorem (substituting ``m`` for ``a``):

.. math::

    m^{phi(n)} = 1 \ (mod \ n)
    
Raise to the power ``k``:

.. math::

    m^{k \cdot phi(n)} = 1 \ (mod \ n)

.. math::

    m^{k \cdot phi(n) + 1} = m \ (mod \ n)

So, we see that it will work to find

.. math::

    e \cdot d := k \cdot phi(n) + 1

And thus

.. math::

    e \cdot d := 1 \ mod \ phi(n)

And that's why it works.


