# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BookkeepingAccountBalanceParams"]


class BookkeepingAccountBalanceParams(TypedDict, total=False):
    at_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The moment to query the balance at. If not set, returns the current balances."""
