from dataclasses import dataclass, field
from ..object_model.pattern import *
from ..object_model.options import *
from ..object_model.separator_pattern import SeparatorPattern
from ..object_model.regex_literal import RegexLiteral
from ..object_model.character import Character


@dataclass
class SSN(Pattern):

    extra_spaces : Repetitions = Repetitions.None_

    def build(self):

        # TODO: complete.

        separator = SeparatorPattern(Character("-"), Options.Mandatory, extra_spaces = self.extra_spaces, allow_no_separation=True)
        
        part1 = RegexLiteral(r"(?!000|666)[0-8][0-9]{2}")
        part2 = RegexLiteral(r"(?!00)[0-9]{2}")
        part3 = RegexLiteral(r"(?!0000)[0-9]{4}")

        final_pattern = part1 + separator + part2 + separator + part3

        return final_pattern