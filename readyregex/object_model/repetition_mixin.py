from abc import ABC
from typing import Union, Tuple, Optional
from readyregex.object_model.repetition import Repetition

class RepetitionMixin(ABC):
    
    def __mul__(self, spec : Union[int,Tuple[Optional[int],Optional[int]]]):
        
        LB = None
        UB = None

        if isinstance(spec, int):
            spec = (spec, spec)
        elif isinstance(spec, tuple):
            pass
        else:
            raise Exception("Right hand side of multiplication must be an integer, or a repetition bound such as (2,5), (None,6), (7,None), or (None,None)")

        return Repetition(self, spec[0], spec[1])