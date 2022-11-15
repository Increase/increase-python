# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OauthConnection"]


class OauthConnection(BaseModel):
    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp when the OAuth
    Connection was created.
    """

    group_id: str
    """The identifier of the Group that has authorized your OAuth application."""

    id: str
    """The OAuth Connection's identifier."""

    status: Literal["active", "inactive"]
    """Whether the connection is active."""

    type: Literal["oauth_connection"]
    """A constant representing the object's type.

    For this resource it will always be `oauth_connection`.
    """
