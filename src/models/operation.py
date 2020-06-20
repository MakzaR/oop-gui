from decimal import Decimal
from enum import Enum

from pydantic import BaseModel


class OperationType(Enum):
    BUY = 'BUY'
    SELL = 'SELL'


class Operation(BaseModel):
    operation_type: OperationType
    currency_id: int
    amount: Decimal


class OperationToShow(Operation):
    currency_name: str
