# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PhysicalCardTrackingUpdatesParams"]


class PhysicalCardTrackingUpdatesParams(TypedDict, total=False):
    category: Required[Literal["in_transit", "processed_for_delivery", "delivered", "returned_to_sender"]]
    """The type of tracking event.

    - `in_transit` - The physical card is in transit.
    - `processed_for_delivery` - The physical card has been processed for delivery.
    - `delivered` - The physical card has been delivered.
    - `returned_to_sender` - Delivery failed and the physical card was returned to
      sender.
    """

    carrier_estimated_delivery_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time when the
    carrier expects the card to be delivered.
    """

    city: str
    """The city where the event took place."""

    postal_code: str
    """The postal code where the event took place."""

    state: str
    """The state where the event took place."""
