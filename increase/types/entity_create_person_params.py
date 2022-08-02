# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EntityCreatePersonParams"]


class EntityCreatePersonParams(TypedDict, total=False):
    address_city: Required[str]
    """The city of the person's address."""

    address_line1: Required[str]
    """The first line of the person's address.

    This is usually the street number and street.
    """

    address_state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the person's address.
    """

    address_zip: Required[str]
    """The ZIP code of the person's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    name: Required[str]
    """The person's legal name."""

    social_security_number_last4: Required[str]
    """The last four digits of the person's Social Security Number (SSN)."""

    address_line2: str
    """The second line of the person's address.

    This might be the floor or room number.
    """
