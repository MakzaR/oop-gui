from abc import ABC, abstractmethod

import requests

from src.models.user import User
from src.urls import Urls


class AbstractUserGetter(ABC):
    @abstractmethod
    def get(self, user_id: int) -> User:
        pass


class ConcreteUserGetter(AbstractUserGetter):
    def get(self, user_id: int) -> User:
        response = requests.get(Urls.USERS.value, params={'user_id': user_id})
        return User.parse_obj(response.json())
