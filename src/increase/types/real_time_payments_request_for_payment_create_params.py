# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RealTimePaymentsRequestForPaymentCreateParams", "Debtor", "DebtorAddress"]


class RealTimePaymentsRequestForPaymentCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The requested amount in USD cents. Must be positive."""

    debtor: Required[Debtor]
    """Details of the person being requested to pay."""

    destination_account_number_id: Required[str]
    """The identifier of the Account Number where the funds will land."""

    expires_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The expiration time for this request, in UTC.

    The requestee will not be able to pay after this date.
    """

    remittance_information: Required[str]
    """Unstructured information that will show on the requestee's bank statement."""

    source_account_number: Required[str]
    """The account number the funds will be requested from."""

    source_routing_number: Required[str]
    """
    The requestee's American Bankers' Association (ABA) Routing Transit Number
    (RTN).
    """


class DebtorAddress(TypedDict, total=False):
    country: Required[str]
    """The ISO 3166, Alpha-2 country code."""

    city: str
    """The town or city."""

    post_code: str
    """The postal code or zip."""

    street_name: str
    """The street name without the street number."""


class Debtor(TypedDict, total=False):
    address: Required[DebtorAddress]
    """Address of the debtor."""

    name: Required[str]
    """The name of the debtor."""
