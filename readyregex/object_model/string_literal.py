import re
from addable import Addable
from dataclasses import dataclass

@dataclass
class StringLiteral(Addable):

    regex_escaped_string : str
    
    def __post_init__(self, string : str):
        self.regex_escaped_string = re.escape(string)

    def regex(self):
        return self.regex_escaped_string
    
