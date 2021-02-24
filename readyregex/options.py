import enum

class Options(enum.Flag):


    Default = enum.auto()
    
    # Phone Number Options
    OptionalAreaCode = enum.auto()
    AreaCode     = enum.auto()
    DashSeparators  = enum.auto()
    SpaceSeparators = enum.auto()
    AreaCodeParentheses = enum.auto()


    # Global Options
    #IgnoreCase = enum.auto()
    #Singleline = enum.auto()