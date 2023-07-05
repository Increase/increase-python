# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BookkeepingAccountCreateParams"]


class BookkeepingAccountCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name you choose for the account."""

    account_id: str
    """The entity, if `compliance_category` is `commingled_cash`."""

    compliance_category: Literal["commingled_cash", "customer_balance"]
    """The account compliance category.

    - `commingled_cash` - A cash in an commingled Increase Account.
    - `customer_balance` - A customer balance.
    """

    entity_id: str
    """The entity, if `compliance_category` is `customer_balance`."""
