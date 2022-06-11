from dataclasses import dataclass, field
from ..object_model.pattern import *
from ..object_model.options import *


@dataclass
class Emoji(Pattern):

    def regex(self):
        raise Exception("Unimplemented.")