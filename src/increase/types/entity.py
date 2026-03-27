# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

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
    "CorporationLegalIdentifier",
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
    "RiskRating",
    "TermsAgreement",
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
    "Validation",
    "ValidationIssue",
    "ValidationIssueBeneficialOwnerAddress",
    "ValidationIssueBeneficialOwnerIdentity",
    "ValidationIssueEntityAddress",
    "ValidationIssueEntityTaxIdentifier",
]


class CorporationAddress(BaseModel):
    """The corporation's address."""

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


class CorporationBeneficialOwnerIndividualAddress(BaseModel):
    """The person's address."""

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
    """A means of verifying the person's identity."""

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

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class CorporationBeneficialOwnerIndividual(BaseModel):
    """Personal details for the beneficial owner."""

    address: CorporationBeneficialOwnerIndividualAddress
    """The person's address."""

    date_of_birth: date
    """The person's date of birth in YYYY-MM-DD format."""

    identification: CorporationBeneficialOwnerIndividualIdentification
    """A means of verifying the person's identity."""

    name: str
    """The person's legal name."""


class CorporationBeneficialOwner(BaseModel):
    id: str
    """The identifier of this beneficial owner."""

    company_title: Optional[str] = None
    """This person's role or title within the entity."""

    individual: CorporationBeneficialOwnerIndividual
    """Personal details for the beneficial owner."""

    prongs: List[Literal["ownership", "control"]]
    """Why this person is considered a beneficial owner of the entity."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class CorporationLegalIdentifier(BaseModel):
    """The legal identifier of the corporation."""

    category: Literal["us_employer_identification_number", "other"]
    """The category of the legal identifier.

    - `us_employer_identification_number` - The Employer Identification Number (EIN)
      for the company. The EIN is a 9-digit number assigned by the IRS.
    - `other` - A legal identifier issued by a foreign government, like a tax
      identification number or registration number.
    """

    value: str
    """The identifier of the legal identifier."""


class Corporation(BaseModel):
    """Details of the corporation entity.

    Will be present if `structure` is equal to `corporation`.
    """

    address: CorporationAddress
    """The corporation's address."""

    beneficial_owners: List[CorporationBeneficialOwner]
    """
    The identifying details of anyone controlling or owning 25% or more of the
    corporation.
    """

    email: Optional[str] = None
    """An email address for the business."""

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

    legal_identifier: Optional[CorporationLegalIdentifier] = None
    """The legal identifier of the corporation."""

    name: str
    """The legal name of the corporation."""

    website: Optional[str] = None
    """The website of the corporation."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class GovernmentAuthorityAddress(BaseModel):
    """The government authority's address."""

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


class GovernmentAuthorityAuthorizedPerson(BaseModel):
    authorized_person_id: str
    """The identifier of this authorized person."""

    name: str
    """The person's legal name."""


class GovernmentAuthority(BaseModel):
    """Details of the government authority entity.

    Will be present if `structure` is equal to `government_authority`.
    """

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
    """The person's address."""

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


class JointIndividualIdentification(BaseModel):
    """A means of verifying the person's identity."""

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

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


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
    """Details of the joint entity.

    Will be present if `structure` is equal to `joint`.
    """

    individuals: List[JointIndividual]
    """The two individuals that share control of the entity."""

    name: str
    """The entity's name."""


class NaturalPersonAddress(BaseModel):
    """The person's address."""

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


class NaturalPersonIdentification(BaseModel):
    """A means of verifying the person's identity."""

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

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class NaturalPerson(BaseModel):
    """Details of the natural person entity.

    Will be present if `structure` is equal to `natural_person`.
    """

    address: NaturalPersonAddress
    """The person's address."""

    date_of_birth: date
    """The person's date of birth in YYYY-MM-DD format."""

    identification: NaturalPersonIdentification
    """A means of verifying the person's identity."""

    name: str
    """The person's legal name."""


class RiskRating(BaseModel):
    """
    An assessment of the entity’s potential risk of involvement in financial crimes, such as money laundering.
    """

    rated_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the risk
    rating was performed.
    """

    rating: Literal["low", "medium", "high"]
    """The rating given to this entity.

    - `low` - Minimal risk of involvement in financial crime.
    - `medium` - Moderate risk of involvement in financial crime.
    - `high` - Elevated risk of involvement in financial crime.
    """


class TermsAgreement(BaseModel):
    agreed_at: datetime
    """The timestamp of when the Entity agreed to the terms."""

    ip_address: str
    """The IP address the Entity accessed reviewed the terms from."""

    terms_url: str
    """The URL of the terms agreement.

    This link will be provided by your bank partner.
    """


class ThirdPartyVerification(BaseModel):
    """
    If you are using a third-party service for identity verification, you can use this field to associate this Entity with the identifier that represents them in that service.
    """

    reference: str
    """The reference identifier for the third party verification."""

    vendor: Literal["alloy", "middesk", "oscilar", "persona", "taktile"]
    """The vendor that was used to perform the verification.

    - `alloy` - Alloy. See https://alloy.com for more information.
    - `middesk` - Middesk. See https://middesk.com for more information.
    - `oscilar` - Oscilar. See https://oscilar.com for more information.
    - `persona` - Persona. See https://withpersona.com for more information.
    - `taktile` - Taktile. See https://taktile.com for more information.
    """


class TrustAddress(BaseModel):
    """The trust's address."""

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


class TrustGrantorAddress(BaseModel):
    """The person's address."""

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


class TrustGrantorIdentification(BaseModel):
    """A means of verifying the person's identity."""

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

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class TrustGrantor(BaseModel):
    """The grantor of the trust. Will be present if the `category` is `revocable`."""

    address: TrustGrantorAddress
    """The person's address."""

    date_of_birth: date
    """The person's date of birth in YYYY-MM-DD format."""

    identification: TrustGrantorIdentification
    """A means of verifying the person's identity."""

    name: str
    """The person's legal name."""


class TrustTrusteeIndividualAddress(BaseModel):
    """The person's address."""

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


class TrustTrusteeIndividualIdentification(BaseModel):
    """A means of verifying the person's identity."""

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

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class TrustTrusteeIndividual(BaseModel):
    """The individual trustee of the trust.

    Will be present if the trustee's `structure` is equal to `individual`.
    """

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
    """Details of the trust entity.

    Will be present if `structure` is equal to `trust`.
    """

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


class ValidationIssueBeneficialOwnerAddress(BaseModel):
    """Details when the issue is with a beneficial owner's address."""

    beneficial_owner_id: str
    """The ID of the beneficial owner."""

    reason: Literal["mailbox_address"]
    """The reason the address is invalid.

    - `mailbox_address` - The address is a mailbox or other non-physical address.
    """


class ValidationIssueBeneficialOwnerIdentity(BaseModel):
    """Details when the issue is with a beneficial owner's identity verification."""

    beneficial_owner_id: str
    """The ID of the beneficial owner."""


class ValidationIssueEntityAddress(BaseModel):
    """Details when the issue is with the entity's address."""

    reason: Literal["mailbox_address"]
    """The reason the address is invalid.

    - `mailbox_address` - The address is a mailbox or other non-physical address.
    """


class ValidationIssueEntityTaxIdentifier(BaseModel):
    """Details when the issue is with the entity's tax ID."""

    pass


class ValidationIssue(BaseModel):
    beneficial_owner_address: Optional[ValidationIssueBeneficialOwnerAddress] = None
    """Details when the issue is with a beneficial owner's address."""

    beneficial_owner_identity: Optional[ValidationIssueBeneficialOwnerIdentity] = None
    """Details when the issue is with a beneficial owner's identity verification."""

    category: Literal[
        "entity_tax_identifier", "entity_address", "beneficial_owner_identity", "beneficial_owner_address"
    ]
    """The type of issue.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.

    - `entity_tax_identifier` - The entity's tax identifier could not be validated.
      Update the tax ID with the
      [update an entity API](/documentation/api/entities#update-an-entity.corporation.legal_identifier).
    - `entity_address` - The entity's address could not be validated. Update the
      address with the
      [update an entity API](/documentation/api/entities#update-an-entity.corporation.address).
    - `beneficial_owner_identity` - A beneficial owner's identity could not be
      verified. Update the identification with the
      [update a beneficial owner API](/documentation/api/beneficial-owners#update-a-beneficial-owner).
    - `beneficial_owner_address` - A beneficial owner's address could not be
      validated. Update the address with the
      [update a beneficial owner API](/documentation/api/beneficial-owners#update-a-beneficial-owner).
    """

    entity_address: Optional[ValidationIssueEntityAddress] = None
    """Details when the issue is with the entity's address."""

    entity_tax_identifier: Optional[ValidationIssueEntityTaxIdentifier] = None
    """Details when the issue is with the entity's tax ID."""


class Validation(BaseModel):
    """The validation results for the entity.

    Learn more about [validations](/documentation/entity-validation).
    """

    issues: List[ValidationIssue]
    """The list of issues that need to be addressed."""

    status: Literal["pending", "valid", "invalid"]
    """The validation status for the entity.

    If the status is `invalid`, the `issues` array will be populated.

    - `pending` - The submitted data is being validated.
    - `valid` - The submitted data is valid.
    - `invalid` - Additional information is required to validate the data.
    """


class Entity(BaseModel):
    """Entities are the legal entities that own accounts.

    They can be people, corporations, partnerships, government authorities, or trusts. To learn more, see [Entities](/documentation/entities).
    """

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

    risk_rating: Optional[RiskRating] = None
    """
    An assessment of the entity’s potential risk of involvement in financial crimes,
    such as money laundering.
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

    terms_agreements: List[TermsAgreement]
    """The terms that the Entity agreed to.

    Not all programs are required to submit this data.
    """

    third_party_verification: Optional[ThirdPartyVerification] = None
    """
    If you are using a third-party service for identity verification, you can use
    this field to associate this Entity with the identifier that represents them in
    that service.
    """

    trust: Optional[Trust] = None
    """Details of the trust entity.

    Will be present if `structure` is equal to `trust`.
    """

    type: Literal["entity"]
    """A constant representing the object's type.

    For this resource it will always be `entity`.
    """

    validation: Optional[Validation] = None
    """The validation results for the entity.

    Learn more about [validations](/documentation/entity-validation).
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
