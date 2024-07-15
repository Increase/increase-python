# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..transaction import Transaction
from ..declined_transaction import DeclinedTransaction

__all__ = ["InboundRealTimePaymentsTransferCreateResponse"]


class InboundRealTimePaymentsTransferCreateResponse(BaseModel):
    declined_transaction: Optional[DeclinedTransaction] = None
    """
    If the Real-Time Payments Transfer attempt fails, this will contain the
    resulting [Declined Transaction](#declined-transactions) object. The Declined
    Transaction's `source` will be of
    `category: inbound_real_time_payments_transfer_decline`.
    """

    transaction: Optional[Transaction] = None
    """
    If the Real-Time Payments Transfer attempt succeeds, this will contain the
    resulting [Transaction](#transactions) object. The Transaction's `source` will
    be of `category: inbound_real_time_payments_transfer_confirmation`.
    """

    type: Literal["inbound_real_time_payments_transfer_simulation_result"]
    """A constant representing the object's type.

    For this resource it will always be
    `inbound_real_time_payments_transfer_simulation_result`.
    """
