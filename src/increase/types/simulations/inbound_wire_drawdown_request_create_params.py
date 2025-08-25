# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InboundWireDrawdownRequestCreateParams"]


class InboundWireDrawdownRequestCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The amount being requested in cents."""

    creditor_account_number: Required[str]
    """The creditor's account number."""

    creditor_routing_number: Required[str]
    """The creditor's routing number."""

    currency: Required[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being
    requested. Will always be "USD".
    """

    recipient_account_number_id: Required[str]
    """
    The Account Number to which the recipient of this request is being requested to
    send funds from.
    """

    creditor_address_line1: str
    """
    A free-form address field set by the sender representing the first line of the
    creditor's address.
    """

    creditor_address_line2: str
    """
    A free-form address field set by the sender representing the second line of the
    creditor's address.
    """

    creditor_address_line3: str
    """
    A free-form address field set by the sender representing the third line of the
    creditor's address.
    """

    creditor_name: str
    """A free-form name field set by the sender representing the creditor's name."""

    debtor_account_number: str
    """The debtor's account number."""

    debtor_address_line1: str
    """
    A free-form address field set by the sender representing the first line of the
    debtor's address.
    """

    debtor_address_line2: str
    """
    A free-form address field set by the sender representing the second line of the
    debtor's address.
    """

    debtor_address_line3: str
    """A free-form address field set by the sender."""

    debtor_name: str
    """A free-form name field set by the sender representing the debtor's name."""

    debtor_routing_number: str
    """The debtor's routing number."""

    end_to_end_identification: str
    """A free-form reference string set by the sender, to help identify the transfer."""

    instruction_identification: str
    """The sending bank's identifier for the wire transfer."""

    unique_end_to_end_transaction_reference: str
    """
    The Unique End-to-end Transaction Reference
    ([UETR](https://www.swift.com/payments/what-unique-end-end-transaction-reference-uetr))
    of the transfer.
    """

    unstructured_remittance_information: str
    """A free-form message set by the sender."""
