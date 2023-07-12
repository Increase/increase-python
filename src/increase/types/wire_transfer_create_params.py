# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WireTransferCreateParams"]


class WireTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in cents."""

    beneficiary_name: Required[str]
    """The beneficiary's name."""

    message_to_recipient: Required[str]
    """The message that will show on the recipient's bank statement."""

    account_number: str
    """The account number for the destination account."""

    beneficiary_address_line1: str
    """The beneficiary's address line 1."""

    beneficiary_address_line2: str
    """The beneficiary's address line 2."""

    beneficiary_address_line3: str
    """The beneficiary's address line 3."""

    external_account_id: str
    """The ID of an External Account to initiate a transfer to.

    If this parameter is provided, `account_number` and `routing_number` must be
    absent.
    """

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    routing_number: str
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
    """

    unique_identifier: str
    """A unique identifier you choose for the transfer.

    Reusing this identifer for another transfer will result in an error. You can
    query for the transfer associated with this identifier using the List endpoint.
    """
