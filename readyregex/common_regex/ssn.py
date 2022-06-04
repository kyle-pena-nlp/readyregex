from dataclasses import dataclass, field
from readyregex.object_model.character import Character
from readyregex.object_model.pattern import Pattern
from readyregex.object_model.options import Options, RepetitionOptions
from readyregex.object_model.regex_literal import RegexLiteral
from readyregex.object_model.separator_pattern import SeparatorPattern

@dataclass
class SSN(Pattern):

    extra_spaces : RepetitionOptions = RepetitionOptions.None_

    def build(self):

        # TODO: complete.

        separator = SeparatorPattern(Character("-"), Options.Mandatory, extra_spaces = self.extra_spaces, allow_no_separation=True)
        
        part1 = RegexLiteral(r"(?!000|666)[0-8][0-9]{2}")
        part2 = RegexLiteral(r"(?!00)[0-9]{2}")
        part3 = RegexLiteral(r"(?!0000)[0-9]{4}")

        final_pattern = part1 + separator + part2 + separator + part3

        return final_pattern