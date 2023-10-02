import asyncio
import json
import pytest
import datetime
from datetime import timezone
from controllers.spaceship_controllers import SpaceshipController

INSTRUMENT = "BTC-EUR"
WRONG_INSTRUMENT = "BTC-WRONG"
ENCODING = 'utf-8'
PRICES_CHANNEL = "prices"
ORDERS_CHANNEL = "orders"
WRONG_CHANNEL_NAME = "spices"


def level_selector(array, quantity):
    array = sorted(array, key=lambda x: float(x['quantity']))
    print(array)
    for index, element in enumerate(array):
        if float(element['quantity']) < float(quantity):
            return array[index-1]


def tz_to_timestamp(tz):
    try:
        return datetime.datetime.strptime(tz, "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError as e:
        print(tz)


class TestWSConnection:
    spaceship_controller = SpaceshipController()

    async def return_first_message(self):
        async for message in self.spaceship_controller.tickers(channel_name=PRICES_CHANNEL,
                                                               instruments_array=[INSTRUMENT]):
            return json.loads(message.decode(ENCODING))

    async def return_multiple_messages(self, number_of_messages, channel_name=PRICES_CHANNEL, instruments_array=None):
        if instruments_array is None:
            instruments_array = [INSTRUMENT]
        messages = []
        async for message in self.spaceship_controller.tickers(channel_name=channel_name,
                                                               instruments_array=instruments_array,
                                                               print_messages=False, disconnect_after=20):
            messages.append(json.loads(message.decode(ENCODING)))
            if len(messages) == number_of_messages:
                break
        return messages

    async def place_order(self, order):
        messages = []
        await asyncio.sleep(5)
        async for message in self.spaceship_controller.orders(order, print_messages=False, disconnect_after=15):
            messages.append(json.loads(message.decode(ENCODING)))
        return messages

    @pytest.mark.asyncio
    async def test_wrong_channel_name(self):
        messages = []
        async for message in self.spaceship_controller.tickers(channel_name=WRONG_CHANNEL_NAME,
                                                               instruments_array=[INSTRUMENT]):
            messages.append(json.loads(message.decode(ENCODING)))
            if len(messages) == 2:
                break
        assert messages[0]["type"] == "subscribe"
        assert messages[0]["message"] == "Websocket Connected"
        assert messages[1]["type"] == "subscribe"
        assert messages[1]["message"] == "Invalid SubChannel"

    @pytest.mark.asyncio
    async def test_connect_multiple_times(self):
        NUMBER_OF_MESSAGES = 20
        tasks = []
        for task in range(5):
            tasks.append(asyncio.create_task(self.return_multiple_messages(NUMBER_OF_MESSAGES)))
        await asyncio.gather(*tasks)
        buy_prices = {}
        for task in range(len(tasks)):
            for j in range(task + 1, 5):
                assert tasks[task].result()[0]['type'] == tasks[j].result()[0]['type']
                assert tasks[task].result()[0]['message'] == tasks[j].result()[0]['message']
                assert tasks[task].result()[1]['type'] == tasks[j].result()[1]['type']
                assert tasks[task].result()[1]['message'] == tasks[j].result()[1]['message']
            for price_update in range(2, NUMBER_OF_MESSAGES):
                timestamp = tasks[task].result()[price_update]['timestamp']
                for level in range(len(tasks[task].result()[price_update]['levels']['buy'])):
                    price = tasks[task].result()[price_update]['levels']['buy'][level]['price']
                    quantity = tasks[task].result()[price_update]['levels']['buy'][level]['quantity']
                    if quantity not in buy_prices:
                        buy_prices[quantity] = {}
                    buy_prices[quantity][timestamp] = price
        for quantity in buy_prices.keys():
            assert len(buy_prices[quantity]) == NUMBER_OF_MESSAGES - 2


    @pytest.mark.asyncio
    async def test_multiple_instruments_single_connection(self):
        instruments_array = ["BTC-EUR", "ETH-EUR", "XRP-EUR", "LTC-EUR", "BCH-EUR"]
        collected_instruments = []
        messages = []
        async for message in self.spaceship_controller.tickers(channel_name=PRICES_CHANNEL,
                                                               instruments_array=instruments_array,
                                                               disconnect_after=15):
            messages.append(json.loads(message.decode(ENCODING)))
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
        async for message in self.spaceship_controller.tickers(channel_name=PRICES_CHANNEL,
                                                               instruments_array=[INSTRUMENT], disconnect_after=100):
            if counter == 50:
                break
            else:
                counter += 1
            try:
                timestamp = json.loads(message.decode(ENCODING))['timestamp']
                time_diff = datetime.datetime.utcnow().replace(tzinfo=timezone.utc) - tz_to_timestamp(timestamp)
                assert float(time_diff.total_seconds()) > 0
            except KeyError:
                pass

    @pytest.mark.asyncio
    async def test_ordered_prices(self):
        timestamps = []
        async for message in self.spaceship_controller.tickers(channel_name=PRICES_CHANNEL,
                                                               instruments_array=[INSTRUMENT], disconnect_after=100):
            if len(timestamps) == 50:
                break
            try:
                timestamp = json.loads(message.decode(ENCODING))['timestamp']
                timestamps.append(timestamp)

            except KeyError:
                pass
        for i in range(len(timestamps) - 1):
            assert tz_to_timestamp(timestamps[i]) < tz_to_timestamp(timestamps[i + 1])

    @pytest.mark.asyncio
    async def test_diff_subscription_messages(self):
        for i in range(5):
            right_messages = await self.return_multiple_messages(number_of_messages=2, channel_name=PRICES_CHANNEL,
                                                                 instruments_array=[INSTRUMENT])
            assert right_messages[0]['type'] == "subscribe"
            assert right_messages[0]['message'] == "Websocket Connected"
            assert right_messages[1]['type'] == "subscribed"
            assert right_messages[1]['message'] == "success"
        wrong_messages = await self.return_multiple_messages(number_of_messages=2, channel_name=WRONG_CHANNEL_NAME,
                                                             instruments_array=[WRONG_INSTRUMENT])
        assert wrong_messages[0]['type'] == "subscribe"
        assert wrong_messages[0]['message'] == "Websocket Connected"
        assert wrong_messages[1]['type'] == "subscribe"
        assert wrong_messages[1]['message'] == "Invalid SubChannel"

    @pytest.mark.asyncio
    async def test_execution_quality(self):
        eur_amount_order = {
            "type": "CREATE_ORDER",
            "order": {
                "instrument": INSTRUMENT,
                "order_type": "MARKET",
                "side": "SELL",
                "amount": "1000",
                "currency": "EUR",
            }
        }
        tasks = [
            asyncio.create_task(self.return_multiple_messages(15)),
            asyncio.create_task(self.place_order(eur_amount_order))
        ]
        await asyncio.gather(*tasks)
        prices = tasks[0].result()
        execution_messages = tasks[1].result()
        prices_timestamps = []
        prices_list = []
        sorted_prices_list = []
        execution_data = {}
        for message in execution_messages:
            if 'confirmed_price' in message:
                execution_data['execution_price'] = message['confirmed_price']
                execution_data['execution_time'] = tz_to_timestamp(message['executed_at'])
                execution_data['side'] = message['side'].lower()
        for message in prices:

            if 'levels' in message:
                prices_timestamps.append(message['timestamp'])
                if execution_data['execution_time']:
                    if tz_to_timestamp(message['timestamp']) < execution_data['execution_time']:
                        prices_list.append(message)
                        sorted_prices_list = sorted(prices_list, key=lambda k: k['timestamp'])
        closest_price = None
        for price in sorted_prices_list:
            if tz_to_timestamp(price['timestamp']) >= execution_data['execution_time']:
                break
            closest_price = price['levels']['sell'][0]['price']
        assert execution_data['execution_price'] == closest_price
