########################
Euclidean algorithm (EA)
########################

As a result of our interest in modular arithmetic, we take a look at the famous Euclidean algorithm, which yields the `gcd` (greatest common divisor) of two integers `a` and `b`.

The reason this is important is that factoring large numbers is very difficult.

Consider the calculation of the greatest common divisor (gcd) of

``819 = 3 * 3 * 7 * 13``

``462 = 2 * 3 * 7 * 11``

We see immediately that the gcd ``(819,462) = 21``. 

The problem with this method is that, as we said, there is no efficient algorithm to factor integers, and for the very large integers of interest it is impossible.

The **gcd** algorithm consists of the following steps:

* compute ``r = a % b``
* if ``r == 0:  return b``
* set ``a = b, b = r``

Example

::

    a =   b * r +  m
  421 = 111 * 3 + 88
  111 =  88 * 1 + 23
   88 =  23 * 3 + 19
   23 =  19 * 1 +  4
   19 =   4 * 4 +  3
    4 =   3 * 1 +  1
    3 =   1 * 3 +  0

The last non-zero remainder is 1, which we return as ``b`` when ``r = 0``.  This is gcd ``(421,111)``. 

gcd ``= 1`` means that these two numbers do not share any factors.  

Hint:  421 is on `this list <https://primes.utm.edu/lists/small/1000.txt>`_, although 111 is not.

Here are three very similar Python implementations.  We require ``b < a`` and if necessary we can do this before invoking the algorithmic code:


.. code-block:: python

    if b > a:
        a,b = b,a

My favorite loop ``while True``:

.. code-block:: python

     gcd(a,b):
        while True:
            r = a % b
            if r == 0:
                return b
            a,b = b,r

    print gcd(421,111)  # 1
    print gcd(60,24)    # 12
    print gcd(11838*2888, 99991987*2888) # 2888

Although I like it, some people may prefer:

.. code-block:: python

    def gcd(a,b):
        r = a % b
        while r != 0:
            a,b = b,r
            r = a % b
        return b

And here is a recursive version, which calls itself:

.. code-block:: python

    def gcd(a,b):
        r = a % b
        if r == 0:
            return b
        return gcd(b,r)

Whatever suits you.

-----------
Explanation
-----------

Consider two integers *a* and *b* and we compute ``m = a % b``.

One possibility is that *a* is evenly divided by *b*, then the result of the mod operation is zero, and *b* is the gcd *(a,b)*.

If not, then either *a* and *b* have at least one common divisor smaller than *b* or they do not share a common factor (we do not consider *1* as a factor).

The mod operation can be expressed as

.. code-block:: python
    
    m = a - k * b

where *k* can be computed variously as the "floor" of *a/b* (the next smallest integer from the real number that is computed), or the integer *k* such that

.. code-block:: python

    k * b < a 

while 

.. code-block:: python

    (k+1) * b > a  

(If there were an integer *k* so that *kb = a* exactly, that would correspond to the case of zero remainder).
    
So we suppose *a* and *b* have a common factor *f*.  Then we can factor *f* from each term of the previous equation:

.. code-block:: python

    m = a - k * b
    m = f * [a/f - (k * b)/f]

By the hypothesis of a common factor, the terms *a/f* and *(k * b)/f* are integers.  

But then clearly *m* is also evenly divided by *f* (because *m/f* is equal to an integer) and

.. code-block:: python

    m/f = a/f - (k * b)/f

The insight is that now we can just find *gcd(b,m)*, since *b* and *m* also have the common factor *f*, and all the same logic applies.

It is easy to show that the algorithm always terminates, but I leave that aside for now.