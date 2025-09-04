# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EntityUpdateParams", "RiskRating"]


class EntityUpdateParams(TypedDict, total=False):
    risk_rating: RiskRating
    """
    An assessment of the entity’s potential risk of involvement in financial crimes,
    such as money laundering.
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
