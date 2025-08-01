# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .entity_supplemental_document import EntitySupplementalDocument

__all__ = [
    "Entity",
    "Corporation",
    "CorporationAddress",
    "CorporationBeneficialOwner",
    "CorporationBeneficialOwnerIndividual",
    "CorporationBeneficialOwnerIndividualAddress",
    "CorporationBeneficialOwnerIndividualIdentification",
    "GovernmentAuthority",
    "GovernmentAuthorityAddress",
    "GovernmentAuthorityAuthorizedPerson",
    "Joint",
    "JointIndividual",
    "JointIndividualAddress",
    "JointIndividualIdentification",
    "NaturalPerson",
    "NaturalPersonAddress",
    "NaturalPersonIdentification",
    "ThirdPartyVerification",
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

    line2: Optional[str] = None
    """The second line of the address."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: str
    """The ZIP code of the address."""


class CorporationBeneficialOwnerIndividualAddress(BaseModel):
    city: Optional[str] = None
    """The city, district, town, or village of the address."""

    country: str
    """The two-letter ISO 3166-1 alpha-2 code for the country of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str] = None
    """The second line of the address."""

    state: Optional[str] = None
    """
    The two-letter United States Postal Service (USPS) abbreviation for the US
    state, province, or region of the address.
    """

    zip: Optional[str] = None
    """The ZIP or postal code of the address."""


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
    beneficial_owner_id: str
    """The identifier of this beneficial owner."""

    company_title: Optional[str] = None
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

    incorporation_state: Optional[str] = None
    """
    The two-letter United States Postal Service (USPS) abbreviation for the
    corporation's state of incorporation.
    """

    industry_code: Optional[str] = None
    """
    The numeric North American Industry Classification System (NAICS) code submitted
    for the corporation.
    """

    name: str
    """The legal name of the corporation."""

    tax_identifier: Optional[str] = None
    """The Employer Identification Number (EIN) for the corporation."""

    website: Optional[str] = None
    """The website of the corporation."""


class GovernmentAuthorityAddress(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str] = None
    """The second line of the address."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """

    zip: str
    """The ZIP code of the address."""


class GovernmentAuthorityAuthorizedPerson(BaseModel):
    authorized_person_id: str
    """The identifier of this authorized person."""

    name: str
    """The person's legal name."""


class GovernmentAuthority(BaseModel):
    address: GovernmentAuthorityAddress
    """The government authority's address."""

    authorized_persons: List[GovernmentAuthorityAuthorizedPerson]
    """The identifying details of authorized persons of the government authority."""

    category: Literal["municipality", "state_agency", "state_government", "federal_agency"]
    """The category of the government authority.

    - `municipality` - A municipality.
    - `state_agency` - A state agency.
    - `state_government` - A state government.
    - `federal_agency` - A federal agency.
    """

    name: str
    """The government authority's name."""

    tax_identifier: Optional[str] = None
    """The Employer Identification Number (EIN) of the government authority."""

    website: Optional[str] = None
    """The government authority's website."""


class JointIndividualAddress(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str] = None
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

    line2: Optional[str] = None
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


class ThirdPartyVerification(BaseModel):
    reference: str
    """The reference identifier for the third party verification."""

    vendor: Literal["alloy", "middesk", "oscilar"]
    """The vendor that was used to perform the verification.

    - `alloy` - Alloy. See https://alloy.com for more information.
    - `middesk` - Middesk. See https://middesk.com for more information.
    - `oscilar` - Oscilar. See https://oscilar.com for more information.
    """


class TrustAddress(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str] = None
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

    line2: Optional[str] = None
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

    line2: Optional[str] = None
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
    individual: Optional[TrustTrusteeIndividual] = None
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

    formation_document_file_id: Optional[str] = None
    """The ID for the File containing the formation document of the trust."""

    formation_state: Optional[str] = None
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state in
    which the trust was formed.
    """

    grantor: Optional[TrustGrantor] = None
    """The grantor of the trust. Will be present if the `category` is `revocable`."""

    name: str
    """The trust's name."""

    tax_identifier: Optional[str] = None
    """The Employer Identification Number (EIN) of the trust itself."""

    trustees: List[TrustTrustee]
    """The trustees of the trust."""


class Entity(BaseModel):
    id: str
    """The entity's identifier."""

    corporation: Optional[Corporation] = None
    """Details of the corporation entity.

    Will be present if `structure` is equal to `corporation`.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Entity
    was created.
    """

    description: Optional[str] = None
    """The entity's description for display purposes."""

    details_confirmed_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the
    Entity's details were most recently confirmed.
    """

    government_authority: Optional[GovernmentAuthority] = None
    """Details of the government authority entity.

    Will be present if `structure` is equal to `government_authority`.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    joint: Optional[Joint] = None
    """Details of the joint entity.

    Will be present if `structure` is equal to `joint`.
    """

    natural_person: Optional[NaturalPerson] = None
    """Details of the natural person entity.

    Will be present if `structure` is equal to `natural_person`.
    """

    status: Literal["active", "archived", "disabled"]
    """The status of the entity.

    - `active` - The entity is active.
    - `archived` - The entity is archived, and can no longer be used to create
      accounts.
    - `disabled` - The entity is temporarily disabled and cannot be used for
      financial activity.
    """

    structure: Literal["corporation", "natural_person", "joint", "trust", "government_authority"]
    """The entity's legal structure.

    - `corporation` - A corporation.
    - `natural_person` - An individual person.
    - `joint` - Multiple individual people.
    - `trust` - A trust.
    - `government_authority` - A government authority.
    """

    supplemental_documents: List[EntitySupplementalDocument]
    """Additional documentation associated with the entity.

    This is limited to the first 10 documents for an entity. If an entity has more
    than 10 documents, use the GET /entity_supplemental_documents list endpoint to
    retrieve them.
    """

    third_party_verification: Optional[ThirdPartyVerification] = None
    """A reference to data stored in a third-party verification service.

    Your integration may or may not use this field.
    """

    trust: Optional[Trust] = None
    """Details of the trust entity.

    Will be present if `structure` is equal to `trust`.
    """

    type: Literal["entity"]
    """A constant representing the object's type.

    For this resource it will always be `entity`.
    """
