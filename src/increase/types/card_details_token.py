# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardDetailsToken"]


class CardDetailsToken(BaseModel):
    """
    A short-lived token that authorizes Increase Card Elements to render the details of a single Card.
    """

    token: str
    """The token.

    Pass this to the `@increasebank/card-elements` library in your frontend. Treat
    it as a credential: it authorizes anyone holding it to read the Card's details
    until it expires.
    """

    expires_at: datetime
    """The time the token will expire. Tokens are valid for one hour."""

    type: Literal["card_details_token"]
    """A constant representing the object's type.

    For this resource it will always be `card_details_token`.
    """
