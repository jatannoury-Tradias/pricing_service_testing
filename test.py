import asyncio
import json

import websockets

from config.tokens import UAT_SPACESHIP_CLIENT_TOKEN, PREPROD_SPACESHIP_CLIENT_TOKEN

env = "preprod"
base_url = f"https://{env}.tradias.link/api"
ws_url = f"wss://ws.{env}.tradias.link"
client_token = PREPROD_SPACESHIP_CLIENT_TOKEN
ws_headers = {
    "x-token-id": f"{client_token}",
}
async def tickers():
    async with websockets.connect(uri=ws_url, extra_headers=ws_headers) as websocket:
        # For Loop to generate subscription messages for all the instruments in the array
        for instrument in ['BTC-EUR']:
            await websocket.send(json.dumps({
                "type": "subscribe",
                "channelname": 'prices',
                "instrument": instrument,
                "heartbeat": False
            }))

        start_time = asyncio.get_event_loop().time()
        while True:
            message = await websocket.recv()
            print(message)

asyncio.run(tickers())
