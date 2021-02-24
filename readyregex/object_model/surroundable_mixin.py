from abc import ABC
from dataclasses import dataclass

@dataclass
class SurroundableMixin:

    def surround_inner(self, left, right):
        klass = type(self)
        kwargs = self.todict()
        assert "content" in kwargs
        kwargs["content"] = left + self.content + right
        return klass(**kwargs)