from dataclasses import dataclass
import uuid

@dataclass
class Street:
    name: str
    length: float
    snow_cover_cm: float

@dataclass
class SnowSweeper:
    id: uuid.UUID
    name: str
    location: str | None
    available: bool = True


def create_city() -> dict[str, Street]:
    s1 = Street('Cieszyńska', 2.41, snow_cover_cm=0.1)
    s2 = Street('Krakowska', 3.12, snow_cover_cm=0.2)
    s3 = Street('Akademicka', 2.12, snow_cover_cm=0.1)
    s4 = Street('Blekitna', 6.42, snow_cover_cm=0.3)
    s5 = Street('Legionow', 3.44, snow_cover_cm=0.5)

    ss = [s1, s2, s3, s4, s5]

    city = dict()
    for street in ss:
        city[street.name] = street
    return city


if __name__ == '__main__':
    city = create_city()
    print(city)

    ssweeper1 = SnowSweeper(uuid.uuid4(), 'Snowdestroy1', None)
    ssweeper2 = SnowSweeper(uuid.uuid4(), 'Furia2', None)
    ssweeper3 = SnowSweeper(uuid.uuid4(), 'Bravo3', None)
    ssweeper4 = SnowSweeper(uuid.uuid4(), 'Demon4', None)