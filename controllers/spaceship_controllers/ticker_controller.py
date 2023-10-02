import asyncio
import json
import websockets
from typing import List
from controllers.spaceship_controllers.controllers_initiator import ControllersInitiator


class TickerController(ControllersInitiator):
    def  __init__(self):
        super().__init__()

    async def tickers(self,instruments_array: List,message_flag: list[bool], channel_name: str = 'prices', disconnect_after: int = 5,print_messages = False):
        """
        This asynchronous generator function connects to the websocket,
        subscribes to the prices channel, and yields messages as they are received.
        It disconnects from the websocket after the specified duration.
        :param instruments_array: array containing required instruments for subscription in the following format: LEG1-LEG2
        :param channel_name: required channel name for subscription
        :param disconnect_after: integer that represents the disconnection time in seconds
        """
        # Array of instruments you want to subscribe to
        async with websockets.connect(uri=self.ws_url, extra_headers=self.ws_headers) as websocket:
            # For Loop to generate subscription messages for all the instruments in the array
            for instrument in instruments_array:
                await websocket.send(json.dumps({
                    "type": "subscribe",
                    "channelname": channel_name,
                    "instrument": instrument,
                    "heartbeat": False
                }))



            start_time = asyncio.get_event_loop().time()
            while message_flag[0]:
                message = await websocket.recv()
                if print_messages == True:
                    print(message)
                if message.decode("utf-8") == {"type":"subscribe","message":"Websocket Connected"}:
                    start_time = asyncio.get_event_loop().time()

                yield message

                # Check if it's time to disconnect
                current_time = asyncio.get_event_loop().time()
                if current_time - start_time >= disconnect_after:
                    break
        print("Succesful close of websocket")


if __name__ == '__main__':
    async def main():
        async for message in TickerController().tickers(instruments_array = ['BTC-EUR']):
            print(message)

    asyncio.run(main())
