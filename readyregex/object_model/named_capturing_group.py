from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Set, Tuple, Sequence, Union, Any
from enum import Enum
from concatenatable import Concatenatable
from surroundable_mixin import SurroundableMixin

@dataclass
class NamedCapturingGroup(Concatenatable, SurroundableMixin):
    name : str
    content : Concatenatable

    def regex(self):
        return "(?P<{}>{})".format(self.name, self.content.regex())