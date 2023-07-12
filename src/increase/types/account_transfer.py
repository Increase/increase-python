# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountTransfer", "Approval", "Cancellation"]


class Approval(BaseModel):
    approved_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was approved.
    """

    approved_by: Optional[str]
    """
    If the Transfer was approved by a user in the dashboard, the email address of
    that user.
    """


class Cancellation(BaseModel):
    canceled_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Transfer was canceled.
    """

    canceled_by: Optional[str]
    """
    If the Transfer was canceled by a user in the dashboard, the email address of
    that user.
    """


class AccountTransfer(BaseModel):
    id: str
    """The account transfer's identifier."""

    account_id: str
    """The Account to which the transfer belongs."""

    amount: int
    """The transfer amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    approval: Optional[Approval]
    """
    If your account requires approvals for transfers and the transfer was approved,
    this will contain details of the approval.
    """

    cancellation: Optional[Cancellation]
    """
    If your account requires approvals for transfers and the transfer was not
    approved, this will contain details of the cancellation.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination
    account currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    description: str
    """The description that will show on the transactions."""

    destination_account_id: str
    """The destination account's identifier."""

    destination_transaction_id: Optional[str]
    """The ID for the transaction receiving the transfer."""

    network: Literal["account"]
    """The transfer's network."""

    status: Literal["pending_approval", "canceled", "complete"]
    """The lifecycle status of the transfer.

    - `pending_approval` - The transfer is pending approval.
    - `canceled` - The transfer has been canceled.
    - `complete` - The transfer has been completed.
    """

    transaction_id: Optional[str]
    """The ID for the transaction funding the transfer."""

    type: Literal["account_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `account_transfer`.
    """

    unique_identifier: Optional[str]
    """The unique identifier you chose for this transfer."""
