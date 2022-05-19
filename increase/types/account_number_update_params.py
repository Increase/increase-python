# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AccountNumberUpdateParams"]


class AccountNumberUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """The name you choose for the Account Number."""

    status: Optional[Literal["active", "disabled", "canceled"]]
    """This indicates if transfers can be made to the Account Number."""
