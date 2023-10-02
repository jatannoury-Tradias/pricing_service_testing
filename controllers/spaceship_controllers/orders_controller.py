import asyncio
import json
import websockets
from typing import List
from controllers.spaceship_controllers.controllers_initiator import ControllersInitiator


class OrdersController(ControllersInitiator):
    def __init__(self):
        super().__init__()

    async def orders(self,order, channel_name: str = 'orders', disconnect_after: int = 5, print_messages=False):

        async with websockets.connect(uri=self.ws_url, extra_headers=self.ws_headers) as websocket:
            await websocket.send(json.dumps({
                "type": "subscribe",
                "channelname": channel_name
            }))
            await asyncio.sleep(1)
            await websocket.send(json.dumps(order))
            start_time = asyncio.get_event_loop().time()
            while True:
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

if __name__ == "__main__":
    async def main():
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
            print(message)
    asyncio.run(main())