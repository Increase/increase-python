# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RoutingNumber"]


class RoutingNumber(BaseModel):
    name: str
    """The name of the financial institution belonging to a routing number."""

    routing_number: str
    """The nine digit routing number identifier."""

    type: Literal["routing_number"]
    """A constant representing the object's type.

    For this resource it will always be `routing_number`.
    """
