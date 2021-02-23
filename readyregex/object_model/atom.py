from abc import ABC
from dataclasses import dataclass
from addable import Addable
from character_class import CharacterSetItem

@dataclass
class Atom(Addable, CharacterSetItem, ABC):
    pass

    