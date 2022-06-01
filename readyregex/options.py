import enum

# I don't use enum.auto() because I worry about hard to detect cross-version pickling stability problems

class Options(enum.IntEnum):
    Mandatory    = 1
    Optional     = 2
    Prohibited   = 4

    def mandatory(self):
        return self == Options.Mandatory

    def optional(self):
        return self == Options.Optional   

    def prohibited(self):
        return self == Options.Prohibited

class RepetitionOptions(enum.IntEnum):
    None_ = 1
    Any  = 2
    AtLeastOne = 4
    AtMostOne  = 8

    def none(self):
        return RepetitionOptions.None_ in self

    def any(self):
        return RepetitionOptions.Any in self

    def atleastone(self):
        return RepetitionOptions.AtLeastOne in self

    def atmostone(self):
        return RepetitionOptions.AtMostOne in self

class Buffers(enum.Flag):
    Spaces     = 1 
    Tabs       = 2
    Whitespace = 4

    def has_spaces(self):
        return Buffers.Spaces in self

    def has_tabs(self):
        return Buffers.Tabs in self

    def has_whitespace(self):
        return Buffers.Whitespace in self

class Separators(enum.Flag):
    Spaces      = 1
    Tabs        = 2
    LineReturns = 4
    Whitespace  = 8
    Dashes      = 16

    def has_spaces(self):
        return Separators.Spaces in self

    def has_tabs(self):
        return Separators.Tabs in self

    def has_linereturns(self):
        return Separators.LineReturns in self

    def has_whitespace(self):
        return Separators.Whitespace in self

    def has_dashes(self):
        return Separators.Dashes in self