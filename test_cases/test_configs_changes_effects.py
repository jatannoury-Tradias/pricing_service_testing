import asyncio
import time

import websockets

from config.variables import  opc_confg_by_env
import pytest
import json
import random

from controllers.spaceship_controllers import SpaceshipController, OrdersController, MarketConnectorController
from controllers.spaceship_controllers.controllers_initiator import ControllersInitiator


class TestConfigChangeEffects:
    spaceship_instance = SpaceshipController()
    opc_config = ControllersInitiator().opc_config
    def generate_random_quantity(self, value_to_avoid):
        while True:
            random_integer = random.randint(1, 10)  # Generate a random integer between 0 and 10
            if str(random_integer) != value_to_avoid and str(random_integer) < value_to_avoid:
                return random_integer

    async def place_order(self, order):
        messages = []
        async for message in self.spaceship_instance.orders(order, print_messages= False, disconnect_after=15):
            messages.append(json.loads(message.decode('utf-8')))
        return messages
    @pytest.mark.asyncio
    async def test_time_needed_for_new_tier_to_start_streaming(self):
        instruments = ['BTC-EUR']
        tier_creation_response = self.spaceship_instance.create_tier()
        end_time = None
        if "tier_id" not in tier_creation_response:
            assert False,  "Tier creation failed"
        # Used to assign client to a tier
        user_tier_update_response = self.spaceship_instance.modify_client_tier(tier_id=tier_creation_response['tier_id'])
        if user_tier_update_response.status_code != 200:
            assert False, "User tier update failed"
        start_time = time.time()
        receive_messages = [True]
        async for message in self.spaceship_instance.tickers(instruments, disconnect_after=30,message_flag=receive_messages, print_messages=False):
            end_time = time.time()
            receive_messages[0] = False

        if end_time == None:
            if user_tier_update_response.status_code != 200:
                assert False, "User tier update failed"
            else:
                assert False, f"Ticker not started or took more than {10} seconds to connect"
        print(f"Time needed for new tier to start streaming is {end_time - start_time} seconds")
        user_tier_update_response = self.spaceship_instance.modify_client_tier(
            tier_id=self.opc_config.tier_id.value)
        assert True

    @pytest.mark.asyncio  # Use the pytest-asyncio marker
    async def test_quantity_change_effect(self):
        instruments = ['BTC-EUR']
        assertion = False
        curr_level1_quantity = self.opc_config.outbound_price_channels.value['outbound_price_channels'][0]['quantity']
        opc_changed = False
        new_random_qty = self.generate_random_quantity(curr_level1_quantity)
        self.opc_config.outbound_price_channels.value['outbound_price_channels'][0][
            'quantity'] = new_random_qty
        message_flag = [True]
        try:
            async for message in self.spaceship_instance.tickers(instruments, disconnect_after=30,message_flag=message_flag,
                                                                 print_messages=False):
                decoded_message = message.decode('utf-8')
                message_data = json.loads(decoded_message)
                if "levels" not in message_data:
                    continue
                print(new_random_qty, message_data['levels']['buy'][0]['quantity'])
                if float(message_data['levels']['buy'][0]['quantity']) == \
                        float(self.opc_config.outbound_price_channels.value[
                                  'outbound_price_channels'][0]['quantity']):
                    assertion = True
                    message_flag[0] = False

                if "instrument" in message_data and opc_changed == False:
                    modify_quantity_response = self.spaceship_instance.modify_opc()
                    opc_changed = True
                    if modify_quantity_response.status_code == 200 or modify_quantity_response.status_code == 409:
                        print("Channels modified")
                    else:
                        raise Exception("Channels not modified")
        except websockets.ConnectionClosedOK:
            print("Connection Closed")

        self.opc_config.outbound_price_channels.value['outbound_price_channels'][0]['quantity'] = curr_level1_quantity
        modify_quantity_response = self.spaceship_instance.modify_opc()

        assert assertion
    def get_required_index(self,fb_hierarchies_first_opc):
        first_fallback_first_opc_name = fb_hierarchies_first_opc[0]['name']
        if first_fallback_first_opc_name == self.opc_config.outbound_price_channels.value['outbound_price_channels'][1][
            'price_fallback_hierarchies'][0]['name']:
            return 1
        if first_fallback_first_opc_name == self.opc_config.outbound_price_channels.value['outbound_price_channels'][2][
            'price_fallback_hierarchies'][0]['name']:
            return 2
    def change_fbs_and_return_required_index(self):
        fb_hierarchies_first_opc = self.opc_config.outbound_price_channels.value['outbound_price_channels'][0][
            'price_fallback_hierarchies']
        temp = fb_hierarchies_first_opc[0]
        fb_hierarchies_first_opc[0] = fb_hierarchies_first_opc[1]
        fb_hierarchies_first_opc[1] = temp
        fb_hierarchies_first_opc[0]['order'] = 0
        fb_hierarchies_first_opc[1]['order'] = 1
        return self.get_required_index(fb_hierarchies_first_opc)
    @pytest.mark.asyncio
    async def test_fallback_policy_change_effect(self):
        instruments = ['BTC-EUR']
        assertion = False
        opc_changed = False
        index_to_compare = self.change_fbs_and_return_required_index()
        start_time = time.time()
        change_fb_triggered = False
        message_flag = [True]
        async for message in self.spaceship_instance.tickers(instruments, disconnect_after=40, print_messages=False,message_flag=message_flag,):
            decoded_message = message.decode('utf-8')
            message_data = json.loads(decoded_message)
            if "levels" not in message_data:
                continue
            try:
                if change_fb_triggered and message_data['levels']['buy'][0]['price'] == \
                        message_data['levels']['buy'][index_to_compare]['price'] and len(
                        message_data['levels']['buy']) == 3:
                    end_time = time.time()
                    print(f"Time needed for changed fb hierarchy to start streaming is {end_time - start_time} seconds")
                    assertion = True
                    print(message)
                    message_flag[0] = False

            except:
                pass
            if "instrument" in message_data and opc_changed == False:
                modify_quantity_response = self.spaceship_instance.modify_opc()
                opc_changed = True
                if modify_quantity_response.status_code == 200:
                    print("Channels modified")
                    start_time = time.time()
                    change_fb_triggered = True
                else:
                    raise Exception("Channels not modified")

        assert assertion






    @pytest.mark.asyncio
    async def test_turn_off_unused_market_connectors(self):
        instruments = ['BTC-EUR']
        assertion = False
        TEMP = self.opc_config.outbound_price_channels.value['outbound_price_channels'][0]['price_fallback_hierarchies']
        self.opc_config.outbound_price_channels.value['outbound_price_channels'][0][
            'price_fallback_hierarchies'] = [self.opc_config.outbound_price_channels.value['outbound_price_channels'][0][
            'price_fallback_hierarchies'][0]]

        change_fb_triggered = False
        start_time = None
        message_flag = [True]
        async for message in self.spaceship_instance.tickers(instruments, disconnect_after=30, print_messages=False,message_flag=message_flag,):
            decoded_message = message.decode('utf-8')
            message_data = json.loads(decoded_message)
            if "levels" not in message_data:
                continue
            if change_fb_triggered:
                end_time = time.time()
                print(f"Time needed for changed fb hierarchy to start streaming is {end_time - start_time} seconds")
                assertion = True
                message_flag[0] = False

            if "instrument" in message_data:
                modify_quantity_response = self.spaceship_instance.modify_opc()
                if modify_quantity_response.status_code == 200:
                    #TODO: EMPTY THE QUEUE
                    print("Channels modified")
                    start_time = time.time()
                    change_fb_triggered = True
                else:
                    raise Exception("Channels not modified")
        self.opc_config.outbound_price_channels.value['outbound_price_channels'][0]['price_fallback_hierarchies'] = TEMP
        modify_quantity_response = self.spaceship_instance.modify_opc()

        assert assertion

    @pytest.mark.asyncio
    async def test_change_configs_and_place_order(self):
        instruments = ['BTC-EUR']
        assertion = False

        self.opc_config.outbound_price_channels.value['outbound_price_channels'][0][
            'price_fallback_hierarchies'].pop(0)
        market_connector_controller = MarketConnectorController()
        response = market_connector_controller.get_market_connectors_data()
        json_response = response.json()
        market_connector_data = list(filter(lambda element: element['name'] == self.opc_config.outbound_price_channels.value["outbound_price_channels"][0]['price_fallback_hierarchies'][0]['name'], json_response['items']))
        market_connector_health_checks_data = market_connector_controller.get_health_checks_market_connectors_data(
            market_connector_data[0]['id']).json()
        market_connector_health_checks_data_of_first_fb_hierarchy = list(filter(lambda element: element['instrument_code'] == "BTC-EUR", market_connector_health_checks_data['instruments']))
        market_connector_health_policy =  market_connector_health_checks_data_of_first_fb_hierarchy[0]['health_policy']
        message_flag = [True]
        async for message in self.spaceship_instance.tickers(instruments, disconnect_after=30, print_messages=False, message_flag=message_flag):
            decoded_message = message.decode('utf-8')
            message_data = json.loads(decoded_message)
            if "levels" not in message_data:
                continue
            if "instrument" in message_data:
                modify_quantity_response = self.spaceship_instance.modify_opc()
                if modify_quantity_response.status_code == 200:
                    message_flag[0] = False
                else:
                    raise Exception("Channels not modified")
        time.sleep(int(market_connector_health_policy['unhealthy_interval']))
        async for message in OrdersController().orders(order={
            "type": "CREATE_ORDER",
            "order": {
                "instrument": "BTC-EUR",
                "order_type": "MARKET",
                "side": "BUY",
                "amount": "1",
                "currency": "EUR",
            }
        }):
            decoded_message = message.decode('utf-8')
            json_message = json.loads(decoded_message)
            if "event" in json_message:
                if json_message['event'] == "orders":
                    assertion = True
                    break
        assert assertion
# import asyncio
# @pytest.fixture(autouse=True)
# def close_event_loop():
#     yield
#     asyncio.get_event_loop().close()