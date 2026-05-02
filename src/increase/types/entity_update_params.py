# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EntityUpdateParams",
    "Corporation",
    "CorporationAddress",
    "CorporationLegalIdentifier",
    "GovernmentAuthority",
    "GovernmentAuthorityAddress",
    "NaturalPerson",
    "NaturalPersonAddress",
    "NaturalPersonIdentification",
    "NaturalPersonIdentificationDriversLicense",
    "NaturalPersonIdentificationOther",
    "NaturalPersonIdentificationPassport",
    "RiskRating",
    "TermsAgreement",
    "ThirdPartyVerification",
    "Trust",
    "TrustAddress",
]


class EntityUpdateParams(TypedDict, total=False):
    corporation: Corporation
    """Details of the corporation entity to update.

    If you specify this parameter and the entity is not a corporation, the request
    will fail.
    """

    details_confirmed_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When your user last confirmed the Entity's details.

    Depending on your program, you may be required to affirmatively confirm details
    with your users on an annual basis.
    """

    government_authority: GovernmentAuthority
    """Details of the government authority entity to update.

    If you specify this parameter and the entity is not a government authority, the
    request will fail.
    """

    natural_person: NaturalPerson
    """Details of the natural person entity to update.

    If you specify this parameter and the entity is not a natural person, the
    request will fail.
    """

    risk_rating: RiskRating
    """
    An assessment of the entity’s potential risk of involvement in financial crimes,
    such as money laundering.
    """

    terms_agreements: Iterable[TermsAgreement]
    """New terms that the Entity agreed to.

    Not all programs are required to submit this data. This will not archive
    previously submitted terms.
    """

    third_party_verification: ThirdPartyVerification
    """
    If you are using a third-party service for identity verification, you can use
    this field to associate this Entity with the identifier that represents them in
    that service.
    """

    trust: Trust
    """Details of the trust entity to update.

    If you specify this parameter and the entity is not a trust, the request will
    fail.
    """


class CorporationAddress(TypedDict, total=False):
    """The entity's physical address.

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


class CorporationLegalIdentifier(TypedDict, total=False):
    """The legal identifier of the corporation.

    This is usually the Employer Identification Number (EIN).
    """

    value: Required[str]
    """The identifier of the legal identifier.

    For US Employer Identification Numbers, submit nine digits with no dashes or
    other separators.
    """

    category: Literal["us_employer_identification_number", "other"]
    """The category of the legal identifier.

    - `us_employer_identification_number` - The Employer Identification Number (EIN)
      for the company. The EIN is a 9-digit number assigned by the IRS; submit it as
      nine digits with no dashes or other separators.
    - `other` - A legal identifier issued by a foreign government, like a tax
      identification number or registration number.
    """


class Corporation(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Details of the corporation entity to update.

    If you specify this parameter and the entity is not a corporation, the request will fail.
    """

    address: CorporationAddress
    """The entity's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

    email: str
    """An email address for the business.

    Not every program requires an email for submitted Entities.
    """

    incorporation_state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the
    corporation's state of incorporation.
    """

    industry_code: str
    """
    The North American Industry Classification System (NAICS) code for the
    corporation's primary line of business. This is a number, like `5132` for
    `Software Publishers`. A full list of classification codes is available
    [here](https://increase.com/documentation/data-dictionary#north-american-industry-classification-system-codes).
    """

    legal_identifier: CorporationLegalIdentifier
    """The legal identifier of the corporation.

    This is usually the Employer Identification Number (EIN).
    """

    name: str
    """The legal name of the corporation."""

    website: str
    """A website for the business.

    Not every program requires a website for submitted Entities.
    """


class GovernmentAuthorityAddress(TypedDict, total=False):
    """The entity's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

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


class GovernmentAuthority(TypedDict, total=False):
    """Details of the government authority entity to update.

    If you specify this parameter and the entity is not a government authority, the request will fail.
    """

    address: GovernmentAuthorityAddress
    """The entity's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

    name: str
    """The legal name of the government authority."""


class NaturalPersonAddress(TypedDict, total=False):
    """The entity's physical address.

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


class NaturalPersonIdentificationDriversLicense(TypedDict, total=False):
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


class NaturalPersonIdentificationOther(TypedDict, total=False):
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


class NaturalPersonIdentificationPassport(TypedDict, total=False):
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


class NaturalPersonIdentification(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    such as a social security number. For Social Security Numbers and Individual
    Taxpayer Identification Numbers, submit nine digits with no dashes or other
    separators.
    """

    drivers_license: NaturalPersonIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    other: NaturalPersonIdentificationOther
    """Information about the identification document provided.

    Required if `method` is equal to `other`.
    """

    passport: NaturalPersonIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class NaturalPerson(TypedDict, total=False):
    """Details of the natural person entity to update.

    If you specify this parameter and the entity is not a natural person, the request will fail.
    """

    address: NaturalPersonAddress
    """The entity's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

    confirmed_no_us_tax_id: bool
    """
    The identification method for an individual can only be a passport, driver's
    license, or other document if you've confirmed the individual does not have a US
    tax id (either a Social Security Number or Individual Taxpayer Identification
    Number).
    """

    identification: NaturalPersonIdentification
    """A means of verifying the person's identity."""

    name: str
    """The legal name of the natural person."""


class RiskRating(TypedDict, total=False):
    """
    An assessment of the entity’s potential risk of involvement in financial crimes, such as money laundering.
    """

    rated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the risk
    rating was performed.
    """

    rating: Required[Literal["low", "medium", "high"]]
    """The rating given to this entity.

    - `low` - Minimal risk of involvement in financial crime.
    - `medium` - Moderate risk of involvement in financial crime.
    - `high` - Elevated risk of involvement in financial crime.
    """


class TermsAgreement(TypedDict, total=False):
    agreed_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp of when the Entity agreed to the terms."""

    ip_address: Required[str]
    """The IP address the Entity accessed reviewed the terms from."""

    terms_url: Required[str]
    """The URL of the terms agreement.

    This link will be provided by your bank partner.
    """


class ThirdPartyVerification(TypedDict, total=False):
    """
    If you are using a third-party service for identity verification, you can use this field to associate this Entity with the identifier that represents them in that service.
    """

    reference: Required[str]
    """The reference identifier for the third party verification."""

    vendor: Required[Literal["alloy", "middesk", "oscilar", "persona", "taktile"]]
    """The vendor that was used to perform the verification.

    - `alloy` - Alloy. See https://alloy.com for more information.
    - `middesk` - Middesk. See https://middesk.com for more information.
    - `oscilar` - Oscilar. See https://oscilar.com for more information.
    - `persona` - Persona. See https://withpersona.com for more information.
    - `taktile` - Taktile. See https://taktile.com for more information.
    """


class TrustAddress(TypedDict, total=False):
    """The entity's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

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


class Trust(TypedDict, total=False):
    """Details of the trust entity to update.

    If you specify this parameter and the entity is not a trust, the request will fail.
    """

    address: TrustAddress
    """The entity's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

    name: str
    """The legal name of the trust."""
