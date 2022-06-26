from dataclasses import dataclass
from enum import Flag
from ..object_model.pattern import Pattern

class IPAddressType(Flag):
    Any = 0
    IPV4 = 1
    IPV6 = 2

@dataclass
class IPAddress(Pattern):
    pass