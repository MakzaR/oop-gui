from decimal import Decimal

from pydantic import BaseModel


class User(BaseModel):
    id: int
    login: str
    money: Decimal
