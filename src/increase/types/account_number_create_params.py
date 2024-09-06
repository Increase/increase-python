# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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


class InboundACH(TypedDict, total=False):
    debit_status: Required[Literal["allowed", "blocked"]]
    """Whether ACH debits are allowed against this Account Number.

    Note that ACH debits will be declined if this is `allowed` but the Account
    Number is not active. If you do not specify this field, the default is
    `allowed`.

    - `allowed` - ACH Debits are allowed.
    - `blocked` - ACH Debits are blocked.
    """


class InboundChecks(TypedDict, total=False):
    status: Required[Literal["allowed", "check_transfers_only"]]
    """How Increase should process checks with this account number printed on them.

    If you do not specify this field, the default is `check_transfers_only`.

    - `allowed` - Checks with this Account Number will be processed even if they are
      not associated with a Check Transfer.
    - `check_transfers_only` - Checks with this Account Number will be processed
      only if they can be matched to an existing Check Transfer.
    """
