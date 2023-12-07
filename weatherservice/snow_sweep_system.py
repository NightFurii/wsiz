import asyncio
from asyncio import run, sleep
from loguru import logger
import random
from streets import create_city
from streets import Street, SnowSweeper


class WeatherService:
    """
    Random weather conditions over the city
    """

    def __init__(self):
        self.name = 'Polyanna'
        self.current_snow_fall_rate = 0

    async def initialize(self):
        logger.info('Service weather initializing')
        while True:
            await sleep(2)  # Zmiana na 2 sekundy
            new_rate = random.uniform(0, 2)
            logger.info(f"Updated snow fall rate: {new_rate}")
            self.current_snow_fall_rate = new_rate

    async def get_current_snow_fall_rate(self):
        return self.current_snow_fall_rate


class StreetMonitoringService:
    """
    Monitors city CCTV cameras periodically, and updates snow cover for each of the streets of self.city
    """

    def __init__(self, city: dict[str, Street], weather: WeatherService):
        self.city = city
        self.weather = weather
        self.current_snow_fall_rate = 0

    async def initialize(self):
        logger.info('Street monitoring initializing')
        while True:
            await sleep(0.5)
            await self.update_street_snow_cover()

    async def update_street_snow_cover(self):
        for street_name, street in self.city.items():
            # X to aktualny current_snow_fall_rate z serwisu pogodowego
            X = await self.weather.get_current_snow_fall_rate()

            # Y to mała liczba losowa z przedziału [0, 1]
            Y = random.uniform(0, 1)

            # Aktualizacja snow cover dla ulicy
            street.snow_cover_cm += (X + Y)

            logger.info(f"Updated snow cover for {street_name}: {street.snow_cover_cm}")

        # Aktualizacja self.current_snow_fall_rate
        self.current_snow_fall_rate = X


class SnowSweeperDispatcher:

    def __init__(self, city: dict[str, Street], sweepers: list[SnowSweeper]):
        self.sweepers = sweepers
        self.city = city

    async def initialize(self):
        logger.info('Dispatcher initializing')
        while True:
            await sleep(0.5)
            await self.check_city_dispatch_sweeper()

    async def check_city_dispatch_sweeper(self):
        for street_name, street in self.city.items():
            logger.info(f'Checking {street_name} with snow cover: {street.snow_cover_cm}')
            if street.snow_cover_cm > 4:  # Zmienić na odpowiednią wartość progową
               logger.info(f'Snow cover for {street_name} is above the threshold.')
               available_sweeper = self.find_available_sweeper()
               if available_sweeper:
                   logger.info(f'Dispatching sweeper for {street_name}.')
                   await self.dispatch_to_sweep_street(street, available_sweeper)
            else:
                logger.info('No available sweeper.')



async def dispatch_to_sweep_street(self, street: Street, sweeper: SnowSweeper):
    cover = street.snow_cover_cm
    street.snow_cover_cm = 0
    logger.info(f'sweeper {sweeper.id} sweeping {street.name}')
    sweeper.location = street.name

    await sleep(street.length * cover)

    logger.info(f'sweeper {sweeper.id} sweeping {street.name} complete')
    sweeper.location = None

    def find_available_sweeper(self):
        for sweeper in self.sweepers:
            if sweeper.location is None:
                return sweeper
        return None


async def main():
    # Tworzymy instancję WeatherService
    weather_service = WeatherService()

    # Tworzymy instancję StreetMonitoringService, używając create_city() do utworzenia miasta
    street_monitoring_service = StreetMonitoringService(create_city(), weather_service)

    # Uruchamiamy obie usługi w osobnych zadaniach (tasks)
    tasks = [asyncio.create_task(weather_service.initialize()), asyncio.create_task(street_monitoring_service.initialize())]

    # Czekamy pewien czas (możesz dostosować czas oczekiwania)
    await sleep(10)

    # Zatrzymujemy zadania
    for task in tasks:
        task.cancel()

    # Wypisujemy końcową wartość current_snow_fall_rate
    final_rate = await weather_service.get_current_snow_fall_rate()
    logger.info(f"Final snow fall rate: {final_rate}")

if __name__ == '__main__':
    run(main())
