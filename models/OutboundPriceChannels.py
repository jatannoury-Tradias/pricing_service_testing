from pydantic import BaseModel, validator
import re

from models.OutboudPriceChannel import OutboundPriceChannel


class OutboundPriceChannels(BaseModel):
    outbound_price_channels: list[OutboundPriceChannel]
    slow_quoting_interval:str
    instrument_code:str

    @validator("instrument_code")
    def instrument_code_validator(cls, instrument_code):
        pattern = r"^[A-Z]{3}-[A-Z]{3}$"
        if re.match(pattern, instrument_code):
            return instrument_code
        else:
            raise ValueError(
                f"{instrument_code} is not a valid format for the instrument code. Please consider the following pattern {pattern}")



