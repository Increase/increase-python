# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundFednowTransfer", "Confirmation", "Decline"]


class Confirmation(BaseModel):
    transfer_id: str
    """The identifier of the FedNow Transfer that led to this Transaction."""


class Decline(BaseModel):
    reason: Literal[
        "account_number_canceled",
        "account_number_disabled",
        "account_restricted",
        "group_locked",
        "entity_not_active",
        "fednow_not_enabled",
    ]
    """Why the transfer was declined.

    - `account_number_canceled` - The account number is canceled.
    - `account_number_disabled` - The account number is disabled.
    - `account_restricted` - Your account is restricted.
    - `group_locked` - Your account is inactive.
    - `entity_not_active` - The account's entity is not active.
    - `fednow_not_enabled` - Your account is not enabled to receive FedNow
      transfers.
    """

    transfer_id: str
    """The identifier of the FedNow Transfer that led to this declined transaction."""


class InboundFednowTransfer(BaseModel):
    id: str
    """The inbound FedNow transfer's identifier."""

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
    currency. This will always be "USD" for a FedNow transfer.

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

    status: Literal["pending_confirming", "timed_out", "confirmed", "declined", "requires_attention"]
    """The lifecycle status of the transfer.

    - `pending_confirming` - The transfer is pending confirmation.
    - `timed_out` - The transfer was not responded to in time.
    - `confirmed` - The transfer has been received successfully and is confirmed.
    - `declined` - The transfer has been declined.
    - `requires_attention` - The transfer requires attention from an Increase
      operator.
    """

    transaction_id: Optional[str] = None
    """
    The identifier of the Transaction object created when the transfer was
    confirmed.
    """

    type: Literal["inbound_fednow_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_fednow_transfer`.
    """

    unstructured_remittance_information: Optional[str] = None
    """Additional information included with the transfer."""
