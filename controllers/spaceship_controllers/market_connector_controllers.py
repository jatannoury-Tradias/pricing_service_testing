import asyncio
import json
import websockets
from typing import List
from controllers.spaceship_controllers.controllers_initiator import ControllersInitiator

import requests


class MarketConnectorController(ControllersInitiator):
    def __init__(self):
        super().__init__()
    def get_market_connectors_data(self):
        return requests.get(self.market_connector_url,headers=self.user_apis_headers)
    def get_health_checks_market_connectors_data(self,market_connector_id):
        return requests.get(f"{self.market_connector_url}/{market_connector_id}",headers=self.user_apis_headers)
if __name__ =="__main__":
    market_connector_controller = MarketConnectorController()
    response = market_connector_controller.get_market_connectors_data()
    json_response = response.json()
    b2c2_data = list(filter(lambda element: element['name'] == "B2C2",json_response['items']))
    b2c2_health_checks_data = market_connector_controller.get_health_checks_market_connectors_data(b2c2_data[0]['id'])
    pass