# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RealTimePaymentsTransferCreateInboundParams"]


class RealTimePaymentsTransferCreateInboundParams(TypedDict, total=False):
    account_number_id: Required[str]
    """
    The identifier of the Account Number the inbound Real Time Payments Transfer is
    for.
    """

    amount: Required[int]
    """The transfer amount in USD cents. Must be positive."""

    debtor_account_number: str
    """The account number of the account that sent the transfer."""

    debtor_name: str
    """The name provided by the sender of the transfer."""

    debtor_routing_number: str
    """The routing number of the account that sent the transfer."""

    remittance_information: str
    """Additional information included with the transfer."""

    request_for_payment_id: str
    """
    The identifier of a pending Request for Payment that this transfer will fulfill.
    """
