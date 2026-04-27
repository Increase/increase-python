# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LockboxAddressUpdateParams"]


class LockboxAddressUpdateParams(TypedDict, total=False):
    description: str
    """The description you choose for the Lockbox Address."""

    status: Literal["active", "disabled", "canceled"]
    """The status of the Lockbox Address.

    - `active` - This Lockbox Address is active.
    - `disabled` - This Lockbox Address is disabled.
    - `canceled` - This Lockbox Address is permanently disabled.
    """
