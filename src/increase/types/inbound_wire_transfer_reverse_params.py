# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InboundWireTransferReverseParams"]


class InboundWireTransferReverseParams(TypedDict, total=False):
    reason: Required[Literal["duplicate", "creditor_request", "transaction_forbidden", "fraud"]]
    """Reason for the reversal.

    - `duplicate` - The inbound wire transfer was a duplicate.
    - `creditor_request` - The recipient of the wire transfer requested the funds be
      returned to the sender.
    - `transaction_forbidden` - The account cannot currently receive inbound wires.
    - `fraud` - The inbound wire transfer was fraudulent.
    """

    amount: int
    """The amount to return, in USD cents.

    Defaults to the full amount of the Inbound Wire Transfer. A transfer can only be
    reversed once, so any amount you don't return now stays with the recipient.
    """
