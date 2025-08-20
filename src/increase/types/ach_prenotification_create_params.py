# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ACHPrenotificationCreateParams"]


class ACHPrenotificationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Increase identifier for the account that will send the ACH Prenotification."""

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
    """The description of the date of the ACH Prenotification."""

    company_discretionary_data: str
    """The data you choose to associate with the ACH Prenotification."""

    company_entry_description: str
    """The description you wish to be shown to the recipient."""

    company_name: str
    """The name by which the recipient knows you."""

    credit_debit_indicator: Literal["credit", "debit"]
    """Whether the Prenotification is for a future debit or credit.

    - `credit` - The Prenotification is for an anticipated credit.
    - `debit` - The Prenotification is for an anticipated debit.
    """

    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    The ACH Prenotification effective date in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    individual_id: str
    """Your identifier for the recipient."""

    individual_name: str
    """The name of therecipient.

    This value is informational and not verified by the recipient's bank.
    """

    standard_entry_class_code: Literal[
        "corporate_credit_or_debit",
        "corporate_trade_exchange",
        "prearranged_payments_and_deposit",
        "internet_initiated",
    ]
    """The Standard Entry Class (SEC) code to use for the ACH Prenotification.

    - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
    - `corporate_trade_exchange` - Corporate Trade Exchange (CTX).
    - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
    - `internet_initiated` - Internet Initiated (WEB).
    """
