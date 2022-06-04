from readyregex.object_model.choice import Choice
from readyregex.object_model.options import Options
from readyregex.object_model.concatenatable_mixin import ConcatenatableMixin
from readyregex.object_model.pattern import Pattern
from readyregex.object_model.character_set import CharacterSet
from readyregex.object_model.options import RepetitionOptions

class SeparatorPattern(Pattern, ConcatenatableMixin):

    # What separator
    separator : Pattern
    # Is the separator mandatory/optional/prohibited
    separator_options : Options
    # What to surround the separator with
    extra_whitespace : CharacterSet 
    # How much whitespace to surround the separator with (can be "No whitespace")
    extra_whitespace_amount : RepetitionOptions

    def regex(self):
        if self.separator_options == Options.prohibited():
            self._build_with_separator()
        elif self.separator_options == Options.mandatory():
            self._build_with_separator()
        elif self.separator_options == Options.optional():
            opt1 = SeparatorPattern(self.separator, Options.Mandatory, self.extra_whitespace, self.extra_whitespace_amount)
            opt2 = SeparatorPattern(self.separator, Options.Prohibited, self.extra_whitespace, self.extra_whitespace_amount)
            pattern = Choice([opt1, opt2])
        else:
            raise Exception(str(self.separator_options))

        return pattern.regex()

    def _build_without_separator(self):
        return self.extra_whitespace * self.extra_whitespace_amount

    def _build_with_separator(self):
        pre = self.extra_whitespace * self.extra_whitespace_amount
        post = pre
        return pre + self.separator + post
    
        