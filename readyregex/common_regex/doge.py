from dataclasses import dataclass, field
from readyregex.object_model.concatenatable_mixin import ConcatenatableMixin
from readyregex.object_model.pattern import Pattern
from readyregex.object_model.string_literal import StringLiteral
from readyregex.object_model.options import Options


@dataclass
class Doge(Pattern, ConcatenatableMixin):

    def regex(self):
        # TODO: options for ear types
        return StringLiteral("U・ᴥ・U")