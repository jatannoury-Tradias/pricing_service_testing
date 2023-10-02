import requests

from controllers.spaceship_controllers.controllers_initiator import ControllersInitiator
from config.endpoints import RequestHandler
from controllers.inputs_collector import get_all_inputs
from tools.generate_opcs import generate_opcs
from tools.get_price_algo import get_price_algo
from tools.read_price_precision import get_price_precisions
from tools.read_pricing_csv import read_pricing_df


class TiersController(ControllersInitiator):
    def  __init__(self):
        super().__init__()
    def create_tier(self):
        environment, new_tier_info, tier_type = get_all_inputs()
        request_object = RequestHandler(environment)
        tier_creation_response = request_object.create_tier(new_tier_info.__dict__)
        tier_info_response = request_object.get_tiers_by_type(tier_type=tier_type)['tiers']

        name = tier_creation_response['name']
        description = tier_creation_response['description']
        instrument_codes = tier_creation_response['instrument_codes']
        tier_id = \
            list(filter(lambda element: element['name'] == name and element['description'] == description,
                        tier_info_response))[
                0]['id']
        price_precision_df = get_price_precisions()
        pricing_df = read_pricing_df()
        price_algo = get_price_algo()
        all_outbounds = generate_opcs(instrument_codes, request_object, pricing_df, price_precision_df, tier_id,
                                      price_algo)
        counter = 0
        for instrument_code, opc_info in all_outbounds.items():
            if counter == 5:
                break
            counter +=1
            status_code, response = request_object.create_opc(opc_info, instrument_code)
            print(response)
        return {
            'name': name,
            'description': description,
            'instrument_codes': instrument_codes,
            'tier_id': tier_id,
            'all_outbounds': all_outbounds
        }


if __name__ == '__main__':
    print(TiersController().create_tier())