# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InboundACHTransferTransferReturnParams"]


class InboundACHTransferTransferReturnParams(TypedDict, total=False):
    reason: Required[
        Literal[
            "insufficient_funds",
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

    - `insufficient_funds` - The customer's account has insufficient funds. This
      reason is only allowed for debits. The Nacha return code is R01.
    - `authorization_revoked_by_customer` - The customer no longer authorizes this
      transaction. The Nacha return code is R07.
    - `payment_stopped` - The customer asked for the payment to be stopped. This
      reason is only allowed for debits. The Nacha return code is R08.
    - `customer_advised_unauthorized_improper_ineligible_or_incomplete` - The
      customer advises that the debit was unauthorized. The Nacha return code is
      R10.
    - `representative_payee_deceased_or_unable_to_continue_in_that_capacity` - The
      payee is deceased. The Nacha return code is R14.
    - `beneficiary_or_account_holder_deceased` - The account holder is deceased. The
      Nacha return code is R15.
    - `credit_entry_refused_by_receiver` - The customer refused a credit entry. This
      reason is only allowed for credits. The Nacha return code is R23.
    - `duplicate_entry` - The account holder identified this transaction as a
      duplicate. The Nacha return code is R24.
    - `corporate_customer_advised_not_authorized` - The corporate customer no longer
      authorizes this transaction. The Nacha return code is R29.
    """
