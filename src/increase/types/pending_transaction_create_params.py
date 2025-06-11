# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PendingTransactionCreateParams"]


class PendingTransactionCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account to place the hold on."""

    amount: Required[int]
    """The amount to hold in the minor unit of the account's currency.

    For dollars, for example, this is cents. This should be a negative amount - to
    hold $1.00 from the account, you would pass -100.
    """

    description: str
    """The description you choose to give the hold."""
