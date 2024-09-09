# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundRealTimePaymentsTransfer", "Confirmation", "Decline"]


class Confirmation(BaseModel):
    confirmed_at: datetime
    """The time at which the transfer was confirmed."""

    transaction_id: str
    """The id of the transaction for the confirmed transfer."""


class Decline(BaseModel):
    declined_at: datetime
    """The time at which the transfer was declined."""

    declined_transaction_id: str
    """The id of the transaction for the declined transfer."""

    reason: Literal[
        "account_number_canceled",
        "account_number_disabled",
        "account_restricted",
        "group_locked",
        "entity_not_active",
        "real_time_payments_not_enabled",
    ]
    """The reason for the transfer decline.

    - `account_number_canceled` - The account number is canceled.
    - `account_number_disabled` - The account number is disabled.
    - `account_restricted` - Your account is restricted.
    - `group_locked` - Your account is inactive.
    - `entity_not_active` - The account's entity is not active.
    - `real_time_payments_not_enabled` - Your account is not enabled to receive
      Real-Time Payments transfers.
    """


class InboundRealTimePaymentsTransfer(BaseModel):
    id: str
    """The inbound Real-Time Payments transfer's identifier."""

    account_id: str
    """The Account to which the transfer was sent."""

    account_number_id: str
    """The identifier of the Account Number to which this transfer was sent."""

    amount: int
    """The amount in USD cents."""

    confirmation: Optional[Confirmation] = None
    """If your transfer is confirmed, this will contain details of the confirmation."""

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

    decline: Optional[Decline] = None
    """If your transfer is declined, this will contain details of the decline."""

    remittance_information: Optional[str] = None
    """Additional information included with the transfer."""

    status: Literal["pending_confirming", "timed_out", "confirmed", "declined"]
    """The lifecycle status of the transfer.

    - `pending_confirming` - The transfer is pending confirmation.
    - `timed_out` - The transfer was not responded to in time.
    - `confirmed` - The transfer has been received successfully and is confirmed.
    - `declined` - The transfer has been declined.
    """

    transaction_identification: str
    """The Real-Time Payments network identification of the transfer."""

    type: Literal["inbound_real_time_payments_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_real_time_payments_transfer`.
    """
