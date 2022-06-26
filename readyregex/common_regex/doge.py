from dataclasses import dataclass
from ..object_model.pattern import Pattern, StringLiteral

@dataclass
class Doge(Pattern):

    def regex(self):
        # TODO: options for ear types
        return StringLiteral("U・ᴥ・U")