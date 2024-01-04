# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhysicalCard", "Cardholder", "Shipment", "ShipmentAddress", "ShipmentTracking"]


class Cardholder(BaseModel):
    first_name: str
    """The cardholder's first name."""

    last_name: str
    """The cardholder's last name."""


class ShipmentAddress(BaseModel):
    city: str
    """The city of the shipping address."""

    line1: str
    """The first line of the shipping address."""

    line2: Optional[str] = None
    """The second line of the shipping address."""

    line3: Optional[str] = None
    """The third line of the shipping address."""

    name: str
    """The name of the recipient."""

    postal_code: str
    """The postal code of the shipping address."""

    state: str
    """The US state of the shipping address."""


class ShipmentTracking(BaseModel):
    number: str
    """The tracking number."""

    return_number: Optional[str] = None
    """For returned shipments, the tracking number of the return shipment."""

    return_reason: Optional[str] = None
    """For returned shipments, this describes why the package was returned."""

    shipped_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the fulfillment provider marked the card as ready for pick-up by the shipment
    carrier.
    """


class Shipment(BaseModel):
    address: ShipmentAddress
    """The location to where the card's packing label is addressed."""

    method: Literal["usps", "fedex_priority_overnight", "fedex_2_day"]
    """The shipping method.

    - `usps` - USPS Post with tracking.
    - `fedex_priority_overnight` - FedEx Priority Overnight, no signature.
    - `fedex_2_day` - FedEx 2-day.
    """

    status: Literal["pending", "canceled", "submitted", "acknowledged", "rejected", "shipped", "returned"]
    """The status of this shipment.

    - `pending` - The physical card has not yet been shipped.
    - `canceled` - The physical card shipment was canceled prior to submission.
    - `submitted` - The physical card shipment has been submitted to the card
      fulfillment provider.
    - `acknowledged` - The physical card shipment has been acknowledged by the card
      fulfillment provider and will be processed in their next batch.
    - `rejected` - The physical card shipment was rejected by the card printer due
      to an error.
    - `shipped` - The physical card has been shipped.
    - `returned` - The physical card shipment was returned to the sender and
      destroyed by the production facility.
    """

    tracking: Optional[ShipmentTracking] = None
    """Tracking details for the shipment."""


class PhysicalCard(BaseModel):
    id: str
    """The physical card identifier."""

    card_id: str
    """The identifier for the Card this Physical Card represents."""

    card_profile_id: Optional[str] = None
    """The Card Profile used for this Physical Card."""

    cardholder: Optional[Cardholder] = None
    """Details about the cardholder, as it appears on the printed card."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Physical Card was created.
    """

    shipment: Shipment
    """The details used to ship this physical card."""

    status: Literal["active", "disabled", "canceled"]
    """The status of the Physical Card.

    - `active` - The physical card is active.
    - `disabled` - The physical card is temporarily disabled.
    - `canceled` - The physical card is permanently canceled.
    """

    type: Literal["physical_card"]
    """A constant representing the object's type.

    For this resource it will always be `physical_card`.
    """
