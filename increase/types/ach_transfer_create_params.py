# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ACHTransferCreateParams"]


class ACHTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    account_number: Required[str]
    """The account number for the destination account."""

    amount: Required[int]
    """The transfer amount in cents.

    A positive amount originates a credit transfer pushing funds to the receiving
    account. A negative amount originates a debit transfer pulling funds from the
    receiving account.
    """

    routing_number: Required[str]
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
    """

    statement_descriptor: Required[str]
    """The description you choose to give the transfer.

    This will be shown to the recipient.
    """

    addendum: str
    """Additional information that will be sent to the recipient."""

    company_descriptive_date: str
    """The description of the date of the transfer."""

    company_discretionary_data: str
    """The data you choose to associate with the transfer."""

    company_entry_description: str
    """The description of the transfer you wish to be shown to the recipient."""

    company_name: str
    """The name by which the recipient knows you."""

    effective_date: str
    """
    The transfer effective date in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    funding: Literal["checking", "savings"]
    """The type of the account to which the transfer will be sent."""

    individual_id: str
    """Your identifer for the transfer recipient."""

    individual_name: str
    """The name of the transfer recipient.

    This value is information and not verified by the recipient's bank.
    """

    standard_entry_class_code: Literal[
        "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
    ]
    """The Standard Entry Class (SEC) code to use for the transfer."""
