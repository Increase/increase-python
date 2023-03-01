# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document"]


class Document(BaseModel):
    category: Literal["form_1099_int"]
    """The type of document."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the
    Document was created.
    """

    entity_id: Optional[str]
    """The identifier of the Entity the document was generated for."""

    file_id: str
    """The identifier of the File containing the Document's contents."""

    id: str
    """The Document identifier."""

    type: Literal["document"]
    """A constant representing the object's type.

    For this resource it will always be `document`.
    """
