from dataclasses import dataclass, field
from readyregex.object_model.concatenatable_mixin import ConcatenatableMixin
from readyregex.object_model.pattern import Pattern
from readyregex.options import Options


@dataclass
class _Example(Pattern, ConcatenatableMixin):

    options: Options = Options.Default

    def regex(self):
        raise Exception("Unimplemented.")