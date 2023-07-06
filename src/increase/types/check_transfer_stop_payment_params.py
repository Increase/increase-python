# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CheckTransferStopPaymentParams"]


class CheckTransferStopPaymentParams(TypedDict, total=False):
    reason: Literal["mail_delivery_failed", "unknown"]
    """The reason why this transfer should be stopped.

    - `mail_delivery_failed` - The check could not be delivered.
    - `unknown` - The check was stopped for another reason.
    """
