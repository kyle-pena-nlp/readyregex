from dataclasses import dataclass

from readyregex.object_model.repetition_mixin import RepetitionMixin
from .concatenatable_mixin import ConcatenatableMixin
from .pattern import Pattern

@dataclass
class EmptyPattern(Pattern, ConcatenatableMixin, RepetitionMixin):

    def regex(self):
        return ""