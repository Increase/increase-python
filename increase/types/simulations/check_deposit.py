# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DepositRejection", "DepositReturn", "CheckDeposit"]


class DepositRejection(BaseModel):
    amount: int
    """The rejected amount in the minor unit of check's currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.
    """

    reason: Literal[
        "incomplete_image", "duplicate", "poor_image_quality", "incorrect_amount", "incorrect_recipient", "unknown"
    ]
    """Why the check deposit was rejected."""

    rejected_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check deposit was rejected.
    """


class DepositReturn(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    check_deposit_id: str
    """The identifier of the Check Deposit that was returned."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    return_reason: Literal[
        "ach_conversion_not_supported",
        "duplicate_submission",
        "insufficient_funds",
        "no_account",
        "unmatched_details",
        "unreadable_image",
        "unknown_reason",
        "not_authorized",
    ]

    returned_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check deposit was returned.
    """

    transaction_id: str
    """
    The identifier of the transaction that reversed the original check deposit
    transaction.
    """


class CheckDeposit(BaseModel):
    account_id: str
    """The Account the check was deposited into."""

    amount: int
    """The deposited amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    back_image_file_id: Optional[str]
    """The ID for the File containing the image of the back of the check."""

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    currency: str
    """The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the deposit."""

    deposit_rejection: Optional[DepositRejection]
    """
    If your deposit is rejected by Increase, this will contain details as to why it
    was rejected.
    """

    deposit_return: Optional[DepositReturn]
    """
    If your deposit is returned, this will contain details as to why it was
    returned.
    """

    front_image_file_id: str
    """The ID for the File containing the image of the front of the check."""

    id: str
    """The deposit's identifier."""

    status: Literal["pending", "submitted", "rejected", "returned"]
    """The status of the Check Deposit."""

    transaction_id: Optional[str]
    """The ID for the Transaction created by the deposit."""

    type: Literal["check_deposit"]
    """A constant representing the object's type.

    For this resource it will always be `check_deposit`.
    """
