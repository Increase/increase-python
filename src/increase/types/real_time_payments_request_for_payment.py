# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RealTimePaymentsRequestForPayment", "Refusal", "Rejection", "Submission"]


class Refusal(BaseModel):
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


class Rejection(BaseModel):
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
      Real-Time Payments reason code `AC04`.
    - `account_blocked` - The destination account is currently blocked from
      receiving transactions. Corresponds to the Real-Time Payments reason code
      `AC06`.
    - `invalid_creditor_account_type` - The destination account is ineligible to
      receive Real-Time Payments transfers. Corresponds to the Real-Time Payments
      reason code `AC14`.
    - `invalid_creditor_account_number` - The destination account does not exist.
      Corresponds to the Real-Time Payments reason code `AC03`.
    - `invalid_creditor_financial_institution_identifier` - The destination routing
      number is invalid. Corresponds to the Real-Time Payments reason code `RC04`.
    - `end_customer_deceased` - The destination account holder is deceased.
      Corresponds to the Real-Time Payments reason code `MD07`.
    - `narrative` - The reason is provided as narrative information in the
      additional information field.
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
    - `invalid_creditor_address` - The creditor's address is required, but missing
      or invalid. Corresponds to the Real-Time Payments reason code `BE04`.
    - `unknown_end_customer` - The specified creditor is unknown. Corresponds to the
      Real-Time Payments reason code `BE06`.
    - `invalid_debtor_address` - The debtor's address is required, but missing or
      invalid. Corresponds to the Real-Time Payments reason code `BE07`.
    - `timeout` - There was a timeout processing the transfer. Corresponds to the
      Real-Time Payments reason code `DS24`.
    - `unsupported_message_for_recipient` - Real-Time Payments transfers are not
      enabled for the destination account. Corresponds to the Real-Time Payments
      reason code `NOAT`.
    - `recipient_connection_not_available` - The destination financial institution
      is currently not connected to Real-Time Payments. Corresponds to the Real-Time
      Payments reason code `9912`.
    - `real_time_payments_suspended` - Real-Time Payments is currently unavailable.
      Corresponds to the Real-Time Payments reason code `9948`.
    - `instructed_agent_signed_off` - The destination financial institution is
      currently signed off of Real-Time Payments. Corresponds to the Real-Time
      Payments reason code `9910`.
    - `processing_error` - The transfer was rejected due to an internal Increase
      issue. We have been notified.
    - `other` - Some other error or issue has occurred.
    """


class Submission(BaseModel):
    payment_information_identification: str
    """The Real-Time Payments payment information identification of the request."""


class RealTimePaymentsRequestForPayment(BaseModel):
    id: str
    """The Real-Time Payments Request for Payment's identifier."""

    amount: int
    """The transfer amount in USD cents."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the request for payment was created.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For real-time payments transfers this is always equal to `USD`.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    debtor_name: str
    """The name of the recipient the sender is requesting a transfer from."""

    destination_account_number_id: str
    """The Account Number in which a successful transfer will arrive."""

    expires_at: date
    """The expiration time for this request, in UTC.

    The requestee will not be able to pay after this date.
    """

    fulfillment_transaction_id: Optional[str] = None
    """The transaction that fulfilled this request."""

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

    remittance_information: str
    """Unstructured information that will show on the recipient's bank statement."""

    source_account_number: str
    """The account number the request is sent to."""

    source_routing_number: str
    """
    The receiver's American Bankers' Association (ABA) Routing Transit Number (RTN).
    """

    status: Literal["pending_submission", "pending_response", "rejected", "accepted", "refused", "fulfilled"]
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
