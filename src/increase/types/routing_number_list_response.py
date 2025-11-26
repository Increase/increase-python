# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RoutingNumberListResponse", "Data"]


class Data(BaseModel):
    ach_transfers: Literal["supported", "not_supported"]
    """This routing number's support for ACH Transfers.

    - `supported` - The routing number can receive this transfer type.
    - `not_supported` - The routing number cannot receive this transfer type.
    """

    fednow_transfers: Literal["supported", "not_supported"]
    """This routing number's support for FedNow Transfers.

    - `supported` - The routing number can receive this transfer type.
    - `not_supported` - The routing number cannot receive this transfer type.
    """

    name: str
    """The name of the financial institution belonging to a routing number."""

    real_time_payments_transfers: Literal["supported", "not_supported"]
    """This routing number's support for Real-Time Payments Transfers.

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


class RoutingNumberListResponse(BaseModel):
    data: List[Data]
    """The contents of the list."""

    next_cursor: Optional[str] = None
    """A pointer to a place in the list."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
