# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OAuthApplication"]


class OAuthApplication(BaseModel):
    id: str
    """The OAuth Application's identifier."""

    client_id: str
    """The OAuth Application's client_id.

    Use this to authenticate with the OAuth Application.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp when the OAuth
    Application was created.
    """

    deleted_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp when the OAuth
    Application was deleted.
    """

    name: Optional[str] = None
    """The name you chose for this OAuth Application."""

    status: Literal["active", "deleted"]
    """Whether the application is active.

    - `active` - The application is active and can be used by your users.
    - `deleted` - The application is deleted.
    """

    type: Literal["oauth_application"]
    """A constant representing the object's type.

    For this resource it will always be `oauth_application`.
    """
