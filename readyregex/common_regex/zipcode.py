from dataclasses import dataclass, field
from ..object_model.pattern import *
from ..object_model.options import *


@dataclass
class Zipcode(Pattern):

    def regex(self):
        raise Exception("Unimplemented.")