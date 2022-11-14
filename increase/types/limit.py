# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Limit"]


class Limit(BaseModel):
    id: str
    """The Limit identifier."""

    interval: Optional[Literal["transaction", "day", "week", "month", "year", "all_time"]]
    """The interval for the metric.

    This is required if `metric` is `count` or `volume`.
    """

    metric: Literal["count", "volume"]
    """The metric for the Limit."""

    model_id: str
    """The identifier of the Account Number or Account the Limit applies to."""

    model_type: Literal["account", "account_number"]
    """The type of the model you wish to associate the Limit with."""

    status: Literal["active", "inactive"]
    """The current status of the Limit."""

    type: Literal["limit"]
    """A constant representing the object's type.

    For this resource it will always be `limit`.
    """

    value: int
    """The value to evaluate the Limit against."""
