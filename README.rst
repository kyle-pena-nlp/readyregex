==========
readyregex
==========


.. image:: https://img.shields.io/pypi/v/readyregex.svg
        :target: https://pypi.python.org/pypi/readyregex

.. image:: https://img.shields.io/travis/kyle-pena-nlp/readyregex.svg
        :target: https://travis-ci.com/kyle-pena-nlp/readyregex

.. image:: https://readthedocs.org/projects/readyregex/badge/?version=latest
        :target: https://readyregex.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/kyle-pena-nlp/readyregex/shield.svg
     :target: https://pyup.io/repos/github/kyle-pena-nlp/readyregex/
     :alt: Updates



readyregex contains a wide range of customizable and ready-made regex patterns for everyday use


* Free software: Apache Software License 2.0
* Documentation: https://readyregex.readthedocs.io.


Features
--------

* TODO
--------
Common Regexes and Variations
#no one-size-fits all regex solution

    Validation of Email addresses:
        Email_Simple
        """ validates if string contains a "@" preceded or followed by characters:"""
        ^\S+@\S+$
        
        Email_Simple(character_restrictions=True)
        """restricted to characters allowed in domain names"""
        ^[A-Z0-9+_.-]+@[A-Z0-9.-]+$
        
        Email_Simple(dot_checker=True)
        """no consecutive dots, first and last characters cant be dots"""
        ^[A-Z0-9_!#$%&'*+/=?`{|}~^.-]+@[A-Z0-9.-]+$

        Email_Simple(domain_name=True)
        """top level domain level must be have between 2 to 6 characters i.e .uk"""

        Email_Simple(common_domain_name=True)
        "only allows common domain names: com|net|org|edu|gov
        Can also use https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains"
        
       
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
