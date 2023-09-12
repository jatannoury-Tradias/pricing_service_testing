import requests

from config.variables import PricingServiceJosephTierTestingVariables
from controllers.spaceship_controllers.controllers_initiator import ControllersInitiator


class OpcsController(ControllersInitiator):
    def  __init__(self):
        super().__init__()
    def modify_opc(self):
        return requests.put(self.opc_url,headers=self.user_apis_headers,json=PricingServiceJosephTierTestingVariables.outbound_price_channels.value)

if __name__ == '__main__':
    OpcsController().modify_opc()