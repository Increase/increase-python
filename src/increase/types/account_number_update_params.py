# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccountNumberUpdateParams", "InboundACH"]


class AccountNumberUpdateParams(TypedDict, total=False):
    inbound_ach: InboundACH
    """Options related to how this Account Number handles inbound ACH transfers."""

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
