import dataclasses


from models.base_category import BaseCategory
from config.instruments.instrument_classification import STABLE,   MAJOR_FIAT_SYMBOLS

@dataclasses.dataclass
class Instrument:
    currency_1: str
    currency_2: str
    currency_1_base_category: BaseCategory
    currency_2_base_category: BaseCategory


    @property
    def category(self) -> BaseCategory:
        if self.currency_1_base_category == STABLE:
            if self.currency_2 in MAJOR_FIAT_SYMBOLS:
                return STABLE
        if self.currency_2_base_category == STABLE:
            if self.currency_1 in MAJOR_FIAT_SYMBOLS:
                return STABLE
        if self.currency_1_base_category.tier_number >= self.currency_2_base_category.tier_number:
            return self.currency_1_base_category
        if self.currency_2_base_category.tier_number >= self.currency_1_base_category.tier_number:
            return self.currency_2_base_category

    @property
    def instrument_code(self) -> str:
        return f"{self.currency_1}{self.currency_2}"

    @property
    def instrument_code_reverse(self) -> str:
        return f"{self.currency_2}{self.currency_1}"

    def __str__(self):
        return f"{self.currency_1}-{self.currency_2}"