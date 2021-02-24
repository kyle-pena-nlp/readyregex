from dataclasses import dataclass, field
from ..object_model.character_set import CharacterSet
from ..object_model.special_character_classes import SpecialCharacterClasses
from ..object_model.optional import Optional
from ..object_model.character import Character
from ..object_model.digits import Digits
from ..object_model.concatenatable import Concatenatable
from ..object_model.empty_pattern import EmptyPattern
from ..options import Options


from ..object_model.concatenatable_sequence import ConcatenatableSequence

@dataclass
class PhoneNumber(Concatenatable):

    options : Options

    @staticmethod
    def DEFAULT_PHONE_NUMBER_OPTIONS():
        return Options.AreaCode & Options.DashSeparators & Options.SpaceSeparators

    def __post_init__(self, options):
        if not options:
            self.options = PhoneNumber.DEFAULT_PHONE_NUMBER_OPTIONS()
        else:
            self.options = options

    def regex(self):  

        pattern = EmptyPattern()

        separators = CharacterSet([ Character("-"), Character(" ") ])

        if (self.options & Options.OptionalAreaCode):
            pattern += Optional(Digits(3) + separators)
        elif (self.options & Options.AreaCode):
            pattern += Digits(3) + separators

        pattern += Digits(3) + separators + Digits(4)

        return pattern

    
