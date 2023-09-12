from config.OPC_config import OpcConfig
from config.instruments.instrument_classification import MAJOR,MINOR,EXOTIC,RARE,STABLE,ETF,MANUAL
from models.Instrument import Instrument


def get_euro_levels(instrument: Instrument):
    if instrument.category == MAJOR:
        return OpcConfig.MAJOR_LEVELS
    elif instrument.category == MINOR:
        return OpcConfig.MINOR_LEVELS
    elif instrument.category == EXOTIC:
        return OpcConfig.EXOTIC_LEVELS
    elif instrument.category == STABLE:
        return OpcConfig.STABLE_LEVELS
    elif instrument.category == ETF:
        return OpcConfig.ETF_LEVELS
    elif instrument.category == RARE:
        return OpcConfig.RARE_LEVELS
    elif instrument.category == MANUAL:
        return OpcConfig.MANUAL_LEVELS
