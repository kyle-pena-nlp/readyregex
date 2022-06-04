from dataclasses import dataclass, field
from readyregex.object_model.concatenatable_mixin import ConcatenatableMixin
from readyregex.object_model.pattern import Pattern
from readyregex.object_model.string_literal import StringLiteral
from readyregex.object_model.choice import Choice
from readyregex.object_model.options import Options


@dataclass
class WesternEmoticon(Pattern, ConcatenatableMixin):

    options: Options = Options.Default

    # source: https://en.wikipedia.org/wiki/List_of_emoticons
    # todo: include flags / metadata so that user can specify Options.Smiley | Options.Surprise, for example
    western_emoticons = [
        ":‑)",
        ":)",   ":-]",
        ":]",   ":-3",
        ":3",   ":->",
        ":>",   "8-)",
        "8)",   ":-}",
        ":}",   ":o)",   ":c)",   ":^)",   "=]",   "=)",   
        ":‑D",
        ":D",   "8‑D",
        "8D",   "x‑D",
        "xD",   "X‑D",
        "XD",   "=D",   "=3",   "B^D",   "c:",   "C:",   
        ":-))",   
        ":‑(",
        ":(",   ":‑c",
        ":c",   ":‑<",
        ":<",   ":‑[",
        ":[",   ":-||",   ">:[",   ":{",   ":@",   ":(",   ";(",   
        ":'‑(",
        ":'(",   
        ":'‑)",
        ":')",   
        "D‑':",   "D:<",   "D:",   "D8",   "D;",   "D=",   "DX",   
        ":‑O",
        ":O",   ":‑o",
        ":o",   ":-0",   "8‑0",   ">:O",   
        ":-*",
        ":*",   
        ":×",   
        ";‑)",
        ";)",   "*-)",
        "*)",   ";‑]",
        ";]",   ";^)",   ":‑,",   ";D",   
        ":‑P",
        ":P",   "X‑P",
        "XP",   "x‑p",
        "xp",   ":‑p",
        ":p",   ":‑Þ",
        ":Þ",   ":‑þ",
        ":þ",   ":‑b",
        ":b",   "d:",   "=p",   ">:P",   
        ":-/",
        ":/",   ":‑.",   '>:\\',   ">:/",   ':\\',   "=/",   '=\\',   ":L",   "=L",   ":S",   
        ":‑|",
        ":|",   
        ":$",   "://)",
        "://3",   
        ":‑X",
        ":X",   ":‑#",
        ":#",   ":‑&",
        ":&",   
        "O:‑)",
        "O:)",   "0:‑3",
        "0:3",   "0:‑)",
        "0:)",   "0;^)",   
        ">:‑)",
        ":)",   "}:‑)",
        "}:)",   "3:‑)",
        "3:)",   ">;)",   ">:3",
        ";3",   
        "|;‑)",   "|‑O",   "B-)",   
        ":‑J",   
        "#‑)",
        "%‑)",
        "%)",   
        ":‑###..",
        ":###..",   
        "<:‑|",   
        "',:-|",   "',:-l",   
        ":E",   
        "<_<",   ">_>"
    ]

    def build(self):
        return Choice([ StringLiteral(emoticon_string) for emoticon_string in WesternEmoticon.western_emoticons ])