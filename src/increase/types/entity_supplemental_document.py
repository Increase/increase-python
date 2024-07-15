# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EntitySupplementalDocument"]


class EntitySupplementalDocument(BaseModel):
    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the
    Supplemental Document was created.
    """

    entity_id: str
    """The Entity the supplemental document is attached to."""

    file_id: str
    """The File containing the document."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    type: Literal["entity_supplemental_document"]
    """A constant representing the object's type.

    For this resource it will always be `entity_supplemental_document`.
    """
