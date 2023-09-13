import asyncio
import json
import pytest

from controllers.spaceship_controllers import SpaceshipController


class TestWSConnection:
    spaceship_controller = SpaceshipController()

    async def return_first_message(self):
        async for message in self.spaceship_controller.tickers(channel_name="prices", instruments_array=["BTC-EUR"]):
            return json.loads(message.decode('utf-8'))

    async def return_multiple_messages(self, number_of_messages):
        messages = []
        async for message in self.spaceship_controller.tickers(channel_name="prices", instruments_array=["BTC-EUR"]):
            messages.append(json.loads(message.decode('utf-8')))
            if len(messages) == number_of_messages:
                break
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





