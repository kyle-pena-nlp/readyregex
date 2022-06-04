from dataclasses import dataclass, field
from readyregex.object_model.concatenatable_mixin import ConcatenatableMixin
from readyregex.object_model.pattern import Pattern
from readyregex.object_model.options import Options
from readyregex.object_model.regex_literal import RegexLiteral

@dataclass
class SSN(Pattern, ConcatenatableMixin):

    options: Options = Options.Default

    def regex(self):

        # TODO: complete.

        if (self.options & Options.IgnoreExtraWhitespace):
            separator = RegexLiteral(r"\s*-?\s*")
        else:
            separator = RegexLiteral(r"-?")

        
        part1 = RegexLiteral(r"(?!000|666)[0-8][0-9]{2}")
        part2 = RegexLiteral(r"(?!00)[0-9]{2}")
        part3 = RegexLiteral(r"(?!0000)[0-9]{4}")

        final_pattern = part1 + separator + part2 + separator + part3

        return final_pattern.regex()