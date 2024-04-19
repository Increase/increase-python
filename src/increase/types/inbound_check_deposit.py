# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundCheckDeposit"]


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

    amount: int
    """The deposited amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

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

    front_image_file_id: Optional[str] = None
    """The ID for the File containing the image of the front of the check."""

    status: Literal["pending", "accepted", "declined"]
    """The status of the Inbound Check Deposit.

    - `pending` - The Inbound Check Deposit is pending.
    - `accepted` - The Inbound Check Deposit was accepted.
    - `declined` - The Inbound Check Deposit was rejected.
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
