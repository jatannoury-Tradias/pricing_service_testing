import time

from config.variables import PricingServiceJosephTierTestingVariables
import pytest
import json
import random

from controllers.spaceship_controllers import SpaceshipController


class TestConfigChangeEffects:
    spaceship_instance = SpaceshipController()

    def generate_random_quantity(self, value_to_avoid):
        while True:
            random_integer = random.randint(1, 10)  # Generate a random integer between 0 and 10
            if random_integer != value_to_avoid:
                return random_integer

    # @pytest.mark.asyncio  # Use the pytest-asyncio marker
    # async def test_time_needed_for_new_tier_to_start_streaming(self):
    #     instruments = ['BTC-EUR']
    #     tier_creation_response = self.spaceship_instance.create_tier()
    #     end_time = None
    #     if "tier_id" not in tier_creation_response:
    #         assert False,  "Tier creation failed"
    #     user_tier_update_response = self.spaceship_instance.modify_client_tier(tier_id=tier_creation_response['tier_id'])
    #     if user_tier_update_response.status_code != 200:
    #         assert False, "User tier update failed"
    #     start_time = time.time()
    #     async for message in self.spaceship_instance.tickers(instruments, disconnect_after=10,print_messages=False):
    #         end_time = time.time()
    #         break
    #     if end_time == None:
    #         user_tier_update_response = self.spaceship_instance.modify_client_tier(
    #             tier_id=PricingServiceJosephTierTestingVariables.tier_id.value)
    #         if user_tier_update_response.status_code != 200:
    #             assert False, "User tier re-update failed"
    #         else:
    #             assert False, f"Ticker not started or took more than {10} seconds to connect"
    #     assert True, f"Time needed for new tier to start streaming is {end_time - start_time} seconds"
    #
    #     user_tier_update_response = self.spaceship_instance.modify_client_tier(
    #         tier_id=PricingServiceJosephTierTestingVariables.tier_id.value)

    @pytest.mark.asyncio  # Use the pytest-asyncio marker
    async def test_quantity_change_effect(self):
        instruments = ['BTC-EUR']
        assertion = False
        curr_level1_quantity = PricingServiceJosephTierTestingVariables.outbound_price_channels.value['outbound_price_channels'][0]['quantity']

        PricingServiceJosephTierTestingVariables.outbound_price_channels.value['outbound_price_channels'][0][
            'quantity'] = self.generate_random_quantity(curr_level1_quantity)

        async for message in self.spaceship_instance.tickers(instruments, disconnect_after=10,print_messages=True):
            decoded_message = message.decode('utf-8')
            try:
                message_data = json.loads(decoded_message)
                if int(message_data['levels']['buy'][0]['quantity']) == \
                        int(PricingServiceJosephTierTestingVariables.outbound_price_channels.value[
                            'outbound_price_channels'][0]['quantity']):
                    assertion = True
                if "instrument" in message_data:
                    curr_level1_quantity = message_data['levels']['buy'][0]['quantity']
                    modify_quantity_response = self.spaceship_instance.modify_opc()
                    if modify_quantity_response.json()['status'] == 200:
                        print("Channels modified")
                    else:
                        raise Exception("Channels not modified")


            except json.JSONDecodeError:
                # Handle JSON decoding errors here
                print("Error decoding JSON:", decoded_message)

            except KeyError:
                # Handle missing 'instrument' key here
                print("Missing 'instrument' key in message:", decoded_message)

        assert assertion
    #
