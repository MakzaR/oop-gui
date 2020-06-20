from abc import ABC, abstractmethod
from http import HTTPStatus
from typing import Any, Dict, List

import requests
from requests import Response

from src.models.currency import Currency
from src.models.user import User
from src.urls import Urls
from pydantic import parse_obj_as


class AbstractAuthorization(ABC):
    @abstractmethod
    def sign_in(self, username: str) -> User:
        pass


class AbstractCurrenciesGetter(ABC):
    @abstractmethod
    def get(self) -> List[Currency]:
        pass


class ConcreteAuthorization(AbstractAuthorization):
    def _deserialize(self, json_: Dict[str, Any]):
        return User.parse_obj(json_)

    def _get_user(self, username: str) -> User:
        response: Response = requests.get(
            Urls.USERS.value, params={'user_name': username}
        )
        return self._deserialize(response.json())

    def sign_in(self, username: str) -> User:
        response: Response = requests.post(Urls.USERS.value, json={'login': username})
        if response.status_code == HTTPStatus.BAD_REQUEST:
            return self._get_user(username)
        return self._deserialize(response.json())


class ConcreteCurrencyGetter(AbstractCurrenciesGetter):
    def get(self) -> List[Currency]:
        response: Response = requests.get(Urls.CURRENCIES.value)
        return parse_obj_as(List[Currency], response.json())


class Client:
    def __init__(
            self,
            authorization: AbstractAuthorization = ConcreteAuthorization(),
            currencies_getter: AbstractCurrenciesGetter = ConcreteCurrencyGetter(),
    ):
        self._authorization: AbstractAuthorization = authorization
        self._currencies_getter: AbstractCurrenciesGetter = currencies_getter

    def get_currencies(self) -> List[Currency]:
        return self._currencies_getter.get()

    def sign_in(self, username: str) -> User:
        return self._authorization.sign_in(username)
