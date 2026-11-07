# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccountNumberUpdateParams"]


class AccountNumberUpdateParams(TypedDict, total=False):
    inbound_ach_debits: Literal["allowed", "blocked"]
    """Whether inbound ACH debits are allowed against this Account Number.

    Note that ACH debits will be declined if this is `allowed` but the Account
    Number is not active.

    - `allowed` - ACH Debits are allowed.
    - `blocked` - ACH Debits are blocked. Received debits will be declined and
      returned with code `R20` (non-transaction account).
    """

    name: str
    """The name you choose for the Account Number."""

    status: Literal["active", "disabled", "canceled"]
    """This indicates if transfers can be made to the Account Number.

    - `active` - The account number is active.
    - `disabled` - The account number is temporarily disabled.
    - `canceled` - The account number is permanently disabled.
    """

    unregistered_inbound_checks: Literal["allowed", "blocked"]
    """Whether unregistered inbound checks for this Account Number can be deposited.

    - `allowed` - Accept all Inbound Check Deposits, even if they are not associated
      with a Check Transfer or Checkbook Check.
    - `blocked` - Only accept Inbound Check Deposits if they can be matched to a
      Check Transfer or Checkbook Check.
    """
