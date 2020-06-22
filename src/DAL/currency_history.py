from abc import ABC, abstractmethod
from typing import List

import requests
from requests import Response

from src.models.currency import CurrencyHistory
from src.urls import Urls
from pydantic import parse_obj_as


class AbstractCurrencyHistoryGetter(ABC):
    @abstractmethod
    def get(self, currency_id: int) -> List[CurrencyHistory]:
        pass


class ConcreteCurrencyHistoryGetter(AbstractCurrencyHistoryGetter):
    def get(self, currency_id: int) -> List[CurrencyHistory]:
        response: Response = requests.get(f'{Urls.CURRENCIES.value}/{currency_id}/history')
        return parse_obj_as(List[CurrencyHistory], response.json())
