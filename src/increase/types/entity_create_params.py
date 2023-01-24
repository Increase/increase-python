# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CorporationAddress",
    "CorporationBeneficialOwnersIndividualAddress",
    "CorporationBeneficialOwnersIndividualIdentificationPassport",
    "CorporationBeneficialOwnersIndividualIdentificationDriversLicense",
    "CorporationBeneficialOwnersIndividualIdentification",
    "CorporationBeneficialOwnersIndividual",
    "CorporationBeneficialOwners",
    "Corporation",
    "NaturalPersonAddress",
    "NaturalPersonIdentificationPassport",
    "NaturalPersonIdentificationDriversLicense",
    "NaturalPersonIdentification",
    "NaturalPerson",
    "JointIndividualsAddress",
    "JointIndividualsIdentificationPassport",
    "JointIndividualsIdentificationDriversLicense",
    "JointIndividualsIdentification",
    "JointIndividuals",
    "Joint",
    "TrustAddress",
    "TrustTrusteesIndividualAddress",
    "TrustTrusteesIndividualIdentificationPassport",
    "TrustTrusteesIndividualIdentificationDriversLicense",
    "TrustTrusteesIndividualIdentification",
    "TrustTrusteesIndividual",
    "TrustTrustees",
    "TrustGrantorAddress",
    "TrustGrantorIdentificationPassport",
    "TrustGrantorIdentificationDriversLicense",
    "TrustGrantorIdentification",
    "TrustGrantor",
    "Trust",
    "SupplementalDocuments",
    "EntityCreateParams",
]


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


class CorporationBeneficialOwnersIndividualAddress(TypedDict, total=False):
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


class CorporationBeneficialOwnersIndividualIdentificationPassport(TypedDict, total=False):
    country: Required[str]
    """The country that issued the passport."""

    expiration_date: Required[str]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class CorporationBeneficialOwnersIndividualIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[str]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""


class CorporationBeneficialOwnersIndividualIdentification(TypedDict, total=False):
    method: Required[
        Literal["social_security_number", "individual_taxpayer_identification_number", "passport", "drivers_license"]
    ]
    """A method that can be used to verify the individual's identity."""

    number: Required[str]
    """
    An identification number that can be used to verify the individual's identity,
    such as a social security number.
    """

    drivers_license: CorporationBeneficialOwnersIndividualIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    passport: CorporationBeneficialOwnersIndividualIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class CorporationBeneficialOwnersIndividual(TypedDict, total=False):
    address: Required[CorporationBeneficialOwnersIndividualAddress]
    """The individual's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[CorporationBeneficialOwnersIndividualIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""

    confirmed_no_us_tax_id: bool
    """
    The identification method for an individual can only be a passport or driver's
    license if you've confirmed they do not have a US tax id (either a Social
    Security Number or Individual Taxpayer Identification Number).
    """


class CorporationBeneficialOwners(TypedDict, total=False):
    individual: Required[CorporationBeneficialOwnersIndividual]
    """Personal details for the beneficial owner."""

    prong: Required[Literal["ownership", "control"]]
    """Why this person is considered a beneficial owner of the entity."""

    company_title: str
    """This person's role or title within the entity."""


class Corporation(TypedDict, total=False):
    address: Required[CorporationAddress]
    """The corporation's address."""

    beneficial_owners: Required[List[CorporationBeneficialOwners]]
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


class NaturalPersonIdentificationPassport(TypedDict, total=False):
    country: Required[str]
    """The country that issued the passport."""

    expiration_date: Required[str]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class NaturalPersonIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[str]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""


class NaturalPersonIdentification(TypedDict, total=False):
    method: Required[
        Literal["social_security_number", "individual_taxpayer_identification_number", "passport", "drivers_license"]
    ]
    """A method that can be used to verify the individual's identity."""

    number: Required[str]
    """
    An identification number that can be used to verify the individual's identity,
    such as a social security number.
    """

    drivers_license: NaturalPersonIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    passport: NaturalPersonIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class NaturalPerson(TypedDict, total=False):
    address: Required[NaturalPersonAddress]
    """The individual's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[NaturalPersonIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""

    confirmed_no_us_tax_id: bool
    """
    The identification method for an individual can only be a passport or driver's
    license if you've confirmed they do not have a US tax id (either a Social
    Security Number or Individual Taxpayer Identification Number).
    """


class JointIndividualsAddress(TypedDict, total=False):
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


class JointIndividualsIdentificationPassport(TypedDict, total=False):
    country: Required[str]
    """The country that issued the passport."""

    expiration_date: Required[str]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class JointIndividualsIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[str]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""


class JointIndividualsIdentification(TypedDict, total=False):
    method: Required[
        Literal["social_security_number", "individual_taxpayer_identification_number", "passport", "drivers_license"]
    ]
    """A method that can be used to verify the individual's identity."""

    number: Required[str]
    """
    An identification number that can be used to verify the individual's identity,
    such as a social security number.
    """

    drivers_license: JointIndividualsIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    passport: JointIndividualsIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class JointIndividuals(TypedDict, total=False):
    address: Required[JointIndividualsAddress]
    """The individual's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[JointIndividualsIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""

    confirmed_no_us_tax_id: bool
    """
    The identification method for an individual can only be a passport or driver's
    license if you've confirmed they do not have a US tax id (either a Social
    Security Number or Individual Taxpayer Identification Number).
    """


class Joint(TypedDict, total=False):
    individuals: Required[List[JointIndividuals]]
    """The two individuals that share control of the entity."""

    name: str
    """The name of the joint entity."""


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


class TrustTrusteesIndividualAddress(TypedDict, total=False):
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


class TrustTrusteesIndividualIdentificationPassport(TypedDict, total=False):
    country: Required[str]
    """The country that issued the passport."""

    expiration_date: Required[str]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class TrustTrusteesIndividualIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[str]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""


class TrustTrusteesIndividualIdentification(TypedDict, total=False):
    method: Required[
        Literal["social_security_number", "individual_taxpayer_identification_number", "passport", "drivers_license"]
    ]
    """A method that can be used to verify the individual's identity."""

    number: Required[str]
    """
    An identification number that can be used to verify the individual's identity,
    such as a social security number.
    """

    drivers_license: TrustTrusteesIndividualIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    passport: TrustTrusteesIndividualIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class TrustTrusteesIndividual(TypedDict, total=False):
    address: Required[TrustTrusteesIndividualAddress]
    """The individual's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[TrustTrusteesIndividualIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""

    confirmed_no_us_tax_id: bool
    """
    The identification method for an individual can only be a passport or driver's
    license if you've confirmed they do not have a US tax id (either a Social
    Security Number or Individual Taxpayer Identification Number).
    """


class TrustTrustees(TypedDict, total=False):
    structure: Required[Literal["individual"]]
    """The structure of the trustee."""

    individual: TrustTrusteesIndividual
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


class TrustGrantorIdentificationPassport(TypedDict, total=False):
    country: Required[str]
    """The country that issued the passport."""

    expiration_date: Required[str]
    """The passport's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the passport."""


class TrustGrantorIdentificationDriversLicense(TypedDict, total=False):
    expiration_date: Required[str]
    """The driver's license's expiration date in YYYY-MM-DD format."""

    file_id: Required[str]
    """The identifier of the File containing the driver's license."""

    state: Required[str]
    """The state that issued the provided driver's license."""


class TrustGrantorIdentification(TypedDict, total=False):
    method: Required[
        Literal["social_security_number", "individual_taxpayer_identification_number", "passport", "drivers_license"]
    ]
    """A method that can be used to verify the individual's identity."""

    number: Required[str]
    """
    An identification number that can be used to verify the individual's identity,
    such as a social security number.
    """

    drivers_license: TrustGrantorIdentificationDriversLicense
    """Information about the United States driver's license used for identification.

    Required if `method` is equal to `drivers_license`.
    """

    passport: TrustGrantorIdentificationPassport
    """Information about the passport used for identification.

    Required if `method` is equal to `passport`.
    """


class TrustGrantor(TypedDict, total=False):
    address: Required[TrustGrantorAddress]
    """The individual's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[TrustGrantorIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""

    confirmed_no_us_tax_id: bool
    """
    The identification method for an individual can only be a passport or driver's
    license if you've confirmed they do not have a US tax id (either a Social
    Security Number or Individual Taxpayer Identification Number).
    """


class Trust(TypedDict, total=False):
    address: Required[TrustAddress]
    """The trust's address."""

    category: Required[Literal["revocable", "irrevocable"]]
    """Whether the trust is `revocable` or `irrevocable`.

    Irrevocable trusts require their own Employer Identification Number. Revocable
    trusts require information about the individual `grantor` who created the trust.
    """

    name: Required[str]
    """The legal name of the trust."""

    trustees: Required[List[TrustTrustees]]
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


class SupplementalDocuments(TypedDict, total=False):
    file_id: Required[str]
    """The identifier of the File containing the document."""


class EntityCreateParams(TypedDict, total=False):
    relationship: Required[Literal["affiliated", "informational", "unaffiliated"]]
    """The relationship between your group and the entity."""

    structure: Required[Literal["corporation", "natural_person", "joint", "trust"]]
    """The type of Entity to create."""

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

    Required if `structure` is equal to `natural_person`.
    """

    supplemental_documents: List[SupplementalDocuments]
    """Additional documentation associated with the entity."""

    trust: Trust
    """Details of the trust entity to create.

    Required if `structure` is equal to `trust`.
    """
