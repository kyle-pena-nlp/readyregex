.. _get-started:

Get Started
===================================

.. _`getstarted`:
.. _`installation`:

Install ``readyregex``
----------------------------------------

``readyregex`` requires: Python 3.7+.

1. (Pip) Run the following command in your command line:

.. code-block:: bash

    pip install -U readyregex

2. (Conda) Run the following command in your conda environment:

.. code-block:: bash

    conda install readyregex

Import ``readyregex``
-----------------------------------------

.. code-block:: python

    from readyregex import *
    phone_number = PhoneNumber()
    print(phone_number.match("904 123 4567"))

Browse Tons of Out-Of-The-Box Patterns
-------------------------------------------
See :ref:`this list <oob-pattern-listing>`.

Create Your Own Patterns (Or Tweak Existing Ones)
-------------------------------------------
See :ref:`pattern customization <oob-pattern-customization>` or :ref:`patterns from scratch <patterns-from-scratch>`.