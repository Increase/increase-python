# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LockboxUpdateParams"]


class LockboxUpdateParams(TypedDict, total=False):
    check_deposit_behavior: Literal["enabled", "disabled"]
    """This indicates if checks mailed to this lockbox will be deposited.

    - `enabled` - Checks mailed to this Lockbox will be deposited.
    - `disabled` - Checks mailed to this Lockbox will not be deposited.
    """

    description: str
    """The description you choose for the Lockbox."""

    recipient_name: str
    """The recipient name you choose for the Lockbox."""
