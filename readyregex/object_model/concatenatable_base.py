from abc import ABC
from dataclasses import dataclass
from pattern import Pattern

@dataclass
class ConcatenatableBase(Pattern, ABC):
    
    def _get_content_array(self):
        return getattr(self, "concatenatables")  if hasattr(self, "concatenatables")  else [ self ]