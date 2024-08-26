# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundRealTimePaymentsTransfer"]


class InboundRealTimePaymentsTransfer(BaseModel):
    id: str
    """The inbound Real-Time Payments transfer's identifier."""

    account_id: str
    """The Account to which the transfer was sent."""

    account_number_id: str
    """The identifier of the Account Number to which this transfer was sent."""

    amount: int
    """The amount in USD cents."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    creditor_name: str
    """The name the sender of the transfer specified as the recipient of the transfer."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code of the transfer's
    currency. This will always be "USD" for a Real-Time Payments transfer.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    debtor_account_number: str
    """The account number of the account that sent the transfer."""

    debtor_name: str
    """The name provided by the sender of the transfer."""

    debtor_routing_number: str
    """The routing number of the account that sent the transfer."""

    remittance_information: Optional[str] = None
    """Additional information included with the transfer."""

    status: Literal["pending_confirmation", "timed_out", "confirmed"]
    """The lifecycle status of the transfer.

    - `pending_confirmation` - The transfer is pending confirmation.
    - `timed_out` - Your webhook failed to respond to the transfer in time.
    - `confirmed` - The transfer has been received successfully and is confirmed.
    """

    transaction_identification: str
    """The Real-Time Payments network identification of the transfer."""

    type: Literal["inbound_real_time_payments_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_real_time_payments_transfer`.
    """
