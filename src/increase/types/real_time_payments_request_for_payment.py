# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "RealTimePaymentsRequestForPayment",
    "Cancellation",
    "Debtor",
    "DebtorAddress",
    "Refusal",
    "Rejection",
    "Submission",
]


class Cancellation(BaseModel):
    """If a cancellation has been requested, this will contain supplemental details.

    The request for payment moves to `canceled` once the recipient bank acknowledges the cancellation.
    """

    additional_information: Optional[str] = None
    """Additional information about the cancellation, sent on to the recipient bank."""

    canceled_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the cancellation was requested.
    """

    reason: Literal["requested_by_customer", "paid_by_other_means", "duplicate", "wrong_amount"]
    """The reason the request for payment was canceled.

    - `requested_by_customer` - The creditor no longer wants to be paid. Corresponds
      to the Real-Time Payments reason code `CUST`.
    - `paid_by_other_means` - The requested payment has already been made through
      another channel. Corresponds to the Real-Time Payments reason code `UPAY`.
    - `duplicate` - The request for payment duplicated another request for payment.
      Corresponds to the Real-Time Payments reason code `DUPL`.
    - `wrong_amount` - The request for payment was sent for the wrong amount.
      Corresponds to the Real-Time Payments reason code `AM09`.
    """


class DebtorAddress(BaseModel):
    """Address of the debtor."""

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


class Debtor(BaseModel):
    """Details of the person being requested to pay."""

    address: DebtorAddress
    """Address of the debtor."""

    name: str
    """The name of the debtor."""


class Refusal(BaseModel):
    """
    If the request for payment is refused by the destination financial institution or the receiving customer, this will contain supplemental details.
    """

    refusal_reason_additional_information: Optional[str] = None
    """
    Additional information about the refusal provided by the recipient bank or the
    customer. This is typically present when the `refusal_reason_code` is `other`.
    """

    refusal_reason_code: Literal[
        "account_blocked",
        "transaction_forbidden",
        "transaction_type_not_supported",
        "unexpected_amount",
        "amount_exceeds_bank_limits",
        "invalid_debtor_address",
        "invalid_creditor_address",
        "creditor_identifier_incorrect",
        "requested_by_customer",
        "order_rejected",
        "end_customer_deceased",
        "customer_has_opted_out",
        "other",
    ]
    """
    The reason the request for payment was refused as provided by the recipient bank
    or the customer.

    - `account_blocked` - The destination account is currently blocked from
      receiving transactions. Corresponds to the Real-Time Payments reason code
      `AC06`.
    - `transaction_forbidden` - Real-Time Payments transfers are not allowed to the
      destination account. Corresponds to the Real-Time Payments reason code `AG01`.
    - `transaction_type_not_supported` - Real-Time Payments transfers are not
      enabled for the destination account. Corresponds to the Real-Time Payments
      reason code `AG03`.
    - `unexpected_amount` - The amount of the transfer is different than expected by
      the recipient. Corresponds to the Real-Time Payments reason code `AM09`.
    - `amount_exceeds_bank_limits` - The amount is higher than the recipient is
      authorized to send or receive. Corresponds to the Real-Time Payments reason
      code `AM14`.
    - `invalid_debtor_address` - The debtor's address is required, but missing or
      invalid. Corresponds to the Real-Time Payments reason code `BE07`.
    - `invalid_creditor_address` - The creditor's address is required, but missing
      or invalid. Corresponds to the Real-Time Payments reason code `BE04`.
    - `creditor_identifier_incorrect` - Creditor identifier incorrect. Corresponds
      to the Real-Time Payments reason code `CH11`.
    - `requested_by_customer` - The customer refused the request. Corresponds to the
      Real-Time Payments reason code `CUST`.
    - `order_rejected` - The order was rejected. Corresponds to the Real-Time
      Payments reason code `DS04`.
    - `end_customer_deceased` - The destination account holder is deceased.
      Corresponds to the Real-Time Payments reason code `MD07`.
    - `customer_has_opted_out` - The customer has opted out of receiving requests
      for payments from this creditor. Corresponds to the Real-Time Payments reason
      code `SL12`.
    - `other` - Some other error or issue has occurred.
    """

    refused_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the request for payment was refused.
    """


class Rejection(BaseModel):
    """
    If the request for payment is rejected by Real-Time Payments or the destination financial institution, this will contain supplemental details.
    """

    reject_reason_additional_information: Optional[str] = None
    """
    Additional information about the rejection provided by the recipient bank or the
    Real-Time Payments network. This is typically present when the
    `reject_reason_code` is `narrative`.
    """

    reject_reason_code: Literal[
        "account_closed",
        "account_blocked",
        "invalid_creditor_account_type",
        "invalid_creditor_account_number",
        "invalid_creditor_financial_institution_identifier",
        "end_customer_deceased",
        "narrative",
        "transaction_forbidden",
        "transaction_type_not_supported",
        "unexpected_amount",
        "amount_exceeds_bank_limits",
        "invalid_creditor_address",
        "unknown_end_customer",
        "invalid_debtor_address",
        "timeout",
        "unsupported_message_for_recipient",
        "recipient_connection_not_available",
        "real_time_payments_suspended",
        "instructed_agent_signed_off",
        "processing_error",
        "other",
    ]
    """
    The reason the request for payment was rejected as provided by the recipient
    bank or the Real-Time Payments network.

    - `account_closed` - The destination account is closed. Corresponds to the
      Real-Time Payments reason code "AC04".
    - `account_blocked` - The destination account is currently blocked from
      receiving transactions. Corresponds to the Real-Time Payments reason code
      "AC06".
    - `invalid_creditor_account_type` - The destination account is ineligible to
      receive Real-Time Payments transfers. Corresponds to the Real-Time Payments
      reason code "AC14".
    - `invalid_creditor_account_number` - The destination account does not exist.
      Corresponds to the Real-Time Payments reason code "AC03".
    - `invalid_creditor_financial_institution_identifier` - The destination routing
      number is invalid. Corresponds to the Real-Time Payments reason code "RC04".
    - `end_customer_deceased` - The destination account holder is deceased.
      Corresponds to the Real-Time Payments reason code "MD07".
    - `narrative` - The reason is provided as narrative information in the
      additional information field.
    - `transaction_forbidden` - Real-Time Payments transfers are not allowed to the
      destination account. Corresponds to the Real-Time Payments reason code "AG01".
    - `transaction_type_not_supported` - Real-Time Payments transfers are not
      enabled for the destination account. Corresponds to the Real-Time Payments
      reason code "AG03".
    - `unexpected_amount` - The amount of the transfer is different than expected by
      the recipient. Corresponds to the Real-Time Payments reason code "AM09".
    - `amount_exceeds_bank_limits` - The amount is higher than the recipient is
      authorized to send or receive. Corresponds to the Real-Time Payments reason
      code "AM14".
    - `invalid_creditor_address` - The creditor's address is required, but missing
      or invalid. Corresponds to the Real-Time Payments reason code "BE04".
    - `unknown_end_customer` - The specified creditor is unknown. Corresponds to the
      Real-Time Payments reason code "BE06".
    - `invalid_debtor_address` - The debtor's address is required, but missing or
      invalid. Corresponds to the Real-Time Payments reason code "BE07".
    - `timeout` - There was a timeout processing the transfer. Corresponds to the
      Real-Time Payments reason code "DS24".
    - `unsupported_message_for_recipient` - Real-Time Payments transfers are not
      enabled for the destination account. Corresponds to the Real-Time Payments
      reason code "NOAT".
    - `recipient_connection_not_available` - The destination financial institution
      is currently not connected to Real-Time Payments. Corresponds to the Real-Time
      Payments reason code "9912".
    - `real_time_payments_suspended` - Real-Time Payments is currently unavailable.
      Corresponds to the Real-Time Payments reason code "9948".
    - `instructed_agent_signed_off` - The destination financial institution is
      currently signed off of Real-Time Payments. Corresponds to the Real-Time
      Payments reason code "9910".
    - `processing_error` - The transfer was rejected due to an internal Increase
      issue. We have been notified.
    - `other` - Some other error or issue has occurred.
    """

    rejected_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the request for payment was rejected.
    """


class Submission(BaseModel):
    """
    After the request for payment is submitted to Real-Time Payments, this will contain supplemental details.
    """

    payment_information_identification: str
    """The Real-Time Payments payment information identification of the request."""


class RealTimePaymentsRequestForPayment(BaseModel):
    """
    Real-Time Payments transfers move funds, within seconds, between your Increase account and any other account on the Real-Time Payments network. A request for payment is a request to the receiver to send funds to your account. The permitted uses of Requests For Payment are limited by the Real-Time Payments network to business-to-business payments and transfers between two accounts at different banks owned by the same individual. Please contact [support@increase.com](mailto:support@increase.com) to enable this API for your team.
    """

    id: str
    """The Real-Time Payments Request for Payment's identifier."""

    account_id: str
    """The Account in which a successful transfer will arrive."""

    account_number_id: str
    """The Account Number in which a successful transfer will arrive."""

    amount: int
    """The transfer amount in USD cents."""

    cancellation: Optional[Cancellation] = None
    """If a cancellation has been requested, this will contain supplemental details.

    The request for payment moves to `canceled` once the recipient bank acknowledges
    the cancellation.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the request for payment was created.
    """

    creditor_name: str
    """The name of the creditor requesting the payment."""

    currency: Literal["USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For real-time payments transfers this is always equal to `USD`.

    - `USD` - US Dollar (USD)
    """

    debtor: Debtor
    """Details of the person being requested to pay."""

    debtor_account_number: str
    """The debtor's account number, which the request is sent to."""

    debtor_routing_number: str
    """The debtor's American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    expires_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time after which
    the request for payment is no longer valid. After this time the debtor's bank
    should no longer allow the debtor to pay it.
    """

    fulfillment_inbound_real_time_payments_transfer_id: Optional[str] = None
    """
    The identifier of the Inbound Real-Time Payments Transfer that fulfilled this
    request.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    refusal: Optional[Refusal] = None
    """
    If the request for payment is refused by the destination financial institution
    or the receiving customer, this will contain supplemental details.
    """

    rejection: Optional[Rejection] = None
    """
    If the request for payment is rejected by Real-Time Payments or the destination
    financial institution, this will contain supplemental details.
    """

    requested_execution_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time by which
    the payment was requested to be made.
    """

    status: Literal[
        "pending_submission", "pending_response", "rejected", "accepted", "refused", "fulfilled", "canceled"
    ]
    """The lifecycle status of the request for payment.

    - `pending_submission` - The request for payment is queued to be submitted to
      Real-Time Payments.
    - `pending_response` - The request for payment has been submitted and is pending
      a response from Real-Time Payments.
    - `rejected` - The request for payment was rejected by the network or the
      recipient.
    - `accepted` - The request for payment was accepted by the recipient but has not
      yet been paid.
    - `refused` - The request for payment was refused by the recipient.
    - `fulfilled` - The request for payment was fulfilled by the receiver.
    - `canceled` - The request for payment was canceled and can no longer be paid.
    """

    submission: Optional[Submission] = None
    """
    After the request for payment is submitted to Real-Time Payments, this will
    contain supplemental details.
    """

    type: Literal["real_time_payments_request_for_payment"]
    """A constant representing the object's type.

    For this resource it will always be `real_time_payments_request_for_payment`.
    """

    unstructured_remittance_information: str
    """Unstructured information that will show on the recipient's bank statement."""
