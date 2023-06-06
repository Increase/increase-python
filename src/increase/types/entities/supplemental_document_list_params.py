# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SupplementalDocumentListParams"]


class SupplementalDocumentListParams(TypedDict, total=False):
    entity_id: Required[str]
    """The identifier of the Entity to list supplemental documents for."""

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """
