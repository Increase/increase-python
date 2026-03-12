# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "BeneficialOwnerUpdateParams",
    "Address",
    "Identification",
    "IdentificationDriversLicense",
    "IdentificationOther",
    "IdentificationPassport",
]


class BeneficialOwnerUpdateParams(TypedDict, total=False):
    address: Address
    """The individual's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

    confirmed_no_us_tax_id: bool
    """
    The identification method for an individual can only be a passport, driver's
    license, or other document if you've confirmed the individual does not have a US
    tax id (either a Social Security Number or Individual Taxpayer Identification
    Number).
    """

    identification: Identification
    """A means of verifying the person's identity."""

    name: str
    """The individual's legal name."""


class Address(TypedDict, total=False):
    """The individual's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

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


class IdentificationDriversLicense(TypedDict, total=False):
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the front of the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""

    back_file_id: str
    """The identifier of the File containing the back of the driver's license."""


class IdentificationOther(TypedDict, total=False):
    """Information about the identification document provided.

    Required if `method` is equal to `other`.
    """

    country: Required[str]
    """
    The two-character ISO 3166-1 code representing the country that issued the
    document (e.g., `US`).
    """

    description: Required[str]
    """A description of the document submitted."""

    file_id: Required[str]
    """The identifier of the File containing the front of the document."""

    back_file_id: str
    """The identifier of the File containing the back of the document.

    Not every document has a reverse side.
    """

    expiration_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The document's expiration date in YYYY-MM-DD format."""


class IdentificationPassport(TypedDict, total=False):
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """

    country: Required[str]
    """
    The two-character ISO 3166-1 code representing the country that issued the
    document (e.g., `US`).
    """

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class Identification(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A means of verifying the person's identity."""

    method: Required[
        Literal[
            "social_security_number",
            "individual_taxpayer_identification_number",
            "passport",
            "drivers_license",
            "other",
        ]
    ]
    """A method that can be used to verify the individual's identity.

    - `social_security_number` - A social security number.
    - `individual_taxpayer_identification_number` - An individual taxpayer
      identification number (ITIN).
    - `passport` - A passport number.
    - `drivers_license` - A driver's license number.
    - `other` - Another identifying document.
    """

    number: Required[str]
    """
    An identification number that can be used to verify the individual's identity,
    such as a social security number.
    """

    drivers_license: IdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    other: IdentificationOther
    """Information about the identification document provided.

    Required if `method` is equal to `other`.
    """

    passport: IdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """
