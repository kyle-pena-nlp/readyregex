import re
from dataclasses import dataclass
from .pattern import Pattern
from .concatenatable_mixin import ConcatenatableMixin

@dataclass
class RegexLiteral(ConcatenatableMixin):

    regex_string : str

    def __post_init__(self):
        assert RegexLiteral.is_valid_regex(self.regex_string)

    @staticmethod
    def is_valid_regex(string):
        try:
            re.compile(string)
            return True
        except re.error:
            return False

    def regex(self):
        return self.regex_string