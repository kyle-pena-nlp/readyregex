from dataclasses import dataclass, field
from readyregex.object_model.concatenatable_mixin import ConcatenatableMixin
from readyregex.object_model.pattern import Pattern
from readyregex.object_model.options import Options


@dataclass
class Number(Pattern, ConcatenatableMixin):

    options: Options = Options.Default

    def regex(self):

        # Options: Whole, Decimal, Scientific, Negative, etc., combinations, per the readme suggestions.  Not sure about fraction?  Maybe this is a separate pattern.

        raise Exception("Unimplemented.")