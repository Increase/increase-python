# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CorporationAddress",
    "CorporationBeneficialOwnersIndividualAddress",
    "CorporationBeneficialOwnersIndividualIdentification",
    "CorporationBeneficialOwnersIndividual",
    "CorporationBeneficialOwners",
    "Corporation",
    "NaturalPersonAddress",
    "NaturalPersonIdentification",
    "NaturalPerson",
    "JointIndividualsAddress",
    "JointIndividualsIdentification",
    "JointIndividuals",
    "Joint",
    "TrustAddress",
    "TrustTrusteesIndividualAddress",
    "TrustTrusteesIndividualIdentification",
    "TrustTrusteesIndividual",
    "TrustTrustees",
    "TrustGrantorAddress",
    "TrustGrantorIdentification",
    "TrustGrantor",
    "Trust",
    "SupplementalDocuments",
    "Entity",
]


class CorporationAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the address."""

    line1: Required[str]
    """The first line of the address."""

    line2: Required[Optional[str]]
    """The second line of the address."""

    state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: Required[str]
    """The ZIP code of the address."""


class CorporationBeneficialOwnersIndividualAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the address."""

    line1: Required[str]
    """The first line of the address."""

    line2: Required[Optional[str]]
    """The second line of the address."""

    state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: Required[str]
    """The ZIP code of the address."""


class CorporationBeneficialOwnersIndividualIdentification(TypedDict, total=False):
    method: Required[Literal["social_security_number", "individual_taxpayer_identification_number", "passport"]]
    """A method that can be used to verify the individual's identity."""

    number_last4: Required[str]
    """
    The last 4 digits of the identification number that can be used to verify the
    individual's identity.
    """


class CorporationBeneficialOwnersIndividual(TypedDict, total=False):
    address: Required[CorporationBeneficialOwnersIndividualAddress]
    """The person's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[CorporationBeneficialOwnersIndividualIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""


class CorporationBeneficialOwners(TypedDict, total=False):
    company_title: Required[Optional[str]]
    """This person's role or title within the entity."""

    individual: Required[CorporationBeneficialOwnersIndividual]
    """Personal details for the beneficial owner."""

    prong: Required[Literal["ownership", "control"]]
    """Why this person is considered a beneficial owner of the entity."""


class Corporation(TypedDict, total=False):
    address: Required[CorporationAddress]
    """The corporation's address."""

    beneficial_owners: Required[List[CorporationBeneficialOwners]]
    """
    The identifying details of anyone controlling or owning 25% or more of the
    corporation.
    """

    incorporation_state: Required[Optional[str]]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the
    corporation's state of incorporation.
    """

    name: Required[str]
    """The legal name of the corporation."""

    tax_identifier: Required[Optional[str]]
    """The Employer Identification Number (EIN) for the corporation."""

    website: Required[Optional[str]]
    """The website of the corporation."""


class NaturalPersonAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the address."""

    line1: Required[str]
    """The first line of the address."""

    line2: Required[Optional[str]]
    """The second line of the address."""

    state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: Required[str]
    """The ZIP code of the address."""


class NaturalPersonIdentification(TypedDict, total=False):
    method: Required[Literal["social_security_number", "individual_taxpayer_identification_number", "passport"]]
    """A method that can be used to verify the individual's identity."""

    number_last4: Required[str]
    """
    The last 4 digits of the identification number that can be used to verify the
    individual's identity.
    """


class NaturalPerson(TypedDict, total=False):
    address: Required[NaturalPersonAddress]
    """The person's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[NaturalPersonIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""


class JointIndividualsAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the address."""

    line1: Required[str]
    """The first line of the address."""

    line2: Required[Optional[str]]
    """The second line of the address."""

    state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: Required[str]
    """The ZIP code of the address."""


class JointIndividualsIdentification(TypedDict, total=False):
    method: Required[Literal["social_security_number", "individual_taxpayer_identification_number", "passport"]]
    """A method that can be used to verify the individual's identity."""

    number_last4: Required[str]
    """
    The last 4 digits of the identification number that can be used to verify the
    individual's identity.
    """


class JointIndividuals(TypedDict, total=False):
    address: Required[JointIndividualsAddress]
    """The person's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[JointIndividualsIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""


class Joint(TypedDict, total=False):
    individuals: Required[List[JointIndividuals]]
    """The two individuals that share control of the entity."""

    name: Required[str]
    """The entity's name."""


class TrustAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the address."""

    line1: Required[str]
    """The first line of the address."""

    line2: Required[Optional[str]]
    """The second line of the address."""

    state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: Required[str]
    """The ZIP code of the address."""


class TrustTrusteesIndividualAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the address."""

    line1: Required[str]
    """The first line of the address."""

    line2: Required[Optional[str]]
    """The second line of the address."""

    state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: Required[str]
    """The ZIP code of the address."""


class TrustTrusteesIndividualIdentification(TypedDict, total=False):
    method: Required[Literal["social_security_number", "individual_taxpayer_identification_number", "passport"]]
    """A method that can be used to verify the individual's identity."""

    number_last4: Required[str]
    """
    The last 4 digits of the identification number that can be used to verify the
    individual's identity.
    """


class TrustTrusteesIndividual(TypedDict, total=False):
    address: Required[TrustTrusteesIndividualAddress]
    """The person's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[TrustTrusteesIndividualIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""


class TrustTrustees(TypedDict, total=False):
    individual: Required[Optional[TrustTrusteesIndividual]]
    """The individual trustee of the trust.

    Will be present if the trustee's `structure` is equal to `individual`.
    """

    structure: Required[Literal["individual"]]
    """The structure of the trustee. Will always be equal to `individual`."""


class TrustGrantorAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the address."""

    line1: Required[str]
    """The first line of the address."""

    line2: Required[Optional[str]]
    """The second line of the address."""

    state: Required[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: Required[str]
    """The ZIP code of the address."""


class TrustGrantorIdentification(TypedDict, total=False):
    method: Required[Literal["social_security_number", "individual_taxpayer_identification_number", "passport"]]
    """A method that can be used to verify the individual's identity."""

    number_last4: Required[str]
    """
    The last 4 digits of the identification number that can be used to verify the
    individual's identity.
    """


class TrustGrantor(TypedDict, total=False):
    address: Required[TrustGrantorAddress]
    """The person's address."""

    date_of_birth: Required[str]
    """The person's date of birth in YYYY-MM-DD format."""

    identification: Required[TrustGrantorIdentification]
    """A means of verifying the person's identity."""

    name: Required[str]
    """The person's legal name."""


class Trust(TypedDict, total=False):
    address: Required[TrustAddress]
    """The trust's address."""

    category: Required[Literal["revocable", "irrevocable"]]
    """Whether the trust is `revocable` or `irrevocable`."""

    formation_document_file_id: Required[Optional[str]]
    """The ID for the File containing the formation document of the trust."""

    formation_state: Required[Optional[str]]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state in
    which the trust was formed.
    """

    grantor: Required[Optional[TrustGrantor]]
    """The grantor of the trust. Will be present if the `category` is `revocable`."""

    name: Required[str]
    """The trust's name"""

    tax_identifier: Required[Optional[str]]
    """The Employer Identification Number (EIN) of the trust itself."""

    trustees: Required[List[TrustTrustees]]
    """The trustees of the trust."""


class SupplementalDocuments(TypedDict, total=False):
    file_id: Required[str]
    """The File containing the document."""


class Entity(TypedDict, total=False):
    corporation: Required[Optional[Corporation]]
    """Details of the corporation entity.

    Will be present if `structure` is equal to `corporation`.
    """

    description: Required[Optional[str]]
    """The entity's description for display purposes."""

    id: Required[str]
    """The entity's identifier."""

    joint: Required[Optional[Joint]]
    """Details of the joint entity.

    Will be present if `structure` is equal to `joint`.
    """

    natural_person: Required[Optional[NaturalPerson]]
    """Details of the natural person entity.

    Will be present if `structure` is equal to `natural_person`.
    """

    relationship: Required[Literal["affiliated", "informational", "unaffiliated"]]
    """The relationship between your group and the entity."""

    structure: Required[Literal["corporation", "natural_person", "joint", "trust"]]
    """The entity's legal structure."""

    supplemental_documents: Required[List[SupplementalDocuments]]
    """Additional documentation associated with the entity."""

    trust: Required[Optional[Trust]]
    """Details of the trust entity.

    Will be present if `structure` is equal to `trust`.
    """

    type: Required[Literal["entity"]]
    """A constant representing the object's type.

    For this resource it will always be `entity`.
    """
