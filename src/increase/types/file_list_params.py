# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileListParams", "CreatedAt", "Purpose"]


class FileListParams(TypedDict, total=False):
    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    purpose: Purpose


class CreatedAt(TypedDict, total=False):
    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    on_or_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or after this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """

    on_or_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
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
                "trust_formation_document",
                "digital_wallet_artwork",
                "digital_wallet_app_icon",
                "physical_card_front",
                "physical_card_back",
                "physical_card_carrier",
                "document_request",
                "entity_supplemental_document",
                "export",
            ]
        ],
    },
    total=False,
)


class Purpose(_PurposeReservedKeywords, total=False):
    pass
