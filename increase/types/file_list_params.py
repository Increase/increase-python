# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["CreatedAt", "Purpose", "FileListParams"]


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


_PurposeReservedKeywords = TypedDict(
    "_PurposeReservedKeywords",
    {
        "in": List[
            Literal[
                "check_image_front",
                "check_image_back",
                "form_1099_int",
                "form_ss_4",
                "identity_document",
                "increase_statement",
                "other",
            ]
        ],
    },
    total=False,
)


class Purpose(_PurposeReservedKeywords):
    pass


class FileListParams(TypedDict, total=False):
    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    purpose: Purpose
