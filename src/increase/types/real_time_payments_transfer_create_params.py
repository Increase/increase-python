# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RealTimePaymentsTransferCreateParams"]


class RealTimePaymentsTransferCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The transfer amount in USD cents.

    For Real-Time Payments transfers, must be positive.
    """

    creditor_name: Required[str]
    """The name of the transfer's recipient."""

    remittance_information: Required[str]
    """Unstructured information that will show on the recipient's bank statement."""

    source_account_number_id: Required[str]
    """The identifier of the Account Number from which to send the transfer."""

    debtor_name: str
    """The name of the transfer's sender.

    If not provided, defaults to the name of the account's entity.
    """

    destination_account_number: str
    """The destination account number."""

    destination_routing_number: str
    """
    The destination American Bankers' Association (ABA) Routing Transit Number
    (RTN).
    """

    external_account_id: str
    """The ID of an External Account to initiate a transfer to.

    If this parameter is provided, `destination_account_number` and
    `destination_routing_number` must be absent.
    """

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    ultimate_creditor_name: str
    """The name of the ultimate recipient of the transfer.

    Set this if the creditor is an intermediary receiving the payment for someone
    else.
    """

    ultimate_debtor_name: str
    """The name of the ultimate sender of the transfer.

    Set this if the funds are being sent on behalf of someone who is not the account
    holder at Increase.
    """
