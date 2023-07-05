# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundACHTransferReturn", "Submission"]


class Submission(BaseModel):
    submitted_at: datetime
    """When the ACH transfer return was sent to FedACH."""

    trace_number: str
    """The trace number for the submission."""


class InboundACHTransferReturn(BaseModel):
    id: str
    """The ID of the Inbound ACH Transfer Return."""

    inbound_ach_transfer_transaction_id: str
    """The ID for the Transaction that is being returned."""

    reason: Literal[
        "authorization_revoked_by_customer",
        "payment_stopped",
        "customer_advised_unauthorized_improper_ineligible_or_incomplete",
        "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
        "beneficiary_or_account_holder_deceased",
        "credit_entry_refused_by_receiver",
        "duplicate_entry",
        "corporate_customer_advised_not_authorized",
    ]
    """The reason why this transfer will be returned.

    This is sent to the initiating bank.

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

    status: Literal["pending_submitting", "submitted"]
    """The lifecycle status of the transfer.

    - `pending_submitting` - The transfer return is pending submission to the
      Federal Reserve.
    - `submitted` - The transfer has been submitted to the Federal Reserve.
    """

    submission: Optional[Submission]
    """
    After the return is submitted to FedACH, this will contain supplemental details.
    """

    transaction_id: Optional[str]
    """The ID for the transaction refunding the transfer."""

    type: Literal["inbound_ach_transfer_return"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_ach_transfer_return`.
    """
