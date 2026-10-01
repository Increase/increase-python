# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PhysicalCheckBatchCreateParams", "MailingAddress", "ReturnAddress"]


class PhysicalCheckBatchCreateParams(TypedDict, total=False):
    mailing_address: Required[MailingAddress]
    """Details for where the parcel will be mailed."""

    return_address: Required[ReturnAddress]
    """Details for where the parcel should return if it is unable to be delivered."""

    shipping_method: Literal["usps_first_class", "fedex_overnight"]
    """How to ship the batch.

    - `usps_first_class` - USPS First Class
    - `fedex_overnight` - FedEx Overnight
    """


class MailingAddress(TypedDict, total=False):
    """Details for where the parcel will be mailed."""

    city: Required[str]
    """The city of the destination address."""

    line1: Required[str]
    """The first line of the destination address."""

    name: Required[str]
    """The recipient at the destination address."""

    postal_code: Required[str]
    """The postal code of the destination address."""

    state: Required[str]
    """The US state of the destination address."""

    line2: str
    """The second line of the destination address."""

    phone: str
    """The phone number used for delivery issues at the destination address.

    Only used when `shipping_method` is `fedex_overnight`.
    """


class ReturnAddress(TypedDict, total=False):
    """Details for where the parcel should return if it is unable to be delivered."""

    city: Required[str]
    """The city of the return address."""

    line1: Required[str]
    """The first line of the return address."""

    name: Required[str]
    """The recipient at the return address."""

    postal_code: Required[str]
    """The postal code of the return address."""

    state: Required[str]
    """The US state of the return address."""

    line2: str
    """The second line of the return address."""

    phone: str
    """The phone number used for delivery issues at the return address.

    Only used when `shipping_method` is `fedex_overnight`.
    """
