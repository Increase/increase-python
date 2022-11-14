# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["RealTimePaymentsTransferCreateInboundParams"]

class RealTimePaymentsTransferCreateInboundParams(TypedDict, total=False):
    account_number_id: Required[str]
    """
    The identifier of the Account Number the inbound Real Time Payments Transfer is
    for.
    """

    amount: Required[int]
    """The transfer amount in USD cents. Must be positive."""