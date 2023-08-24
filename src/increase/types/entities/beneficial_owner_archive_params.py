# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BeneficialOwnerArchiveParams"]


class BeneficialOwnerArchiveParams(TypedDict, total=False):
    beneficial_owner_id: Required[str]
    """
    The identifying details of anyone controlling or owning 25% or more of the
    corporation.
    """

    entity_id: Required[str]
    """The identifier of the Entity to retrieve."""
