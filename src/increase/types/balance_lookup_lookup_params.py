# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BalanceLookupLookupParams"]


class BalanceLookupLookupParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account to query the balance for."""
