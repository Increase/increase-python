# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountNumberCreateParams"]


class AccountNumberCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account the Account Number should belong to."""

    name: Required[str]
    """The name you choose for the Account Number."""

    inbound_ach_debits: Literal["allowed", "blocked"]
    """Whether inbound ACH debits are allowed against this Account Number.

    Note that ACH debits will be declined if this is `allowed` but the Account
    Number is not active. If you do not specify this field, the default is
    `allowed`.

    - `allowed` - ACH Debits are allowed.
    - `blocked` - ACH Debits are blocked. Received debits will be declined and
      returned with code `R20` (non-transaction account).
    """

    unregistered_inbound_checks: Literal["allowed", "blocked"]
    """Whether unregistered inbound checks for this Account Number can be deposited.

    If you do not specify this field, the default is `blocked`.

    - `allowed` - Accept all Inbound Check Deposits, even if they are not associated
      with a Check Transfer or Checkbook Check.
    - `blocked` - Only accept Inbound Check Deposits if they can be matched to a
      Check Transfer or Checkbook Check.
    """
