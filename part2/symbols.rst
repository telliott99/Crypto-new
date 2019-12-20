#######
Symbols
#######

We're using Python quite a bit in this document.  

Although the Sphinx documentation is nice, it has a few quirks.  For the most part, we will adopt the symbols for mathematical functions used in Python, as given below.  Occasionally we want to typeset mathematics (especially for subscripts like :math:`p_1`), and in that case we may use more standard math symbols.

--------------
Multiplication
--------------

In typeset math (say, LaTeX) we may write

.. math::

    a \times b

or in pseudo-code ``a x b``.  Here we will mainly use the ``*`` operator, as in:

.. code-block::  python

    a * b

--------------
Exponentiation
--------------

In typeset math we may write

.. math::

    m^e

or in pseudo-code ``m^e``.  Here we will use the ``**`` operator, as in:

.. code-block::  python

    m**e

-------
Modulus
-------

Rather than use the word mod, write the symbol ``%``.

---
Phi
---

Euler's totient function is symbolized by the Greek letter phi.

That symbol is easy to find in Unicode, and modern Python will accept it, however LaTeX will not.  Since I want to produce pdf output as well as html, we must stick with ``phi``.

----------------
Set intersection
----------------

For the same reason, lack of an appropriate symbol, I have adopted ``^`` as the symbol for set intersection, and ``U`` as the symbol for set union.  

We will also use ``^`` in Python as the symbol for XOR, exclusive or.

--------------
Evenly divides
--------------

In the previous chapter I used the notation :math:`n | p`, which should be understood to mean that *p* *evenly divides* *n* with no remainder.  Equivalently, the result of the mod operation :math:`n % p` is zero.




