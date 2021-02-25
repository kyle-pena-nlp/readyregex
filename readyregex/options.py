import enum

class Options(enum.Flag):


    Default = enum.auto()
    
    # Phone Number Options
    MandatoryAreaCodeParentheses = enum.auto()
    NoAreaCodeParentheses = enum.auto()
    OptionalAreaCode    = enum.auto()
    NoAreaCode          = enum.auto()
    OnlyDashSeparators  = enum.auto()
    OnlySpaceSeparators = enum.auto()    
    NoSeparators        = enum.auto()
    OptionalSeparators  = enum.auto()    

    # General Options
    IgnoreExtraWhitespace = enum.auto()

    # Global Options
    #IgnoreCase = enum.auto()
    #Singleline = enum.auto()