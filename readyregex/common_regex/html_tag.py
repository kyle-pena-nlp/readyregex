from dataclasses import dataclass
from ..object_model.pattern import Pattern
from ..object_model.options import Options
from enum import Enum

"""
    Intrepid reader -
    Please note that this matches html *tags*, not html itself
    As we all (hopefully) know, it is impossible to match html with regex
"""

class HtmlTagTypes(Enum):
    Any = 0
    Begin = 1
    End = 2
    SelfClosing = 4
    # Known as "void tags" in the standard like the "area" element
    # https://html.spec.whatwg.org/#the-area-element
    NoContentTag = 8 
    BeginComment = 16
    EndComment = 32
    DocType = 64


@dataclass
class HtmlTag(Pattern):
    attributes : Options
    tag_types : HtmlTagTypes