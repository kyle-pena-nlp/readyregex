from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

@dataclass
class Pattern(ABC):

    @abstractmethod
    def regex(self):
        pass