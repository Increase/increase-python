# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["CardSettlementParams"]

class CardSettlementParams(TypedDict, total=False):
    card_id: Required[str]
    """The identifier of the Card to create a settlement on."""

    pending_transaction_id: Required[str]
    """
    The identifier of the Pending Transaction for the Card Authorization you wish to
    settle.
    """

    amount: int
    """The amount to be settled.

    This defaults to the amount of the Pending Transaction being settled.
    """