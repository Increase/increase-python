# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LimitCreateParams"]


class LimitCreateParams(TypedDict, total=False):
    metric: Required[Literal["count", "volume"]]
    """The metric for the limit.

    - `count` - The maximum number of debits allowed.
    - `volume` - The maximum volume of debits allowed in the minor unit of the
      model's currency.
    """

    model_id: Required[str]
    """
    The identifier of the Account, Account Number, or Card you wish to associate the
    limit with.
    """

    value: Required[int]
    """The value to test the limit against."""

    interval: Literal["transaction", "day", "week", "month", "year", "all_time"]
    """The interval for the metric. Required if `metric` is `count` or `volume`.

    - `transaction` - Enforce the limit per-transaction.
    - `day` - Enforce the limit based on the previous 24 hour period.
    - `week` - Enforce the limit based on the previous seven days.
    - `month` - Enforce the limit based on the previous month, going back to the
      current day in the previous month, or as close as possible given month length
      differences.
    - `year` - Enforce the limit based on the previous year.
    - `all_time` - Enforce the limit for all time.
    """
