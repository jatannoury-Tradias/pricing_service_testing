from controllers.spaceship_controllers.client_controller import ClientsController
from controllers.spaceship_controllers.market_connector_controllers import MarketConnectorController
from controllers.spaceship_controllers.opcs_controller import OpcsController
from controllers.spaceship_controllers.orders_controller import OrdersController
from controllers.spaceship_controllers.ticker_controller import TickerController
from controllers.spaceship_controllers.tiers_controller import TiersController


class SpaceshipController(
                          OpcsController,
                          TickerController,
                          ClientsController,
                          TiersController,
                          OrdersController,
                          MarketConnectorController
                          ):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    import asyncio
    async def main():
        async for message in  SpaceshipController().tickers(["BTC-EUR"]):
            print(message)

    asyncio.run(main())