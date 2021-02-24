from dataclasses import dataclass
from concatenatable import Concatenatable

@dataclass
class EmptyPattern(Concatenatable):

    def regex(self):
        return ""