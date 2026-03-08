# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InboundCheckDepositAdjustmentParams"]


class InboundCheckDepositAdjustmentParams(TypedDict, total=False):
    amount: int
    """The adjustment amount in cents.

    Defaults to the amount of the Inbound Check Deposit.
    """

    reason: Literal["late_return", "wrong_payee_credit", "adjusted_amount", "non_conforming_item", "paid"]
    """The reason for the adjustment. Defaults to `wrong_payee_credit`.

    - `late_return` - The return was initiated too late and the receiving
      institution has responded with a Late Return Claim.
    - `wrong_payee_credit` - The check was deposited to the wrong payee and the
      depositing institution has reimbursed the funds with a Wrong Payee Credit.
    - `adjusted_amount` - The check was deposited with a different amount than what
      was written on the check.
    - `non_conforming_item` - The recipient was not able to process the check. This
      usually happens for e.g., low quality images.
    - `paid` - The check has already been deposited elsewhere and so this is a
      duplicate.
    """
