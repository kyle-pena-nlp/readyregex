from dataclasses import dataclass
from readyregex.object_model.character_set import CharacterSet
from readyregex.object_model.character import Character
from readyregex.object_model.digits import Digits
from readyregex.object_model.empty_pattern import EmptyPattern
from readyregex.object_model.optional import Optional
from readyregex.object_model.separator_pattern import SeparatorPattern
from readyregex.object_model.choice import Choice
from readyregex.object_model.pattern import Pattern
from readyregex.object_model.options import Options, Repetitions
from readyregex.object_model.string_literal import StringLiteral



@dataclass
class PhoneNumber(Pattern):
    """
        A phone number following the North American Numbering Plan (NANP), per: https://en.wikipedia.org/wiki/North_American_Numbering_Plan
        These are seven digit phone numbers possibly preceeded by +1 
    """

    international : Options            = Options.Prohibited
    areacode : Options                 = Options.Mandatory
    areacode_parentheses : Options     = Options.Optional
    dashes : Options                   = Options.Optional
    extra_spaces : Repetitions = Repetitions.AtMostOne

    def _validate_input(self):
        if self.international.mandatory() and not self.areacode.mandatory():
            raise Exception("If international is mandatory then areacode must also be mandatory")
        if self.international.optional() and self.areacode.prohibited():
            raise Exception("If international is optional then areacode must not be prohibited")

    def build(self):

        digits_separator = SeparatorPattern(Character("-"), self.dashes, self.extra_spaces, allow_no_separation = False)
        separator = Character(" ") * self.extra_spaces
        digits1 = Digits(3)
        digits2 = Digits(4)

        local_number           = digits1 + digits_separator + digits2
        area_code_preamble     = (self._area_code() + digits_separator)
        international_preamble = (self._international() + separator)

        if self.international.optional() and self.areacode.optional():
            pattern : Pattern = (international_preamble + area_code_preamble) * Options.Optional + local_number
        else:
            pattern : Pattern = international_preamble * self.international + area_code_preamble * self.areacode + local_number

        return pattern

    def _international(self):
        return StringLiteral("+1")

    def _area_code(self):
        
        parenthesized_area_code = Character("(") + Digits(3) + Character(")")
        nonparenthesized_area_code = Digits(3)
        
        if (self.areacode_parentheses.mandatory()):
            area_code = parenthesized_area_code
        elif (self.areacode_parentheses.prohibited()):
            area_code =  nonparenthesized_area_code
        elif (self.areacode_parentheses.optional()):
            area_code = Choice([ parenthesized_area_code, nonparenthesized_area_code ])
        
        return area_code

    def _separators(self):
        pass

