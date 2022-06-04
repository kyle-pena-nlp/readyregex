from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Iterable, Union, Tuple, Optional
import re, logging
from .type_hint_validation_mixin import TypeHintValidationMixin
from ..ready_regex_exception import ReadyRegexException
from .options import Options, RepetitionOptions

# Thought:  Separate regex method into a build() -> Pattern and regex() -> str method?

@dataclass
class Pattern(ABC, TypeHintValidationMixin):

    def __post_init__(self):
        self._validate_types()
        self._validate_input()        

    def _validate_input(self):
        pass
    
    # TODO: options on 'build'?
    def build(self):
        return self
    
    def regex(self):
        return self.build().regex()
    
    def match(self, string):
        regex_string = self.regex()
        self.debug("regex_string: {}, string: {}", regex_string, string)
        return re.match(regex_string, string)

    def match_whole_string(self, string):
        regex_string = self.regex()
        regex_string = "^{}$".format(regex_string)
        self.debug("regex_string: {}, string: {}", regex_string, string)       
        return re.match(regex_string, string)      
    
    def debug(self, msg, *args):
        # logging.debug does not do new-style formatting, so we have to do it ourselves
        msg = msg.format(*args)
        msg = "(In {}) ".format(type(self)) + msg
        logging.debug(msg)

    def add(self, other : 'Pattern') -> 'Pattern':
        if isinstance(self, PatternSequence):
            items = list(self.items)
        else:
            items = [self]
        if isinstance(other, PatternSequence):
            items.extend(other.items)
        else:
            items.append(other)
        return PatternSequence(items)

    def __add__(self, other : 'Pattern') -> 'Pattern':
        return self.add(other)

    def join(self, others : Iterable['Pattern']) -> 'Pattern':
        parts = []
        for i, part in enumerate(others):
            if isinstance(part, PatternSequence):
                parts.extend(part.items)
            else:
                parts.append(part)
            if i < len(others) - 1:
                parts.append(self)
        return PatternSequence(parts)         

    def __mul__(self, spec : Union[Options, RepetitionOptions, int, Tuple[Optional[int],Optional[int]]]):
        
        LB = None
        UB = None

        if isinstance(spec, Options):
            spec = spec.to_rep_spec()
        elif isinstance(spec, RepetitionOptions):
            spec = spec.to_rep_spec()
        elif isinstance(spec, int):
            spec = (spec, spec)
        elif isinstance(spec, tuple):
            pass
        else:
            raise Exception("Right hand side of multiplication must be an integer, or a repetition bound such as (2,5), (None,6), (7,None), or (None,None)")

        return Repetition(self, spec[0], spec[1])

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
