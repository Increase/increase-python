# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CheckDeposit", "DepositAcceptance", "DepositRejection", "DepositReturn"]


class DepositAcceptance(BaseModel):
    account_number: str
    """The account number printed on the check."""

    amount: int
    """The amount to be deposited in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    auxiliary_on_us: Optional[str]
    """An additional line of metadata printed on the check.

    This typically includes the check number for business checks.
    """

    check_deposit_id: str
    """The ID of the Check Deposit that was accepted."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    routing_number: str
    """The routing number printed on the check."""

    serial_number: Optional[str]
    """The check serial number, if present, for consumer checks.

    For business checks, the serial number is usually in the `auxiliary_on_us`
    field.
    """


class DepositRejection(BaseModel):
    amount: int
    """The rejected amount in the minor unit of check's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.
    """

    reason: Literal[
        "incomplete_image",
        "duplicate",
        "poor_image_quality",
        "incorrect_amount",
        "incorrect_recipient",
        "not_eligible_for_mobile_deposit",
        "missing_required_data_elements",
        "unknown",
    ]
    """Why the check deposit was rejected."""

    rejected_at: datetime
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

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    return_reason: Literal[
        "ach_conversion_not_supported",
        "closed_account",
        "duplicate_submission",
        "insufficient_funds",
        "no_account",
        "not_authorized",
        "stale_dated",
        "stop_payment",
        "unknown_reason",
        "unmatched_details",
        "unreadable_image",
    ]

    returned_at: datetime
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

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the deposit."""

    deposit_acceptance: Optional[DepositAcceptance]
    """
    If your deposit is successfully parsed and accepted by Increase, this will
    contain details of the parsed check.
    """

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
