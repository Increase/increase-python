# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EntityUpdateBeneficialOwnerAddressParams", "Address"]


class EntityUpdateBeneficialOwnerAddressParams(TypedDict, total=False):
    address: Required[Address]
    """The individual's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

    beneficial_owner_id: Required[str]
    """
    The identifying details of anyone controlling or owning 25% or more of the
    corporation.
    """


class Address(TypedDict, total=False):
    city: Required[str]
    """The city, district, town, or village of the address."""

    country: Required[str]
    """The two-letter ISO 3166-1 alpha-2 code for the country of the address."""

    line1: Required[str]
    """The first line of the address. This is usually the street number and street."""

    line2: str
    """The second line of the address. This might be the floor or room number."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the US
    state, province, or region of the address. Required in certain countries.
    """

    zip: str
    """The ZIP or postal code of the address. Required in certain countries."""
