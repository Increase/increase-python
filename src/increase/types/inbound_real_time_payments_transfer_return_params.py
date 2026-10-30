# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InboundRealTimePaymentsTransferReturnParams"]


class InboundRealTimePaymentsTransferReturnParams(TypedDict, total=False):
    amount: int
    """The amount to return, in USD cents.

    Defaults to the full amount of the Inbound Real-Time Payments Transfer, and
    can't be higher than it.
    """
