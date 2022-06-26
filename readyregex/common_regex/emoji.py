from dataclasses import dataclass
from ..object_model.pattern import Pattern

@dataclass
class Emoji(Pattern):

    def regex(self):
        raise Exception("Unimplemented.")