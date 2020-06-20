from abc import ABC, abstractmethod
from concurrent.futures.thread import ThreadPoolExecutor
from typing import List

import requests
from pydantic import parse_obj_as
from requests import Response

from config import service_settings
from src.models.currency import Currency
from src.models.operation import Operation, OperationToShow
from src.urls import Urls


class AbstractOperationsGetter(ABC):
    @abstractmethod
    def get(self, user_id: int) -> List[OperationToShow]:
        pass


class ConcreteOperationsGetter(AbstractOperationsGetter):
    def _get_operation(self, operation: Operation) -> OperationToShow:
        response: Response = requests.get(
            f'{Urls.CURRENCIES.value}/{operation.currency_id}'
        )
        currency = Currency.parse_obj(response.json())
        return OperationToShow(**operation.dict(), currency_name=currency.name)

    def get(self, user_id: int) -> List[OperationToShow]:
        response: Response = requests.get(f'{Urls.USERS.value}/{user_id}/operations')
        operations = parse_obj_as(List[Operation], response.json())
        with ThreadPoolExecutor(service_settings.max_workers) as executor:
            return list(executor.map(self._get_operation, operations))
