from abc import ABC
from dataclasses import dataclass, field, fields
from collections import defaultdict
from typing import Iterable, Union, Tuple, Optional, List, Dict
import re, logging
from .type_hint_validation_mixin import TypeHintValidationMixin
from ..ready_regex_exception import ReadyRegexException
from .options import Options, Repetitions

@dataclass
class Pattern(ABC, TypeHintValidationMixin):

    def __post_init__(self):
        self._validate_types()
        self._validate_input()        

    # Can be overriden
    def _validate_input(self):
        pass

    # Can be overriden
    def build(self):
        return self

    # Can be overriden
    def simplify(self):
        return self
    
    # Can be (but probably shouldn't be) overriden
    def regex(self):
        return self.build().simplify().regex()

    def debug(self, msg, *args):
        # logging.debug does not do new-style formatting, so we have to do it ourselves
        msg = msg.format(*args)
        msg = "(In {}) ".format(type(self)) + msg
        logging.debug(msg)

    def match(self, string):
        regex_string = self.regex()
        self.debug("regex_string: {}, string: {}", regex_string, string)
        return re.match(regex_string, string)

    def match_whole_string(self, string):
        regex_string = self.regex()
        regex_string = "^{}$".format(regex_string)
        self.debug("regex_string: {}, string: {}", regex_string, string)       
        return re.match(regex_string, string)      

    def findall(self, string):
        return re.findall(self.regex(), string)

    def finditer(self, string):
        return re.finditer(self.regex(), string)

    def withname(self, name):
        return NamedCapturingGroup(name, self)

    def join(self, others : Iterable[Union['Pattern',str]]) -> 'Pattern':
        parts = []
        for i, part in enumerate(others):
            if isinstance(part, PatternSequence):
                parts.extend(part.items)
            elif isinstance(part, str):
                parts.append(StringLiteral(part))
            else:
                parts.append(part)
            if i < len(others) - 1:
                parts.append(self)
        return PatternSequence(parts)   

    def add(self, other : 'Pattern') -> 'Pattern':
        if isinstance(self, PatternSequence):
            items = list(self.items)
        else:
            items = [self]
        if isinstance(other, PatternSequence):
            items.extend(other.items)
        elif isinstance(other, str):
            items.append(StringLiteral(other))
        else:
            items.append(other)
        return PatternSequence(items)

    def __add__(self, other : 'Pattern') -> 'Pattern':
        return self.add(other)      

    def __mul__(self, spec : Union[Options, Repetitions, int, Tuple[Optional[int],Optional[int]]]):

        if isinstance(spec, Options):
            spec = spec.to_rep_spec()
        elif isinstance(spec, Repetitions):
            spec = spec.to_rep_spec()
        elif isinstance(spec, int):
            spec = (spec, spec)
        elif isinstance(spec, tuple):
            pass
        else:
            raise Exception("Right hand side of multiplication must be an integer, or a repetition bound such as (2,5), (None,6), (7,None), or (None,None)")

        return Repetition(self, spec[0], spec[1])

    def __or__(self, other : Union['Pattern', str]):
        return self.or_(other)

    def or_(self, other : Union['Pattern', str]):
        choices = [self]
        if isinstance(other, Choice):
            choices.extend(other.choices)
        elif isinstance(other, str):
            choices.append(StringLiteral(other))
        return Choice(choices)

    def expected_match(self, string):
        EXPECTED_MATCHES[id(self)].append(string)

    def expected_nonmatch(self, string):
        EXPECTED_NONMATCHES[id(self)].append(string)

    def test(self, visited = None):
        self_id = id(self)
        visited = visited or set()
        for expected_match in EXPECTED_MATCHES[self_id]:
            assert self.match(expected_match)
        for expected_nonmatch in EXPECTED_NONMATCHES[self_id]:
            assert not self.match(expected_nonmatch)
        visited.add(self_id)
        for field_ in fields(self):
            field_value = getattr(self, field_.name)
            field_value_id = id(field_value)
            if field_value_id in visited:
                continue
            if not isinstance(field_value, Pattern):
                continue
            field_value.test(visited = visited)

    def issue_url(self):
        raise Exception("todo - CLI - Generate issue URL and formatted content")


# Unfortunately I could not store these on the object itself because I cannot have fields with default values in the parent class
# So, I simulate object storage with this awfulness
EXPECTED_MATCHES : Dict[int,List[str]] = defaultdict(lambda: [])
EXPECTED_NONMATCHES : Dict[int,List[str]] = defaultdict(lambda: [])
            


@dataclass
class PatternSequence(Pattern):
    
    items : Iterable[Pattern] = field(default_factory = list)

    def regex(self):
        return "".join(item.regex() for item in self.items)


@dataclass
class Repetition(Pattern):

    content : Pattern
    lb : Union[None,int]
    ub : Union[None,int]
    
    def __post_init__(self):

        if not (self.lb is None or self.lb >= 0):
            raise ReadyRegexException("lb must be None or non-negative, was {}".format(self.lb))

        if not (self.ub is None or self.ub >= 0):
            raise ReadyRegexException("ub must be None or non-negative, was {}".format(self.ub))

        if not ((self.lb is None or self.ub is None) or (self.lb <= self.ub)):
            raise ReadyRegexException("either lb or ub must be none, or lb must be less than or equal to ub.  Was {} and {}, respectively".format(self.lb, self.ub))

        self._validate_types()
    
    def regex(self):
        # Omit (zero reptitions). Note: Here, 0 *does not* mean the same thing as None (which means "unspecified")
        if self.lb == self.ub == 0:
            return ""        
        # Optional
        elif not self.lb and self.ub == 1:
            return "({})?".format(self.content.regex())
        # Exactly one repetition
        elif self.lb == 1 and self.ub == 1:
            return self.content.regex()
        # m == n, m != None
        elif self.lb is not None and self.lb == self.ub:
            return "({}){{{}}}".format(self.content.regex(), self.lb)        
        # Range of repetitions (m,n)            
        elif self.lb is not None and self.ub is not None:
            return "({}){{{},{}}}".format(self.content.regex(), self.lb, self.ub)
        # At least one (min 1, no max)
        elif self.lb == 1 and self.ub is None:
            return "({})+".format(self.content.regex())
        # Min but no max repetitions
        elif self.lb is not None and self.ub is None:
            return "({}){{{},}}".format(self.content.regex(), self.lb)
        # Max but no min repetitions
        elif self.lb is None and self.ub is not None:
            return "({}){{,{}}}".format(self.content.regex(), self.ub)
        # Zero or None min, and no max (interpreted as *)
        elif not self.lb and self.ub is None:
            return "({})*".format(self.content.regex())
        else:
            raise Exception()

@dataclass
class StringLiteral(Pattern):

    string : str
    
    def __post_init__(self):
        self.regex_escaped_string = re.escape(self.string)
        self._validate_types()

    def regex(self):
        return self.regex_escaped_string


@dataclass
class Choice(Pattern):

    choices : Iterable[Pattern] = field(default_factory = list)

    def __post_init__(self):
        self.choices = [ StringLiteral(item) if isinstance(item,str) else item for item in self.choices ]
        self._validate_types()

    def regex(self):
        return "({})".format("|".join("({})".format(choice.regex()) for choice in self.choices))


@dataclass
class NamedCapturingGroup(Pattern):
    name : str
    content : Pattern

    def __post_init__(self):
        if len(self.name) == 0:
            raise ReadyRegexException("name must have at least one character")
        elif self.name[0].isalpha():
            raise ReadyRegexException("name must start with a letter, was '{}'".format(self.name))
        elif self.name.isalnum():
            raise ReadyRegexException("name must consist solely of alphanumeric characters, was '{}'".format(self.name))
        self._validate_types()

    def regex(self):
        return "(?P<{}>{})".format(self.name, self.content.regex())