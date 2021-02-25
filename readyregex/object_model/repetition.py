from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Set, Tuple, Sequence, Union, Any
from enum import Enum
from .concatenatable_mixin import ConcatenatableMixin
from .surroundable_mixin import SurroundableMixin
from .pattern import Pattern


@dataclass
class Repetition(Pattern, ConcatenatableMixin, SurroundableMixin):

    content : ConcatenatableMixin
    lb : Union[None,int]
    ub : Union[None,int]
    
    def __post_init__(self):
        assert self.lb is None or self.lb >= 0
        assert self.ub is None or self.ub >= 1
        assert (self.lb is None or self.ub is None) or (self.lb <= self.ub)
    
    def regex(self):
        # Optional
        if not self.lb and self.ub == 1:
            return "({})?".format(self.content.regex())
        # Exactly one repetition
        elif self.lb == 1 and self.ub == 1:
            return self.content.regex()
        # Range of repetitions (m,n)
        elif self.lb is not None and self.ub is not None:
            return "({}){{{},{}}}".format(self.content.regex(), self.lb, self.ub)
        # At least one (min 1, no max)
        elif self.lb == 1 and self.ub is None:
            return "({})+".format(self.content.regex())
        # Min but no max repetitions
        elif self.lb is not None and self.ub is None:
            return "({}){{{},}}".format(self.content.regex(), self.lb)
        # Max but no min repetitions
        elif self.lb is None and self.ub is not None:
            return "({}){{,{}}}".format(self.content.regex(), self.ub)
        # Zero or None min, and no max (interpreted as *)
        elif not self.lb and self.ub is None:
            return "({})*".format(self.content.regex())
        else:
            raise Exception()
