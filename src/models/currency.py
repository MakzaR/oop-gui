from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class CurrencyHistory(BaseModel):
    purchasing_price: Decimal
    selling_price: Decimal
    time: datetime


class Currency(CurrencyHistory):
    id: int
    name: str


class CurrencyItem(BaseModel):
    user_id: int
    currency_id: int
    amount: Decimal


class UserCurrency(Currency):
    amount: Decimal = Decimal('0')
