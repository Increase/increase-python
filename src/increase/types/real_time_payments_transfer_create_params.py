# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RealTimePaymentsTransferCreateParams", "DebtorAddress"]


class RealTimePaymentsTransferCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The transfer amount in USD cents.

    For Real-Time Payments transfers, must be positive.
    """

    creditor_name: Required[str]
    """The name of the transfer's recipient."""

    source_account_number_id: Required[str]
    """The identifier of the Account Number from which to send the transfer."""

    unstructured_remittance_information: Required[str]
    """Unstructured information that will show on the recipient's bank statement."""

    account_number: str
    """The destination account number."""

    debtor_address: DebtorAddress
    """The address of the transfer's sender.

    If not provided, no debtor address is sent with the transfer.
    """

    debtor_name: str
    """The name of the transfer's sender.

    If not provided, defaults to the name of the account's entity.
    """

    external_account_id: str
    """The ID of an External Account to initiate a transfer to.

    If this parameter is provided, `account_number` and `routing_number` must be
    absent.
    """

    inbound_real_time_payments_request_for_payment_id: str
    """
    The ID of an Inbound Real-Time Payments Request for Payment in response to which
    this transfer is being sent.
    """

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    routing_number: str
    """
    The destination American Bankers' Association (ABA) Routing Transit Number
    (RTN).
    """

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


class DebtorAddress(TypedDict, total=False):
    """The address of the transfer's sender.

    If not provided, no debtor address is sent with the transfer.
    """

    city: Required[str]
    """The town or city."""

    country: Required[str]
    """The ISO 3166, Alpha-2 country code.

    Defaults to `US`.
    """

    postal_code: Required[str]
    """The postal code or zip."""

    state: Required[str]
    """The US state component of the address."""

    street_name: Required[str]
    """The street name without the street number."""

    address_line2: str
    """A second address line, such as an apartment or suite number.

    The first address line is separated into `building_number` and `street_name`.
    """

    building_number: str
    """The number identifying the position of the building on the street."""
