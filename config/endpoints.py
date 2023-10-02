from typing import Tuple

import requests

from config.OPC_config import OpcConfig
from config.tokens import PREPROD_SPACESHIP_USER_TOKEN, UAT_SPACESHIP_USER_TOKEN
from models.OutboudPriceChannel import OutboundPriceChannel
from tools.convert_to_dict import convert_to_dict


class RequestHandler:
    def __init__(self,env):
        self.base_url = f"https://{env}.tradias.link/api"
        self.tier_endpoint = "/tiers"
        self.create_opc_endpoint = "/tiers/outbound_price_channels"
        self.price_fallbacks_endpoint = "/channels/price-fallbacks"
        self.auth_endpoint = "/authenticate"
        self.token = None

    def authenticate_user(self,auth_with_email_and_pass = False):
        if auth_with_email_and_pass == True:
            payload = {
                "email": str(input("Kindly input your spaceship email:")).strip(),
                "secret": str(input("Kindly input your spaceship password:")).strip()
            }
            url = f"{self.base_url}{self.auth_endpoint}"
            response = requests.post(url=url, json=payload)
            if response.status_code == 200:
                self.token = response.json()['auth_token']
            else:
                print("Wrong credentials!")
                self.authenticate_user()
        else:
            self.token = PREPROD_SPACESHIP_USER_TOKEN
    def construct_headers(self):
        if self.token == None:
            self.authenticate_user()
        return {
            "Authorization":f"Bearer {self.token}"
        }
    def create_tier(self,tier_info:dict) -> dict:
        url = f"{self.base_url}{self.tier_endpoint}"
        return requests.post(url=url,json=tier_info,headers=self.construct_headers()).json()

    def get_tiers_by_type(self,tier_type:str = None) -> dict:
        url = f"{self.base_url}{self.tier_endpoint}{f'?tier_type={tier_type}' if tier_type!=None else ''}"
        return requests.get(url=url,headers=self.construct_headers()).json()

    def get_instrument_price_fallback(self,instrument:str) -> dict:
        url = f"{self.base_url}{self.price_fallbacks_endpoint}?instruments={instrument}"
        return requests.get(url,headers=self.construct_headers()).json()
    def create_opc(self,opcs:list[OutboundPriceChannel],instrument_code)-> Tuple[int,dict]:
        url = f"{self.base_url}{self.create_opc_endpoint}"
        payload = {
            "outbound_price_channels":convert_to_dict(opcs),
            "instrument_code":instrument_code,
            "slow_quoting_interval":OpcConfig.slow_quoting_interval
        }
        response = requests.put(url,headers=self.construct_headers(),json=payload)
        return response.status_code,response.json()



