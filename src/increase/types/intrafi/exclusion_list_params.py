# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExclusionListParams"]


class ExclusionListParams(TypedDict, total=False):
    cursor: str
    """Return the page of entries after this one."""

    entity_id: str
    """Filter IntraFi Exclusions for those belonging to the specified Entity."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """
