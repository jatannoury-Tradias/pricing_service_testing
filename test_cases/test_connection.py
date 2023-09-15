import asyncio
import json
import pytest
import datetime

from controllers.spaceship_controllers import SpaceshipController


def tz_to_timestamp(tz):
    return datetime.datetime.strptime(tz, "%Y-%m-%dT%H:%M:%S.%fZ")


class TestWSConnection:
    spaceship_controller = SpaceshipController()

    async def return_first_message(self):
        async for message in self.spaceship_controller.tickers(channel_name="prices", instruments_array=["BTC-EUR"]):
            return json.loads(message.decode('utf-8'))

    async def return_multiple_messages(self, number_of_messages, channel_name='prices', instruments_array=None):
        if instruments_array is None:
            instruments_array = ['BTC-EUR']
        messages = []
        async for message in self.spaceship_controller.tickers(channel_name=channel_name, instruments_array=instruments_array, print_messages=True):
            messages.append(json.loads(message.decode('utf-8')))
            if len(messages) == number_of_messages:
                break
        return messages

    async def place_order(self, order):
        messages = []
        async for message in self.spaceship_controller.orders(order, print_messages=True, disconnect_after=15):
            messages.append(json.loads(message.decode('utf-8')))
        return messages

    @pytest.mark.asyncio
    async def test_wrong_channel_name(self):
        messages = []
        async for message in self.spaceship_controller.tickers(channel_name="spices", instruments_array=["BTC-EUR"]):
            messages.append(json.loads(message.decode('utf-8')))
            if len(messages) == 2:
                break
        assert messages[0]["type"] == "subscribe"
        assert messages[0]["message"] == "Websocket Connected"
        assert messages[1]["type"] == "subscribe"
        assert messages[1]["message"] == "Invalid SubChannel"

    @pytest.mark.asyncio
    async def test_connect_multiple_times(self):
        tasks = []
        for i in range(5):
            tasks.append(asyncio.create_task(self.return_multiple_messages(6)))
        await asyncio.gather(*tasks)
        for i in range(len(tasks)):
            for j in range(i + 1, 5):
                assert tasks[i].result()[0]['type'] == tasks[j].result()[0]['type']
                assert tasks[i].result()[0]['message'] == tasks[j].result()[0]['message']
                assert tasks[i].result()[1]['type'] == tasks[j].result()[1]['type']
                assert tasks[i].result()[1]['message'] == tasks[j].result()[1]['message']
                for k in range(2, 6):
                    for l in range(len(tasks[i].result()[2]['levels']['buy'])):
                        assert tasks[i].result()[k]['levels']['buy'][l]['quantity'] == \
                               tasks[j].result()[k]['levels']['buy'][l]['quantity']
                    for l in range(len(tasks[i].result()[2]['levels']['sell'])):
                        assert tasks[i].result()[k]['levels']['sell'][l]['quantity'] == \
                               tasks[j].result()[k]['levels']['sell'][l]['quantity']

    @pytest.mark.asyncio
    async def test_multiple_instruments_single_connection(self):
        instruments_array = ["BTC-EUR", "ETH-EUR", "XRP-EUR", "LTC-EUR", "BCH-EUR"]
        collected_instruments = []
        messages = []
        async for message in self.spaceship_controller.tickers(channel_name="prices",
                                                               instruments_array=instruments_array,
                                                               disconnect_after=15):
            messages.append(json.loads(message.decode('utf-8')))
        for message in messages:
            try:
                if message['instrument'] in collected_instruments:
                    pass
                else:
                    collected_instruments.append(message['instrument'])
            except KeyError:
                pass
        assert instruments_array.sort() == collected_instruments.sort()

    @pytest.mark.asyncio
    async def test_connect_multiple_times_sync(self):
        for i in range(5):
            connection_response = await self.return_multiple_messages(2)
            assert connection_response[0]['type'] == "subscribe"
            assert connection_response[0]['message'] == "Websocket Connected"
            assert connection_response[1]['type'] == "subscribed"
            assert connection_response[1]['message'] == "success"

    @pytest.mark.asyncio
    async def test_no_prices_from_the_future(self):
        counter = 0
        async for message in self.spaceship_controller.tickers(channel_name="prices", instruments_array=["BTC-EUR"], disconnect_after=100):
            if counter == 50:
                break
            else:
                counter += 1
            try:
                timestamp = json.loads(message.decode('utf-8'))['timestamp']
                assert tz_to_timestamp(timestamp) < datetime.datetime.utcnow()
            except KeyError:
                pass

    @pytest.mark.asyncio
    async def test_ordered_prices(self):
        timestamps = []
        async for message in self.spaceship_controller.tickers(channel_name="prices", instruments_array=["BTC-EUR"], disconnect_after=100):
            if len(timestamps) == 50:
                break
            try:
                timestamp = json.loads(message.decode('utf-8'))['timestamp']
                timestamps.append(timestamp)

            except KeyError:
                pass
        for i in range(len(timestamps)-1):
            assert tz_to_timestamp(timestamps[i]) < tz_to_timestamp(timestamps[i+1])


    @pytest.mark.asyncio
    async def test_diff_subscription_messages(self):
        for i in range(5):
            right_messages = await self.return_multiple_messages(number_of_messages=2, channel_name="prices", instruments_array=["BTC-EUR"])
            assert right_messages[0]['type'] == "subscribe"
            assert right_messages[0]['message'] == "Websocket Connected"
            assert right_messages[1]['type'] == "subscribed"
            assert right_messages[1]['message'] == "success"
        wrong_messages = await self.return_multiple_messages(number_of_messages=2, channel_name="00000", instruments_array=["btc-EUR"])
        assert wrong_messages[0]['type'] == "subscribe"
        assert wrong_messages[0]['message'] == "Websocket Connected"
        assert wrong_messages[1]['type'] == "subscribe"
        assert wrong_messages[1]['message'] == "Invalid SubChannel"

    @pytest.mark.asyncio
    async def test_execution_quality(self):
        eur_amount_order = {
            "type": "CREATE_ORDER",
            "order": {
                "instrument": "BTC-EUR",
                "order_type": "MARKET",
                "side": "BUY",
                "amount": "1000",
                "currency": "EUR",
            }
        }

        tasks = []
        tasks.append(asyncio.create_task(self.return_multiple_messages(15)))
        tasks.append(asyncio.create_task(self.place_order(eur_amount_order)))
        await asyncio.gather(*tasks)








