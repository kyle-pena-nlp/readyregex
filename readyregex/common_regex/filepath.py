from dataclasses import dataclass
from enum import Enum, Flag
from ..object_model.pattern import *

class FilepathType(Enum):
    Windows = 1
    Unix = 2
    Both = 3

class FilepathOptions(Flag):
    Any = 0
    Relative = 1
    Absolute = 2

@dataclass
class Filepath(Pattern):
    pass