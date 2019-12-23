#######
Symbols
#######

Although the Sphinx documentation is nice, it has a few quirks.  Python has its own symbols for mathematical functions, as given below.

Sometimes we will typeset mathematics to make the output prettier (especially for subscripts like :math:`p_1`), and in that case we may use more standard math symbols.

On the other hand, the mod operator ``%`` is not allowed outside of Python syntax.

--------------
Multiplication
--------------

In typeset math (say, LaTeX) we may write

.. math::

    a \cdot b \\

    a \times b

or in pseudo-code ``a x b``.  Python uses the ``*`` operator:

.. code-block::  python

    a * b

--------------
Exponentiation
--------------

In typeset math we may write

.. math::

    m^e

or in pseudo-code ``m^e``.  Python uses the ``**`` operator, as in:

.. code-block::  python

    m**e

-------
Modulus
-------

For math markup, we use the work ``mod``, and for Python write the symbol ``%``.

-------
Divides
-------

If there exists an integer *c* such that :math:`y = cx`, we denote this property by :math:`x|y`.  We say that *x* divides *y*.

Equivalently, the result of the mod operation is zero: 

.. code-block:: python

    y % x = 0

---
Phi
---

Euler's totient function is symbolized by the Greek letter phi.

.. image:: /_static/phi.png
   :scale: 20 %

That symbol is easy to find in Unicode, and modern Python allows Unicode, however LaTeX does not.  Since I want to produce pdf output as well as html, we must stick with ``phi``.

----------------
Set intersection
----------------

For the same reason, lack of an appropriate symbol, I have adopted ``^`` as the symbol for set intersection, and ``U`` as the symbol for set union.  

``^`` is used in Python as the symbol for XOR, exclusive or.
