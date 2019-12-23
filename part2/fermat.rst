################
Fermat and Euler
################

We'll attempt a high-level sketch of how/why RSA works here.  At some point in the future, perhaps I'll fill in the details.

-----------------------
Fermat's Little Theorem
-----------------------

This theorem says that for any integer ``a`` and any prime ``p``:

.. math::

    a^p := a \ mod \ p
    
where ``:=`` means "defined to be equal".

We can also write this in Python as

.. code-block:: python

    a**(p-1) = 1 % p

**Extension**

Euler proved this theorem (Fermat did not) and he extended it by showing that it is true, not just for *p* prime, but for any *n* coprime to a.

.. code-block:: python

    a**(p-1) = 1 % p

That is:

.. code-block:: python

    a**phi(n) = 1 % n

for any *a* coprime to *n*
    
**Example**

Suppose ``p=3`` then for any number co-prime to ``3``

.. math::

    a^2 = 1 \ mod \ 3

Clearly, this is true for :math:`a = 2, 4, 5, 7` and so on, but not for numbers divisible by *3*, because then the remainder mod *3* is just zero.

-----
Proof
-----

Our theorem is that for *a* and *p* coprime and *p* prime

.. math::

    a^{p-1} = 1 \ mod \ p

To see this, write out the first *(p-1)* consecutive multiples of *a*

.. math::

    \{ a,\ 2a,\ 3a,\ \dots \ (p-1)a \}

Now multiply all the terms together and then consider the result mod *p*

.. math::

    a \cdot 2a \cdot 3a \dots \cdot (p-1)a \ mod \ p
    
By the rule of modular multiplication this is equal to
    
.. math::

    (a \ mod \ p)(2a \ mod \ p)(3a \ mod \ p) \ \dots \ ((p-1)a) \ mod \ p  

Now suppose that any two terms were equal to one another (mod *p*), say

.. math::

    3a \ mod \ p = 5a \ mod \ p
    
Recall that if :math:`ra = sa` (mod *p*), then :math:`r = s` (mod *p*).  But clearly :math:`3 \ne 5`, so therefore no two terms in the product have the same remainder mod *p*.

Therefore these values

.. math::

    (a \ mod \ p)(2a \ mod \ p)(3a \ mod \ p) \dots ((p-1)a \ mod \ p)

are all distinct, and since there are *(p-1)* of them, they cycle through the same integers :math:`1..(p-1)` (though not necessarily in the same order).  

Which is to say that the product is equal to *(p-1)!*, and we can then write

.. math::

    a \cdot 2a \cdot 3a \dots \cdot (p-1)a \ mod p = (p-1)! \ mod \ p
    
Factor out the *a*

.. math::

    a^{p-1} \ (p-1)! \ mod \ p = (p-1)! \ mod \ p

Therefore

.. math::

    a^{p-1} = 1 \ mod \ p

    a^p = a \ mod \ p
    
The requirement for *a* and *p* coprime arises because it ensures that the terms in 

.. math::

    a \cdot 2a \cdot 3a \dots \cdot (p-1)a \ mod \ p  

each appear only once. 

On a side note, recall our earlier proof that :math:`(p-1)! = 1` mod *p*.

--------
Our goal
--------

What we're looking for here is a function that has an inverse, where

.. math::

    (m^e)^d = (m^d)^e = m
    
Always, mod ``n``.

So with Euler's extension of Fermat's little theorem (substituting ``m`` for ``a``):

.. math::

    m^{phi(n)} = 1 \ (mod \ n)
    
In this case, raising to the power ``k`` doesn't change the result:

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


