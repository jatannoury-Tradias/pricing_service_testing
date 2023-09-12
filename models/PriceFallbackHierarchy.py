import re
import uuid

from pydantic import BaseModel, validator

class PriceFallbackHierarchy(BaseModel):
    fallback_id:str
    fallback_type:str
    order:int
    name:str
    enabled:bool

    # @validator("fallback_id")
    # def fallback_id_validator(cls, fallback_id):
    #     try:
    #         uuid.UUID(fallback_id)
    #         return fallback_id
    #     except:
    #         raise ValueError(f"{fallback_id} is not a valid UUID")
    # @validator("fallback_type")
    # def fallback_type_validator(cls, fallback_type):
    #     if fallback_type == "FALLBACK_TYPE_MARKET_CONNECTOR":
    #         return fallback_type
    #     else:
    #         raise ValueError(f"{fallback_type} is not a valid value for fallback_type parameter")