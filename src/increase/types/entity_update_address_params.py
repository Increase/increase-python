# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EntityUpdateAddressParams", "Address"]


class EntityUpdateAddressParams(TypedDict, total=False):
    address: Required[Address]
    """The entity's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """


class Address(TypedDict, total=False):
    city: Required[str]
    """The city of the address."""

    line1: Required[str]
    """The first line of the address. This is usually the street number and street."""

    state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: Required[str]
    """The ZIP code of the address."""

    line2: str
    """The second line of the address. This might be the floor or room number."""
