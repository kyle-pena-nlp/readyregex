from dataclasses import dataclass
from .concatenatable_mixin import ConcatenatableMixin

@dataclass
class EmptyPattern(ConcatenatableMixin):

    def regex(self):
        return ""