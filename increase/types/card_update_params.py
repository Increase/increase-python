# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BillingAddress", "CardUpdateParams"]


class BillingAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the billing address."""

    line1: Required[str]
    """The first line of the billing address."""

    postal_code: Required[str]
    """The postal code of the billing address."""

    state: Required[str]
    """The US state of the billing address."""

    line2: Optional[str]
    """The second line of the billing address."""


class CardUpdateParams(TypedDict, total=False):
    billing_address: Optional[BillingAddress]
    """The card's updated billing address."""

    description: Optional[str]
    """The description you choose to give the card."""

    status: Optional[Literal["active", "disabled", "canceled"]]
    """The status to update the Card with."""
