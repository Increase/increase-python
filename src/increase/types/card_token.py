# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardToken"]


class CardToken(BaseModel):
    id: str
    """The Card Token's identifier."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the card token was created.
    """

    expiration_date: date
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the card
    expires.
    """

    last4: str
    """The last 4 digits of the card number."""

    length: int
    """The length of the card number."""

    prefix: str
    """The prefix of the card number, usually 8 digits."""

    type: Literal["card_token"]
    """A constant representing the object's type.

    For this resource it will always be `card_token`.
    """
