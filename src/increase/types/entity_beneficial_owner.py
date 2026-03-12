# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EntityBeneficialOwner", "Individual", "IndividualAddress", "IndividualIdentification"]


class IndividualAddress(BaseModel):
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


class IndividualIdentification(BaseModel):
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


class Individual(BaseModel):
    """Personal details for the beneficial owner."""

    address: IndividualAddress
    """The person's address."""

    date_of_birth: date
    """The person's date of birth in YYYY-MM-DD format."""

    identification: IndividualIdentification
    """A means of verifying the person's identity."""

    name: str
    """The person's legal name."""


class EntityBeneficialOwner(BaseModel):
    """
    Beneficial owners are the individuals who control or own 25% or more of a `corporation` entity. Beneficial owners are always people, and never organizations. Generally, you will need to submit between 1 and 5 beneficial owners for every `corporation` entity. You should update and archive beneficial owners for a corporation entity as their details change.
    """

    id: str
    """The identifier of this beneficial owner."""

    company_title: Optional[str] = None
    """This person's role or title within the entity."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the
    Beneficial Owner was created.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    individual: Individual
    """Personal details for the beneficial owner."""

    prongs: List[Literal["ownership", "control"]]
    """Why this person is considered a beneficial owner of the entity."""

    type: Literal["entity_beneficial_owner"]
    """A constant representing the object's type.

    For this resource it will always be `entity_beneficial_owner`.
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
