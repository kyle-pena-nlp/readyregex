from dataclasses import dataclass
from atom import Atom
from special_character_classes import SpecialCharacterClasses

@dataclass
class SpecialCharacterClassAtom(Atom):

    value : SpecialCharacterClasses

    def regex(self):
        return self.value.regex
