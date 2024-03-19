# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EventSubscriptionUpdateParams"]


class EventSubscriptionUpdateParams(TypedDict, total=False):
    status: Literal["active", "disabled", "deleted"]
    """The status to update the Event Subscription with.

    - `active` - The subscription is active and Events will be delivered normally.
    - `disabled` - The subscription is temporarily disabled and Events will not be
      delivered.
    - `deleted` - The subscription is permanently disabled and Events will not be
      delivered.
    """
