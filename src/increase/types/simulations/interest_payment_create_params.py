# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InterestPaymentCreateParams"]


class InterestPaymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier of the Account Number the Interest Payment is for."""

    amount: Required[int]
    """The interest amount in cents. Must be positive."""
