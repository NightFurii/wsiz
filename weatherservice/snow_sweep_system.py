import asyncio
from asyncio import sleep
from loguru import logger
import random
import uuid
from streets import create_city, Street, SnowSweeper


class WeatherService:
    def __init__(self):
        self.name = 'Polyanna'
        self.current_snow_fall_rate = 0

    async def initialize(self):
        logger.info('Service weather initializing')
        while True:
            await sleep(2)
            new_rate = random.uniform(0, 2)
            logger.info(f"Updated snow fall rate: {new_rate}")
            self.current_snow_fall_rate = new_rate

    async def get_current_snow_fall_rate(self):
        return self.current_snow_fall_rate


class StreetMonitoringService:
    def __init__(self, city: dict[str, Street], weather: WeatherService):
        self.city = city
        self.weather = weather
        self.current_snow_fall_rate = 1

    async def initialize(self):
        logger.info('Street monitoring initializing')
        while True:
            await sleep(0.5)
            await self.update_street_snow_cover()

    async def update_street_snow_cover(self):
        for street_name, street in self.city.items():
            X = await self.weather.get_current_snow_fall_rate()
            Y = random.uniform(0, 0.1)
            street.snow_cover_cm += (X + Y)
            logger.info(f"Updated snow cover for {street_name}: {street.snow_cover_cm}")

        self.current_snow_fall_rate = X


class SnowSweeperDispatcher:
    def __init__(self, city: dict[str, Street], sweepers: list[SnowSweeper]):
        self.sweepers = sweepers
        self.city = city

    async def initialize(self):
        logger.info('Dispatcher initializing')
        while True:
            await sleep(0.1) 
            await self.check_city_dispatch_sweeper()

    async def check_city_dispatch_sweeper(self):
        for street_name, street in self.city.items():
            logger.info(f'Checking {street_name} with snow cover: {street.snow_cover_cm}')
            if street.snow_cover_cm > 0.1:
                logger.info(f'Snow cover for {street_name} is above the threshold.')
                available_sweepers = self.find_available_sweepers() # wyszukanie dostępnych odśnieżarek
                if available_sweepers:
                    for available_sweeper in available_sweepers:
                        logger.info(f'Dispatching sweeper {available_sweeper.name} for {street_name}.')
                        await self.dispatch_to_sweep_street(street, available_sweeper)
                else:
                    logger.info('No available sweeper.')
            else:
                logger.info('No need for sweeping.')

    async def dispatch_to_sweep_street(self, street: Street, sweeper: SnowSweeper):
        cover = street.snow_cover_cm
        street.snow_cover_cm = 0.3
        logger.info(f'Sweeper {sweeper.name} sweeping {street.name}')
        sweeper.location = street.name
        await sleep(street.length * cover)
        logger.info(f'Sweeper {sweeper.id} completed sweeping {street.name}')
        sweeper.location = None
        sweeper.available = True

    def find_available_sweepers(self):
        available_sweepers = [sweeper for sweeper in self.sweepers if sweeper.location is None and sweeper.available]

        if not available_sweepers:
            return None

        return available_sweepers


async def main():
    city = create_city()

    weather_service = WeatherService()
    street_monitoring_service = StreetMonitoringService(city, weather_service)

    # Instancja SnowSweeper
    ssweeper1 = SnowSweeper(uuid.uuid4(), 'Snowdestroy1', None)
    ssweeper2 = SnowSweeper(uuid.uuid4(), 'Furia2', None)
    ssweeper3 = SnowSweeper(uuid.uuid4(), 'Bravo3', None)
    ssweeper4 = SnowSweeper(uuid.uuid4(), 'Demon4', None)

    # Instancja SnowSweeperDispatcher
    sweeper_dispatcher = SnowSweeperDispatcher(city, [ssweeper1, ssweeper2, ssweeper3, ssweeper4])

    tasks = [
        asyncio.create_task(weather_service.initialize()),
        asyncio.create_task(street_monitoring_service.initialize()),
        asyncio.create_task(sweeper_dispatcher.initialize())
    ]

    await sleep(30)

    for task in tasks:
        task.cancel()

    final_rate = await weather_service.get_current_snow_fall_rate()
    logger.info(f"Final snow fall rate: {final_rate}")


if __name__ == '__main__':
    asyncio.run(main())



async def main():
    city = create_city()

    weather_service = WeatherService()
    street_monitoring_service = StreetMonitoringService(city, weather_service)

    # Instancja SnowSweeper
    ssweeper1 = SnowSweeper(uuid.uuid4(), 'Snowdestroy1', None)
    ssweeper2 = SnowSweeper(uuid.uuid4(), 'Furia2', None)
    ssweeper3 = SnowSweeper(uuid.uuid4(), 'Bravo3', None)
    ssweeper4 = SnowSweeper(uuid.uuid4(), 'Demon4', None)

    # Instancja SnowSweeperDispatcher
    sweeper_dispatcher = SnowSweeperDispatcher(city, [ssweeper1, ssweeper2, ssweeper3])

    tasks = [
        asyncio.create_task(weather_service.initialize()),
        asyncio.create_task(street_monitoring_service.initialize()),
        asyncio.create_task(sweeper_dispatcher.initialize())
    ]

    await sleep(20)

    for task in tasks:
        task.cancel()

    final_rate = await weather_service.get_current_snow_fall_rate()
    logger.info(f"Final snow fall rate: {final_rate}")


if __name__ == '__main__':
    asyncio.run(main())
