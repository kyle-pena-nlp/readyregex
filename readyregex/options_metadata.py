import enum
from typing import Tuple
from enriched_enum_base import EnrichedEnumBase


class OptionType(enum.Flag):
    """
        What kind of enum type is this?
    """
    MutuallyExclusive = enum.auto()
    Additive          = enum.auto()
