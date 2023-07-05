# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import date, datetime
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
    "Joint",
    "JointIndividual",
    "JointIndividualAddress",
    "JointIndividualIdentification",
    "NaturalPerson",
    "NaturalPersonAddress",
    "NaturalPersonIdentification",
    "SupplementalDocument",
    "Trust",
    "TrustAddress",
    "TrustGrantor",
    "TrustGrantorAddress",
    "TrustGrantorIdentification",
    "TrustTrustee",
    "TrustTrusteeIndividual",
    "TrustTrusteeIndividualAddress",
    "TrustTrusteeIndividualIdentification",
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
    """A method that can be used to verify the individual's identity.

    - `social_security_number` - A social security number.
    - `individual_taxpayer_identification_number` - An individual taxpayer
      identification number (ITIN).
    - `passport` - A passport number.
    - `drivers_license` - A driver's license number.
    - `other` - Another identifying document.
    """

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
    """Why this person is considered a beneficial owner of the entity.

    - `ownership` - A person with 25% or greater direct or indirect ownership of the
      entity.
    - `control` - A person who manages, directs, or has significant control of the
      entity.
    """


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
    """A method that can be used to verify the individual's identity.

    - `social_security_number` - A social security number.
    - `individual_taxpayer_identification_number` - An individual taxpayer
      identification number (ITIN).
    - `passport` - A passport number.
    - `drivers_license` - A driver's license number.
    - `other` - Another identifying document.
    """

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
    """A method that can be used to verify the individual's identity.

    - `social_security_number` - A social security number.
    - `individual_taxpayer_identification_number` - An individual taxpayer
      identification number (ITIN).
    - `passport` - A passport number.
    - `drivers_license` - A driver's license number.
    - `other` - Another identifying document.
    """

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


class SupplementalDocument(BaseModel):
    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the
    Supplemental Document was created.
    """

    file_id: str
    """The File containing the document."""

    type: Literal["entity_supplemental_document"]
    """A constant representing the object's type.

    For this resource it will always be `entity_supplemental_document`.
    """


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
    """A method that can be used to verify the individual's identity.

    - `social_security_number` - A social security number.
    - `individual_taxpayer_identification_number` - An individual taxpayer
      identification number (ITIN).
    - `passport` - A passport number.
    - `drivers_license` - A driver's license number.
    - `other` - Another identifying document.
    """

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
    """A method that can be used to verify the individual's identity.

    - `social_security_number` - A social security number.
    - `individual_taxpayer_identification_number` - An individual taxpayer
      identification number (ITIN).
    - `passport` - A passport number.
    - `drivers_license` - A driver's license number.
    - `other` - Another identifying document.
    """

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
    """The structure of the trustee. Will always be equal to `individual`.

    - `individual` - The trustee is an individual.
    """


class Trust(BaseModel):
    address: TrustAddress
    """The trust's address."""

    category: Literal["revocable", "irrevocable"]
    """Whether the trust is `revocable` or `irrevocable`.

    - `revocable` - The trust is revocable by the grantor.
    - `irrevocable` - The trust cannot be revoked.
    """

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


class Entity(BaseModel):
    id: str
    """The entity's identifier."""

    corporation: Optional[Corporation]
    """Details of the corporation entity.

    Will be present if `structure` is equal to `corporation`.
    """

    description: Optional[str]
    """The entity's description for display purposes."""

    joint: Optional[Joint]
    """Details of the joint entity.

    Will be present if `structure` is equal to `joint`.
    """

    natural_person: Optional[NaturalPerson]
    """Details of the natural person entity.

    Will be present if `structure` is equal to `natural_person`.
    """

    relationship: Literal["affiliated", "informational", "unaffiliated"]
    """The relationship between your group and the entity.

    - `affiliated` - The entity is controlled by your group.
    - `informational` - The entity is for informational purposes only.
    - `unaffiliated` - The entity is not controlled by your group, but can still
      directly open accounts.
    """

    structure: Literal["corporation", "natural_person", "joint", "trust"]
    """The entity's legal structure.

    - `corporation` - A corporation.
    - `natural_person` - An individual person.
    - `joint` - Multiple individual people.
    - `trust` - A trust.
    """

    supplemental_documents: List[SupplementalDocument]
    """Additional documentation associated with the entity.

    This is limited to the first 10 documents for an entity. If an entity has more
    than 10 documents, use the GET /entity_supplemental_documents list endpoint to
    retrieve them.
    """

    trust: Optional[Trust]
    """Details of the trust entity.

    Will be present if `structure` is equal to `trust`.
    """

    type: Literal["entity"]
    """A constant representing the object's type.

    For this resource it will always be `entity`.
    """
