import logging

from config.instruments.nuri_config import NURI_EXCHANGE_CURRENCIES
from models.base_category import BaseCategory

my_logger = logging.getLogger(__name__)

STABLE = BaseCategory(name='STABLE', tier_number=0)
MAJOR = BaseCategory(name='MAJOR', tier_number=1)
MINOR = BaseCategory(name='MINOR', tier_number=2)
EXOTIC = BaseCategory(name='EXOTIC', tier_number=3)
RARE = BaseCategory(name='RARE', tier_number=4)
ETF = BaseCategory(name='ETF', tier_number=5)
MANUAL = BaseCategory(name='MANUAL', tier_number=6)

CATEGORIES = [STABLE, MAJOR, MINOR, EXOTIC, RARE, ETF, MANUAL]

# MAJOR
MAJOR_CRYPTO_1_SYMBOLS = ['ADA', 'BCH', 'BTC', 'DOT', 'ETH', 'LTC', 'MATIC', 'XRP']
MAJOR_CRYPTO_2_SYMBOLS = ['USDT']
MAJOR_FIAT_1_SYMBOLS = ['EUR']
MAJOR_FIAT_2_SYMBOLS = ['USD']
MAJOR_FIAT_SYMBOLS = MAJOR_FIAT_1_SYMBOLS + MAJOR_FIAT_2_SYMBOLS
MAJOR_SYMBOLS = MAJOR_CRYPTO_1_SYMBOLS + MAJOR_FIAT_1_SYMBOLS + MAJOR_FIAT_2_SYMBOLS + MAJOR_CRYPTO_2_SYMBOLS

# MINOR
MINOR_CRYPTO_SYMBOLS = ['AAVE', 'ATOM', 'AVAX', 'BNB', 'COMP', 'DOGE', 'EOS', 'ETC', 'LINK', 'SOL', 'TRX', 'UNI', 'XLM',
                        'XTZ']
MINOR_FIAT_1_SYMBOLS = ['CAD']
MINOR_FIAT_2_SYMBOLS = ['SEK', 'ZAR', 'SGD']
MINOR_FIAT_SYMBOLS = MINOR_FIAT_1_SYMBOLS + MINOR_FIAT_2_SYMBOLS
MINOR_SYMBOLS = MINOR_CRYPTO_SYMBOLS + MINOR_FIAT_SYMBOLS

# EXOTIC
EXOTIC_CRYPTO_SYMBOLS = ['ALGO', 'ANT', 'APE', 'AUDIO', 'AXS', 'BAT', 'BUSD', 'C98', 'CELO', 'CHZ', 'CRV',
                         'CTSI', 'CUSD', 'DYDX', 'EGLD', 'ENJ', 'EURT', 'FIL', 'FTM', 'GALA', 'GMT', 'HNT', 'IMX',
                         'KNC', 'MANA', 'MIOTA', 'MKR', 'NEO', 'NULS', 'OMG', 'REP', 'ROSE', 'SANTOS', 'SGB',
                         'SNX', 'SSV', 'STORJ', 'TBTC', 'YFI', 'ZIL', 'SCRT', 'ETHW', 'BADGER', 'LSK', 'XNO',
                         'BLUR']

EXOTIC_FIAT_SYMBOLS = ['PLN', 'BRL']
EXOTIC_SYMBOLS = EXOTIC_CRYPTO_SYMBOLS + EXOTIC_FIAT_SYMBOLS

# RARE
RARE_CRYPTO_SYMBOLS = ['1INCH', 'ALICE', 'ALPHA', 'AMP', 'ANKR', 'BAL', 'BAND', 'BNT', 'BOND', 'CLV', 'CQT', 'CRO',
                       'CVX', 'DAI', 'DENT', 'EWT', 'FET', 'FIS', 'FLOW', 'GHST', 'GLMR', 'GNO', 'GRT', 'HBAR', 'HOT',
                       'ICP', 'ICX', 'INJ', 'IOTX', 'KIN', 'KSM', 'LDO', 'LPT', 'LRC', 'MASK', 'MINA', 'MIR',
                       'MLN', 'NEAR', 'NMR', 'OCEAN', 'OGN', 'OXT', 'PAXG', 'PERP', 'PHA', 'POWR', 'QNT', 'QTUM',
                       'RAD', 'RARI', 'RAY', 'REN', 'RLY', 'RNDR', 'RPL', 'SAND', 'SHIB', 'SKL', 'SLP', 'SRM',
                       'STG', 'STX', 'SUSHI', 'SXP', 'THETA', 'UMA', 'VET', 'WOO', 'XYO', 'ZRX']
RARE_FIAT_SYMBOLS = []
RARE_SYMBOLS = RARE_CRYPTO_SYMBOLS + RARE_FIAT_SYMBOLS

# STABLE
STABLE_SYMBOLS = ['USDC']

# FIAT
# FIAT_SYMBOLS = MAJOR_FIAT_1_SYMBOLS + MAJOR_FIAT_2_SYMBOLS + MINOR_FIAT_SYMBOLS + EXOTIC_FIAT_SYMBOLS + RARE_FIAT_SYMBOLS
FIAT_SYMBOLS = MAJOR_FIAT_1_SYMBOLS + MAJOR_FIAT_2_SYMBOLS + MINOR_FIAT_1_SYMBOLS + RARE_FIAT_SYMBOLS

# Custom
ETF_SYMBOLS = list(NURI_EXCHANGE_CURRENCIES.keys())
MANUAL_SYMBOLS = ['TFA',"CSI"]
CUSTOM_SYMBOLS = ETF_SYMBOLS + MANUAL_SYMBOLS

# FORBIDDEN
FORBIDDEN_SYMBOLS = ['AEON', 'ONION', 'BTCP', 'RTM', 'BTCZ', 'TRTL', 'DASH', 'BWP', 'SUMO', 'CCX', 'EXC', 'BTCN',
                     'EVOX', 'BEAM', 'ZEC', 'XMR', 'ZER', 'HUSH', 'XVG', 'XHV', 'GRS', 'ZEN', 'GRIN', 'XSPEC',
                     'PRCY', 'PART', 'BDX', 'NAV', 'PHR', 'ARRR', 'KURT', 'IRD', 'DERO', 'PIVX', 'WAVES', 'KEEP', 'RUNE', 'NU', 'CEL']
ALL_TRADEABLE_SYMBOLS = MAJOR_CRYPTO_1_SYMBOLS + MAJOR_CRYPTO_2_SYMBOLS + MINOR_CRYPTO_SYMBOLS + EXOTIC_CRYPTO_SYMBOLS + RARE_CRYPTO_SYMBOLS + STABLE_SYMBOLS + FIAT_SYMBOLS + ETF_SYMBOLS + MANUAL_SYMBOLS

SYMBOLS_CATEGORY = {}

for symbol in ALL_TRADEABLE_SYMBOLS+FIAT_SYMBOLS:
    if symbol in STABLE_SYMBOLS:
        SYMBOLS_CATEGORY[symbol] = STABLE
    elif symbol in MAJOR_SYMBOLS:
        SYMBOLS_CATEGORY[symbol] = MAJOR
    elif symbol in MINOR_SYMBOLS:
        SYMBOLS_CATEGORY[symbol] = MINOR
    elif symbol in EXOTIC_SYMBOLS:
        SYMBOLS_CATEGORY[symbol] = EXOTIC
    elif symbol in RARE_SYMBOLS:
        SYMBOLS_CATEGORY[symbol] = RARE
    elif symbol in ETF_SYMBOLS:
        SYMBOLS_CATEGORY[symbol] = ETF
    elif symbol in MANUAL_SYMBOLS:
        SYMBOLS_CATEGORY[symbol] = MANUAL
