# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LockboxUpdateParams"]


class LockboxUpdateParams(TypedDict, total=False):
    description: str
    """The description you choose for the Lockbox."""

    recipient_name: str
    """The recipient name you choose for the Lockbox."""

    status: Literal["active", "inactive"]
    """This indicates if checks can be sent to the Lockbox.

    - `active` - This Lockbox is active. Checks mailed to it will be deposited
      automatically.
    - `inactive` - This Lockbox is inactive. Checks mailed to it will not be
      deposited.
    """
