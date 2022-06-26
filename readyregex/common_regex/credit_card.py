from dataclasses import dataclass
from enum import Flag
from ..object_model.pattern import Pattern, Choice
from ..object_model.options import Repetitions

class CreditCardType(Flag):
    Any = 0    
    VISA = 1
    MasterCard = 2
    AmericanExpress = 4
    DiscoverCard = 8

@dataclass
class CreditCard(Pattern):
    
    card_type : CreditCardType
    extra_space : Repetitions

    def build(self):
        card_type = self._card_type()

        IIN_numbers, valid_lengths, validation_type = self._pattern_parts(card_type)

        choices = []

        raise Exception("TODO")

        return Choice(choices)        
    
    def _card_type(self):
        if self.card_type == CreditCardType.Any:
            return CreditCardType.VISA | CreditCardType.MasterCard | CreditCardType.AmericanExpress | CreditCardType.DiscoverCard
        else:
            return self.card_type