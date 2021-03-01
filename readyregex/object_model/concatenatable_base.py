from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class ConcatenatableBase(ABC):
    
    @abstractmethod
    def _get_content_array(self):
        pass

    @abstractmethod
    def add(self, other : 'ConcatenatableBase') -> 'ConcatenatableBase':
        pass