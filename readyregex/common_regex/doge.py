from dataclasses import dataclass, field
from ..object_model.pattern import *
from ..object_model.options import *


@dataclass
class Doge(Pattern):

    def regex(self):
        # TODO: options for ear types
        return StringLiteral("U・ᴥ・U")