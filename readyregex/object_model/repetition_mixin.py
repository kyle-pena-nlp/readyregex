from abc import ABC
from typing import Union, Tuple, Optional
from readyregex.object_model.repetition import Repetition
from readyregex.object_model.options import RepetitionOptions, Options

class RepetitionMixin(ABC):
    
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