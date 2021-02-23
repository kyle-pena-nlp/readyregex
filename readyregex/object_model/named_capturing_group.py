from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Set, Tuple, Sequence, Union, Any
from enum import Enum
from pattern import Pattern


@dataclass
class NamedCapturingGroup(Pattern):
    name : Union[str,None] = None
    pattern : Pattern

    def regex(self):
        return "(?P<{}>{})".format(self.name, self.pattern.regex())