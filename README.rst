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
        
    Validation of Traditional Date formats:
        Date()
        """mm/dd/yy, mm/dd/yyyy, dd/mm/yy, and dd/mm/yyyy. Omit leading zeros"""
        ^(?:
        # m/d or mm/dd | )
        (1[0-2]|0?[1-9])/(3[01]|[12][0-9]|0?[1-9])
        
        # d/m or dd/mm          
        (3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9]) 
        
        # /yy or /yyyy
        /(?:[0-9]{2})?[0-9]{2}$
        
        SearchDate()
        """Match date in text"""
        \b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/[0-9]{4}\b
        
        Date(valid_dates=True)
        """Ignore things like Feb 30"""
        ^(?:
        # 28 day months
        # 30 day months
        # 31 day months
        #More on this - there might be a more elegant solution
        
        Date(month_text=True)
        """ Transform '7 July 1958' into 07/07/1958"""
        
        #Other date variations

    Validation of Postal Codes:
        ZIP()
        """ US postal code (ZIP (five digits), "-" ,4(optional))"""
        ^[0-9]{5}(?:-[0-9]{4})?$
        
        ZIP(UK=True, basic=True)
        ^[A-Z]{1,2}[0-9R][0-9A-Z]?●[0-9][ABD-HJLNP-UW-Z]{2}$
          
        ZIP(UK=True, basic=False)
        ^(?:(?:[A-PR-UWYZ][0-9]{1,2}|[A-PR-UWYZ][A-HK-Y][0-9]{1,2} 
        |[A-PR-UWYZ][0-9][A-HJKSTUW]|[A-PR-UWYZ][A-HK-Y][0-9]
        [ABEHMNPRV-Y])●[0-9][ABD-HJLNP-UW-Z]{2}|GIR 0AA)$         
         
        ZIP(Canadian=True)
        ^(?!.*[DFIOQU])[A-VXY][0-9][A-Z]●?[0-9][A-Z][0-9]$
         
        #Other countries
        
        #Create your own
        ZIP(Custom=True)
        #Set rules
        
         
    Validation of  Passwords:
        Password(lenght_1= ,length_2= ,ASCIII_only= True,uppercase= ,special_characters= ,consecutive_characters=, )
        ^(?=.{8,32}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*
        #other rules
        
    Validation of Credit Card Numbers:
        CreditCard()
        """Visa 13 or 16 digits, starting with 4. MasterCard 16 digits, starting with 51 through 55.
        Discover 16 digits, starting with 6011 or 65. 
        American Express 15 digits, starting with 34 or 37.
        Diners Club 14 digits, starting with 300 through 305, 36, or 38. 
        JCB 15 digits, starting with 2131 or 1800, or 16 digits starting with 35."""

        ^(?:
        (?<visa>4[0-9]{12}(?:[0-9]{3})?) |
        (?<mastercard>5[1-5][0-9]{14}) | 
        (?<discover>6(?:011|5[0-9]{2})[0-9]{12}) |
        (?<amex>3[47][0-9]{13}) |
        (?<diners>3(?:0[0-5]|[68][0-9])[0-9]{11}) |
        (?<jcb>(?:2131|1800|35[0-9]{3})[0-9]{11}) )$
        
   Validation of Social Security Numbers:
        
        """The area number cannot be 000, 666, or between 900 and 999
        Digits four and five are called the group number and range from 01 to 99.
        The last four digits are serial numbers from 0001 to 9999."""
        SSN()
        
        regex= ^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$
        
        #Find SSN in text
        use \b(regex)\b
        
        
    Validation of time formats
        """hh:mm and hh:mm:ss 
        12-hour and 24-hour"""
        
        TimeFormat(seconds= False,Format12h= True)
        ^(1[0-2]|0?[1-9]):([0-5]?[0-9])(●?[AP]M)?$
         
        TimeFormat(seconds= False,Format12h= False)
        ^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$        
        
        TimeFormat(seconds= True,Format12h= True)
        ^(1[0-2]|0?[1-9]):([0-5]?[0-9]):([0-5]?[0-9])(●?[AP]M)?$        

        TimeFormat(seconds= True,Format12h= False)
        ^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$

        ISODate()
        """ISO 8601 Date and timeformat"
        #more on this

     Validation of text length
     Validation of Numbers of lines in text
     #more on this
     
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
