# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LockboxRecipientCreateParams"]


class LockboxRecipientCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """
    The Account that checks sent to this Lockbox Recipient should be deposited into.
    """

    lockbox_address_id: Required[str]
    """The Lockbox Address where this Lockbox Recipient may receive mail."""

    description: str
    """The description you choose for the Lockbox Recipient."""

    recipient_name: str
    """The name of the Lockbox Recipient"""
