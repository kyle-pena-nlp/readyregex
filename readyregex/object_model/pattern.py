from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Set, Tuple, Sequence, Union, Any
from enum import Enum

@dataclass
class Pattern(ABC):
    
    @abstractmethod
    def regex(self):
        pass