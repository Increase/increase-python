# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RealTimePaymentsRequestsForPaymentCancelParams"]


class RealTimePaymentsRequestsForPaymentCancelParams(TypedDict, total=False):
    additional_information: str
    """Additional information about the cancellation to pass on to the recipient bank."""

    reason: Literal["requested_by_customer", "paid_by_other_means", "duplicate", "wrong_amount"]
    """The reason the request for payment is being canceled.

    Defaults to `requested_by_customer`.

    - `requested_by_customer` - The creditor no longer wants to be paid. Corresponds
      to the Real-Time Payments reason code `CUST`.
    - `paid_by_other_means` - The requested payment has already been made through
      another channel. Corresponds to the Real-Time Payments reason code `UPAY`.
    - `duplicate` - The request for payment duplicated another request for payment.
      Corresponds to the Real-Time Payments reason code `DUPL`.
    - `wrong_amount` - The request for payment was sent for the wrong amount.
      Corresponds to the Real-Time Payments reason code `AM09`.
    """
