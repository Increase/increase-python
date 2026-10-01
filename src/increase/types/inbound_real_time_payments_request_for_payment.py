# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundRealTimePaymentsRequestForPayment", "Creditor", "CreditorAddress"]


class CreditorAddress(BaseModel):
    """Address of the creditor."""

    address_line2: Optional[str] = None
    """A second address line, such as an apartment or suite number.

    The first address line is separated into `building_number` and `street_name`.
    """

    building_number: Optional[str] = None
    """The number identifying the position of the building on the street."""

    city: Optional[str] = None
    """The town or city."""

    country: Optional[str] = None
    """The ISO 3166, Alpha-2 country code."""

    postal_code: Optional[str] = None
    """The postal code or zip."""

    state: Optional[str] = None
    """The US state component of the address."""

    street_name: Optional[str] = None
    """The street name without the street number."""


class Creditor(BaseModel):
    """Details of the party requesting payment."""

    account_name: Optional[str] = None
    """
    The name of the account that would receive the payment, as provided by the
    creditor.
    """

    address: CreditorAddress
    """Address of the creditor."""

    name: str
    """The name of the creditor."""


class InboundRealTimePaymentsRequestForPayment(BaseModel):
    """
    An Inbound Real-Time Payments Request for Payment is a request initiated outside of Increase for one of your accounts to send a Real-Time Payments transfer.
    """

    id: str
    """The inbound Real-Time Payments request for payment's identifier."""

    account_id: str
    """The Account the request for payment is for."""

    account_number_id: str
    """The identifier of the Account Number the request for payment is for."""

    amount: int
    """The requested amount in USD cents."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the request for payment was created.
    """

    creditor: Creditor
    """Details of the party requesting payment."""

    creditor_account_number: str
    """The creditor's account number."""

    creditor_routing_number: str
    """
    The creditor's American Bankers' Association (ABA) Routing Transit Number (RTN).
    """

    currency: Literal["USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code of the requested
    currency. This will always be "USD" for a Real-Time Payments request for
    payment.

    - `USD` - US Dollar (USD)
    """

    debtor_name: str
    """
    The name of the account holder the payment is requested from, as provided by the
    creditor.
    """

    end_to_end_identification: str
    """
    A free-form reference string set by the creditor, to help identify the request
    for payment.
    """

    expires_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time after which
    the request for payment is no longer valid and should no longer be paid.
    """

    fulfillment_real_time_payments_transfer_id: Optional[str] = None
    """
    The identifier of the Real-Time Payments Transfer that fulfilled this request
    for payment. This is set once a transfer sent in response to the request for
    payment has been acknowledged by the Real-Time Payments network.
    """

    invoicer_identification: Optional[str] = None
    """
    An identifier for the party that issued the invoice, for requests for payment
    sent on behalf of another party.
    """

    payment_information_identification: str
    """The Real-Time Payments network identification of the request for payment."""

    requested_execution_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time by which
    the creditor requests the payment to be made.
    """

    type: Literal["inbound_real_time_payments_request_for_payment"]
    """A constant representing the object's type.

    For this resource it will always be
    `inbound_real_time_payments_request_for_payment`.
    """

    unstructured_remittance_information: Optional[str] = None
    """Unstructured information included with the request for payment."""
