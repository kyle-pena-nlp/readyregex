from dataclasses import dataclass, field
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
from readyregex.options import Options


@dataclass
class PhoneNumber(Pattern, ConcatenatableMixin):

    options : Options = Options.Default

    def regex(self): 

        # Whether or not the area code itself is included.  Default: included.
        if (self.options & Options.NoAreaCode):
            parts = []
        else:
            parts = [ self._area_code() ]
        
        # The rest of the parts of the phone number (3 and 4 digit blocks)
        parts.extend([Digits(3), Digits(4)])

        # Join the parts together with the separators pattern
        final_pattern = self._separators().join(parts)

        # If the area code is optional, produce the no-area-code version of the pattern with a self-call and 'Choice'-together it to this pattern
        if (self.options & Options.OptionalAreaCode):
            choice1 = final_pattern
            choice2 = PhoneNumber((self.options | Options.NoAreaCode) & (~Options.OptionalAreaCode))
            final_pattern = Choice([choice1, choice2])

        return final_pattern.regex()

    def _area_code(self):
        # Area Code.  Can either come with mandatory parentheses, or no parentheses.  Default: optional parentheses.
        parenthesized_area_code = Character("(") + self._maybe_extra_whitespace() + Digits(3) + self._maybe_extra_whitespace() + Character(")")
        if (self.options & Options.MandatoryAreaCodeParentheses):
            area_code = parenthesized_area_code
        elif (self.options & Options.NoAreaCodeParentheses):
            area_code =  Digits(3)
        else:
            area_code = Choice([ parenthesized_area_code, Digits(3) ])
        return area_code

    def _separators(self):

        # What the separators between the area code and digit blocks look like. Default:  Either a single dash or single whitespace character.
        if (self.options & Options.SingleDashSeparators):
            separators = Character("-")
        elif (self.options & Options.SingleSpaceSeparators):
            separators = Character(" ")
        elif (self.options & Options.NoSeparators):
            separators = EmptyPattern()
        else:
            separators = Choice([ Character("-"), SpecialCharacterClasses.WHITESPACE ])
        
        # Surround the separators with maybe_extra_whitespace
        separators = self._maybe_extra_whitespace() + separators + self._maybe_extra_whitespace()

        # Make the separators optional, if desired
        if (self.options & Options.OptionalSeparators):
            separators = Optional(separators)

        return separators

    def _maybe_extra_whitespace(self):
        # Spacing between tokens of phone number (like around dashes or around parentheses).  Default: nothing (empty).
        if (self.options & Options.IgnoreExtraWhitespace):
            maybe_extra_whitespace = Repetition(SpecialCharacterClasses.WHITESPACE, None, None)
        else:
            maybe_extra_whitespace = EmptyPattern()
        return maybe_extra_whitespace

