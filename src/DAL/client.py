from decimal import Decimal
from typing import List

from src.DAL.auth import AbstractAuthorization, ConcreteAuthorization
from src.DAL.currencies import AbstractCurrenciesGetter, ConcreteCurrencyGetter
from src.DAL.currency_history import (
    AbstractCurrencyHistoryGetter,
    ConcreteCurrencyHistoryGetter,
)
from src.DAL.operation_maker import AbstractOperationMaker, ConcreteOperationMaker
from src.DAL.operations import AbstractOperationsGetter, ConcreteOperationsGetter
from src.DAL.user_currencies import (
    AbstractUserCurrencyGetter,
    ConcreteUserCurrencyGetter,
)
from src.DAL.user_getter import AbstractUserGetter, ConcreteUserGetter
from src.DAL.utils import run_in_threadpool
from src.models.currency import Currency, CurrencyHistory, UserCurrency
from src.models.operation import OperationToShow, OperationType
from src.models.user import User


class Client:
    def __init__(
        self,
        authorization: AbstractAuthorization = ConcreteAuthorization(),
        currencies_getter: AbstractCurrenciesGetter = ConcreteCurrencyGetter(),
        user_currencies_getter: AbstractUserCurrencyGetter = ConcreteUserCurrencyGetter(),
        user_operations_getter: AbstractOperationsGetter = ConcreteOperationsGetter(),
        currency_history_getter: AbstractCurrencyHistoryGetter = ConcreteCurrencyHistoryGetter(),
        operation_maker: AbstractOperationMaker = ConcreteOperationMaker(),
        user_getter: AbstractUserGetter = ConcreteUserGetter(),
    ):
        self._authorization: AbstractAuthorization = authorization
        self._currencies_getter: AbstractCurrenciesGetter = currencies_getter
        self._user_currencies_getter = user_currencies_getter
        self._operations_getter = user_operations_getter
        self._currency_history_getter = currency_history_getter
        self._operation_maker = operation_maker
        self._user_getter: AbstractUserGetter = user_getter

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

    @run_in_threadpool
    def get_currency_history(self, currency_id: int) -> List[CurrencyHistory]:
        return self._currency_history_getter.get(currency_id)

    @run_in_threadpool
    def make_operation(
        self,
        operation_type: OperationType,
        user: User,
        currency: UserCurrency,
        amount: Decimal,
    ):
        return self._operation_maker.make(operation_type, user, currency, amount)

    @run_in_threadpool
    def get_user(self, user_id: int) -> User:
        return self._user_getter.get(user_id)

    @run_in_threadpool
    def get_user_currency(self, user_id: int, currency_id: int) -> UserCurrency:
        return self._user_currencies_getter.get_currency(user_id, currency_id)
