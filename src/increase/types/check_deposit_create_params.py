# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CheckDepositCreateParams"]


class CheckDepositCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the Account to deposit the check in."""

    amount: Required[int]
    """The deposit amount in the minor unit of the account currency.

    For dollars, for example, this is cents.
    """

    back_image_file_id: Required[str]
    """The File containing the check's back image."""

    currency: Required[str]
    """The currency to use for the deposit."""

    front_image_file_id: Required[str]
    """The File containing the check's front image."""
