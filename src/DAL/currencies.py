from abc import ABC, abstractmethod
from typing import List

import requests
from pydantic import parse_obj_as
from requests import Response

from src.models.currency import Currency
from src.urls import Urls


class AbstractCurrenciesGetter(ABC):
    @abstractmethod
    def get(self) -> List[Currency]:
        pass


class ConcreteCurrencyGetter(AbstractCurrenciesGetter):
    def get(self) -> List[Currency]:
        response: Response = requests.get(Urls.CURRENCIES.value)
        return parse_obj_as(List[Currency], response.json())
