from dataclasses import dataclass
from .concatenatable_mixin import ConcatenatableMixin
from .pattern import Pattern

@dataclass
class EmptyPattern(Pattern, ConcatenatableMixin, RepetitionMixin):

    def regex(self):
        return ""