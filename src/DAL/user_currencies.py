from abc import ABC, abstractmethod
from concurrent.futures.thread import ThreadPoolExecutor
from decimal import Decimal
from http import HTTPStatus
from typing import List

import requests
from pydantic import parse_obj_as
from requests import Response

from config import service_settings
from src.models.currency import Currency, CurrencyItem, UserCurrency
from src.urls import Urls


class AbstractUserCurrencyGetter(ABC):
    @abstractmethod
    def get(self, user_id: int) -> List[UserCurrency]:
        pass

    @abstractmethod
    def get_currency(self, user_id: int, currency_id: int) -> UserCurrency:
        pass


class ConcreteUserCurrencyGetter(AbstractUserCurrencyGetter):
    def get_currency(self, user_id: int, currency_id: int) -> UserCurrency:
        res = requests.get(f'{Urls.USERS.value}/{user_id}/currencies/{currency_id}')
        if res.status_code == HTTPStatus.BAD_REQUEST:
            return self._get_currency(CurrencyItem(user_id=user_id, currency_id=currency_id, amount=Decimal('0')))
        return self._get_currency(CurrencyItem.parse_obj(res.json()))

    def _get_currency(self, currency_item: CurrencyItem) -> UserCurrency:
        response: Response = requests.get(
            f'{Urls.CURRENCIES.value}/{currency_item.currency_id}'
        )
        currency = Currency.parse_obj(response.json())
        return UserCurrency(**currency.dict(), amount=currency_item.amount)

    def get(self, user_id: int) -> List[UserCurrency]:
        response: Response = requests.get(f'{Urls.USERS.value}/{user_id}/currencies')
        user_currencies = parse_obj_as(List[CurrencyItem], response.json())
        with ThreadPoolExecutor(max_workers=service_settings.max_workers) as executor:
            return list(
                executor.map(lambda item: self._get_currency(item), user_currencies)
            )
