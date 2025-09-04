# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EntityUpdateParams", "RiskRating", "ThirdPartyVerification"]


class EntityUpdateParams(TypedDict, total=False):
    risk_rating: RiskRating
    """
    An assessment of the entity’s potential risk of involvement in financial crimes,
    such as money laundering.
    """

    third_party_verification: ThirdPartyVerification
    """A reference to data stored in a third-party verification service.

    Your integration may or may not use this field.
    """


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
