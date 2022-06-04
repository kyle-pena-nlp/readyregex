from dataclasses import dataclass
from .pattern import Pattern

@dataclass
class Optional(Pattern):

    content: Pattern

    def regex(self):
        return "({})?".format(self.content.regex())