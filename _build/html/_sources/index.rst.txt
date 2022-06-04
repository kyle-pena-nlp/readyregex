.. readyregex documentation master file, created by
   sphinx-quickstart on Sat Jun  4 11:14:02 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. |logo| image:: path/filename.png
  :width: 400
  :alt: readyregex

Welcome to readyregex's documentation!
======================================

**readyregex** is a Python library which offers a large number of off-the-shelf, customizable text matching patterns for everyday use.

These patterns include:

* addresses
* credit cards
* dates
* doges
* emails
* emojis
* filepaths
* html tags
* ip addresses
* passport numbers
* phone numbers
* passwords by strength levels
* slugs
* social security numbers
* timestamps in a variety of formats
* zipcodes

...and more!

It's easy to get started:

.. code-block:: Python

  from readyregex import *

  # Customize an off-the-shelf pattern according to your needs
  pn = PhoneNumber(extra_spaces = RepetitionOptions.AtMostOne)

  # Match to text
  pn.match("904-867-5309") # True
    
  # Or get the regex pattern itself, if desired
  pn_regex = pn.regex()

  # Use a pattern to build something more complicated
  three_phone_numbers = (pn + " ") * 3
  three_phone_numbers.match("904-867-5309 904-867-5309 904-867-5309") # True

  # Maybe we don't have what you need? That's ok, you can build your own!
  digit = Range("A", "Z") | Range("0", "9")
  _1800number = "1-800" + digit*3 + " " + digit*4
  _1800number.match("1-800 BUY JUNK") # True

And if we don't have what you need, **readyregex** also offers an object-oriented approach to building regex patterns.  We will also gladly consider pull requests.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
