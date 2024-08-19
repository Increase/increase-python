# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LockboxCreateParams"]


class LockboxCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account checks sent to this Lockbox should be deposited into."""

    description: str
    """The description you choose for the Lockbox, for display purposes."""

    recipient_name: str
    """The name of the recipient that will receive mail at this location."""
