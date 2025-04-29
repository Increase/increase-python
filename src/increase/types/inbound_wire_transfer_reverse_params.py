# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InboundWireTransferReverseParams"]


class InboundWireTransferReverseParams(TypedDict, total=False):
    reason: Required[Literal["duplicate", "creditor_request"]]
    """Reason for the reversal.

    - `duplicate` - The inbound wire transfer was a duplicate.
    - `creditor_request` - The recipient of the wire transfer requested the funds be
      returned to the sender.
    """
