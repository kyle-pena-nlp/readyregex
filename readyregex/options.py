import enum

class Options(enum.Flag):


    Default = enum.auto()
    
    # Phone Number Options
    AreaCode     = enum.auto()
    DashSeparators  = enum.auto()
    SpaceSeparators = enum.auto()
    AreaCodeParentheses = enum.auto()