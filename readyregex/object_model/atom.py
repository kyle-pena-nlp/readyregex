from abc import ABC
from dataclasses import dataclass
from concatenatable import Concatenatable
from character_set_item import CharacterSetItem

@dataclass
class Atom(Concatenatable, CharacterSetItem, ABC):
    pass

    