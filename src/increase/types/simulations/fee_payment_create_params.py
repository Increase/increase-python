# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FeePaymentCreateParams"]


class FeePaymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """
    The identifier of the Account to use as the billing account for the fee payment.
    """

    amount: Required[int]
    """The fee amount in cents. Must be positive."""
