# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EntityArchiveBeneficialOwnerParams"]


class EntityArchiveBeneficialOwnerParams(TypedDict, total=False):
    beneficial_owner_id: Required[str]
    """
    The identifying details of anyone controlling or owning 25% or more of the
    corporation.
    """
