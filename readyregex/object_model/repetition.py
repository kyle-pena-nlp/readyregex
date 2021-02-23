from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Set, Tuple, Sequence, Union, Any
from enum import Enum
from pattern import Pattern


@dataclass
class Repetition(Pattern):
    content : Pattern
    lb : Union[None,int]
    ub : Union[None,int]
    
    def __post_init__(self, content, lb, ub):
        assert lb is None or lb >= 0
        assert ub is None or ub >= 1
        assert (lb is None or ub is None) or (lb <= ub)
        self.content = content
        self.lb = lb
        self.ub = ub
    
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
