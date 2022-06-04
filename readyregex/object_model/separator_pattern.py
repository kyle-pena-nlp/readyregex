from dataclasses import dataclass
from typing import Union
from readyregex.object_model.character import Character
from readyregex.object_model.character_set_item import CharacterSetItem
from readyregex.object_model.choice import Choice
from readyregex.object_model.options import Options
from readyregex.object_model.pattern import Pattern
from readyregex.object_model.character_set import CharacterSet
from readyregex.object_model.options import Repetitions
from readyregex.object_model.regex_literal import RegexLiteral

@dataclass
class SeparatorPattern(Pattern):

    # What separator
    separator : Union[CharacterSetItem,CharacterSet]
    # Is the separator (like a dash or a slash) mandatory/optional/prohibited
    separator_options : Options
    # How much whitespace should we surround the separator with (can be "No whitespace")
    extra_spaces : Repetitions
    # Should we guarantee that the separator is non-zero-width
    allow_no_separation : bool = False

    def build(self):
        if self.separator_options.prohibited():
            pattern = self._build_without_separator()
        elif self.separator_options.mandatory():
            pattern = self._build_with_separator()
        elif self.separator_options.optional():
            opt1 = SeparatorPattern(self.separator, Options.Mandatory, self.extra_spaces, self.allow_no_separation)
            opt2 = SeparatorPattern(self.separator, Options.Prohibited, self.extra_spaces, self.allow_no_separation)
            pattern = Choice([opt1, opt2])
        else:
            raise Exception(str(self.separator_options))

        return pattern

    def _build_without_separator(self):
        spaces_rep_spec = self.extra_spaces.to_rep_spec()
        if not self.allow_no_separation:
            spaces_rep_spec = (1, spaces_rep_spec[1] or 1)
        return Character(" ") * spaces_rep_spec

    def _build_with_separator(self):
        pre = Character(" ") * self.extra_spaces
        post = pre
        return pre + self.separator + post
    
        