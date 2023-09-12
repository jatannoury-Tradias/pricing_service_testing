from config.tokens import PREPROD_SPACESHIP_USER_TOKEN, PREPROD_SPACESHIP_CLIENT_TOKEN


class ControllersInitiator:
    def __init__(self):
        env = "preprod"
        base_url = f"https://{env}.tradias.link/api"
        self.ws_url = f"wss://ws.{env}.tradias.link"
        self.opc_url = f"{base_url}/tiers/outbound_price_channels"
        self.clients_url = f"{base_url}/clients"
        self.user_token = PREPROD_SPACESHIP_USER_TOKEN
        self.client_token = PREPROD_SPACESHIP_CLIENT_TOKEN
        self.user_apis_headers = {
            "Authorization": f"Bearer {self.user_token}",
        }
        self.ws_headers = {
            "x-token-id": f"{self.client_token}",
        }