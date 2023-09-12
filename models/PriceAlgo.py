import re
import uuid
from typing import Union

from pydantic import BaseModel, validator

class PriceAlgo(BaseModel):
    max_spread: Union[str,None] = ""
    min_spread: Union[str,None] = ""
    diff_bid: str
    diff_ask: str
    quote_quantity: str = ""
    mid_point_check: str
    method: str
    spread: str
    spread_basis: str
    quote_buy: str
    quote_sell: str
    # @validator("method")
    # def method_validator(cls,method):
    #     allowed_values = ['Mid',"Bid/Ask"]
    #     if method in allowed_values:
    #         return method
    #     else:
    #         raise ValueError(f"{method} is not a valid method. Kindly consider using one of those algos: {', '.join(allowed_values)}")
    #
    @validator("spread_basis")
    def spread_basis_validator(cls, spread_basis):
        allowed_values = ['Mid', "Bid","Ask"]
        if spread_basis in allowed_values or spread_basis in [value.lower() for value in allowed_values]:
            return spread_basis.lower()
        else:
            raise ValueError(
                f"{spread_basis} is not a valid method. Kindly consider using one of those algos: {', '.join(allowed_values)}")
    #
    # @validator("quote_buy")
    # def quote_buy_validator(cls, quote_buy):
    #     if isinstance(quote_buy,bool):
    #         return str(quote_buy).lower()
    #     elif isinstance(quote_buy,str) and quote_buy.lower() == "false" or quote_buy.lower == "true":
    #         return str(quote_buy).lower()
    #     else:
    #         raise ValueError(f"{quote_buy} is not a valid value for quote_buy parameter. Kindly use a Boolean")
    #
    # @validator("quote_sell")
    # def quote_sell_validator(cls, quote_sell):
    #     if isinstance(quote_sell, bool):
    #         return str(quote_sell).lower()
    #     elif isinstance(quote_sell,str) and quote_sell.lower() == "false" or quote_sell.lower == "true":
    #         return str(quote_sell).lower()
    #     else:
    #         raise ValueError(f"{quote_sell} is not a valid value for quote_sell parameter. Kindly use a Boolean")
    #
    @validator("max_spread")
    def max_spread_validator(cls,max_spread):
        if max_spread == None:
            return ""
        else:
            return max_spread