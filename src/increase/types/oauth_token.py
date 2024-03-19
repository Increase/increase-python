# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OAuthToken"]


class OAuthToken(BaseModel):
    access_token: str
    """
    You may use this token in place of an API key to make OAuth requests on a user's
    behalf.
    """

    token_type: Literal["bearer"]
    """The type of OAuth token."""

    type: Literal["oauth_token"]
    """A constant representing the object's type.

    For this resource it will always be `oauth_token`.
    """
