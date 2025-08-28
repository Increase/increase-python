# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ACHTransferSettleParams"]


class ACHTransferSettleParams(TypedDict, total=False):
    inbound_funds_hold_behavior: Literal["release_immediately", "release_on_default_schedule"]
    """
    The behavior of the inbound funds hold that is created when the ACH Transfer is
    settled. If no behavior is specified, the inbound funds hold will be released
    immediately in order for the funds to be available for use.

    - `release_immediately` - Release the inbound funds hold immediately.
    - `release_on_default_schedule` - Release the inbound funds hold on the default
      schedule.
    """
