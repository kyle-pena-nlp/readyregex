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

        parts = []

        if (self.options & Options.IgnoreExtraWhitespace):
            extra_spaces = Repetition(SpecialCharacterClasses.WHITESPACE, None, None)
        else:
            extra_spaces = EmptyPattern()

        parenthesized_area_code = Character("(") + extra_spaces + Digits(3) + extra_spaces + Character(")")
        if (self.options & Options.MandatoryAreaCodeParentheses):
            area_code = parenthesized_area_code
        elif (self.options & Options.NoAreaCodeParentheses):
            area_code =  Digits(3)
        else:
            area_code = Choice([ parenthesized_area_code, Digits(3) ])

        if (self.options & Options.NoAreaCode):
            pass
        elif (self.options & Options.OptionalAreaCode):
            parts.append(Optional(area_code))
        else:
            parts.append(area_code)
        
        parts.extend([Digits(3), Digits(4)])

        if (self.options & Options.OnlyDashSeparators):
            separators = Character("-")
        elif (self.options & Options.OnlySpaceSeparators):
            separators = Character(" ")
        elif (self.options & Options.NoSeparators):
            separators = EmptyPattern()
        else:
            separators = Choice([ Character("-"), SpecialCharacterClasses.WHITESPACE ])
        
        separators = extra_spaces + separators + extra_spaces
        
        if (self.options & Options.OptionalSeparators):
            separators = Optional(separators)

        return separators.join(parts).regex()
