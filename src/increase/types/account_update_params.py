# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountUpdateParams", "Loan"]


class AccountUpdateParams(TypedDict, total=False):
    loan: Loan
    """The loan details for the account."""

    name: str
    """The new name of the Account."""


class Loan(TypedDict, total=False):
    """The loan details for the account."""

    credit_limit: Required[int]
    """The maximum amount of money that can be drawn from the Account."""
