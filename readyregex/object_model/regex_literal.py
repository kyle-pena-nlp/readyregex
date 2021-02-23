from pattern import Pattern
from addable import Addable
from dataclasses import dataclass
import re

@dataclass
class RegexLiteral(Addable):
    regex_string : str

    def __post_init__(self, regex_string):
        assert RegexLiteral.is_valid_regex(regex_string)
        self.regex_string = regex_string

    @staticmethod
    def is_valid_regex(string):
        try:
            re.compile(string)
            return True
        except re.error:
            return False

    def regex(self):
        return self.regex_string