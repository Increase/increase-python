# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccountNumberUpdateParams"]


class AccountNumberUpdateParams(TypedDict, total=False):
    name: str
    """The name you choose for the Account Number."""

    status: Literal["active", "disabled", "canceled"]
    """This indicates if transfers can be made to the Account Number.

    - `active` - The account number is active.
    - `disabled` - The account number is temporarily disabled.
    - `canceled` - The account number is permanently disabled.
    """
