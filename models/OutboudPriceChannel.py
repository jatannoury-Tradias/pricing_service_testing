import re
import uuid

from pydantic import BaseModel, validator

from models.PriceAlgo import PriceAlgo
from models.PriceFallbackHierarchy import PriceFallbackHierarchy


class OutboundPriceChannel(BaseModel):
    instrument_code:str
    price_function:str
    quantity:str
    price_precision:int
    tier_id:str
    price_algo:PriceAlgo
    price_fallback_hierarchies:list[PriceFallbackHierarchy]
    # @validator("isNew")
    # def isNew_validator(cls,isNew):
    #     if isinstance(isNew,bool):
    #         return str(isNew)
    #     else:
    #         raise ValueError(f"isNew parameter does not accept the given value. Please ensure to pass a bool")
    # @validator("instrument_code")
    # def instrument_code_validator(cls,instrument_code):
    #     pattern = r"^[A-Z]{3}-[A-Z]{3}$"
    #     if re.match(pattern,instrument_code):
    #         return instrument_code
    #     else:
    #         raise ValueError(f"{instrument_code} is not a valid format for the instrument code. Please consider the following pattern {pattern}")
    # @validator("price_function")
    # def price_function_validator(cls,price_function):
    #     allowed_values = ["INTERPOLATE","FLAT"]
    #     if price_function in allowed_values:
    #         return price_function
    #     else:
    #         raise ValueError(f"{price_function} is not a valid parameter. Kindly consoder using one of the following: {', '.join(allowed_values)}")
    # @validator("tier_id")
    # def tier_id_validator(cls,tier_id):
    #     try:
    #         uuid.UUID(tier_id)
    #         return tier_id
    #     except:
    #         raise ValueError(f"{tier_id} is not a valid UUID")
    #
