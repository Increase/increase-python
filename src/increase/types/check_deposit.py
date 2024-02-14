# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CheckDeposit", "DepositAcceptance", "DepositRejection", "DepositReturn", "DepositSubmission"]


class DepositAcceptance(BaseModel):
    account_number: str
    """The account number printed on the check."""

    amount: int
    """The amount to be deposited in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    auxiliary_on_us: Optional[str] = None
    """An additional line of metadata printed on the check.

    This typically includes the check number for business checks.
    """

    check_deposit_id: str
    """The ID of the Check Deposit that was accepted."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    routing_number: str
    """The routing number printed on the check."""

    serial_number: Optional[str] = None
    """The check serial number, if present, for consumer checks.

    For business checks, the serial number is usually in the `auxiliary_on_us`
    field.
    """


class DepositRejection(BaseModel):
    amount: int
    """The rejected amount in the minor unit of check's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    reason: Literal[
        "incomplete_image",
        "duplicate",
        "poor_image_quality",
        "incorrect_amount",
        "incorrect_recipient",
        "not_eligible_for_mobile_deposit",
        "missing_required_data_elements",
        "suspected_fraud",
        "deposit_window_expired",
        "unknown",
    ]
    """Why the check deposit was rejected.

    - `incomplete_image` - The check's image is incomplete.
    - `duplicate` - This is a duplicate check submission.
    - `poor_image_quality` - This check has poor image quality.
    - `incorrect_amount` - The check was deposited with the incorrect amount.
    - `incorrect_recipient` - The check is made out to someone other than the
      account holder.
    - `not_eligible_for_mobile_deposit` - This check was not eligible for mobile
      deposit.
    - `missing_required_data_elements` - This check is missing at least one required
      field.
    - `suspected_fraud` - This check is suspected to be fraudulent.
    - `deposit_window_expired` - This check's deposit window has expired.
    - `unknown` - The check was rejected for an unknown reason.
    """

    rejected_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check deposit was rejected.
    """


class DepositReturn(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    check_deposit_id: str
    """The identifier of the Check Deposit that was returned."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    return_reason: Literal[
        "ach_conversion_not_supported",
        "closed_account",
        "duplicate_submission",
        "insufficient_funds",
        "no_account",
        "not_authorized",
        "stale_dated",
        "stop_payment",
        "unknown_reason",
        "unmatched_details",
        "unreadable_image",
        "endorsement_irregular",
        "altered_or_fictitious_item",
        "frozen_or_blocked_account",
        "post_dated",
        "endorsement_missing",
        "signature_missing",
        "stop_payment_suspect",
        "unusable_image",
        "image_fails_security_check",
        "cannot_determine_amount",
        "signature_irregular",
        "non_cash_item",
        "unable_to_process",
        "item_exceeds_dollar_limit",
        "branch_or_account_sold",
    ]
    """
    Why this check was returned by the bank holding the account it was drawn
    against.

    - `ach_conversion_not_supported` - The check doesn't allow ACH conversion.
    - `closed_account` - The account is closed.
    - `duplicate_submission` - The check has already been deposited.
    - `insufficient_funds` - Insufficient funds
    - `no_account` - No account was found matching the check details.
    - `not_authorized` - The check was not authorized.
    - `stale_dated` - The check is too old.
    - `stop_payment` - The payment has been stopped by the account holder.
    - `unknown_reason` - The reason for the return is unknown.
    - `unmatched_details` - The image doesn't match the details submitted.
    - `unreadable_image` - The image could not be read.
    - `endorsement_irregular` - The check endorsement was irregular.
    - `altered_or_fictitious_item` - The check present was either altered or fake.
    - `frozen_or_blocked_account` - The account this check is drawn on is frozen.
    - `post_dated` - The check is post dated.
    - `endorsement_missing` - The endorsement was missing.
    - `signature_missing` - The check signature was missing.
    - `stop_payment_suspect` - The bank suspects a stop payment will be placed.
    - `unusable_image` - The bank cannot read the image.
    - `image_fails_security_check` - The check image fails the bank's security
      check.
    - `cannot_determine_amount` - The bank cannot determine the amount.
    - `signature_irregular` - The signature is inconsistent with prior signatures.
    - `non_cash_item` - The check is a non-cash item and cannot be drawn against the
      account.
    - `unable_to_process` - The bank is unable to process this check.
    - `item_exceeds_dollar_limit` - The check exceeds the bank or customer's limit.
    - `branch_or_account_sold` - The bank sold this account and no longer services
      this customer.
    """

    returned_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check deposit was returned.
    """

    transaction_id: str
    """
    The identifier of the transaction that reversed the original check deposit
    transaction.
    """


class DepositSubmission(BaseModel):
    submitted_at: datetime
    """When the check deposit was submitted to the Check21 network for processing.

    During business days, this happens within a few hours of the check being
    accepted by Increase.
    """


class CheckDeposit(BaseModel):
    id: str
    """The deposit's identifier."""

    account_id: str
    """The Account the check was deposited into."""

    amount: int
    """The deposited amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    back_image_file_id: Optional[str] = None
    """The ID for the File containing the image of the back of the check."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the deposit.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    deposit_acceptance: Optional[DepositAcceptance] = None
    """
    If your deposit is successfully parsed and accepted by Increase, this will
    contain details of the parsed check.
    """

    deposit_rejection: Optional[DepositRejection] = None
    """
    If your deposit is rejected by Increase, this will contain details as to why it
    was rejected.
    """

    deposit_return: Optional[DepositReturn] = None
    """
    If your deposit is returned, this will contain details as to why it was
    returned.
    """

    deposit_submission: Optional[DepositSubmission] = None
    """After the check is parsed, it is submitted to the Check21 network for
    processing.

    This will contain details of the submission.
    """

    front_image_file_id: str
    """The ID for the File containing the image of the front of the check."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    status: Literal["pending", "submitted", "rejected", "returned"]
    """The status of the Check Deposit.

    - `pending` - The Check Deposit is pending review.
    - `submitted` - The Check Deposit has been deposited.
    - `rejected` - The Check Deposit has been rejected.
    - `returned` - The Check Deposit has been returned.
    """

    transaction_id: Optional[str] = None
    """The ID for the Transaction created by the deposit."""

    type: Literal["check_deposit"]
    """A constant representing the object's type.

    For this resource it will always be `check_deposit`.
    """
