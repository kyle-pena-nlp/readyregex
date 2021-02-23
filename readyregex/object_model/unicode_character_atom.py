import re
from dataclasses import dataclass
from atom import Atom

@dataclass
class UnicodeCharacterAtom(Atom):
    
    hex : int

    @staticmethod
    def hex_parse_or_none(string):
        return int(string, 16)

    def __post_init__(self, hex):
        if isinstance(hex, int):
            hex_int = hex
        elif isinstance(hex, str) and len(hex) == 1:
            hex_int = ord(hex[0])
        elif UnicodeCharacterAtom.hex_parse_or_none(hex):
            hex_int = UnicodeCharacterAtom.hex_parse_or_none(hex)
        else:
            raise Exception(hex)
        assert 0 <= hex_int and hex_int <= 1114111
        self.hex = hex_int

    def regex(self):
        return re.escape(chr(self.hex))