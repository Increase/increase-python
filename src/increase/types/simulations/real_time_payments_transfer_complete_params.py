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
    """The reason code that the simulated rejection will have."""
