# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CardDetailCreateDetailsIframeParams"]


class CardDetailCreateDetailsIframeParams(TypedDict, total=False):
    physical_card_id: str
    """The identifier of the Physical Card to retrieve details for."""
