from config.tokens import PREPROD_SPACESHIP_USER_TOKEN, PREPROD_SPACESHIP_CLIENT_TOKEN, UAT_SPACESHIP_CLIENT_TOKEN, \
    UAT_SPACESHIP_USER_TOKEN
from config.variables import opc_confg_by_env, user_config_by_env


class ControllersInitiator:
    def __init__(self):
        self.env = "preprod"
        self.base_url = f"https://{self.env}.tradias.link/api"
        self.ws_url = f"wss://ws.{self.env}.tradias.link"
        self.opc_url = f"{self.base_url}/tiers/outbound_price_channels"
        self.clients_url = f"{self.base_url}/clients"
        self.market_connector_url = f"{self.base_url}/market-connectors"
        self.user_token = UAT_SPACESHIP_USER_TOKEN if self.env == "uat" else PREPROD_SPACESHIP_USER_TOKEN
        self.client_token = UAT_SPACESHIP_CLIENT_TOKEN if self.env == "uat" else PREPROD_SPACESHIP_CLIENT_TOKEN
        self.opc_config = opc_confg_by_env[self.env]
        self.client_config = user_config_by_env[self.env]
        self.user_apis_headers = {
            "Authorization": f"Bearer {self.user_token}",
        }
        self.ws_headers = {
            "x-token-id": f"{self.client_token}",
        }

