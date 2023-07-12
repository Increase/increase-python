# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EntityCreateParams",
    "Corporation",
    "CorporationAddress",
    "CorporationBeneficialOwner",
    "CorporationBeneficialOwnerIndividual",
    "CorporationBeneficialOwnerIndividualAddress",
    "CorporationBeneficialOwnerIndividualIdentification",
    "CorporationBeneficialOwnerIndividualIdentificationDriversLicense",
    "CorporationBeneficialOwnerIndividualIdentificationOther",
    "CorporationBeneficialOwnerIndividualIdentificationPassport",
    "Joint",
    "JointIndividual",
    "JointIndividualAddress",
    "JointIndividualIdentification",
    "JointIndividualIdentificationDriversLicense",
    "JointIndividualIdentificationOther",
    "JointIndividualIdentificationPassport",
    "NaturalPerson",
    "NaturalPersonAddress",
    "NaturalPersonIdentification",
    "NaturalPersonIdentificationDriversLicense",
    "NaturalPersonIdentificationOther",
    "NaturalPersonIdentificationPassport",
    "SupplementalDocument",
    "Trust",
    "TrustAddress",
    "TrustTrustee",
    "TrustTrusteeIndividual",
    "TrustTrusteeIndividualAddress",
    "TrustTrusteeIndividualIdentification",
    "TrustTrusteeIndividualIdentificationDriversLicense",
    "TrustTrusteeIndividualIdentificationOther",
    "TrustTrusteeIndividualIdentificationPassport",
    "TrustGrantor",
    "TrustGrantorAddress",
    "TrustGrantorIdentification",
    "TrustGrantorIdentificationDriversLicense",
    "TrustGrantorIdentificationOther",
    "TrustGrantorIdentificationPassport",
]


class EntityCreateParams(TypedDict, total=False):
    relationship: Required[Literal["affiliated", "informational", "unaffiliated"]]
    """The relationship between your group and the entity.

    - `affiliated` - The entity is controlled by your group.
    - `informational` - The entity is for informational purposes only.
    - `unaffiliated` - The entity is not controlled by your group, but can still
      directly open accounts.
    """

    structure: Required[Literal["corporation", "natural_person", "joint", "trust"]]
    """The type of Entity to create.

    - `corporation` - A corporation.
    - `natural_person` - An individual person.
    - `joint` - Multiple individual people.
    - `trust` - A trust.
    """

    corporation: Corporation
    """Details of the corporation entity to create.

    Required if `structure` is equal to `corporation`.
    """

    description: str
    """The description you choose to give the entity."""

    joint: Joint
    """Details of the joint entity to create.

    Required if `structure` is equal to `joint`.
    """

    natural_person: NaturalPerson
    """Details of the natural person entity to create.

    Required if `structure` is equal to `natural_person`. Natural people entities
    should be submitted with `social_security_number` or
    `individual_taxpayer_identification_number` identification methods.
    """

    supplemental_documents: List[SupplementalDocument]
    """Additional documentation associated with the entity."""

    trust: Trust
    """Details of the trust entity to create.

    Required if `structure` is equal to `trust`.
    """


class CorporationAddress(TypedDict, total=False):
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


class CorporationBeneficialOwnerIndividualAddress(TypedDict, total=False):
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


class CorporationBeneficialOwnerIndividualIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the front of the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""

    back_file_id: str
    """The identifier of the File containing the back of the driver's license."""


class CorporationBeneficialOwnerIndividualIdentificationOther(TypedDict, total=False):
    country: Required[str]
    """
    The two-character ISO 3166-1 code representing the country that issued the
    document.
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


class CorporationBeneficialOwnerIndividualIdentificationPassport(TypedDict, total=False):
    country: Required[str]
    """The country that issued the passport."""

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class CorporationBeneficialOwnerIndividualIdentification(TypedDict, total=False):
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

    drivers_license: CorporationBeneficialOwnerIndividualIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    other: CorporationBeneficialOwnerIndividualIdentificationOther
    """Information about the identification document provided.

    Required if `method` is equal to `other`.
    """

    passport: CorporationBeneficialOwnerIndividualIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class CorporationBeneficialOwnerIndividual(TypedDict, total=False):
    address: Required[CorporationBeneficialOwnerIndividualAddress]
    """The individual's address."""

    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[CorporationBeneficialOwnerIndividualIdentification]
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


class CorporationBeneficialOwner(TypedDict, total=False):
    individual: Required[CorporationBeneficialOwnerIndividual]
    """Personal details for the beneficial owner."""

    prong: Required[Literal["ownership", "control"]]
    """Why this person is considered a beneficial owner of the entity.

    - `ownership` - A person with 25% or greater direct or indirect ownership of the
      entity.
    - `control` - A person who manages, directs, or has significant control of the
      entity.
    """

    company_title: str
    """This person's role or title within the entity."""


class Corporation(TypedDict, total=False):
    address: Required[CorporationAddress]
    """The corporation's address."""

    beneficial_owners: Required[List[CorporationBeneficialOwner]]
    """
    The identifying details of anyone controlling or owning 25% or more of the
    corporation.
    """

    name: Required[str]
    """The legal name of the corporation."""

    tax_identifier: Required[str]
    """The Employer Identification Number (EIN) for the corporation."""

    incorporation_state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the
    corporation's state of incorporation.
    """

    website: str
    """The website of the corporation."""


class JointIndividualAddress(TypedDict, total=False):
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


class JointIndividualIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the front of the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""

    back_file_id: str
    """The identifier of the File containing the back of the driver's license."""


class JointIndividualIdentificationOther(TypedDict, total=False):
    country: Required[str]
    """
    The two-character ISO 3166-1 code representing the country that issued the
    document.
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


class JointIndividualIdentificationPassport(TypedDict, total=False):
    country: Required[str]
    """The country that issued the passport."""

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class JointIndividualIdentification(TypedDict, total=False):
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

    drivers_license: JointIndividualIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    other: JointIndividualIdentificationOther
    """Information about the identification document provided.

    Required if `method` is equal to `other`.
    """

    passport: JointIndividualIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class JointIndividual(TypedDict, total=False):
    address: Required[JointIndividualAddress]
    """The individual's address."""

    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[JointIndividualIdentification]
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


class Joint(TypedDict, total=False):
    individuals: Required[List[JointIndividual]]
    """The two individuals that share control of the entity."""

    name: str
    """The name of the joint entity."""


class NaturalPersonAddress(TypedDict, total=False):
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


class NaturalPersonIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the front of the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""

    back_file_id: str
    """The identifier of the File containing the back of the driver's license."""


class NaturalPersonIdentificationOther(TypedDict, total=False):
    country: Required[str]
    """
    The two-character ISO 3166-1 code representing the country that issued the
    document.
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
    country: Required[str]
    """The country that issued the passport."""

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class NaturalPersonIdentification(TypedDict, total=False):
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
    address: Required[NaturalPersonAddress]
    """The individual's address."""

    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[NaturalPersonIdentification]
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


class SupplementalDocument(TypedDict, total=False):
    file_id: Required[str]
    """The identifier of the File containing the document."""


class TrustAddress(TypedDict, total=False):
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


class TrustTrusteeIndividualAddress(TypedDict, total=False):
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


class TrustTrusteeIndividualIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the front of the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""

    back_file_id: str
    """The identifier of the File containing the back of the driver's license."""


class TrustTrusteeIndividualIdentificationOther(TypedDict, total=False):
    country: Required[str]
    """
    The two-character ISO 3166-1 code representing the country that issued the
    document.
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


class TrustTrusteeIndividualIdentificationPassport(TypedDict, total=False):
    country: Required[str]
    """The country that issued the passport."""

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class TrustTrusteeIndividualIdentification(TypedDict, total=False):
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

    drivers_license: TrustTrusteeIndividualIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    other: TrustTrusteeIndividualIdentificationOther
    """Information about the identification document provided.

    Required if `method` is equal to `other`.
    """

    passport: TrustTrusteeIndividualIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class TrustTrusteeIndividual(TypedDict, total=False):
    address: Required[TrustTrusteeIndividualAddress]
    """The individual's address."""

    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[TrustTrusteeIndividualIdentification]
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


class TrustTrustee(TypedDict, total=False):
    structure: Required[Literal["individual"]]
    """The structure of the trustee.

    - `individual` - The trustee is an individual.
    """

    individual: TrustTrusteeIndividual
    """Details of the individual trustee.

    Required when the trustee `structure` is equal to `individual`.
    """


class TrustGrantorAddress(TypedDict, total=False):
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


class TrustGrantorIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the front of the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""

    back_file_id: str
    """The identifier of the File containing the back of the driver's license."""


class TrustGrantorIdentificationOther(TypedDict, total=False):
    country: Required[str]
    """
    The two-character ISO 3166-1 code representing the country that issued the
    document.
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


class TrustGrantorIdentificationPassport(TypedDict, total=False):
    country: Required[str]
    """The country that issued the passport."""

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class TrustGrantorIdentification(TypedDict, total=False):
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

    drivers_license: TrustGrantorIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    other: TrustGrantorIdentificationOther
    """Information about the identification document provided.

    Required if `method` is equal to `other`.
    """

    passport: TrustGrantorIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class TrustGrantor(TypedDict, total=False):
    address: Required[TrustGrantorAddress]
    """The individual's address."""

    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[TrustGrantorIdentification]
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


class Trust(TypedDict, total=False):
    address: Required[TrustAddress]
    """The trust's address."""

    category: Required[Literal["revocable", "irrevocable"]]
    """Whether the trust is `revocable` or `irrevocable`.

    Irrevocable trusts require their own Employer Identification Number. Revocable
    trusts require information about the individual `grantor` who created the trust.

    - `revocable` - The trust is revocable by the grantor.
    - `irrevocable` - The trust cannot be revoked.
    """

    name: Required[str]
    """The legal name of the trust."""

    trustees: Required[List[TrustTrustee]]
    """The trustees of the trust."""

    formation_document_file_id: str
    """The identifier of the File containing the formation document of the trust."""

    formation_state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state in
    which the trust was formed.
    """

    grantor: TrustGrantor
    """The grantor of the trust. Required if `category` is equal to `revocable`."""

    tax_identifier: str
    """The Employer Identification Number (EIN) for the trust.

    Required if `category` is equal to `irrevocable`.
    """
