# from tools.excel_tools.config import path
# from tools.excel_tools.read_functions.read_manual_params import load_manual_params_from

EXCHANGE_NAME_MANUAL_PRICING = 'ManualPricing'

TFA_PARAMETERS = {
    'xchg_code': 'ManualPricing',
    'curr_pair_1': 'TFA',
    'curr_pair_2': 'EUR',
    'curr_pair': 'TFAEUR',
    'xchg_curr_pair': 'TFAEUR.MANUAL',
    'qty_precision': 10,
    'curr_precision': 0,
    'min_qty': 0.00000001,
    'max_qty': 9999999999.00000000
}

CSI_PARAM ={
    'xchg_code': 'ManualPricing',
    'curr_pair_1': 'CSI',
    'curr_pair_2': 'EUR',
    'curr_pair': 'CSIEUR',
    'xchg_curr_pair': 'CSIEUR.MANUAL',
    'qty_precision': 10,
    'curr_precision': 10,
    'min_qty': 1,
    'max_qty': 10
}

MANUAL_PRICE_DICT = {
    'TFAEUR': 1.000,
    'CSIEUR':1.000
}

BID_ASK_STREAMS = {
    'TFAEUR': {'bid': 16, 'ask': 16},
    'CSIEUR': {'bid': 16.2, 'ask': 16.8}
}

MANUAL_PARAMETERS = [CSI_PARAM,TFA_PARAMETERS]

# if __name__ == "__main__":
#     manual_params = load_manual_params_from(path)
#     EXCHANGE_NAME_MANUAL_PRICING = manual_params[list(manual_params.keys())[0]][' xchg_code']
#     TFA_PARAMETERS = {
#         'xchg_code': manual_params[' TFA'][' xchg_code'],
#         'curr_pair_1': manual_params[' TFA'][' curr_pair_1'],
#         'curr_pair_2': manual_params[' TFA'][' curr_pair_2'],
#         'curr_pair': manual_params[' TFA'][' curr_pair'],
#         'xchg_curr_pair': manual_params[' TFA'][' xchg_curr_pair'],
#         'qty_precision': manual_params[' TFA'][' qty_precision'],
#         'curr_precision': manual_params[' TFA'][' curr_precision'],
#         'min_qty': manual_params[' TFA'][' min_qty'],
#         'max_qty': manual_params[' TFA'][' max_qty'],
#     }
#     CSI_PARAM={
#         'xchg_code': manual_params[' CSI'][' xchg_code'],
#         'curr_pair_1': manual_params[' CSI'][' curr_pair_1'],
#         'curr_pair_2': manual_params[' CSI'][' curr_pair_2'],
#         'curr_pair': manual_params[' CSI'][' curr_pair'],
#         'xchg_curr_pair': manual_params[' CSI'][' xchg_curr_pair'],
#         'qty_precision': manual_params[' CSI'][' qty_precision'],
#         'curr_precision': manual_params[' CSI'][' curr_precision'],
#         'min_qty': manual_params[' CSI'][' min_qty'],
#         'max_qty': manual_params[' CSI'][' max_qty'],
#     }
#     MANUAL_PRICE_DICT = {
#         manual_params[element][' curr_pair']:float(manual_params[element][' price']) for element in manual_params
#     }
#     BID_ASK_STREAMS = {
#         manual_params[element][' curr_pair']:{"bid":manual_params[element][' bid'],"ask":manual_params[element][' ask']} for element in manual_params
#     }
#     pass