# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "Entity",
    "Corporation",
    "CorporationAddress",
    "CorporationBeneficialOwner",
    "CorporationBeneficialOwnerIndividual",
    "CorporationBeneficialOwnerIndividualAddress",
    "CorporationBeneficialOwnerIndividualIdentification",
    "NaturalPerson",
    "NaturalPersonAddress",
    "NaturalPersonIdentification",
    "Joint",
    "JointIndividual",
    "JointIndividualAddress",
    "JointIndividualIdentification",
    "Trust",
    "TrustAddress",
    "TrustTrustee",
    "TrustTrusteeIndividual",
    "TrustTrusteeIndividualAddress",
    "TrustTrusteeIndividualIdentification",
    "TrustGrantor",
    "TrustGrantorAddress",
    "TrustGrantorIdentification",
    "SupplementalDocument",
]


class CorporationAddress(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str]
    """The second line of the address."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: str
    """The ZIP code of the address."""


class CorporationBeneficialOwnerIndividualAddress(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str]
    """The second line of the address."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: str
    """The ZIP code of the address."""


class CorporationBeneficialOwnerIndividualIdentification(BaseModel):
    method: Literal[
        "social_security_number", "individual_taxpayer_identification_number", "passport", "drivers_license", "other"
    ]
    """A method that can be used to verify the individual's identity."""

    number_last4: str
    """
    The last 4 digits of the identification number that can be used to verify the
    individual's identity.
    """


class CorporationBeneficialOwnerIndividual(BaseModel):
    address: CorporationBeneficialOwnerIndividualAddress
    """The person's address."""

    date_of_birth: date
    """The person's date of birth in YYYY-MM-DD format."""

    identification: CorporationBeneficialOwnerIndividualIdentification
    """A means of verifying the person's identity."""

    name: str
    """The person's legal name."""


class CorporationBeneficialOwner(BaseModel):
    company_title: Optional[str]
    """This person's role or title within the entity."""

    individual: CorporationBeneficialOwnerIndividual
    """Personal details for the beneficial owner."""

    prong: Literal["ownership", "control"]
    """Why this person is considered a beneficial owner of the entity."""


class Corporation(BaseModel):
    address: CorporationAddress
    """The corporation's address."""

    beneficial_owners: List[CorporationBeneficialOwner]
    """
    The identifying details of anyone controlling or owning 25% or more of the
    corporation.
    """

    incorporation_state: Optional[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the
    corporation's state of incorporation.
    """

    name: str
    """The legal name of the corporation."""

    tax_identifier: Optional[str]
    """The Employer Identification Number (EIN) for the corporation."""

    website: Optional[str]
    """The website of the corporation."""


class NaturalPersonAddress(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str]
    """The second line of the address."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: str
    """The ZIP code of the address."""


class NaturalPersonIdentification(BaseModel):
    method: Literal[
        "social_security_number", "individual_taxpayer_identification_number", "passport", "drivers_license", "other"
    ]
    """A method that can be used to verify the individual's identity."""

    number_last4: str
    """
    The last 4 digits of the identification number that can be used to verify the
    individual's identity.
    """


class NaturalPerson(BaseModel):
    address: NaturalPersonAddress
    """The person's address."""

    date_of_birth: date
    """The person's date of birth in YYYY-MM-DD format."""

    identification: NaturalPersonIdentification
    """A means of verifying the person's identity."""

    name: str
    """The person's legal name."""


class JointIndividualAddress(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str]
    """The second line of the address."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: str
    """The ZIP code of the address."""


class JointIndividualIdentification(BaseModel):
    method: Literal[
        "social_security_number", "individual_taxpayer_identification_number", "passport", "drivers_license", "other"
    ]
    """A method that can be used to verify the individual's identity."""

    number_last4: str
    """
    The last 4 digits of the identification number that can be used to verify the
    individual's identity.
    """


class JointIndividual(BaseModel):
    address: JointIndividualAddress
    """The person's address."""

    date_of_birth: date
    """The person's date of birth in YYYY-MM-DD format."""

    identification: JointIndividualIdentification
    """A means of verifying the person's identity."""

    name: str
    """The person's legal name."""


class Joint(BaseModel):
    individuals: List[JointIndividual]
    """The two individuals that share control of the entity."""

    name: str
    """The entity's name."""


class TrustAddress(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str]
    """The second line of the address."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: str
    """The ZIP code of the address."""


class TrustTrusteeIndividualAddress(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str]
    """The second line of the address."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: str
    """The ZIP code of the address."""


class TrustTrusteeIndividualIdentification(BaseModel):
    method: Literal[
        "social_security_number", "individual_taxpayer_identification_number", "passport", "drivers_license", "other"
    ]
    """A method that can be used to verify the individual's identity."""

    number_last4: str
    """
    The last 4 digits of the identification number that can be used to verify the
    individual's identity.
    """


class TrustTrusteeIndividual(BaseModel):
    address: TrustTrusteeIndividualAddress
    """The person's address."""

    date_of_birth: date
    """The person's date of birth in YYYY-MM-DD format."""

    identification: TrustTrusteeIndividualIdentification
    """A means of verifying the person's identity."""

    name: str
    """The person's legal name."""


class TrustTrustee(BaseModel):
    individual: Optional[TrustTrusteeIndividual]
    """The individual trustee of the trust.

    Will be present if the trustee's `structure` is equal to `individual`.
    """

    structure: Literal["individual"]
    """The structure of the trustee. Will always be equal to `individual`."""


class TrustGrantorAddress(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str]
    """The second line of the address."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: str
    """The ZIP code of the address."""


class TrustGrantorIdentification(BaseModel):
    method: Literal[
        "social_security_number", "individual_taxpayer_identification_number", "passport", "drivers_license", "other"
    ]
    """A method that can be used to verify the individual's identity."""

    number_last4: str
    """
    The last 4 digits of the identification number that can be used to verify the
    individual's identity.
    """


class TrustGrantor(BaseModel):
    address: TrustGrantorAddress
    """The person's address."""

    date_of_birth: date
    """The person's date of birth in YYYY-MM-DD format."""

    identification: TrustGrantorIdentification
    """A means of verifying the person's identity."""

    name: str
    """The person's legal name."""


class Trust(BaseModel):
    address: TrustAddress
    """The trust's address."""

    category: Literal["revocable", "irrevocable"]
    """Whether the trust is `revocable` or `irrevocable`."""

    formation_document_file_id: Optional[str]
    """The ID for the File containing the formation document of the trust."""

    formation_state: Optional[str]
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state in
    which the trust was formed.
    """

    grantor: Optional[TrustGrantor]
    """The grantor of the trust. Will be present if the `category` is `revocable`."""

    name: str
    """The trust's name"""

    tax_identifier: Optional[str]
    """The Employer Identification Number (EIN) of the trust itself."""

    trustees: List[TrustTrustee]
    """The trustees of the trust."""


class SupplementalDocument(BaseModel):
    file_id: str
    """The File containing the document."""


class Entity(BaseModel):
    corporation: Optional[Corporation]
    """Details of the corporation entity.

    Will be present if `structure` is equal to `corporation`.
    """

    description: Optional[str]
    """The entity's description for display purposes."""

    id: str
    """The entity's identifier."""

    joint: Optional[Joint]
    """Details of the joint entity.

    Will be present if `structure` is equal to `joint`.
    """

    natural_person: Optional[NaturalPerson]
    """Details of the natural person entity.

    Will be present if `structure` is equal to `natural_person`.
    """

    relationship: Literal["affiliated", "informational", "unaffiliated"]
    """The relationship between your group and the entity."""

    structure: Literal["corporation", "natural_person", "joint", "trust"]
    """The entity's legal structure."""

    supplemental_documents: List[SupplementalDocument]
    """Additional documentation associated with the entity."""

    trust: Optional[Trust]
    """Details of the trust entity.

    Will be present if `structure` is equal to `trust`.
    """

    type: Literal["entity"]
    """A constant representing the object's type.

    For this resource it will always be `entity`.
    """
