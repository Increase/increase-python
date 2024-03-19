# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountNumberUpdateParams", "InboundACH", "InboundChecks"]


class AccountNumberUpdateParams(TypedDict, total=False):
    inbound_ach: InboundACH
    """Options related to how this Account Number handles inbound ACH transfers."""

    inbound_checks: InboundChecks
    """
    Options related to how this Account Number should handle inbound check
    withdrawals.
    """

    name: str
    """The name you choose for the Account Number."""

    status: Literal["active", "disabled", "canceled"]
    """This indicates if transfers can be made to the Account Number.

    - `active` - The account number is active.
    - `disabled` - The account number is temporarily disabled.
    - `canceled` - The account number is permanently disabled.
    """


class InboundACH(TypedDict, total=False):
    debit_status: Literal["allowed", "blocked"]
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
