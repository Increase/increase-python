# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "EntitySetupSubmissionCorporationSubmittedAddress",
    "EntitySetupSubmissionCorporationBeneficialOwners",
    "EntitySetupSubmissionCorporation",
    "EntitySetupSubmissionNaturalPersonSubmittedAddress",
    "EntitySetupSubmissionNaturalPerson",
    "EntitySetupSubmission",
    "Entity",
]


class EntitySetupSubmissionCorporationSubmittedAddress(BaseModel):
    city: str
    """The city."""

    line1: str
    """The first line."""

    line2: Optional[str]
    """The second line."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the US state
    of the address.
    """

    zip: str
    """The ZIP code."""


class EntitySetupSubmissionCorporationBeneficialOwners(BaseModel):
    submitted_address_city: Optional[str]
    """The city of the person's address."""

    submitted_address_line1: str
    """The first line of the person's address."""

    submitted_address_line2: Optional[str]
    """The second line of the person's address."""

    submitted_address_state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the person's
    US state of residence.
    """

    submitted_address_zip: str
    """The ZIP code of the person's address."""

    submitted_date_of_birth: str
    """The person's date of birth in YYYY-MM-DD format."""

    submitted_name: str
    """The person's name."""

    submitted_prong: Literal["ownership", "control"]
    """Why this person is considered a beneficial owner of the entity."""

    submitted_social_security_number_last4: str
    """The last 4 digits of the person's Social Security Number."""


class EntitySetupSubmissionCorporation(BaseModel):
    beneficial_owners: List[EntitySetupSubmissionCorporationBeneficialOwners]
    """The corporation's beneficial owners."""

    submitted_address: EntitySetupSubmissionCorporationSubmittedAddress
    """The corporation's address."""

    submitted_name: str
    """The corporation's name."""

    submitted_state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the
    corporation's state of incorporation.
    """

    submitted_tax_id: Optional[str]
    """The corporation's Employer Identification Number (EIN)."""

    submitted_website: Optional[str]
    """The corporation's website."""


class EntitySetupSubmissionNaturalPersonSubmittedAddress(BaseModel):
    city: str
    """The city."""

    line1: str
    """The first line."""

    line2: Optional[str]
    """The second line."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the US state
    of the address.
    """

    zip: str
    """The ZIP code."""


class EntitySetupSubmissionNaturalPerson(BaseModel):
    submitted_address: EntitySetupSubmissionNaturalPersonSubmittedAddress
    """The person's address."""

    submitted_date_of_birth: str
    """The person's date of birth in YYYY-MM-DD format."""

    submitted_name: str
    """The person's name."""

    submitted_social_security_number_last4: str
    """The last 4 digits of the person's social security number."""


class EntitySetupSubmission(BaseModel):
    corporation: Optional[EntitySetupSubmissionCorporation]
    """
    If the Entity has `structure: corporation`, this will contain the details that
    were submitted for that corporation.
    """

    natural_person: Optional[EntitySetupSubmissionNaturalPerson]
    """
    If the Entity has `structure: natural_person`, this will contain the details
    that were submitted for that person.
    """


class Entity(BaseModel):
    entity_setup_submission: Optional[EntitySetupSubmission]
    """The details that were submitted to create the entity.

    Note that for backwards compatibility reasons, additional undocumented keys may
    appear in this object. These should be treated as deprecated and will be removed
    in the future.
    """

    id: str
    """The entity's identifier."""

    name: str
    """The entity's name."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    establishment, incorporation, or residence.
    """

    structure: Literal["corporation", "natural_person"]
    """The entity's legal structure."""

    tax_id: Optional[str]
    """The tax ID such as a Social Security Number or Employer Identification Number."""

    type: Literal["entity"]
    """A constant representing the object's type.

    For this resource it will always be `entity`.
    """
