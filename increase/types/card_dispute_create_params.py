# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["CardDisputeCreateParams"]

class CardDisputeCreateParams(TypedDict, total=False):
    disputed_transaction_id: Required[str]
    """The Transaction you wish to dispute.

    This Transaction must have a `source_type` of `card_settlement`.
    """

    explanation: Required[str]
    """Why you are disputing this Transaction."""