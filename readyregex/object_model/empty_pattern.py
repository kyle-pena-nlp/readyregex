from dataclasses import dataclass
from .pattern import Pattern

@dataclass
class EmptyPattern(Pattern):

    def regex(self):
        return ""