# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BeneficialOwners", "EntityCreateCorporationParams"]


class BeneficialOwners(TypedDict, total=False):
    address_city: Required[str]
    """The city of the beneficial owner's address."""

    address_line1: Required[str]
    """The first line of the beneficial owner's address.

    This is usually the street number and street.
    """

    address_state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the beneficial owner's address.
    """

    address_zip: Required[str]
    """The ZIP code of the beneficial owner's address."""

    date_of_birth: Required[str]
    """
    The beneficial owner's date of birth in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    name: Required[str]
    """The beneficial owner's legal name."""

    prong: Required[Literal["ownership", "control"]]
    """Why this person is considered a beneficial owner of the entity."""

    social_security_number_last4: Required[str]
    """The last four digits of the beneficial owner's Social Security Number (SSN)."""

    address_line2: str
    """The second line of the beneficial owner's address.

    This might be the floor or room number.
    """


class EntityCreateCorporationParams(TypedDict, total=False):
    address_city: Required[str]
    """The city of the corporation's address."""

    address_line1: Required[str]
    """The first line of the corporation's address.

    This is usually the street number and street.
    """

    address_state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the corporation's address.
    """

    address_zip: Required[str]
    """The ZIP code of the corporation's address."""

    name: Required[str]
    """The legal name of the corporation."""

    state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the
    corporation's state of incorporation.
    """

    address_line2: str
    """The second line of the corporation's address.

    This might be the floor or room number.
    """

    beneficial_owners: List[BeneficialOwners]
    """The identifying details of anyone owning 25% or more of the corporation."""

    ss4_file_id: str
    """
    The identifier of the File containing the SS4 form submitted to the IRS
    (optional, must specify tax_id if absent).
    """

    tax_id: str
    """
    The Employer Identification Number (EIN) for the corporation (optional, must
    specify ss4_file_id if absent).
    """

    website: str
    """The website of the corporation."""
