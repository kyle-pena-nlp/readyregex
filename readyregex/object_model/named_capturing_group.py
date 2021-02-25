from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Set, Tuple, Sequence, Union, Any
from enum import Enum
from .concatenatable_mixin import ConcatenatableMixin
from .surroundable_mixin import SurroundableMixin

@dataclass
class NamedCapturingGroup(ConcatenatableMixin, SurroundableMixin):
    name : str
    content : ConcatenatableMixin

    def regex(self):
        return "(?P<{}>{})".format(self.name, self.content.regex())