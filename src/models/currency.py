from decimal import Decimal

from pydantic import BaseModel


class Currency(BaseModel):
    id: int
    name: str
    purchasing_price: Decimal
    selling_price: Decimal
    time: str


class CurrencyItem(BaseModel):
    id: int
    user_id: int
    currency_id: int
    amount: Decimal


class UserCurrency(Currency):
    amount: Decimal
