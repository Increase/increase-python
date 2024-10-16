# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CheckDepositCreateParams"]


class CheckDepositCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the Account to deposit the check in."""

    amount: Required[int]
    """The deposit amount in USD cents."""

    back_image_file_id: Required[str]
    """The File containing the check's back image."""

    front_image_file_id: Required[str]
    """The File containing the check's front image."""

    description: str
    """
    The description you choose to give the Check Deposit, for display purposes only.
    """
