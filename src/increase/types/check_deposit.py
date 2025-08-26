# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CheckDeposit",
    "DepositAcceptance",
    "DepositRejection",
    "DepositReturn",
    "DepositSubmission",
    "InboundFundsHold",
]


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

    check_deposit_id: str
    """The identifier of the Check Deposit that was rejected."""

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

    declined_transaction_id: str
    """The identifier of the associated declined transaction."""

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
        "requested_by_user",
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
    - `requested_by_user` - The check was rejected at the user's request.
    - `unknown` - The check was rejected for an unknown reason.
    """

    rejected_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check deposit was rejected.
    """


class DepositReturn(BaseModel):
    amount: int
    """The returned amount in USD cents."""

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
    - `closed_account` - The account is closed. (Check21 return code `D`)
    - `duplicate_submission` - The check has already been deposited. (Check21 return
      code `Y`)
    - `insufficient_funds` - Insufficient funds (Check21 return code `A`)
    - `no_account` - No account was found matching the check details. (Check21
      return code `E`)
    - `not_authorized` - The check was not authorized. (Check21 return code `Q`)
    - `stale_dated` - The check is too old. (Check21 return code `G`)
    - `stop_payment` - The payment has been stopped by the account holder. (Check21
      return code `C`)
    - `unknown_reason` - The reason for the return is unknown.
    - `unmatched_details` - The image doesn't match the details submitted.
    - `unreadable_image` - The image could not be read. (Check21 return code `U`)
    - `endorsement_irregular` - The check endorsement was irregular. (Check21 return
      code `J`)
    - `altered_or_fictitious_item` - The check present was either altered or fake.
      (Check21 return code `N`)
    - `frozen_or_blocked_account` - The account this check is drawn on is frozen.
      (Check21 return code `F`)
    - `post_dated` - The check is post dated. (Check21 return code `H`)
    - `endorsement_missing` - The endorsement was missing. (Check21 return code `I`)
    - `signature_missing` - The check signature was missing. (Check21 return code
      `K`)
    - `stop_payment_suspect` - The bank suspects a stop payment will be placed.
      (Check21 return code `T`)
    - `unusable_image` - The bank cannot read the image. (Check21 return code `U`)
    - `image_fails_security_check` - The check image fails the bank's security
      check. (Check21 return code `V`)
    - `cannot_determine_amount` - The bank cannot determine the amount. (Check21
      return code `W`)
    - `signature_irregular` - The signature is inconsistent with prior signatures.
      (Check21 return code `L`)
    - `non_cash_item` - The check is a non-cash item and cannot be drawn against the
      account. (Check21 return code `M`)
    - `unable_to_process` - The bank is unable to process this check. (Check21
      return code `O`)
    - `item_exceeds_dollar_limit` - The check exceeds the bank or customer's limit.
      (Check21 return code `P`)
    - `branch_or_account_sold` - The bank sold this account and no longer services
      this customer. (Check21 return code `R`)
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
    back_file_id: str
    """
    The ID for the File containing the check back image that was submitted to the
    Check21 network.
    """

    front_file_id: str
    """
    The ID for the File containing the check front image that was submitted to the
    Check21 network.
    """

    submitted_at: datetime
    """When the check deposit was submitted to the Check21 network for processing.

    During business days, this happens within a few hours of the check being
    accepted by Increase.
    """


class InboundFundsHold(BaseModel):
    amount: int
    """The held amount in the minor unit of the account's currency.

    For dollars, for example, this is cents.
    """

    automatically_releases_at: datetime
    """When the hold will be released automatically.

    Certain conditions may cause it to be released before this time.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the hold
    was created.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the hold's
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    held_transaction_id: Optional[str] = None
    """The ID of the Transaction for which funds were held."""

    pending_transaction_id: Optional[str] = None
    """The ID of the Pending Transaction representing the held funds."""

    released_at: Optional[datetime] = None
    """When the hold was released (if it has been released)."""

    status: Literal["held", "complete"]
    """The status of the hold.

    - `held` - Funds are still being held.
    - `complete` - Funds have been released.
    """

    type: Literal["inbound_funds_hold"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_funds_hold`.
    """


class CheckDeposit(BaseModel):
    id: str
    """The deposit's identifier."""

    account_id: str
    """The Account the check was deposited into."""

    amount: int
    """The deposited amount in USD cents."""

    back_image_file_id: Optional[str] = None
    """The ID for the File containing the image of the back of the check."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
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

    description: Optional[str] = None
    """The description of the Check Deposit, for display purposes only."""

    front_image_file_id: str
    """The ID for the File containing the image of the front of the check."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    inbound_funds_hold: Optional[InboundFundsHold] = None
    """Increase will sometimes hold the funds for Check Deposits.

    If funds are held, this sub-object will contain details of the hold.
    """

    inbound_mail_item_id: Optional[str] = None
    """
    If the Check Deposit was the result of an Inbound Mail Item, this will contain
    the identifier of the Inbound Mail Item.
    """

    lockbox_id: Optional[str] = None
    """
    If the Check Deposit was the result of an Inbound Mail Item, this will contain
    the identifier of the Lockbox that received it.
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
