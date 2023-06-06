# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SupplementalDocument"]


class SupplementalDocument(BaseModel):
    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the
    Supplemental Document was created.
    """

    file_id: str
    """The File containing the document."""

    type: Literal["entity_supplemental_document"]
    """A constant representing the object's type.

    For this resource it will always be `entity_supplemental_document`.
    """
