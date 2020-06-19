import json
from abc import ABC, abstractmethod
from http import HTTPStatus
from asyncio import run
from typing import Dict, Any

import requests
from requests import Response

from src.models.user import User
from src.urls import Urls


class AbstractAuthorization(ABC):
    @abstractmethod
    def sign_in(self, username: str) -> User:
        pass


class Authorization(AbstractAuthorization):
    def _deserialize(self, json_: Dict[str, Any]):
        return User.parse_obj(json_)

    def _get_user(self, username: str) -> User:
        response: Response = requests.get(Urls.USERS.value, params={'user_name': username})
        return self._deserialize(response.json())

    def sign_in(self, username: str) -> User:
        response: Response = requests.post(Urls.USERS.value, json={'login': username})
        if response.status_code == HTTPStatus.BAD_REQUEST:
            return self._get_user(username)
        return self._deserialize(response.json())
