from dataclasses import dataclass
from .concatenatable_mixin import ConcatenatableMixin
from .surroundable_mixin import SurroundableMixin

@dataclass
class Optional(ConcatenatableMixin, SurroundableMixin):

    content: ConcatenatableMixin

    def regex(self):
        return "({})?".format(self.content.regex())