# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountNumberCreateParams", "InboundACH"]


class AccountNumberCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account the Account Number should belong to."""

    name: Required[str]
    """The name you choose for the Account Number."""

    inbound_ach: InboundACH
    """Options related to how this Account Number should handle inbound ACH transfers."""


class InboundACH(TypedDict, total=False):
    debit_status: Required[Literal["allowed", "blocked"]]
    """Whether ACH debits are allowed against this Account Number.

    Note that ACH debits will be declined if this is `allowed` but the Account
    Number is not active.

    - `allowed` - ACH Debits are allowed.
    - `blocked` - ACH Debits are blocked.
    """
