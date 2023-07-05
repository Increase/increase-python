# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CheckTransferReturnParams"]


class CheckTransferReturnParams(TypedDict, total=False):
    reason: Required[Literal["mail_delivery_failure", "refused_by_recipient", "returned_not_authorized"]]
    """The reason why the Check Transfer was returned to Increase.

    - `mail_delivery_failure` - Mail delivery failed and the check was returned to
      sender.
    - `refused_by_recipient` - The check arrived and the recipient refused to
      deposit it.
    - `returned_not_authorized` - The check was fraudulently deposited and the
      transfer was returned to the Bank of First Deposit.
    """
