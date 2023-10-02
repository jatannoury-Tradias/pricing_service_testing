import dataclasses


@dataclasses.dataclass
class OpcConfig:
    EXCHANGE_HIERARCHY = ["Talos", "Coinbase", "Trever", "B2C2", "Binance", "Bitfinex", "Bitstamp", "Kraken", "BitVavo",
        "ManualPricing", "Test Index"]
    price_function = "INTERPOLATE"
    slow_quoting_interval = "0.0"
    max_spread = None
    min_spread = "0"
    diff_bid = "0"
    diff_ask = "0"
    quote_quantity = ""
    mid_point_check = "0.0"
    method = "Bid/Ask"
    spread = "0"
    spread_basis = "Bid"
    quote_buy = "False"
    quote_sell = "False"
    MAJOR_LEVELS = [100, 1_000, 5_000, 10_000, 50_000, 100_000, 250_000, 500_000, 1_000_000, 5_000_000]
    MINOR_LEVELS = [100, 1_000, 5_000, 10_000, 50_000, 100_000, 250_000, 500_000]
    EXOTIC_LEVELS = [100, 1_000, 5_000, 10_000, 15_000]
    RARE_LEVELS = [100, 1_000, 5_000, 10_000, 15_000]
    STABLE_LEVELS = []
    ETF_LEVELS = []
    MANUAL_LEVELS = [],
