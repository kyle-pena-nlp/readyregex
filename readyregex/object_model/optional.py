from dataclasses import dataclass
from addable import Addable
from pattern import Pattern

@dataclass
class Optional(Addable):

    content: Pattern

    def regex(self):
        return "({})?".format(self.content.regex())