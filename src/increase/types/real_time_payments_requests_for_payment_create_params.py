# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RealTimePaymentsRequestsForPaymentCreateParams", "Debtor", "DebtorAddress"]


class RealTimePaymentsRequestsForPaymentCreateParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The identifier of the Account Number where the funds will land."""

    amount: Required[int]
    """The requested amount in USD cents. Must be positive."""

    debtor: Required[Debtor]
    """Details of the person being requested to pay."""

    debtor_account_number: Required[str]
    """The debtor's account number, which the funds will be requested from."""

    debtor_routing_number: Required[str]
    """The debtor's American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    expires_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time after which
    the request for payment is no longer valid. After this time the debtor's bank
    should no longer allow the debtor to pay it. Must not be before
    `requested_execution_at`.
    """

    requested_execution_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time by which
    you are requesting the payment to be made.
    """

    unstructured_remittance_information: Required[str]
    """Unstructured information that will show on the recipient's bank statement."""

    creditor_name: str
    """The name of the creditor requesting the payment.

    If not provided, defaults to the name of the account's entity.
    """


class DebtorAddress(TypedDict, total=False):
    """Address of the debtor."""

    country: Required[str]
    """The ISO 3166, Alpha-2 country code.

    Defaults to `US`.
    """

    address_line2: str
    """A second address line, such as an apartment or suite number.

    The first address line is separated into `building_number` and `street_name`.
    """

    building_number: str
    """The number identifying the position of the building on the street."""

    city: str
    """The town or city."""

    postal_code: str
    """The postal code or zip."""

    state: str
    """The US state component of the address."""

    street_name: str
    """The street name without the street number."""


class Debtor(TypedDict, total=False):
    """Details of the person being requested to pay."""

    address: Required[DebtorAddress]
    """Address of the debtor."""

    name: Required[str]
    """The name of the debtor."""
