# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InterestPaymentCreateParams"]


class InterestPaymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier of the Account the Interest Payment should be paid to is for."""

    amount: Required[int]
    """The interest amount in cents. Must be positive."""

    accrued_on_account_id: str
    """The identifier of the Account the Interest accrued on.

    Defaults to `account_id`.
    """

    period_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end of the interest period. If not provided, defaults to the current time."""

    period_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The start of the interest period.

    If not provided, defaults to the current time.
    """
