# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InboundACHTransferReturnCreateParams"]


class InboundACHTransferReturnCreateParams(TypedDict, total=False):
    reason: Required[
        Literal[
            "authorization_revoked_by_customer",
            "payment_stopped",
            "customer_advised_unauthorized_improper_ineligible_or_incomplete",
            "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
            "beneficiary_or_account_holder_deceased",
            "credit_entry_refused_by_receiver",
            "duplicate_entry",
            "corporate_customer_advised_not_authorized",
        ]
    ]
    """The reason why this transfer will be returned.

    The most usual return codes are `payment_stopped` for debits and
    `credit_entry_refused_by_receiver` for credits.
    """

    transaction_id: Required[str]
    """
    The transaction identifier of the Inbound ACH Transfer to return to the
    originating financial institution.
    """
