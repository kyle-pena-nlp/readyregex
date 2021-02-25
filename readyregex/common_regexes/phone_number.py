from dataclasses import dataclass, field
from readyregex.object_model.character_set import CharacterSet
from readyregex.object_model.optional import Optional
from readyregex.object_model.character import Character
from readyregex.object_model.digits import Digits
from readyregex.object_model.concatenatable_mixin import ConcatenatableMixin
from readyregex.object_model.empty_pattern import EmptyPattern
from readyregex.options import Options


@dataclass
class PhoneNumber(ConcatenatableMixin):

    options : Options = None

    @staticmethod
    def DEFAULT_PHONE_NUMBER_OPTIONS():
        return Options.AreaCode & Options.DashSeparators & Options.SpaceSeparators

    def __post_init__(self):
        if not self.options:
            self.options = PhoneNumber.DEFAULT_PHONE_NUMBER_OPTIONS()
        else:
            self.options = self.options

    def regex(self):  

        pattern = EmptyPattern()
        
        separators = CharacterSet([ Character("-"), Character(" ") ])

        if (self.options & Options.OptionalSeparators):
            separators = Optional(separators)

        if (self.options & Options.OptionalAreaCode):
            pattern += Optional(Digits(3) + separators)
        elif (self.options & Options.AreaCode):
            pattern += Digits(3) + separators

        pattern += Digits(3) + separators + Digits(4)

        return pattern.regex()

    
