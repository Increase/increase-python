# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SupplementalDocumentCreateParams"]


class SupplementalDocumentCreateParams(TypedDict, total=False):
    entity_id: Required[str]
    """The identifier of the Entity to associate with the supplemental document."""

    file_id: Required[str]
    """The identifier of the File containing the document."""
