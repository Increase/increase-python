# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RealTimePaymentsTransferCompleteParams", "Rejection"]


class RealTimePaymentsTransferCompleteParams(TypedDict, total=False):
    rejection: Rejection
    """If set, the simulation will reject the transfer."""


class Rejection(TypedDict, total=False):
    reject_reason_code: Required[
        Literal[
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
    ]
    """The reason code that the simulated rejection will have.

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
