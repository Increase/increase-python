# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CardValidation",
    "Acceptance",
    "CreatedBy",
    "CreatedByAPIKey",
    "CreatedByOAuthApplication",
    "CreatedByUser",
    "Decline",
    "Submission",
]


class Acceptance(BaseModel):
    accepted_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the validation was accepted by the issuing bank.
    """

    authorization_identification_response: str
    """The authorization identification response from the issuing bank."""

    card_verification_value2_result: Optional[Literal["match", "no_match"]] = None
    """The result of the Card Verification Value 2 match.

    - `match` - The Card Verification Value 2 (CVV2) matches the expected value.
    - `no_match` - The Card Verification Value 2 (CVV2) does not match the expected
      value.
    """

    cardholder_first_name_result: Optional[Literal["match", "no_match", "partial_match"]] = None
    """The result of the cardholder first name match.

    - `match` - The cardholder name component matches the expected value.
    - `no_match` - The cardholder name component does not match the expected value.
    - `partial_match` - The cardholder name component partially matches the expected
      value.
    """

    cardholder_full_name_result: Optional[Literal["match", "no_match", "partial_match"]] = None
    """The result of the cardholder full name match.

    - `match` - The cardholder name component matches the expected value.
    - `no_match` - The cardholder name component does not match the expected value.
    - `partial_match` - The cardholder name component partially matches the expected
      value.
    """

    cardholder_last_name_result: Optional[Literal["match", "no_match", "partial_match"]] = None
    """The result of the cardholder last name match.

    - `match` - The cardholder name component matches the expected value.
    - `no_match` - The cardholder name component does not match the expected value.
    - `partial_match` - The cardholder name component partially matches the expected
      value.
    """

    cardholder_middle_name_result: Optional[Literal["match", "no_match", "partial_match"]] = None
    """The result of the cardholder middle name match.

    - `match` - The cardholder name component matches the expected value.
    - `no_match` - The cardholder name component does not match the expected value.
    - `partial_match` - The cardholder name component partially matches the expected
      value.
    """

    cardholder_postal_code_result: Optional[Literal["match", "no_match"]] = None
    """The result of the cardholder postal code match.

    - `match` - The cardholder address component matches the expected value.
    - `no_match` - The cardholder address component does not match the expected
      value.
    """

    cardholder_street_address_result: Optional[Literal["match", "no_match"]] = None
    """The result of the cardholder street address match.

    - `match` - The cardholder address component matches the expected value.
    - `no_match` - The cardholder address component does not match the expected
      value.
    """

    network_transaction_identifier: Optional[str] = None
    """A unique identifier for the transaction on the card network."""


class CreatedByAPIKey(BaseModel):
    description: Optional[str] = None
    """The description set for the API key when it was created."""


class CreatedByOAuthApplication(BaseModel):
    name: str
    """The name of the OAuth Application."""


class CreatedByUser(BaseModel):
    email: str
    """The email address of the User."""


class CreatedBy(BaseModel):
    api_key: Optional[CreatedByAPIKey] = None
    """If present, details about the API key that created the transfer."""

    category: Literal["api_key", "oauth_application", "user"]
    """The type of object that created this transfer.

    - `api_key` - An API key. Details will be under the `api_key` object.
    - `oauth_application` - An OAuth application you connected to Increase. Details
      will be under the `oauth_application` object.
    - `user` - A User in the Increase dashboard. Details will be under the `user`
      object.
    """

    oauth_application: Optional[CreatedByOAuthApplication] = None
    """If present, details about the OAuth Application that created the transfer."""

    user: Optional[CreatedByUser] = None
    """If present, details about the User that created the transfer."""


class Decline(BaseModel):
    declined_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the validation was declined.
    """

    network_transaction_identifier: Optional[str] = None
    """A unique identifier for the transaction on the card network."""

    reason: Literal[
        "do_not_honor",
        "activity_count_limit_exceeded",
        "refer_to_card_issuer",
        "refer_to_card_issuer_special_condition",
        "invalid_merchant",
        "pick_up_card",
        "error",
        "pick_up_card_special",
        "invalid_transaction",
        "invalid_amount",
        "invalid_account_number",
        "no_such_issuer",
        "re_enter_transaction",
        "no_credit_account",
        "pick_up_card_lost",
        "pick_up_card_stolen",
        "closed_account",
        "insufficient_funds",
        "no_checking_account",
        "no_savings_account",
        "expired_card",
        "transaction_not_permitted_to_cardholder",
        "transaction_not_allowed_at_terminal",
        "suspected_fraud",
        "activity_amount_limit_exceeded",
        "restricted_card",
        "security_violation",
        "transaction_does_not_fulfill_anti_money_laundering_requirement",
        "blocked_first_use",
        "credit_issuer_unavailable",
        "negative_card_verification_value_results",
        "issuer_unavailable",
        "financial_institution_cannot_be_found",
        "transaction_cannot_be_completed",
        "duplicate_transaction",
        "system_malfunction",
        "additional_customer_authentication_required",
        "surcharge_amount_not_permitted",
        "decline_for_cvv2_failure",
        "stop_payment_order",
        "revocation_of_authorization_order",
        "revocation_of_all_authorizations_order",
    ]
    """The reason why the validation was declined.

    - `do_not_honor` - The card issuer has declined the transaction without
      providing a specific reason.
    - `activity_count_limit_exceeded` - The number of transactions for the card has
      exceeded the limit set by the issuer.
    - `refer_to_card_issuer` - The card issuer requires the cardholder to contact
      them for further information regarding the transaction.
    - `refer_to_card_issuer_special_condition` - The card issuer requires the
      cardholder to contact them due to a special condition related to the
      transaction.
    - `invalid_merchant` - The merchant is not valid for this transaction.
    - `pick_up_card` - The card should be retained by the terminal.
    - `error` - An error occurred during processing of the transaction.
    - `pick_up_card_special` - The card should be retained by the terminal due to a
      special condition.
    - `invalid_transaction` - The transaction is invalid and cannot be processed.
    - `invalid_amount` - The amount of the transaction is invalid.
    - `invalid_account_number` - The account number provided is invalid.
    - `no_such_issuer` - The issuer of the card could not be found.
    - `re_enter_transaction` - The transaction should be re-entered for processing.
    - `no_credit_account` - There is no credit account associated with the card.
    - `pick_up_card_lost` - The card should be retained by the terminal because it
      has been reported lost.
    - `pick_up_card_stolen` - The card should be retained by the terminal because it
      has been reported stolen.
    - `closed_account` - The account associated with the card has been closed.
    - `insufficient_funds` - There are insufficient funds in the account to complete
      the transaction.
    - `no_checking_account` - There is no checking account associated with the card.
    - `no_savings_account` - There is no savings account associated with the card.
    - `expired_card` - The card has expired and cannot be used for transactions.
    - `transaction_not_permitted_to_cardholder` - The transaction is not permitted
      for this cardholder.
    - `transaction_not_allowed_at_terminal` - The transaction is not allowed at this
      terminal.
    - `suspected_fraud` - The transaction has been flagged as suspected fraud and
      cannot be processed.
    - `activity_amount_limit_exceeded` - The amount of activity on the card has
      exceeded the limit set by the issuer.
    - `restricted_card` - The card has restrictions that prevent it from being used
      for this transaction.
    - `security_violation` - A security violation has occurred, preventing the
      transaction from being processed.
    - `transaction_does_not_fulfill_anti_money_laundering_requirement` - The
      transaction does not meet the anti-money laundering requirements set by the
      issuer.
    - `blocked_first_use` - The first use of the card has been blocked by the
      issuer.
    - `credit_issuer_unavailable` - The credit issuer is currently unavailable to
      process the transaction.
    - `negative_card_verification_value_results` - The card verification value (CVV)
      results were negative, indicating a potential issue with the card.
    - `issuer_unavailable` - The issuer of the card is currently unavailable to
      process the transaction.
    - `financial_institution_cannot_be_found` - The financial institution associated
      with the card could not be found.
    - `transaction_cannot_be_completed` - The transaction cannot be completed due to
      an unspecified reason.
    - `duplicate_transaction` - The transaction is a duplicate of a previous
      transaction and cannot be processed again.
    - `system_malfunction` - A system malfunction occurred, preventing the
      transaction from being processed.
    - `additional_customer_authentication_required` - Additional customer
      authentication is required to complete the transaction.
    - `surcharge_amount_not_permitted` - The surcharge amount applied to the
      transaction is not permitted by the issuer.
    - `decline_for_cvv2_failure` - The transaction was declined due to a failure in
      verifying the CVV2 code.
    - `stop_payment_order` - A stop payment order has been placed on this
      transaction.
    - `revocation_of_authorization_order` - An order has been placed to revoke
      authorization for this transaction.
    - `revocation_of_all_authorizations_order` - An order has been placed to revoke
      all authorizations for this cardholder.
    """


class Submission(BaseModel):
    retrieval_reference_number: str
    """A 12-digit retrieval reference number that identifies the validation.

    Usually a combination of a timestamp and the trace number.
    """

    submitted_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the validation was submitted to the card network.
    """

    trace_number: str
    """
    A 6-digit trace number that identifies the validation within a short time
    window.
    """


class CardValidation(BaseModel):
    id: str
    """The Card Validation's identifier."""

    acceptance: Optional[Acceptance] = None
    """
    If the validation is accepted by the recipient bank, this will contain
    supplemental details.
    """

    account_id: str
    """The identifier of the Account from which to send the validation."""

    card_token_id: str
    """The ID of the Card Token that was used to validate the card."""

    cardholder_first_name: Optional[str] = None
    """The cardholder's first name."""

    cardholder_last_name: Optional[str] = None
    """The cardholder's last name."""

    cardholder_middle_name: Optional[str] = None
    """The cardholder's middle name."""

    cardholder_postal_code: Optional[str] = None
    """The postal code of the cardholder's address."""

    cardholder_street_address: Optional[str] = None
    """The cardholder's street address."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the validation was created.
    """

    created_by: Optional[CreatedBy] = None
    """What object created the validation, either via the API or the dashboard."""

    decline: Optional[Decline] = None
    """
    If the validation is rejected by the card network or the destination financial
    institution, this will contain supplemental details.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    merchant_category_code: str
    """
    A four-digit code (MCC) identifying the type of business or service provided by
    the merchant.
    """

    merchant_city_name: str
    """The city where the merchant (typically your business) is located."""

    merchant_name: str
    """The merchant name that will appear in the cardholder’s statement descriptor.

    Typically your business name.
    """

    merchant_postal_code: str
    """The postal code for the merchant’s (typically your business’s) location."""

    merchant_state: str
    """The U.S. state where the merchant (typically your business) is located."""

    status: Literal["requires_attention", "pending_submission", "submitted", "complete", "declined"]
    """The lifecycle status of the validation.

    - `requires_attention` - The validation requires attention from an Increase
      operator.
    - `pending_submission` - The validation is queued to be submitted to the card
      network.
    - `submitted` - The validation has been submitted and is pending a response from
      the card network.
    - `complete` - The validation has been sent successfully and is complete.
    - `declined` - The validation was declined by the network or the recipient's
      bank.
    """

    submission: Optional[Submission] = None
    """
    After the validation is submitted to the card network, this will contain
    supplemental details.
    """

    type: Literal["card_validation"]
    """A constant representing the object's type.

    For this resource it will always be `card_validation`.
    """
