# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InboundCheckDepositAdjustmentParams"]


class InboundCheckDepositAdjustmentParams(TypedDict, total=False):
    amount: int
    """The adjustment amount in cents.

    A positive amount means that the funds are being returned to you by the other
    bank and is a credit to your account, as happens for a `wrong_payee_credit`. A
    negative amount is a debit to your account, as happens for a `late_return`.
    Defaults to the amount of the Inbound Check Deposit.
    """

    reason: Literal["late_return", "wrong_payee_credit"]
    """The reason for the adjustment. Defaults to `wrong_payee_credit`.

    - `late_return` - The return was initiated too late and the receiving
      institution has responded with a Late Return Claim.
    - `wrong_payee_credit` - The check was deposited to the wrong payee and the
      depositing institution has reimbursed the funds with a Wrong Payee Credit.
    """
