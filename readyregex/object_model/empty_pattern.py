from dataclasses import dataclass
from addable import Addable

@dataclass
class EmptyPattern(Addable):

    def regex(self):
        return ""