# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ACHTransferCreateParams"]


class ACHTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Increase identifier for the account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in cents.

    A positive amount originates a credit transfer pushing funds to the receiving
    account. A negative amount originates a debit transfer pulling funds from the
    receiving account.
    """

    statement_descriptor: Required[str]
    """A description you choose to give the transfer.

    This will be saved with the transfer details, displayed in the dashboard, and
    returned by the API. If `individual_name` and `company_name` are not explicitly
    set by this API, the `statement_descriptor` will be sent in those fields to the
    receiving bank to help the customer recognize the transfer. You are highly
    encouraged to pass `individual_name` and `company_name` instead of relying on
    this fallback.
    """

    account_number: str
    """The account number for the destination account."""

    addendum: str
    """Additional information that will be sent to the recipient.

    This is included in the transfer data sent to the receiving bank.
    """

    company_descriptive_date: str
    """The description of the date of the transfer, usually in the format `YYMMDD`.

    This is included in the transfer data sent to the receiving bank.
    """

    company_discretionary_data: str
    """The data you choose to associate with the transfer.

    This is included in the transfer data sent to the receiving bank.
    """

    company_entry_description: str
    """A description of the transfer.

    This is included in the transfer data sent to the receiving bank.
    """

    company_name: str
    """The name by which the recipient knows you.

    This is included in the transfer data sent to the receiving bank.
    """

    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    The transfer effective date in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    external_account_id: str
    """The ID of an External Account to initiate a transfer to.

    If this parameter is provided, `account_number`, `routing_number`, and `funding`
    must be absent.
    """

    funding: Literal["checking", "savings"]
    """The type of the account to which the transfer will be sent.

    - `checking` - A checking account.
    - `savings` - A savings account.
    """

    individual_id: str
    """Your identifer for the transfer recipient."""

    individual_name: str
    """The name of the transfer recipient.

    This value is informational and not verified by the recipient's bank.
    """

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    routing_number: str
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
    """

    standard_entry_class_code: Literal[
        "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
    ]
    """The Standard Entry Class (SEC) code to use for the transfer.

    - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
    - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
    - `internet_initiated` - Internet Initiated (WEB).
    """

    unique_identifier: str
    """A unique identifier you choose for the transfer.

    Reusing this identifer for another transfer will result in an error. You can
    query for the transfer associated with this identifier using the List endpoint.
    """
