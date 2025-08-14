# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardTokenCapabilities", "Route"]


class Route(BaseModel):
    cross_border_push_transfers: Literal["supported", "not_supported"]
    """Whether you can push funds to the card using cross-border Card Push Transfers.

    - `supported` - The capability is supported.
    - `not_supported` - The capability is not supported.
    """

    domestic_push_transfers: Literal["supported", "not_supported"]
    """Whether you can push funds to the card using domestic Card Push Transfers.

    - `supported` - The capability is supported.
    - `not_supported` - The capability is not supported.
    """

    route: Literal["visa", "mastercard"]
    """The card network route the capabilities apply to.

    - `visa` - Visa and Interlink
    - `mastercard` - Mastercard and Maestro
    """


class CardTokenCapabilities(BaseModel):
    routes: List[Route]
    """Each route represent a path e.g., a push transfer can take."""

    type: Literal["card_token_capabilities"]
    """A constant representing the object's type.

    For this resource it will always be `card_token_capabilities`.
    """
