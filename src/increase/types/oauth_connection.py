# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OauthConnection"]


class OauthConnection(BaseModel):
    id: str
    """The OAuth Connection's identifier."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp when the OAuth
    Connection was created.
    """

    group_id: str
    """The identifier of the Group that has authorized your OAuth application."""

    status: Literal["active", "inactive"]
    """Whether the connection is active.

    - `active` - The OAuth connection is active.
    - `inactive` - The OAuth connection is permanently deactivated.
    """

    type: Literal["oauth_connection"]
    """A constant representing the object's type.

    For this resource it will always be `oauth_connection`.
    """
