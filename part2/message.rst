.. message:

####################
Messages and numbers
####################

Before thinking about encryption, we need to work out just what a message is.  

Let's write a message in English, for example, "hello world".  What we will do is to generate a number representing the message, designated as *m*. 

First, write this text into a file on disk

.. code-block:: bash

    echo -n 'hello world' > x.txt
    hexdump -C x.txt             

I am going to write code so that it is formatted such that it can just be copied and pasted into a bash shell (above) or the Python interpreter (elsewhere, below).

The result is

::

    00000000  68 65 6c 6c 6f 20 77 6f  72 6c 64        |hello world|
    0000000b


What is actually present on the disk is the sequence of bytes ``68 65 6c ...``. 

That is to say, where ``68`` is written above, what is really present on disk is the binary sequence ``01101000``, formed as a collection of elements in memory that either do or do not have a voltage across them.

Binary ``01101000`` corresponds to decimal ``104`` as well as hexadecimal ``68``.

>>> int('01101000',2)
104
>>> hex(104)
'0x68'

-----
ASCII
-----

As you know, ASCII-encoding is an assignment of many of the 256 possible values for a byte to different codes or values, including letters such as:  ``68 : h``.  

Since the letters are encoded in lexicographical order, the value ``65`` is ``65 - 68 = -3`` 3 places before ``h``, namely, ``e``, and ``6c`` is ``6c - 68 = 4`` places after ``h``, i.e. ``l``.  

So ``68 65 6c 6c 6f`` is ``hello``.

We could use the ASCII-encoding to generate a number.  Write ``hello`` as its decimal equivalent sequence:  ``104-101-108-108-111``.  

To turn this into a single number:

::

    m = 104*256^4 + 101*256^3 + 108*256^2 + 108*256 + 111

::

    m = 448378203247

For a longer message, just use more powers of 256.

In the code sample below, we convert the message ``hello world`` into a binary number using the ``ord`` and ``bin`` functions. Because bin doesn’t show leading zeroes, we add them back with ``zfill``.

.. code-block:: python

    s = "hello world"
    L = [bin(ord(c))[2:].zfill(8) for c in s]      
    b = "".join(L)

Take a look

>>> int(b,2)
126207244316550804821666916L
>>>

However, this approach is fairly wasteful since most bytes never appear in any message (especially if we just use lowercase letters).

A more compact encoding might be achieved like this:

.. code-block:: python

    lc = 'abcdefghijklmnopqrstuvwxyz'
    D = dict(zip(lc,range(1,len(lc)+1)))
    D[" "] = 0


The dictionary ``D`` assigns an integer for each lowercase letter or a space. Now do:

.. code-block:: python

    s = 'hello world'
    m = 0
    N = 27
    for i,c in enumerate(s):
        m += D[c] * N**i
        
The number *m* is being formed from the integer values for each character of ``hello world``. For example, suppose the message is simply ``hel``.  Since ``h`` is the eighth letter, ``e`` is the fifth letter, and ``l`` is letter number 12, the value would be

::

    8 + (5 × 27) + (12 × 27^2) = 8891

The result for 'hello world' can be viewed as:

.. code-block:: bash

    python script2.py

.. code-block:: bash

    920321254041092

The number *is* our message. To read it, just reverse the process:

.. code-block:: python

    N = 27
    m = 920321254041092
    rD = dict(zip(D.values(),D.keys()))
    pL = list()
    while m:
        pL.append(rD[m % N])
        m /= N

    print(''.join(pL))
        
Output:

>>> hello world

While the above encoding could be viewed as a form of encryption, it is pretty weak.