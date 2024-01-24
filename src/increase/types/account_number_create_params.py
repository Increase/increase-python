# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountNumberCreateParams", "InboundACH", "InboundChecks"]


class AccountNumberCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account the Account Number should belong to."""

    name: Required[str]
    """The name you choose for the Account Number."""

    inbound_ach: InboundACH
    """Options related to how this Account Number should handle inbound ACH transfers."""

    inbound_checks: InboundChecks
    """
    Options related to how this Account Number should handle inbound check
    withdrawals.
    """

    unique_identifier: str
    """A unique identifier you choose for the object.

    Reusing this identifier for another object will result in an error. You can
    query for the object associated with this identifier using the List endpoint.
    """


class InboundACH(TypedDict, total=False):
    debit_status: Required[Literal["allowed", "blocked"]]
    """Whether ACH debits are allowed against this Account Number.

    Note that ACH debits will be declined if this is `allowed` but the Account
    Number is not active.

    - `allowed` - ACH Debits are allowed.
    - `blocked` - ACH Debits are blocked.
    """


class InboundChecks(TypedDict, total=False):
    status: Required[Literal["allowed", "check_transfers_only"]]
    """How Increase should process checks with this account number printed on them.

    - `allowed` - Checks with this Account Number will be processed even if they are
      not associated with a Check Transfer.
    - `check_transfers_only` - Checks with this Account Number will be processed
      only if they can be matched to an existing Check Transfer.
    """
