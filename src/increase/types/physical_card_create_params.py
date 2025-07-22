# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PhysicalCardCreateParams", "Cardholder", "Shipment", "ShipmentAddress"]


class PhysicalCardCreateParams(TypedDict, total=False):
    card_id: Required[str]
    """The underlying card representing this physical card."""

    cardholder: Required[Cardholder]
    """Details about the cardholder, as it will appear on the physical card."""

    shipment: Required[Shipment]
    """The details used to ship this physical card."""

    physical_card_profile_id: str
    """The physical card profile to use for this physical card.

    The latest default physical card profile will be used if not provided.
    """


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
    """The state of the shipping address."""

    country: str
    """
    The two-character ISO 3166-1 code of the country where the card should be
    shipped (e.g., `US`). Please reach out to
    [support@increase.com](mailto:support@increase.com) to ship cards
    internationally.
    """

    line2: str
    """The second line of the shipping address."""

    line3: str
    """The third line of the shipping address."""

    phone_number: str
    """The phone number of the recipient."""


class Shipment(TypedDict, total=False):
    address: Required[ShipmentAddress]
    """The address to where the card should be shipped."""

    method: Required[Literal["usps", "fedex_priority_overnight", "fedex_2_day", "dhl_worldwide_express"]]
    """The shipping method to use.

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
