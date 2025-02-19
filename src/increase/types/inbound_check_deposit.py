# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundCheckDeposit", "Adjustment", "DepositReturn"]


class Adjustment(BaseModel):
    adjusted_at: datetime
    """The time at which the return adjustment was received."""

    amount: int
    """The amount of the adjustment."""

    reason: Literal["late_return", "wrong_payee_credit", "adjusted_amount", "non_conforming_item"]
    """The reason for the adjustment.

    - `late_return` - The return was initiated too late and the receiving
      institution has responded with a Late Return Claim.
    - `wrong_payee_credit` - The check was deposited to the wrong payee and the
      depositing institution has reimbursed the funds with a Wrong Payee Credit.
    - `adjusted_amount` - The check was deposited with a different amount than what
      was written on the check.
    - `non_conforming_item` - The recipient was not able to process the check. This
      usually happens for e.g., low quality images.
    """

    transaction_id: str
    """The id of the transaction for the adjustment."""


class DepositReturn(BaseModel):
    reason: Literal[
        "altered_or_fictitious",
        "not_authorized",
        "duplicate_presentment",
        "endorsement_missing",
        "endorsement_irregular",
    ]
    """The reason the deposit was returned.

    - `altered_or_fictitious` - The check was altered or fictitious.
    - `not_authorized` - The check was not authorized.
    - `duplicate_presentment` - The check was a duplicate presentment.
    - `endorsement_missing` - The check was not endorsed.
    - `endorsement_irregular` - The check was not endorsed by the payee.
    """

    returned_at: datetime
    """The time at which the deposit was returned."""

    transaction_id: str
    """The id of the transaction for the returned deposit."""


class InboundCheckDeposit(BaseModel):
    id: str
    """The deposit's identifier."""

    accepted_at: Optional[datetime] = None
    """
    If the Inbound Check Deposit was accepted, the
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which this
    took place.
    """

    account_id: str
    """The Account the check is being deposited against."""

    account_number_id: Optional[str] = None
    """The Account Number the check is being deposited against."""

    adjustments: List[Adjustment]
    """
    If the deposit or the return was adjusted by the sending institution, this will
    contain details of the adjustments.
    """

    amount: int
    """The deposited amount in USD cents."""

    back_image_file_id: Optional[str] = None
    """The ID for the File containing the image of the back of the check."""

    bank_of_first_deposit_routing_number: Optional[str] = None
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    bank depositing this check. In some rare cases, this is not transmitted via
    Check21 and the value will be null.
    """

    check_number: Optional[str] = None
    """The check number printed on the check being deposited."""

    check_transfer_id: Optional[str] = None
    """
    If this deposit is for an existing Check Transfer, the identifier of that Check
    Transfer.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the deposit was attempted.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the deposit.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    declined_at: Optional[datetime] = None
    """
    If the Inbound Check Deposit was declined, the
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which this
    took place.
    """

    declined_transaction_id: Optional[str] = None
    """
    If the deposit attempt has been rejected, the identifier of the Declined
    Transaction object created as a result of the failed deposit.
    """

    deposit_return: Optional[DepositReturn] = None
    """
    If you requested a return of this deposit, this will contain details of the
    return.
    """

    front_image_file_id: Optional[str] = None
    """The ID for the File containing the image of the front of the check."""

    payee_name_analysis: Literal["name_matches", "does_not_match", "not_evaluated"]
    """Whether the details on the check match the recipient name of the check transfer.

    This is an optional feature, contact sales to enable.

    - `name_matches` - The details on the check match the recipient name of the
      check transfer.
    - `does_not_match` - The details on the check do not match the recipient name of
      the check transfer.
    - `not_evaluated` - The payee name analysis was not evaluated.
    """

    status: Literal["pending", "accepted", "declined", "returned", "requires_attention"]
    """The status of the Inbound Check Deposit.

    - `pending` - The Inbound Check Deposit is pending.
    - `accepted` - The Inbound Check Deposit was accepted.
    - `declined` - The Inbound Check Deposit was rejected.
    - `returned` - The Inbound Check Deposit was returned.
    - `requires_attention` - The Inbound Check Deposit requires attention from an
      Increase operator.
    """

    transaction_id: Optional[str] = None
    """
    If the deposit attempt has been accepted, the identifier of the Transaction
    object created as a result of the successful deposit.
    """

    type: Literal["inbound_check_deposit"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_check_deposit`.
    """
