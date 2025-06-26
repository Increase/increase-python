# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WireTransferCreateParams"]


class WireTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in USD cents."""

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

    inbound_wire_drawdown_request_id: str
    """
    The ID of an Inbound Wire Drawdown Request in response to which this transfer is
    being sent.
    """

    originator_address_line1: str
    """The originator's address line 1.

    This is only necessary if you're transferring from a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    originator_address_line2: str
    """The originator's address line 2.

    This is only necessary if you're transferring from a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    originator_address_line3: str
    """The originator's address line 3.

    This is only necessary if you're transferring from a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    originator_name: str
    """The originator's name.

    This is only necessary if you're transferring from a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    routing_number: str
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
    """

    source_account_number_id: str
    """The ID of an Account Number that will be passed to the wire's recipient"""
