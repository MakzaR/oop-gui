from enum import Enum
from config import service_settings


class Urls(Enum):
    BASE_URL = f'http://{service_settings.host}:{service_settings.port}'
    USERS = f'{BASE_URL}/users'