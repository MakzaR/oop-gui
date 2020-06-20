from typing import List

from src.DAL.auth import AbstractAuthorization, ConcreteAuthorization
from src.DAL.currencies import AbstractCurrenciesGetter, ConcreteCurrencyGetter
from src.DAL.operations import AbstractOperationsGetter, ConcreteOperationsGetter
from src.DAL.user_currencies import (
    AbstractUserCurrencyGetter,
    ConcreteUserCurrencyGetter,
)
from src.DAL.utils import run_in_threadpool
from src.models.currency import Currency, UserCurrency
from src.models.operation import OperationToShow
from src.models.user import User


class Client:
    def __init__(
        self,
        authorization: AbstractAuthorization = ConcreteAuthorization(),
        currencies_getter: AbstractCurrenciesGetter = ConcreteCurrencyGetter(),
        user_currencies_getter: AbstractUserCurrencyGetter = ConcreteUserCurrencyGetter(),
        user_operations_getter: AbstractOperationsGetter = ConcreteOperationsGetter(),
    ):
        self._authorization: AbstractAuthorization = authorization
        self._currencies_getter: AbstractCurrenciesGetter = currencies_getter
        self._user_currencies_getter = user_currencies_getter
        self._operations_getter = user_operations_getter

    @run_in_threadpool
    def get_operations(self, user_id: int) -> List[OperationToShow]:
        return self._operations_getter.get(user_id)

    @run_in_threadpool
    def get_all_currencies(self) -> List[Currency]:
        return self._currencies_getter.get()

    @run_in_threadpool
    def get_user_currencies(self, user_id: int) -> List[UserCurrency]:
        return self._user_currencies_getter.get(user_id)

    @run_in_threadpool
    def sign_in(self, username: str) -> User:
        return self._authorization.sign_in(username)
