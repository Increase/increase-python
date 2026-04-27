# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LockboxRecipientUpdateParams"]


class LockboxRecipientUpdateParams(TypedDict, total=False):
    description: str
    """The description you choose for the Lockbox Recipient."""

    recipient_name: str
    """The name of the Lockbox Recipient."""

    status: Literal["active", "disabled", "canceled"]
    """The status of the Lockbox Recipient.

    - `active` - This Lockbox Recipient is active.
    - `disabled` - This Lockbox Recipient is disabled. Checks mailed to this Lockbox
      Recipient will be rejected.
    - `canceled` - This Lockbox Recipient is canceled and cannot be modified. Checks
      mailed to this Lockbox Recipient will be rejected.
    """
