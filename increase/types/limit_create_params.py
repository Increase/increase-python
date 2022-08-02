# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LimitCreateParams"]


class LimitCreateParams(TypedDict, total=False):
    metric: Required[Literal["count", "volume"]]
    """The metric for the limit."""

    model_id: Required[str]
    """
    The identifier of the Account, Card, or Account Number you wish to associate the
    limit with.
    """

    value: Required[int]
    """The value to test the limit against."""

    interval: Literal["transaction", "day", "week", "month", "year", "all_time"]
    """The interval for the metric. Required if `metric` is `count` or `volume`."""
