# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CheckTransferStopPaymentParams"]


class CheckTransferStopPaymentParams(TypedDict, total=False):
    reason: Literal["mail_delivery_failed", "not_authorized", "valid_until_date_passed", "unknown"]
    """The reason why this transfer should be stopped.

    - `mail_delivery_failed` - The check could not be delivered.
    - `not_authorized` - The check was not authorized.
    - `valid_until_date_passed` - The check was stopped for `valid_until_date` being
      in the past.
    - `unknown` - The check was stopped for another reason.
    """
