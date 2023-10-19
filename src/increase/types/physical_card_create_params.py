# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PhysicalCardCreateParams", "Cardholder", "Shipment", "ShipmentAddress"]


class PhysicalCardCreateParams(TypedDict, total=False):
    card_id: Required[str]
    """The underlying card representing this physical card."""

    card_profile_id: Required[str]
    """The card profile to use for this physical card."""

    cardholder: Required[Cardholder]
    """Details about the cardholder, as it will appear on the physical card."""

    shipment: Required[Shipment]
    """The details used to ship this physical card."""


class Cardholder(TypedDict, total=False):
    first_name: Required[str]
    """The cardholder's first name."""

    last_name: Required[str]
    """The cardholder's last name."""


class ShipmentAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the shipping address."""

    line1: Required[str]
    """The first line of the shipping address."""

    name: Required[str]
    """The name of the recipient."""

    postal_code: Required[str]
    """The postal code of the shipping address."""

    state: Required[str]
    """The US state of the shipping address."""

    line2: str
    """The second line of the shipping address."""

    line3: str
    """The third line of the shipping address."""

    phone_number: str
    """The phone number of the recipient."""


class Shipment(TypedDict, total=False):
    address: Required[ShipmentAddress]
    """The address to where the card should be shipped."""

    method: Required[Literal["usps", "fedex_priority_overnight", "fedex_2_day"]]
    """The shipping method to use.

    - `usps` - USPS Post with tracking.
    - `fedex_priority_overnight` - FedEx Priority Overnight, no signature.
    - `fedex_2_day` - FedEx 2-day.
    """
