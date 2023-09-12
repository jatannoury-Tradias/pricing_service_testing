from config.OPC_config import OpcConfig
from models.PriceAlgo import PriceAlgo


def get_price_algo():
    return PriceAlgo(
        max_spread=OpcConfig.max_spread,
        min_spread=OpcConfig.min_spread,
        diff_bid=OpcConfig.diff_bid,
        diff_ask=OpcConfig.diff_ask,
        quote_quantity=OpcConfig.quote_quantity,
        mid_point_check=OpcConfig.mid_point_check,
        method=OpcConfig.method,
        spread=OpcConfig.spread,
        spread_basis=OpcConfig.spread_basis,
        quote_buy=OpcConfig.quote_buy,
        quote_sell=OpcConfig.quote_sell
    )