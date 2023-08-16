# File generated from our OpenAPI spec by Stainless.

import typing_extensions
from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Limit"]


class Limit(BaseModel):
    id: str
    """The Limit identifier."""

    interval: Optional[Literal["transaction", "day", "week", "month", "year", "all_time"]]
    """The interval for the metric.

    This is required if `metric` is `count` or `volume`.

    - `transaction` - Enforce the Limit per-transaction.
    - `day` - Enforce the Limit based on the trailing 24 hour period.
    - `week` - Enforce the Limit based on the trailing seven days.
    - `month` - Enforce the Limit based on the trailing month, going back to the
      current day in the previous month, or as close as possible given month length
      differences.
    - `year` - Enforce the Limit based on the trailing 365 days.
    - `all_time` - Enforce the Limit for all time.
    """

    metric: Literal["count", "volume"]
    """The metric for the Limit.

    - `count` - The maximum number of debits allowed.
    - `volume` - The maximum volume of debits allowed in the minor unit of the
      model's currency.
    """

    resource_id: str = FieldInfo(alias="model_id")
    """The identifier of the Account Number, Account, or Card the Limit applies to."""

    resource_type: Literal["account", "account_number", "card"] = FieldInfo(alias="model_type")
    """The type of the model you wish to associate the Limit with.

    - `account` - Enforce the Limit for the entire account.
    - `account_number` - Enforce the Limit for this specific route.
    - `card` - Enforce the Limit for this specific card.
    """

    status: Literal["active", "inactive"]
    """The current status of the Limit.

    - `active` - The Limit is active.
    - `inactive` - The Limit is temporarily disabled.
    """

    type: Literal["limit"]
    """A constant representing the object's type.

    For this resource it will always be `limit`.
    """

    value: int
    """The value to evaluate the Limit against."""

    @property
    @typing_extensions.deprecated("The resource_id property should be used instead")
    def model_id(self) -> str:
        return self.resource_id

    @property
    @typing_extensions.deprecated("The resource_type property should be used instead")
    def model_type(self) -> Literal["account", "account_number", "card"]:
        return self.resource_type
