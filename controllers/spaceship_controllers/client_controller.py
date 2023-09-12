import requests

from config.variables import PricesServiceTestingClientVariables
from controllers.spaceship_controllers.controllers_initiator import ControllersInitiator


class ClientsController(ControllersInitiator):
    def  __init__(self):
        super().__init__()
    def modify_client_tier(self,tier_id):
        to_update = {
            'tier_id': f"{tier_id}"
        }
        return requests.put(f"{self.clients_url}/{PricesServiceTestingClientVariables.info.value['id']}/update_tier",headers=self.user_apis_headers,json=to_update)

if __name__ == '__main__':
    tier_testing_id = "ab1817a5-c738-433a-90a1-2130c9adf17d"
    pricing_service_joseph_tier_test_id = "4c7f8eaa-939e-4782-810e-b715da77b702"
    print(ClientsController().modify_client_tier(tier_testing_id))
    # print(ClientsController().modify_client_tier(pricing_service_joseph_tier_test_id))