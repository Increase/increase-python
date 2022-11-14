# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountNumberCreateParams"]


class AccountNumberCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account the Account Number should belong to."""

    name: Required[str]
    """The name you choose for the Account Number."""
