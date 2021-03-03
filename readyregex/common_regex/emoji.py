from dataclasses import dataclass, field
from readyregex.object_model.concatenatable_mixin import ConcatenatableMixin
from readyregex.object_model.pattern import Pattern
from readyregex.object_model.string_literal import StringLiteral
from readyregex.options import Options


@dataclass
class Emoji(Pattern, ConcatenatableMixin):

    options: Options = Options.Default

    def regex(self):
        raise Exception("Unimplemented.")