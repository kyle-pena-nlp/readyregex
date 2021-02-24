from dataclasses import dataclass
from concatenatable import Concatenatable
from surroundable_mixin import SurroundableMixin

@dataclass
class Optional(Concatenatable, SurroundableMixin):

    content: Concatenatable

    def regex(self):
        return "({})?".format(self.content.regex())