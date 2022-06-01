from readyregex.object_model.concatenatable_mixin import ConcatenatableMixin
from readyregex.object_model.empty_pattern import EmptyPattern
from readyregex.object_model.pattern import Pattern
from readyregex.object_model.character import Character
from readyregex.object_model.character_set import CharacterSet
from options import Separators, Buffers, RepetitionOptions
from readyregex.object_model.special_character_classes import SpecialCharacterClasses

class SeparatorPattern(Pattern, ConcatenatableMixin):

    separators : Separators
    buffers: Buffers
    buffer_repetition : RepetitionOptions

    def regex(self):

        character_set = CharacterSet()
        
        if self.separators.has_spaces():
            character_set.include(Character(" "))
        
        if self.separators.has_dashes():
            character_set.include(Character("-"))
        
        if self.separators.has_whitespace():
            character_set.include(SpecialCharacterClasses.WHITESPACE)

        if self.separators.has_tabs():
            character_set.include(Character("\t"))

        if self.separators.has_linereturns():
            character_set.include(Character("\r"))
            character_set.include(Character("\n"))

        buffer_character_set = CharacterSet()

        if self.buffers.has_whitespace():
            buffer_character_set.include(SpecialCharacterClasses.WHITESPACE)
        
        if self.buffers.has_spaces():
            buffer_character_set.include(Character(" "))

        if self.buffers.has_tabs():
            buffer_character_set.include(Character("\t"))

        buffer = buffer_character_set

        if self.buffer_repetition.none():
            buffer = EmptyPattern()
        elif self.buffer_repetition.any():
            buffer *= (None,None)
        elif self.buffer_repetition.atleastone():
            buffer *= (1,None)
        elif self.buffer_repetition.atmostone():
            buffer *= (None,1)

        pattern = buffer + character_set + buffer

        return pattern.regex()

        