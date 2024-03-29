import enum

# I don't use enum.auto() because I worry about hard to detect cross-version pickling stability problems

class Options(enum.Enum):
    Mandatory    = 1
    Optional     = 2
    Prohibited   = 4
    # Synonym of Mandatory
    Yes          = 5
    # Synonym of Prohibited
    No           = 6
    # Synonym of Optional
    Maybe        = 7

    def mandatory(self):
        return self == Options.Mandatory or self == Options.Yes

    def optional(self):
        return self == Options.Optional or self == Options.Maybe

    def prohibited(self):
        return self == Options.Prohibited or self == Options.No

    def yes(self):
        return self.mandatory()

    def no(self):
        return self.prohibited()

    def maybe(self):
        return self.optional()

    def to_rep_spec(self):
        if self.mandatory():
            return (1,1)
        elif self.prohibited():
            return (0,0)
        elif self.optional():
            return (0,1)
        else:
            raise Exception(str(self))

class Repetitions(enum.Enum):
    None_       = 0
    Any         = 1
    ExactlyOnce = 2
    AtLeastOne  = 3
    AtMostOne   = 4

    def to_rep_spec(self):
        if self == Repetitions.None_:
            return (0,0)
        elif self == Repetitions.Any:
            return (None,None)
        elif self == Repetitions.ExactlyOnce:
            return (1,1)
        elif self == Repetitions.AtLeastOne:
            return (1,None)
        elif self == Repetitions.AtMostOne:
            return (None,1)
        else:
            raise Exception(str(self))

    def none(self):
        return Repetitions.None_ == self

    def any(self):
        return Repetitions.Any in self

    def exactlyonce(self):
        return Repetitions.ExactlyOnce in self

    def atleastone(self):
        return Repetitions.AtLeastOne in self

    def atmostone(self):
        return Repetitions.AtMostOne in self