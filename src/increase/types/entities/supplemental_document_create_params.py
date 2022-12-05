# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SupplementalDocumentCreateParams"]


class SupplementalDocumentCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """The identifier of the File containing the document."""
