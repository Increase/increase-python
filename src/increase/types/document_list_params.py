# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["Category", "CreatedAt", "DocumentListParams"]

_CategoryReservedKeywords = TypedDict(
    "_CategoryReservedKeywords",
    {
        "in": List[Literal["form_1099_int"]],
    },
    total=False,
)


class Category(_CategoryReservedKeywords):
    pass


class CreatedAt(TypedDict, total=False):
    after: str
    """
    Return results after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    before: str
    """
    Return results before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    on_or_after: str
    """
    Return results on or after this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """

    on_or_before: str
    """
    Return results on or before this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """


class DocumentListParams(TypedDict, total=False):
    category: Category

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    entity_id: str
    """Filter Documents to ones belonging to the specified Entity."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """
