# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BeneficialOwnerUpdateAddressParams", "Address"]


class BeneficialOwnerUpdateAddressParams(TypedDict, total=False):
    address: Required[Address]
    """The individual's physical address. Post Office Boxes are disallowed."""

    beneficial_owner_id: Required[str]
    """
    The identifying details of anyone controlling or owning 25% or more of the
    corporation.
    """

    entity_id: Required[str]
    """The identifier of the Entity to retrieve."""


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
