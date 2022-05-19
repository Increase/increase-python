# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Approval", "Cancellation", "AccountTransfer"]


class Approval(BaseModel):
    approved_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was approved.
    """


class Cancellation(BaseModel):
    canceled_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Transfer was canceled.
    """


class AccountTransfer(BaseModel):
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

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination
    account currency.
    """

    description: str
    """The description that will show on the transactions."""

    destination_account_id: str
    """The destination account's identifier."""

    destination_transaction_id: Optional[str]
    """The ID for the transaction receiving the transfer."""

    id: str
    """The account transfer's identifier."""

    network: Literal["account"]
    """The transfer's network."""

    status: Literal[
        "pending_submission", "pending_approval", "canceled", "requires_attention", "flagged_by_operator", "complete"
    ]
    """The lifecycle status of the transfer."""

    template_id: Optional[str]
    """If the transfer was created from a template, this will be the template's ID."""

    transaction_id: Optional[str]
    """The ID for the transaction funding the transfer."""

    type: Literal["account_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `account_transfer`.
    """
