from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class CharacterSetItem(ABC):
    
    @abstractmethod
    def character_set_regex(self) -> str:
        pass