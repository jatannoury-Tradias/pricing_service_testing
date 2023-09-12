import re
import uuid

from pydantic import BaseModel, validator

class Tier(BaseModel):
    name:str
    description:str
    instrument_codes:list[str]
    tier_type:str
    tradias_entity_id: str

    @validator('tier_type')
    def tier_type_validator(cls,tier_type):
        allowed_inputs = ["OTC","LP"]
        if tier_type not in allowed_inputs:
            raise ValueError("tier type must be OTC or LP")
        return tier_type
    @validator("instrument_codes")
    def instrument_codes_validator(cls,instrument_codes):
        pattern = r"^[A-Z]{3}-[A-Z]{3}$"
        for instrument_code in instrument_codes:
            if re.match(pattern, instrument_code) == False:
                raise ValueError(f"{instrument_code} is not a valid instrument format, the format should be as following: {pattern}")
        return instrument_codes
    @validator("tradias_entity_id")
    def tradias_entity_id_validator(cls,tradias_entity_id):
        try:
            uuid.UUID(tradias_entity_id)
        except:
            raise ValueError( f"Tradias entity ID:{tradias_entity_id} is not a valid UUID")




