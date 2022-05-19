# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EventSubscriptionUpdateParams"]


class EventSubscriptionUpdateParams(TypedDict, total=False):
    status: Optional[Literal["active", "disabled", "deleted"]]
    """The status to update the Event Subscription with."""
