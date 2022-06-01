from dataclasses import dataclass, field
from readyregex.common_regex.separator_pattern import SeparatorPattern
from readyregex.object_model.character_set import CharacterSet
from readyregex.object_model.optional import Optional
from readyregex.object_model.character import Character
from readyregex.object_model.digits import Digits
from readyregex.object_model.concatenatable_mixin import ConcatenatableMixin
from readyregex.object_model.empty_pattern import EmptyPattern
from readyregex.object_model.special_character_classes import SpecialCharacterClasses
from readyregex.object_model.repetition import Repetition
from readyregex.object_model.choice import Choice
from readyregex.object_model.pattern import Pattern
from readyregex.options import Options, RepetitionOptions, Separators, Buffers



@dataclass
class PhoneNumber(Pattern, ConcatenatableMixin):

    areacode : Options              = Options.Mandatory
    areacode_parentheses : Options  = Options.Optional
    separators : Separators         = Separators.Dashes
    separator_buffers : Buffers     = Buffers.Whitespace
    separator_buffer_repetition : RepetitionOptions = RepetitionOptions.Any
    international : Options         = Options.Prohibited

    def _validate_input(self):
        if self.international.mandatory() and not self.areacode.mandatory():
            raise Exception("If international is mandatory then areacode must also be mandatory")
        if self.international.optional() and self.areacode.prohibited():
            raise Exception("If international is optional then areacode must not be prohibited")

    def regex(self): 

        pattern = EmptyPattern()

        # What separators to use
        separators = self._separators()

        # M,M
        if self.international.mandatory() and self.areacode.mandatory():
            pattern += self._international() + separators + self._area_code() + separators
        # !! M,0
        # !! M,P
        # O,M
        elif self.international.optional() and self.areacode.mandatory():
            pattern += Choice([self._international() + separators + self._area_code() + separators, self._area_code() + separators])
        # 0,0
        elif self.international.optional() and self.areacode.optional():
            pattern += Optional(self._international() + separators + self._area_code() + separators)
        elif self.international.optional() and self.areacode.mandatory():
            pattern += Optional(self._international() + separators) + self._area_code() + separators        
        # !! O,P
        # P,M
        elif self.international.prohibited() and self.areacode.mandatory():
            pattern += self._area_code() + separators
        # P,0
        elif self.international.prohibited() and self.areacode.optional():
            pattern += Optional(self._area_code() + separators)
        # P,P
        elif self.international.prohibited() and self.areacode.prohibited():
            pattern = EmptyPattern()
        
        # The rest of the parts of the phone number (3 and 4 digit blocks)
        pattern += ([Digits(3) + separators + Digits(4)])

        return pattern.regex()

    def _international(self):
        raise Exception("TODO")

    def _area_code(self):
        
        parenthesized_area_code = Character("(") + self._maybe_extra_whitespace() + Digits(3) + self._maybe_extra_whitespace() + Character(")")
        nonparenthesized_area_code = Digits(3)
        
        if (self.areacode_parentheses.mandatory()):
            area_code = parenthesized_area_code
        elif (self.areacode_parentheses.prohibited()):
            area_code =  nonparenthesized_area_code
        elif (self.areacode_parentheses.optional()):
            area_code = Choice([ parenthesized_area_code, nonparenthesized_area_code ])
        
        return area_code

    def _separators(self):
        separators = SeparatorPattern(self.separators, buffers = self.separator_buffers, buffer_repetition = self.separator_buffer_repetition)        
        return separators

