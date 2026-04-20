# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    """Groups represent organizations using Increase.

    You can retrieve information about your own organization via the API. More commonly, OAuth platforms can retrieve information about the organizations that have granted them access. Learn more about OAuth [here](https://increase.com/documentation/oauth).
    """

    id: str
    """The Group identifier."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Group
    was created.
    """

    type: Literal["group"]
    """A constant representing the object's type.

    For this resource it will always be `group`.
    """
