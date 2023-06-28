# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Program"]


class Program(BaseModel):
    id: str
    """The Program identifier."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Program
    was created.
    """

    name: str
    """The name of the Program."""

    type: Literal["program"]
    """A constant representing the object's type.

    For this resource it will always be `program`.
    """

    updated_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Program
    was last updated.
    """
