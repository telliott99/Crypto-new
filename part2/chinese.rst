#########################
Chinese Remainder Theorem
#########################

Also called:  CRT

.. image:: /_static/shapes.png
   :scale: 60 %

In the picture above, we have 5 distinct shapes, 3 different colors, and 2 states, either filled or empty.

As you can see, there are precisely 30 possible types.  

For example, each shape can be one of three colors, filled or empty, so there are 6 possibilities for each of the five shapes.

It is easier to draw the picture if the shapes are laid out in a regular array, but once the assignments are made, the order is irrelevant.

This is simply a consequence of the fact that

.. math::

    5 \times 3 \times 2 = 30

Since there are 30 numbers in ``[1..30]``, there is exactly one type for each number.

-----------------
General statement
-----------------

If *N* is composed of coprime factors

.. math::

    N = p \cdot q \cdot r \dots

and *n* is in the range ``[1..N]``.

Suppose *x* has the set of remainders with those factors:

::

    x = a % p
    x = b % q
    x = c % r

Then this tuple ``(a,b,c)`` is unique to *x*.

-------
Example
-------

Suppose N = 60, so 

::

    30 = 2 * 3 * 5

Make a table of remainders:

::

        1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
    2:  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1
    3:  1  2  0  1  2  0  1  2  0  1  2  0  1  2  0
    5:  1  2  3  4  0  1  2  3  4  0  1  2  3  4  0

       16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
    2:  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0
    3:  1  2  0  1  2  0  1  2  0  1  2  0  1  2  0
    5:  1  2  3  4  0  1  2  3  4  0  1  2  3  4  0

Any particular triplet of remainders is unique, say:  (1,1,3) -> 13.

This is also true if the factors are not prime but simply co-prime:

::

        1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
    5:  1  2  3  4  0  1  2  3  4  0  1  2  3  4  0
    6:  1  2  3  4  5  0  1  2  3  4  5  0  1  2  3

       16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
    5:  1  2  3  4  0  1  2  3  4  0  1  2  3  4  0
    6:  4  5  0  1  2  3  4  5  0  1  2  3  4  5  0

------------------
Solving the system
------------------

I picked one column at random from above.  Consider the following table of remainders (congruences):

::  

    x := 1 (mod 2)
    x := 1 (mod 3)
    x := 3 (mod 5)

The CRT says that this tuple uniquely determines ``x``.  

We can actually solve the system for ``x``.

https://brilliant.org/wiki/chinese-remainder-theorem/


Start with the largest modulus eqn(3).  Re-write it as: 

::

    x = 5j + 3

For some integer ``j``.  

Next, substitute into eqn(2):

::

    5j + 3 = 1 (mod 3)

Solve for ``j``:

::

    5j = 1 (mod 3)
    2j = 1 (mod 3)
    j = 2 (mod 3)

Rewrite this as a congruence relation:

::

    j = 3k + 2

for some integer ``k``.  

Substitute into the equation we had above for ``j``:

::

    x = 5j + 3
    x = 5(3k + 2)
    x = 15k + 13

Finally, substitute into eqn(1) and solve for ``k``

::

    15k + 13 = 1 (mod 2)
    15k = -12 = 0 (mod 2)
    k = 0 (mod 2)

which means that

::

    k = 2m

for some m.  And then

::

    x = 15k + 13
    x = 15(2m) + 13
    x = 13 mod 30

