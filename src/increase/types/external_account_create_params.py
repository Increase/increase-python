# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    account_holder: Literal["business", "individual", "unknown"]
    """The type of entity that owns the External Account.

    - `business` - The External Account is owned by a business.
    - `individual` - The External Account is owned by an individual.
    - `unknown` - It's unknown what kind of entity owns the External Account.
    """

    funding: Literal["checking", "savings", "general_ledger", "other"]
    """The type of the destination account. Defaults to `checking`.

    - `checking` - A checking account.
    - `savings` - A savings account.
    - `general_ledger` - A general ledger account.
    - `other` - A different type of account.
    """
