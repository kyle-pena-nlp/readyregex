from abc import ABC
from dataclasses import dataclass
from pattern import Pattern

@dataclass
class AddableBase(Pattern, ABC):
    
    def _get_content_array(self):
        return getattr(self, "addables")  if hasattr(self, "addables")  else [ self ]