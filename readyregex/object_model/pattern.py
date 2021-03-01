from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Any, Set
import re, logging, sys, json
from ..options import Options

@dataclass
class Pattern(ABC):

    @abstractmethod
    def regex(self):
        pass
    
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