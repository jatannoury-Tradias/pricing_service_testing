import math

import pandas as pd

from config.OPC_config import OpcConfig
from config.endpoints import RequestHandler
from config.instruments.instrument_classification import SYMBOLS_CATEGORY
from models.Instrument import Instrument
from models.OutboudPriceChannel import OutboundPriceChannel
from models.PriceAlgo import PriceAlgo
from tools.get_euro_levels import get_euro_levels
from tools.price_fallbacks_parser import parse_price_fallbacks


def generate_opcs(instrument_codes: list[str], request_object: RequestHandler, pricing_df: pd.DataFrame,
                  price_precision_df: pd.DataFrame, tier_id: str, price_algo: PriceAlgo) -> dict[str,list[OutboundPriceChannel]]:
    all_outbounds = {}
    for instrument_code in instrument_codes:
        leg_1 = instrument_code.split("-")[0]
        leg_2 = instrument_code.split("-")[1]
        leg_1_category = SYMBOLS_CATEGORY[leg_1]
        leg_2_category = SYMBOLS_CATEGORY[leg_2]
        instrument = Instrument(
            currency_1=leg_1,
            currency_2=leg_2,
            currency_1_base_category=leg_1_category,
            currency_2_base_category=leg_2_category
        )
        euro_levels = get_euro_levels(instrument)
        price_fallbacks = parse_price_fallbacks(request_object.get_instrument_price_fallback(instrument_code))
        all_outbounds[instrument_code] = []
        for euro_level in euro_levels:
            exact_quantity = euro_level / \
                             pricing_df.loc[pricing_df['symbol'] == instrument_code.split("-")[0], 'euro_price'].values[
                                 0]
            qty = round(exact_quantity,
                        math.ceil(-math.log10(exact_quantity) + 1))
            all_outbounds[instrument_code].append(
                OutboundPriceChannel(
                    instrument_code=instrument_code,
                    price_function=OpcConfig.price_function,
                    quantity=str(qty),
                    price_precision=int(price_precision_df.loc[
                        price_precision_df['symbol'] == instrument_code.split("-")[0], 'precision'].values[0]),
                    tier_id=tier_id,
                    price_algo=price_algo,
                    price_fallback_hierarchies=price_fallbacks,
                )
            )
    return all_outbounds
