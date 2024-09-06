# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..pending_transaction import PendingTransaction
from ..declined_transaction import DeclinedTransaction

__all__ = ["CardAuthorizationCreateResponse"]


class CardAuthorizationCreateResponse(BaseModel):
    declined_transaction: Optional[DeclinedTransaction] = None
    """
    If the authorization attempt fails, this will contain the resulting
    [Declined Transaction](#declined-transactions) object. The Declined
    Transaction's `source` will be of `category: card_decline`.
    """

    pending_transaction: Optional[PendingTransaction] = None
    """
    If the authorization attempt succeeds, this will contain the resulting Pending
    Transaction object. The Pending Transaction's `source` will be of
    `category: card_authorization`.
    """

    type: Literal["inbound_card_authorization_simulation_result"]
    """A constant representing the object's type.

    For this resource it will always be
    `inbound_card_authorization_simulation_result`.
    """
