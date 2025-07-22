# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhysicalCard", "Cardholder", "Shipment", "ShipmentAddress", "ShipmentTracking", "ShipmentTrackingUpdate"]


class Cardholder(BaseModel):
    first_name: str
    """The cardholder's first name."""

    last_name: str
    """The cardholder's last name."""


class ShipmentAddress(BaseModel):
    city: str
    """The city of the shipping address."""

    country: str
    """The country of the shipping address."""

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
    """The state of the shipping address."""


class ShipmentTrackingUpdate(BaseModel):
    carrier_estimated_delivery_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time when the
    carrier expects the card to be delivered.
    """

    category: Literal["in_transit", "processed_for_delivery", "delivered", "returned_to_sender"]
    """The type of tracking event.

    - `in_transit` - The physical card is in transit.
    - `processed_for_delivery` - The physical card has been processed for delivery.
    - `delivered` - The physical card has been delivered.
    - `returned_to_sender` - Delivery failed and the physical card was returned to
      sender.
    """

    city: Optional[str] = None
    """The city where the event took place."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the tracking event took place.
    """

    postal_code: Optional[str] = None
    """The postal code where the event took place."""

    state: Optional[str] = None
    """The state where the event took place."""


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

    updates: List[ShipmentTrackingUpdate]
    """Tracking updates relating to the physical card's delivery."""


class Shipment(BaseModel):
    address: ShipmentAddress
    """The location to where the card's packing label is addressed."""

    method: Literal["usps", "fedex_priority_overnight", "fedex_2_day", "dhl_worldwide_express"]
    """The shipping method.

    - `usps` - USPS Post.
    - `fedex_priority_overnight` - FedEx Priority Overnight, no signature.
    - `fedex_2_day` - FedEx 2-day.
    - `dhl_worldwide_express` - DHL Worldwide Express, international shipping only.
    """

    schedule: Literal["next_day", "same_day"]
    """When this physical card should be produced by the card printer.

    The default timeline is the day after the card printer receives the order,
    except for `FEDEX_PRIORITY_OVERNIGHT` cards, which default to `SAME_DAY`. To use
    faster production methods, please reach out to
    [support@increase.com](mailto:support@increase.com).

    - `next_day` - The physical card will be shipped one business day after the
      order is received by the card printer. A card that is submitted to Increase on
      a Monday evening (Pacific Time) will ship out on Wednesday.
    - `same_day` - The physical card will be shipped on the same business day that
      the order is received by the card printer. A card that is submitted to
      Increase on a Monday evening (Pacific Time) will ship out on Tuesday.
    """

    status: Literal[
        "pending", "canceled", "submitted", "acknowledged", "rejected", "shipped", "returned", "requires_attention"
    ]
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
    - `requires_attention` - The physical card shipment requires attention from
      Increase before progressing.
    """

    tracking: Optional[ShipmentTracking] = None
    """Tracking details for the shipment."""


class PhysicalCard(BaseModel):
    id: str
    """The physical card identifier."""

    card_id: str
    """The identifier for the Card this Physical Card represents."""

    cardholder: Cardholder
    """Details about the cardholder, as it appears on the printed card."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Physical Card was created.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    physical_card_profile_id: Optional[str] = None
    """The Physical Card Profile used for this Physical Card."""

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
