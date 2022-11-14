# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ACHPrenotificationCreateParams"]


class ACHPrenotificationCreateParams(TypedDict, total=False):
    account_number: Required[str]
    """The account number for the destination account."""

    routing_number: Required[str]
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
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

    credit_debit_indicator: Literal["credit", "debit"]
    """Whether the Prenotification is for a future debit or credit."""

    effective_date: str
    """
    The transfer effective date in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    individual_id: str
    """Your identifer for the transfer recipient."""

    individual_name: str
    """The name of the transfer recipient.

    This value is information and not verified by the recipient's bank.
    """

    standard_entry_class_code: Literal[
        "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
    ]
    """The Standard Entry Class (SEC) code to use for the ACH Prenotification."""
