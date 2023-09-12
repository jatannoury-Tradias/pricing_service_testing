import enum
class PricesServiceTestingClientVariables(enum.Enum):
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
class PricingServiceJosephTierTestingVariables(enum.Enum):
    outbound_price_channels = {
        "outbound_price_channels": [
            {
                "quantity": "1",
                "price_precision": 4,
                "price_algo": {
                    "method": "Bid/Ask",
                    "spread": "0.0005",
                    "spread_basis": "mid",
                    "min_spread": "0.0001",
                    "max_spread": "0.0012",
                    "diff_bid": "0",
                    "diff_ask": "0",
                    "quote_buy": True,
                    "quote_sell": True,
                    "mid_point_check": "0",
                    "quote_quantity": "None"
                },
                "id": "a4fd0805-790d-4c7d-8022-2f773cbdea24",
                "tier_id": "71c0b4da-8f49-4ee6-8392-1c0bbfd45e76",
                "instrument_code": "BTC-EUR",
                "price_fallback_hierarchies": [
                    {
                        "name": "Talos",
                        "fallback_type": "FALLBACK_TYPE_MARKET_CONNECTOR",
                        "fallback_id": "8f8ab613-0fdf-4cdb-9e24-b3a235a32e32",
                        "enabled": True,
                        "order": 0
                    },
                    {
                        "order": 1,
                        "name": "Coinbase",
                        "fallback_type": "FALLBACK_TYPE_MARKET_CONNECTOR",
                        "fallback_id": "7993da68-fc8a-42fe-bb39-14366484213a",
                        "enabled": True
                    },
                    {
                        "order": 2,
                        "name": "Bitstamp",
                        "fallback_type": "FALLBACK_TYPE_MARKET_CONNECTOR",
                        "fallback_id": "b8684ba7-eaa0-4958-a9a0-2b120b19a853",
                        "enabled": True
                    },
                    {
                        "order": 3,
                        "name": "Kraken",
                        "fallback_type": "FALLBACK_TYPE_MARKET_CONNECTOR",
                        "fallback_id": "60b0440f-8a1e-48f9-be15-34e0491994f2",
                        "enabled": True
                    },
                    {
                        "order": 4,
                        "name": "Bitfinex",
                        "fallback_type": "FALLBACK_TYPE_MARKET_CONNECTOR",
                        "fallback_id": "6f94e9c6-a93f-4a9b-bd36-e4abb17885ff",
                        "enabled": True
                    },
                    {
                        "order": 5,
                        "name": "Binance",
                        "fallback_type": "FALLBACK_TYPE_MARKET_CONNECTOR",
                        "fallback_id": "89457bc2-629e-4cd7-ac18-6ad7ca3a7353",
                        "enabled": True
                    },
                    {
                        "order": 6,
                        "name": "B2C2",
                        "fallback_type": "FALLBACK_TYPE_MARKET_CONNECTOR",
                        "fallback_id": "270f0a77-0362-4890-aaeb-ff4641737f1c",
                        "enabled": True
                    }
                ],
                "price_function": "FLAT"
            }
        ],
        "slow_quoting_interval": "0.0",
        "instrument_code": "BTC-EUR"
    }
    tier_id = outbound_price_channels["outbound_price_channels"][0]["tier_id"]
    new_tier = None

# import asyncio
# import uuid
#
# import websockets
# import json
#
# # NYALA_TOKEN = "eyJhbGciOiJSUzI1NiJ9.eyJuYW1lIjoiSm9oYW5uZXMgU2NobWl0dCIsImVtYWlsIjoiai5zY2htaXR0QG55YWxhLmRlIiwic3ViIjoiSm9oYW5uZXMgU2NobWl0dCIsImp0aSI6ImU3ZDQ2NDM4LTYwZmEtMTFlZC05ZWM5LWVkYmVkNmRmNWQ1MCIsImlhdCI6MTY2ODA4NjYyNiwiZXhwIjoxNjk5NjIyNjI2fQ.fIT_LIOB83oZyFfUszFMW-phtTQj0QAkpHZpfg3DWyjVw198Kyq-CuabvznuDOttIoSVBFueqdZEHo3cI3DxQjqR5dJPSMWnou7WCKc3JGbrX-469pAt8NW8VO3Q_Yt84ncMs5gIuoi35jau3rrPwckoE_CLo2YFHRo4JCq9m5qq01U9-qPkctvqJA0h50mP2AoGGgQsXchIFS39BYNg8ABMH2B2EjFQeka4vGvssD250xqq-jvibuz834rkT7AZFBsi-bsjVfLJkSKcZ_1IOCih6OF9PyO0fuMw54ediWODCwiVlTh6mTZhus6CmGFtxAu_24rkIp9x0_vGXvWyuw"
# # MY_TOKEN = "eyJhbGciOiJSUzI1NiJ9.eyJuYW1lIjoiT0RJTl9NT05JVE9SIiwiZW1haWwiOiJqLmhhbWFubkBiYW5raGF1cy1zY2hlaWNoLmRlIiwic3ViIjoiT0RJTl9NT05JVE9SIiwianRpIjoiNWRhYTM0Y2QtYjM2MC0xMWViLWJmMzAtZGI5ZjgyN2Y1NDk3IiwiaWF0IjoxNjgwMTc4ODk2LCJleHAiOjE3MTE3MTQ4OTZ9.n6ZZ31Btb27Ik-3v4XwA-PcXwvYDGxPaZZ3fNJEYBVyIq9Akfgh5Eab9wDxVfwSJ3r7fhmPHzq_w7CC6rmixn4J4coaSu3MaXSeZ6MmdYT-yBDKdRl58uYbtCPTh5Q3OrFkS_KxVGvP_vJ6PrTLBrW1O_CJpHkn54WrFJ4htAJJ8peqBApAcUtbxFbqCyEoOay630bZchuqPsR72sIet2r4OgucU8kZ0D-He-mfyJLZovuejk5kNsyQL1baPNC9Dg6dJZo2-WbXSjsW4mtEAs0x23RjkwrWleurmpYeuOJSOZXbK0ASZHaF2aJNQjMD5Mub4iKRbXkkz7LK1XCn_JA"
# MY_TOKEN = "eyJhbGciOiJSUzI1NiJ9.eyJuYW1lIjoiQWxhaW4gRGVzdmlnbmUiLCJlbWFpbCI6InVua25vd25AdW5rbm93bi5kZSIsInN1YiI6IkFsYWluIERlc3ZpZ25lIiwianRpIjoiZjM4MDdhZjctOThjYi0xMWVkLWIyZjgtYTdjYmNkMTM3NzZlIiwiaWF0IjoxNjc0MjIzNzI0LCJleHAiOjE3MDU3NTk3MjR9.oNSAr9pLc_p_W8d53rbXZLe7W61oFeE0DBzNPktwJlv1KLKYpKww8cA2jny0PVvKp67wbzoCQ9hF4qLMAOiDx4rdx0XefRdQRZvMLX5_KJxQSfunA7xnFZKIrgW7MF3IndQuK6BIB14j8CBZwrXQVR4DzZHEcMqk9SSNe7XbgyYB4OoEq1jfp50CKpqUqgNfcgvGdxkLXfBGT3WaQ-HKZGSGOFIpVsTXto20b6Euxz7kPAhbE3K20l43ZH1DLJyA6Lsv_l0EB2nGtJxJqo-e_N0Oynk7ABz3PrfClJMW-U_thZCTmuv6ohP8hF0AIMGRCBsUHoCWe3ryCAVtJs9N8Q"
# ENVIRONMENT = "otcapp-uat"
# PROTOCOL = "wss"
#
# URI = f"{PROTOCOL}://{ENVIRONMENT}.tradias.de/otc/ws"
#
# websocket_headers = {
#     "x-token-id": MY_TOKEN
# }
#
# order_channel_subscription = {
#     "type": "subscribe",
#     "channelname": "orders"
# }
#
# # my_order = {
# #   "type": "CREATE_ORDER",
# #   "order": {
# #     "instrument": "SOLEUR",
# #     "order_type": "MARKET",
# #     "side": "BUY",
# #     "amount": "48.53",
# #     "currency": "EUR",
# #     "client_order_id": "7c656d5a-b3d6-47ae-a26a-a0a000f1bceb",
# #     "client_order_id_2": "1dc83613-9400-473d-a657-ff6f624bac3a"
# #   }
# # }
#
# # my_eur_amount_order = {
# #     "type": "CREATE_ORDER",
# #     "order": {
# #         "instrument": "BTCEUR",
# #         "order_type": "MARKET",
# #         "side": "BUY",
# #         "amount": 30000,
# #         "currency": "EUR",
# #         "client_order_id": "Satoshi Nakamoto",
# #         "client_order_id_1": "23270",
# #         "client_order_id_2": "Hello World!"
# #     }
# # }
#
# my_order = {
#     "type": "CREATE_ORDER",
#     "order": {
#         "instrument": "SOLEUR",
#         "order_type": "MARKET",
#         "side": "BUY",
#         "amount": 1.5,
#         "unique_client_order_id": "7c656d5a-b3d6-17ae-a26a-a0a000fcvvaf",
#         "client_order_id_2": "Hello World!"
#     }
# }
#
# my_eur_amount_order = {
#     "type": "CREATE_ORDER",
#     "order": {
#         "instrument": "SOLEUR",
#         "order_type": "MARKET",
#         "side": "BUY",
#         "amount": "48.53",
#         "currency": "EUR",
#         "client_order_id": "7c656d5a-b3d6-47ae-a26a-a0a100f1bcac",
#     }
# }
# async def make_orders(orders_to_be_sent: list[dict]) -> None:
#     async with websockets.connect(uri=URI, extra_headers=websocket_headers) as websocket:
#         await websocket.send(json.dumps(order_channel_subscription))
#         for order in orders_to_be_sent:
#             asyncio.create_task(websocket.send(json.dumps(order)))
#         while True:
#             print(await websocket.recv())
#
# asyncio.run(make_orders([my_order, my_eur_amount_order]))