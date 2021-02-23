from dataclasses import dataclass, field
from ..object_model.addable import Addable
from ..object_model.special_character_class_atom import SpecialCharacterClassAtom
from ..object_model.regex_literal import RegexLiteral
from ..object_model.optional import Optional
from ..object_model.character_set import CharacterSet
from ..object_model.unicode_character_atom import UnicodeCharacterAtom
from ..object_model.digits import Digits
from ..object_model.empty_pattern import EmptyPattern
from ..options import Options


from ..object_model.addable_sequence import AddableSequence

@dataclass
class PhoneNumber(Addable):

    options : Options

    @staticmethod
    def DEFAULT_PHONE_NUMBER_OPTIONS():
        return Options.AreaCode & Options.DashSeparators & Options.SpaceSeparators & Options.AreaCodeParentheses

    def __post_init__(self, options):
        if not options:
            self.options = PhoneNumber.DEFAULT_PHONE_NUMBER_OPTIONS()
        else:
            self.options = options

    def _separator_pattern(self):
        separators = self._get_valid_separators()
        if len(separators) == 0:
            return EmptyPattern()
        else:
            return CharacterSet(positives = separators)

    def _area_code_and_separator_pattern(self):
        return AddableSequence([
            Digits(3),
            self._separator_pattern()
        ])

    def regex(self):  

        parts = []

        if self._optional_area_code():
            parts.append(Optional(self._area_code_and_separator_pattern()))
        elif self._area_code():
            parts.append(self._area_code_and_separator_pattern())
        
        parts.extend([
            Digits(3),
            self._separator_pattern(),
            Digits(4)
        ])

        return AddableSequence(parts)

    
