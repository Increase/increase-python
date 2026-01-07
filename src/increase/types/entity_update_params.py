# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EntityUpdateParams",
    "Corporation",
    "CorporationAddress",
    "GovernmentAuthority",
    "GovernmentAuthorityAddress",
    "NaturalPerson",
    "NaturalPersonAddress",
    "RiskRating",
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


class Corporation(TypedDict, total=False):
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

    name: str
    """The legal name of the corporation."""


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


class NaturalPerson(TypedDict, total=False):
    """Details of the natural person entity to update.

    If you specify this parameter and the entity is not a natural person, the request will fail.
    """

    address: NaturalPersonAddress
    """The entity's physical address.

    Mail receiving locations like PO Boxes and PMB's are disallowed.
    """

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


class ThirdPartyVerification(TypedDict, total=False):
    """
    If you are using a third-party service for identity verification, you can use this field to associate this Entity with the identifier that represents them in that service.
    """

    reference: Required[str]
    """The reference identifier for the third party verification."""

    vendor: Required[Literal["alloy", "middesk", "oscilar", "persona"]]
    """The vendor that was used to perform the verification.

    - `alloy` - Alloy. See https://alloy.com for more information.
    - `middesk` - Middesk. See https://middesk.com for more information.
    - `oscilar` - Oscilar. See https://oscilar.com for more information.
    - `persona` - Persona. See https://withpersona.com for more information.
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
