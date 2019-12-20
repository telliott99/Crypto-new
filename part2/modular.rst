##################
Modular arithmetic
##################

Without getting too deep into the weeds, we take a quick look at multiplication with some modulus, *n*.

We will prove the following

.. code-block:: python

    (a * b) % n = (a % n) * (b % n) % n

If either *a* or *b* is less than or equal to *n*, the result is trivial, so we assume ``a > n`` and ``b > n``.

Then

.. math::

    a = x*n + r_1

for some *x*.  A similar relation is true for *b* so

.. code-block:: python

    (a * b) % n = (x * n + r_1) * (y * n + r_2) % n

Of the four terms resulting on the right-hand side, three are zero (``% n``) and the other one is

.. code-block:: python

    r_1 * r_2 % n = (a % n) * (b % n) % n

which is what we wanted to prove.

The practical result is that we can carry out exponentiation and modulus operations in interleaved fashion.

Namely, multiply *m* by itself.  If *m > n*, replace *m* by the remainder ``% n``.  Repeat as many times as the exponent dictates.

In Python:

.. code-block:: python

    pow(x,y,z)

works this way.

--------
Examples
--------

.. math::

    7 \times 10 \ mod \ 6 = 1 \times 4 = 4

and

.. math::

    2 a \ mod \ p = (2 \ mod \ p) \cdot (a \ mod \ p)

Hence, if 

.. math::

    m \cdot a = n \cdot a \ mod \ p

it follows that 

.. math::

    m = n \ mod \ p 