# from tools.excel_tools.config import path
# from tools.excel_tools.read_functions.read_nuri_etf import load_nuri_from

NURI_EXCHANGE_CURRENCIES = {
    'PVP': 'ETF_PLAIN_VANILLA',
    'FGP': 'ETF_FEELGOOD',
    'PFT': 'ETF_GENESIS'
}

NURI_EXCHANGE_NAME = 'ETFPotPrices'
NURI_LEG_2 = 'EUR'

NURI_PRICE_DICT = {
    'FGPEUR': 1.000,
    'PFTEUR': 1.000,
    'PVPEUR': 1.000,
}

NURI_QUANTITY_PRECISION = 6
NURI_PRICE_PRECISION = 6
NURI_MINIMUM_QUANTITY = 1.0
NURI_MAXIMUM_QUANTITY = 9999999999
# if __name__ == "__main__":
#     nuri_config = load_nuri_from(path)
#     NURI_EXCHANGE_CURRENCIES = {
#         element: nuri_config[element][' Description'] for element in nuri_config
#     }
#     NURI_EXCHANGE_NAME = nuri_config[list(nuri_config.keys())[0]][' Exchange Name']
#     NURI_LEG_2 = nuri_config[list(nuri_config.keys())[0]][' LEG 2']
#     NURI_PRICE_DICT = {
#         element: nuri_config[element][' Price'] for element in nuri_config
#     }
#     NURI_QUANTITY_PRECISION = nuri_config[list(nuri_config.keys())[0]][' qty precision']
#     NURI_PRICE_PRECISION = nuri_config[list(nuri_config.keys())[0]][' price precision']
#     NURI_MINIMUM_QUANTITY = nuri_config[list(nuri_config.keys())[0]][' min qty']
#     NURI_MAXIMUM_QUANTITY = nuri_config[list(nuri_config.keys())[0]][' max qty']
#     pass