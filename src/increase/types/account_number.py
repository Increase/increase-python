# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountNumber", "InboundACH", "InboundChecks"]


class InboundACH(BaseModel):
    debit_status: Literal["allowed", "blocked"]
    """Whether ACH debits are allowed against this Account Number.

    Note that they will still be declined if this is `allowed` if the Account Number
    is not active.

    - `allowed` - ACH Debits are allowed.
    - `blocked` - ACH Debits are blocked.
    """


class InboundChecks(BaseModel):
    status: Literal["allowed", "check_transfers_only"]
    """How Increase should process checks with this account number printed on them.

    - `allowed` - Checks with this Account Number will be processed even if they are
      not associated with a Check Transfer.
    - `check_transfers_only` - Checks with this Account Number will be processed
      only if they can be matched to an existing Check Transfer.
    """


class AccountNumber(BaseModel):
    id: str
    """The Account Number identifier."""

    account_id: str
    """The identifier for the account this Account Number belongs to."""

    account_number: str
    """The account number."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account
    Number was created.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    inbound_ach: InboundACH
    """Properties related to how this Account Number handles inbound ACH transfers."""

    inbound_checks: InboundChecks
    """
    Properties related to how this Account Number should handle inbound check
    withdrawals.
    """

    name: str
    """The name you choose for the Account Number."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    status: Literal["active", "disabled", "canceled"]
    """This indicates if payments can be made to the Account Number.

    - `active` - The account number is active.
    - `disabled` - The account number is temporarily disabled.
    - `canceled` - The account number is permanently disabled.
    """

    type: Literal["account_number"]
    """A constant representing the object's type.

    For this resource it will always be `account_number`.
    """
