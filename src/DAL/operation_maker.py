from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal
from http import HTTPStatus

import requests
from requests import Response

from src.exceptions import DALError
from src.models.currency import UserCurrency
from src.models.operation import OperationType
from src.models.user import User
from src.urls import Urls


class AbstractOperationMaker(ABC):
    @abstractmethod
    def make(
        self,
        operation_type: OperationType,
        user: User,
        currency: UserCurrency,
        amount: Decimal,
    ) -> None:
        pass


class ConcreteOperationMaker(AbstractOperationMaker):
    def make(
        self,
        operation_type: OperationType,
        user: User,
        currency: UserCurrency,
        amount: Decimal,
    ) -> None:
        if (
            operation_type == OperationType.BUY
            and user.money < amount * currency.purchasing_price
        ):
            raise DALError('У вас недостаточно средств')
        if operation_type == OperationType.SELL and amount > currency.amount:
            raise DALError('У вас нет такого кол-ва валюты')

        response: Response = requests.post(
            f'{Urls.USERS.value}/{user.id}/currencies',
            json={
                'currency_id': currency.id,
                'operation': operation_type.value,
                'amount': str(amount),
                'time': datetime.strftime(currency.time, '%Y-%m-%d %H:%M:%S'),
            },
        )
        if response.status_code == HTTPStatus.BAD_REQUEST:
            raise DALError('Данные устарели, обновите и попробуйте еще раз')
