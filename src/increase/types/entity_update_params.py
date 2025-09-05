# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EntityUpdateParams",
    "Corporation",
    "GovernmentAuthority",
    "NaturalPerson",
    "RiskRating",
    "ThirdPartyVerification",
    "Trust",
]


class EntityUpdateParams(TypedDict, total=False):
    corporation: Corporation
    """Details of the corporation entity to update.

    If you specify this parameter and the entity is not a corporation, the request
    will fail.
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
    """A reference to data stored in a third-party verification service.

    Your integration may or may not use this field.
    """

    trust: Trust
    """Details of the trust entity to update.

    If you specify this parameter and the entity is not a trust, the request will
    fail.
    """


class Corporation(TypedDict, total=False):
    name: str
    """The legal name of the corporation."""


class GovernmentAuthority(TypedDict, total=False):
    name: str
    """The legal name of the government authority."""


class NaturalPerson(TypedDict, total=False):
    name: str
    """The legal name of the natural person."""


class RiskRating(TypedDict, total=False):
    rated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the risk
    rating was performed.
    """

    rating: Required[Literal["low", "medium", "high"]]
    """The rating given to this entity.

    - `low` - Low
    - `medium` - Medium
    - `high` - High
    """


class ThirdPartyVerification(TypedDict, total=False):
    reference: Required[str]
    """The reference identifier for the third party verification."""

    vendor: Required[Literal["alloy", "middesk", "oscilar"]]
    """The vendor that was used to perform the verification.

    - `alloy` - Alloy. See https://alloy.com for more information.
    - `middesk` - Middesk. See https://middesk.com for more information.
    - `oscilar` - Oscilar. See https://oscilar.com for more information.
    """


class Trust(TypedDict, total=False):
    name: str
    """The legal name of the trust."""
