# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EntityCreateBeneficialOwnerParams",
    "BeneficialOwner",
    "BeneficialOwnerIndividual",
    "BeneficialOwnerIndividualAddress",
    "BeneficialOwnerIndividualIdentification",
    "BeneficialOwnerIndividualIdentificationDriversLicense",
    "BeneficialOwnerIndividualIdentificationOther",
    "BeneficialOwnerIndividualIdentificationPassport",
]


class EntityCreateBeneficialOwnerParams(TypedDict, total=False):
    beneficial_owner: Required[BeneficialOwner]
    """
    The identifying details of anyone controlling or owning 25% or more of the
    corporation.
    """


class BeneficialOwnerIndividualAddress(TypedDict, total=False):
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


class BeneficialOwnerIndividualIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the front of the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""

    back_file_id: str
    """The identifier of the File containing the back of the driver's license."""


class BeneficialOwnerIndividualIdentificationOther(TypedDict, total=False):
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


class BeneficialOwnerIndividualIdentificationPassport(TypedDict, total=False):
    country: Required[str]
    """
    The two-character ISO 3166-1 code representing the country that issued the
    document (e.g., `US`).
    """

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class BeneficialOwnerIndividualIdentification(TypedDict, total=False):
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

    drivers_license: BeneficialOwnerIndividualIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    other: BeneficialOwnerIndividualIdentificationOther
    """Information about the identification document provided.

    Required if `method` is equal to `other`.
    """

    passport: BeneficialOwnerIndividualIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class BeneficialOwnerIndividual(TypedDict, total=False):
    address: Required[BeneficialOwnerIndividualAddress]
    """The individual's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[BeneficialOwnerIndividualIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""

    confirmed_no_us_tax_id: bool
    """
    The identification method for an individual can only be a passport, driver's
    license, or other document if you've confirmed the individual does not have a US
    tax id (either a Social Security Number or Individual Taxpayer Identification
    Number).
    """


class BeneficialOwner(TypedDict, total=False):
    individual: Required[BeneficialOwnerIndividual]
    """Personal details for the beneficial owner."""

    prongs: Required[List[Literal["ownership", "control"]]]
    """Why this person is considered a beneficial owner of the entity.

    At least one option is required, if a person is both a control person and owner,
    submit an array containing both.
    """

    company_title: str
    """This person's role or title within the entity."""
