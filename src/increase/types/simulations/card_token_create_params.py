# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CardTokenCreateParams", "Capability"]


class CardTokenCreateParams(TypedDict, total=False):
    capabilities: Iterable[Capability]
    """The capabilities of the outbound card token."""

    expiration: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The expiration date of the card."""

    last4: str
    """The last 4 digits of the card number."""

    prefix: str
    """The prefix of the card number, usually the first 8 digits."""

    primary_account_number_length: int
    """The total length of the card number, including prefix and last4."""


class Capability(TypedDict, total=False):
    cross_border_push_transfers: Required[Literal["supported", "not_supported"]]
    """The cross-border push transfers capability.

    - `supported` - The capability is supported.
    - `not_supported` - The capability is not supported.
    """

    domestic_push_transfers: Required[Literal["supported", "not_supported"]]
    """The domestic push transfers capability.

    - `supported` - The capability is supported.
    - `not_supported` - The capability is not supported.
    """

    route: Required[Literal["visa", "mastercard"]]
    """The route of the capability.

    - `visa` - Visa and Interlink
    - `mastercard` - Mastercard and Maestro
    """
