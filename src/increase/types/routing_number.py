# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RoutingNumber"]


class RoutingNumber(BaseModel):
    ach_transfers: Literal["supported", "not_supported"]
    """This routing number's support for ACH Transfers.

    - `supported` - The routing number can receive this transfer type.
    - `not_supported` - The routing number cannot receive this transfer type.
    """

    name: str
    """The name of the financial institution belonging to a routing number."""

    real_time_payments_transfers: Literal["supported", "not_supported"]
    """This routing number's support for Real Time Payments Transfers.

    - `supported` - The routing number can receive this transfer type.
    - `not_supported` - The routing number cannot receive this transfer type.
    """

    routing_number: str
    """The nine digit routing number identifier."""

    type: Literal["routing_number"]
    """A constant representing the object's type.

    For this resource it will always be `routing_number`.
    """

    wire_transfers: Literal["supported", "not_supported"]
    """This routing number's support for Wire Transfers.

    - `supported` - The routing number can receive this transfer type.
    - `not_supported` - The routing number cannot receive this transfer type.
    """
