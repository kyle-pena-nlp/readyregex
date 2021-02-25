from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
import re

@dataclass
class Pattern(ABC):

    @abstractmethod
    def regex(self):
        pass
    
    def match(self, string):
        # TODO: how do we incorporate flags?  global options?
        return re.match(self.regex(), string) 