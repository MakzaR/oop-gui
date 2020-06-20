from abc import ABC, abstractmethod
from concurrent.futures.thread import ThreadPoolExecutor
from typing import List, Iterator

import requests
from requests import Response

from config import service_settings
from src.models.currency import UserCurrency, Currency, CurrencyItem
from src.urls import Urls
from pydantic import parse_obj_as


class AbstractUserCurrencyGetter(ABC):
    @abstractmethod
    def get(self, user_id: int) -> List[UserCurrency]:
        pass


class ConcreteUserCurrencyGetter(AbstractUserCurrencyGetter):
    def _get_currency(self, currency_item: CurrencyItem) -> UserCurrency:
        response: Response = requests.get(f'{Urls.CURRENCIES.value}/{currency_item.currency_id}')
        currency = Currency.parse_obj(response.json())
        return UserCurrency(**currency.dict(), amount=currency_item.amount)

    def get(self, user_id: int) -> List[UserCurrency]:
        response: Response = requests.get(f'{Urls.USERS.value}/{user_id}/currencies')
        user_currencies = parse_obj_as(List[CurrencyItem], response.json())
        with ThreadPoolExecutor(max_workers=service_settings.max_workers) as executor:
            return list(executor.map(lambda item: self._get_currency(item), user_currencies))