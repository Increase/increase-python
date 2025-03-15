# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileLink"]


class FileLink(BaseModel):
    id: str
    """The File Link identifier."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the File
    Link was created.
    """

    expires_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the File
    Link will expire.
    """

    file_id: str
    """The identifier of the File the File Link points to."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    type: Literal["file_link"]
    """A constant representing the object's type.

    For this resource it will always be `file_link`.
    """

    unauthenticated_url: str
    """A URL where the File can be downloaded.

    The URL will expire after the `expires_at` time. This URL is unauthenticated and
    can be used to download the File without an Increase API key.
    """
