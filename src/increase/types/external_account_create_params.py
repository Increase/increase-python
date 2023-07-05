# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalAccountCreateParams"]


class ExternalAccountCreateParams(TypedDict, total=False):
    account_number: Required[str]
    """The account number for the destination account."""

    description: Required[str]
    """The name you choose for the Account."""

    routing_number: Required[str]
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
    """

    funding: Literal["checking", "savings", "other"]
    """The type of the destination account. Defaults to `checking`.

    - `checking` - A checking account.
    - `savings` - A savings account.
    - `other` - A different type of account.
    """
