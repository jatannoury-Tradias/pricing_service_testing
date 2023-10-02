import enum

import requests

from config.tokens import UAT_SPACESHIP_USER_TOKEN, PREPROD_SPACESHIP_USER_TOKEN


class PricesServiceTestingClientPreprodVariables(enum.Enum):
    info = {
          "id": "267e5cfc-4716-4666-bfd9-e53f1795bc61",
          "name": "prices_service_testing_client",
          "email": "jatannoury01@gmail.com",
          "address": "Beirut, Beirut, Lebanon",
          "phone": "70471877",
          "tier_name": "pricing_service_joseph_tier_test",
          "status": "Active",
          "created_at": "11.09.2023",
          "has_token": True,
          "trading_halt": False,
          "is_deleted": False
        }
class PricesServiceTestingClientUatVariables(enum.Enum):
        info = {
            "id": "893ab216-35a8-4423-9a86-42b383d486d1",
            "name": "Joseph",
            "email": "jatannoury01@gmail.com",
            "address": "Beirut, Beirut, Lebanon",
            "phone": "703084743",
            "type": "CLIENT",
            "has_token": False,
            "tier_name": "Tier_Pricing_Service_Testing",
            "tier_id": "56ebe30c-8d92-4c11-90a4-cc92cd62b9eb",
            "risk_id": "893ab216-35a8-4423-9a86-42b383d486d1",
            "status": "Active",
            "trading_halt": False,
            "created_at": "13.09.2023",
            "client_legacy_id": ""
        }
class PricingServiceJosephTierTestingPreprodVariables(enum.Enum):
    tier_id = "b9738601-3e14-42e8-9d7e-ef9757005c7e"
    new_tier = None
    instrument = "BTC-EUR"
    outbound_price_channels = requests.get(f"https://preprod.tradias.link/api/tiers/{tier_id}/{instrument}/outbound_price_channels",headers={
            "Authorization": f"Bearer {PREPROD_SPACESHIP_USER_TOKEN}"
        }).json()
class PricingServiceJosephTierTestingUatVariables(enum.Enum):

        tier_id = "fcbc6f8c-166b-4a89-8157-73b479ab23c1"
        instrument = "BTC-EUR"
        new_tier = None
        outbound_price_channels = requests.get(f"https://uat.tradias.link/api/tiers/{tier_id}/{instrument}/outbound_price_channels",headers={
            "Authorization": f"Bearer {UAT_SPACESHIP_USER_TOKEN}"
        }).json()

opc_confg_by_env = {
    "uat": PricingServiceJosephTierTestingUatVariables,
    "preprod": PricingServiceJosephTierTestingPreprodVariables,
}
user_config_by_env = {
    "uat": PricesServiceTestingClientUatVariables,
    "preprod": PricesServiceTestingClientPreprodVariables,

}