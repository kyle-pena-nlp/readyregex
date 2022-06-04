from dataclasses import dataclass

from readyregex.object_model.repetition_mixin import RepetitionMixin
from .concatenatable_base import ConcatenatableBase
from .concatenatable_mixin import ConcatenatableMixin
from .surroundable_mixin import SurroundableMixin
from .pattern import Pattern

@dataclass
class Optional(Pattern, ConcatenatableMixin, RepetitionMixin, SurroundableMixin):

    content: ConcatenatableBase

    def regex(self):
        return "({})?".format(self.content.regex())