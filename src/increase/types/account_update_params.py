# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountUpdateParams"]


class AccountUpdateParams(TypedDict, total=False):
    credit_limit: int
    """
    The new credit limit of the Account, if and only if the Account is a loan
    account.
    """

    name: str
    """The new name of the Account."""
