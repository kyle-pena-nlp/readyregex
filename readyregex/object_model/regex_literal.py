import re
from dataclasses import dataclass

from readyregex.object_model.repetition_mixin import RepetitionMixin
from .pattern import Pattern
from .concatenatable_mixin import ConcatenatableMixin
from .pattern import Pattern
from ..ready_regex_exception import ReadyRegexException

@dataclass
class RegexLiteral(Pattern, ConcatenatableMixin, RepetitionMixin):

    regex_string : str

    def __post_init__(self):
        valid, error = RegexLiteral.is_valid_regex(self.regex_string)
        if not valid:
            raise ReadyRegexException("regex_string was not a valid regex string, was: '{}' ({} @ chr idx {})".format(self.regex_string, error.msg, error.pos))
        self._validate_types()

    @staticmethod
    def is_valid_regex(string):
        try:
            # TODO: will this blow out some kind of cache?
            re.compile(string)
            return True, None
        except re.error as e:
            return False, e

    def regex(self):
        return self.regex_string