# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IntrafiExclusionCreateParams"]


class IntrafiExclusionCreateParams(TypedDict, total=False):
    bank_name: Required[str]
    """The name of the financial institution to be excluded."""

    entity_id: Required[str]
    """The identifier of the Entity whose deposits will be excluded."""
