# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ACHTransfer",
    "Acknowledgement",
    "Addenda",
    "AddendaFreeform",
    "AddendaFreeformEntry",
    "AddendaPaymentOrderRemittanceAdvice",
    "AddendaPaymentOrderRemittanceAdviceInvoice",
    "Approval",
    "Cancellation",
    "CreatedBy",
    "CreatedByAPIKey",
    "CreatedByOAuthApplication",
    "CreatedByUser",
    "InboundFundsHold",
    "NotificationsOfChange",
    "PreferredEffectiveDate",
    "Return",
    "Settlement",
    "Submission",
]


class Acknowledgement(BaseModel):
    acknowledged_at: str
    """
    When the Federal Reserve acknowledged the submitted file containing this
    transfer.
    """


class AddendaFreeformEntry(BaseModel):
    payment_related_information: str
    """The payment related information passed in the addendum."""


class AddendaFreeform(BaseModel):
    entries: List[AddendaFreeformEntry]
    """Each entry represents an addendum sent with the transfer."""


class AddendaPaymentOrderRemittanceAdviceInvoice(BaseModel):
    invoice_number: str
    """The invoice number for this reference, determined in advance with the receiver."""

    paid_amount: int
    """The amount that was paid for this invoice in the minor unit of its currency.

    For dollars, for example, this is cents.
    """


class AddendaPaymentOrderRemittanceAdvice(BaseModel):
    invoices: List[AddendaPaymentOrderRemittanceAdviceInvoice]
    """ASC X12 RMR records for this specific transfer."""


class Addenda(BaseModel):
    category: Literal["freeform", "payment_order_remittance_advice", "other"]
    """The type of the resource.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.

    - `freeform` - Unstructured `payment_related_information` passed through with
      the transfer.
    - `payment_order_remittance_advice` - Structured ASC X12 820 remittance advice
      records. Please reach out to
      [support@increase.com](mailto:support@increase.com) for more information.
    - `other` - Unknown addenda type.
    """

    freeform: Optional[AddendaFreeform] = None
    """Unstructured `payment_related_information` passed through with the transfer."""

    payment_order_remittance_advice: Optional[AddendaPaymentOrderRemittanceAdvice] = None
    """Structured ASC X12 820 remittance advice records.

    Please reach out to [support@increase.com](mailto:support@increase.com) for more
    information.
    """


class Approval(BaseModel):
    approved_at: datetime.datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was approved.
    """

    approved_by: Optional[str] = None
    """
    If the Transfer was approved by a user in the dashboard, the email address of
    that user.
    """


class Cancellation(BaseModel):
    canceled_at: datetime.datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Transfer was canceled.
    """

    canceled_by: Optional[str] = None
    """
    If the Transfer was canceled by a user in the dashboard, the email address of
    that user.
    """


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


class InboundFundsHold(BaseModel):
    amount: int
    """The held amount in the minor unit of the account's currency.

    For dollars, for example, this is cents.
    """

    automatically_releases_at: datetime.datetime
    """When the hold will be released automatically.

    Certain conditions may cause it to be released before this time.
    """

    created_at: datetime.datetime
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

    released_at: Optional[datetime.datetime] = None
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


class NotificationsOfChange(BaseModel):
    change_code: Literal[
        "incorrect_account_number",
        "incorrect_routing_number",
        "incorrect_routing_number_and_account_number",
        "incorrect_transaction_code",
        "incorrect_account_number_and_transaction_code",
        "incorrect_routing_number_account_number_and_transaction_code",
        "incorrect_receiving_depository_financial_institution_identification",
        "incorrect_individual_identification_number",
        "addenda_format_error",
        "incorrect_standard_entry_class_code_for_outbound_international_payment",
        "misrouted_notification_of_change",
        "incorrect_trace_number",
        "incorrect_company_identification_number",
        "incorrect_identification_number",
        "incorrectly_formatted_corrected_data",
        "incorrect_discretionary_data",
        "routing_number_not_from_original_entry_detail_record",
        "depository_financial_institution_account_number_not_from_original_entry_detail_record",
        "incorrect_transaction_code_by_originating_depository_financial_institution",
    ]
    """
    The required type of change that is being signaled by the receiving financial
    institution.

    - `incorrect_account_number` - The account number was incorrect.
    - `incorrect_routing_number` - The routing number was incorrect.
    - `incorrect_routing_number_and_account_number` - Both the routing number and
      the account number were incorrect.
    - `incorrect_transaction_code` - The transaction code was incorrect. Try
      changing the `funding` parameter from checking to savings or vice-versa.
    - `incorrect_account_number_and_transaction_code` - The account number and the
      transaction code were incorrect.
    - `incorrect_routing_number_account_number_and_transaction_code` - The routing
      number, account number, and transaction code were incorrect.
    - `incorrect_receiving_depository_financial_institution_identification` - The
      receiving depository financial institution identification was incorrect.
    - `incorrect_individual_identification_number` - The individual identification
      number was incorrect.
    - `addenda_format_error` - The addenda had an incorrect format.
    - `incorrect_standard_entry_class_code_for_outbound_international_payment` - The
      standard entry class code was incorrect for an outbound international payment.
    - `misrouted_notification_of_change` - The notification of change was misrouted.
    - `incorrect_trace_number` - The trace number was incorrect.
    - `incorrect_company_identification_number` - The company identification number
      was incorrect.
    - `incorrect_identification_number` - The individual identification number or
      identification number was incorrect.
    - `incorrectly_formatted_corrected_data` - The corrected data was incorrectly
      formatted.
    - `incorrect_discretionary_data` - The discretionary data was incorrect.
    - `routing_number_not_from_original_entry_detail_record` - The routing number
      was not from the original entry detail record.
    - `depository_financial_institution_account_number_not_from_original_entry_detail_record` -
      The depository financial institution account number was not from the original
      entry detail record.
    - `incorrect_transaction_code_by_originating_depository_financial_institution` -
      The transaction code was incorrect, initiated by the originating depository
      financial institution.
    """

    corrected_data: str
    """The corrected data that should be used in future ACHs to this account.

    This may contain the suggested new account number or routing number. When the
    `change_code` is `incorrect_transaction_code`, this field contains an integer.
    Numbers starting with a 2 encourage changing the `funding` parameter to
    checking; numbers starting with a 3 encourage changing to savings.
    """

    created_at: datetime.datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the notification occurred.
    """


class PreferredEffectiveDate(BaseModel):
    date: Optional[datetime.date] = None
    """
    A specific date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format to
    use as the effective date when submitting this transfer.
    """

    settlement_schedule: Optional[Literal["same_day", "future_dated"]] = None
    """A schedule by which Increase will choose an effective date for the transfer.

    - `same_day` - The chosen effective date will be the same as the ACH processing
      date on which the transfer is submitted. This is necessary, but not sufficient
      for the transfer to be settled same-day: it must also be submitted before the
      last same-day cutoff and be less than or equal to $1,000.000.00.
    - `future_dated` - The chosen effective date will be the business day following
      the ACH processing date on which the transfer is submitted. The transfer will
      be settled on that future day.
    """


class Return(BaseModel):
    created_at: datetime.datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    raw_return_reason_code: str
    """The three character ACH return code, in the range R01 to R85."""

    return_reason_code: Literal[
        "insufficient_fund",
        "no_account",
        "account_closed",
        "invalid_account_number_structure",
        "account_frozen_entry_returned_per_ofac_instruction",
        "credit_entry_refused_by_receiver",
        "unauthorized_debit_to_consumer_account_using_corporate_sec_code",
        "corporate_customer_advised_not_authorized",
        "payment_stopped",
        "non_transaction_account",
        "uncollected_funds",
        "routing_number_check_digit_error",
        "customer_advised_unauthorized_improper_ineligible_or_incomplete",
        "amount_field_error",
        "authorization_revoked_by_customer",
        "invalid_ach_routing_number",
        "file_record_edit_criteria",
        "enr_invalid_individual_name",
        "returned_per_odfi_request",
        "limited_participation_dfi",
        "incorrectly_coded_outbound_international_payment",
        "account_sold_to_another_dfi",
        "addenda_error",
        "beneficiary_or_account_holder_deceased",
        "customer_advised_not_within_authorization_terms",
        "corrected_return",
        "duplicate_entry",
        "duplicate_return",
        "enr_duplicate_enrollment",
        "enr_invalid_dfi_account_number",
        "enr_invalid_individual_id_number",
        "enr_invalid_representative_payee_indicator",
        "enr_invalid_transaction_code",
        "enr_return_of_enr_entry",
        "enr_routing_number_check_digit_error",
        "entry_not_processed_by_gateway",
        "field_error",
        "foreign_receiving_dfi_unable_to_settle",
        "iat_entry_coding_error",
        "improper_effective_entry_date",
        "improper_source_document_source_document_presented",
        "invalid_company_id",
        "invalid_foreign_receiving_dfi_identification",
        "invalid_individual_id_number",
        "item_and_rck_entry_presented_for_payment",
        "item_related_to_rck_entry_is_ineligible",
        "mandatory_field_error",
        "misrouted_dishonored_return",
        "misrouted_return",
        "no_errors_found",
        "non_acceptance_of_r62_dishonored_return",
        "non_participant_in_iat_program",
        "permissible_return_entry",
        "permissible_return_entry_not_accepted",
        "rdfi_non_settlement",
        "rdfi_participant_in_check_truncation_program",
        "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
        "return_not_a_duplicate",
        "return_of_erroneous_or_reversing_debit",
        "return_of_improper_credit_entry",
        "return_of_improper_debit_entry",
        "return_of_xck_entry",
        "source_document_presented_for_payment",
        "state_law_affecting_rck_acceptance",
        "stop_payment_on_item_related_to_rck_entry",
        "stop_payment_on_source_document",
        "timely_original_return",
        "trace_number_error",
        "untimely_dishonored_return",
        "untimely_return",
    ]
    """Why the ACH Transfer was returned.

    This reason code is sent by the receiving bank back to Increase.

    - `insufficient_fund` - Code R01. Insufficient funds in the receiving account.
      Sometimes abbreviated to NSF.
    - `no_account` - Code R03. The account does not exist or the receiving bank was
      unable to locate it.
    - `account_closed` - Code R02. The account is closed at the receiving bank.
    - `invalid_account_number_structure` - Code R04. The account number is invalid
      at the receiving bank.
    - `account_frozen_entry_returned_per_ofac_instruction` - Code R16. The account
      at the receiving bank was frozen per the Office of Foreign Assets Control.
    - `credit_entry_refused_by_receiver` - Code R23. The receiving bank account
      refused a credit transfer.
    - `unauthorized_debit_to_consumer_account_using_corporate_sec_code` - Code R05.
      The receiving bank rejected because of an incorrect Standard Entry Class code.
    - `corporate_customer_advised_not_authorized` - Code R29. The corporate customer
      at the receiving bank reversed the transfer.
    - `payment_stopped` - Code R08. The receiving bank stopped payment on this
      transfer.
    - `non_transaction_account` - Code R20. The receiving bank account does not
      perform transfers.
    - `uncollected_funds` - Code R09. The receiving bank account does not have
      enough available balance for the transfer.
    - `routing_number_check_digit_error` - Code R28. The routing number is
      incorrect.
    - `customer_advised_unauthorized_improper_ineligible_or_incomplete` - Code R10.
      The customer at the receiving bank reversed the transfer.
    - `amount_field_error` - Code R19. The amount field is incorrect or too large.
    - `authorization_revoked_by_customer` - Code R07. The customer at the receiving
      institution informed their bank that they have revoked authorization for a
      previously authorized transfer.
    - `invalid_ach_routing_number` - Code R13. The routing number is invalid.
    - `file_record_edit_criteria` - Code R17. The receiving bank is unable to
      process a field in the transfer.
    - `enr_invalid_individual_name` - Code R45. The individual name field was
      invalid.
    - `returned_per_odfi_request` - Code R06. The originating financial institution
      asked for this transfer to be returned. The receiving bank is complying with
      the request.
    - `limited_participation_dfi` - Code R34. The receiving bank's regulatory
      supervisor has limited their participation in the ACH network.
    - `incorrectly_coded_outbound_international_payment` - Code R85. The outbound
      international ACH transfer was incorrect.
    - `account_sold_to_another_dfi` - Code R12. A rare return reason. The account
      was sold to another bank.
    - `addenda_error` - Code R25. The addenda record is incorrect or missing.
    - `beneficiary_or_account_holder_deceased` - Code R15. A rare return reason. The
      account holder is deceased.
    - `customer_advised_not_within_authorization_terms` - Code R11. A rare return
      reason. The customer authorized some payment to the sender, but this payment
      was not in error.
    - `corrected_return` - Code R74. A rare return reason. Sent in response to a
      return that was returned with code `field_error`. The latest return should
      include the corrected field(s).
    - `duplicate_entry` - Code R24. A rare return reason. The receiving bank
      received an exact duplicate entry with the same trace number and amount.
    - `duplicate_return` - Code R67. A rare return reason. The return this message
      refers to was a duplicate.
    - `enr_duplicate_enrollment` - Code R47. A rare return reason. Only used for US
      Government agency non-monetary automatic enrollment messages.
    - `enr_invalid_dfi_account_number` - Code R43. A rare return reason. Only used
      for US Government agency non-monetary automatic enrollment messages.
    - `enr_invalid_individual_id_number` - Code R44. A rare return reason. Only used
      for US Government agency non-monetary automatic enrollment messages.
    - `enr_invalid_representative_payee_indicator` - Code R46. A rare return reason.
      Only used for US Government agency non-monetary automatic enrollment messages.
    - `enr_invalid_transaction_code` - Code R41. A rare return reason. Only used for
      US Government agency non-monetary automatic enrollment messages.
    - `enr_return_of_enr_entry` - Code R40. A rare return reason. Only used for US
      Government agency non-monetary automatic enrollment messages.
    - `enr_routing_number_check_digit_error` - Code R42. A rare return reason. Only
      used for US Government agency non-monetary automatic enrollment messages.
    - `entry_not_processed_by_gateway` - Code R84. A rare return reason. The
      International ACH Transfer cannot be processed by the gateway.
    - `field_error` - Code R69. A rare return reason. One or more of the fields in
      the ACH were malformed.
    - `foreign_receiving_dfi_unable_to_settle` - Code R83. A rare return reason. The
      Foreign receiving bank was unable to settle this ACH transfer.
    - `iat_entry_coding_error` - Code R80. A rare return reason. The International
      ACH Transfer is malformed.
    - `improper_effective_entry_date` - Code R18. A rare return reason. The ACH has
      an improper effective entry date field.
    - `improper_source_document_source_document_presented` - Code R39. A rare return
      reason. The source document related to this ACH, usually an ACH check
      conversion, was presented to the bank.
    - `invalid_company_id` - Code R21. A rare return reason. The Company ID field of
      the ACH was invalid.
    - `invalid_foreign_receiving_dfi_identification` - Code R82. A rare return
      reason. The foreign receiving bank identifier for an International ACH
      Transfer was invalid.
    - `invalid_individual_id_number` - Code R22. A rare return reason. The
      Individual ID number field of the ACH was invalid.
    - `item_and_rck_entry_presented_for_payment` - Code R53. A rare return reason.
      Both the Represented Check ("RCK") entry and the original check were presented
      to the bank.
    - `item_related_to_rck_entry_is_ineligible` - Code R51. A rare return reason.
      The Represented Check ("RCK") entry is ineligible.
    - `mandatory_field_error` - Code R26. A rare return reason. The ACH is missing a
      required field.
    - `misrouted_dishonored_return` - Code R71. A rare return reason. The receiving
      bank does not recognize the routing number in a dishonored return entry.
    - `misrouted_return` - Code R61. A rare return reason. The receiving bank does
      not recognize the routing number in a return entry.
    - `no_errors_found` - Code R76. A rare return reason. Sent in response to a
      return, the bank does not find the errors alleged by the returning bank.
    - `non_acceptance_of_r62_dishonored_return` - Code R77. A rare return reason.
      The receiving bank does not accept the return of the erroneous debit. The
      funds are not available at the receiving bank.
    - `non_participant_in_iat_program` - Code R81. A rare return reason. The
      receiving bank does not accept International ACH Transfers.
    - `permissible_return_entry` - Code R31. A rare return reason. A return that has
      been agreed to be accepted by the receiving bank, despite falling outside of
      the usual return timeframe.
    - `permissible_return_entry_not_accepted` - Code R70. A rare return reason. The
      receiving bank had not approved this return.
    - `rdfi_non_settlement` - Code R32. A rare return reason. The receiving bank
      could not settle this transaction.
    - `rdfi_participant_in_check_truncation_program` - Code R30. A rare return
      reason. The receiving bank does not accept Check Truncation ACH transfers.
    - `representative_payee_deceased_or_unable_to_continue_in_that_capacity` - Code
      R14. A rare return reason. The payee is deceased.
    - `return_not_a_duplicate` - Code R75. A rare return reason. The originating
      bank disputes that an earlier `duplicate_entry` return was actually a
      duplicate.
    - `return_of_erroneous_or_reversing_debit` - Code R62. A rare return reason. The
      originating financial institution made a mistake and this return corrects it.
    - `return_of_improper_credit_entry` - Code R36. A rare return reason. Return of
      a malformed credit entry.
    - `return_of_improper_debit_entry` - Code R35. A rare return reason. Return of a
      malformed debit entry.
    - `return_of_xck_entry` - Code R33. A rare return reason. Return of a Destroyed
      Check ("XKC") entry.
    - `source_document_presented_for_payment` - Code R37. A rare return reason. The
      source document related to this ACH, usually an ACH check conversion, was
      presented to the bank.
    - `state_law_affecting_rck_acceptance` - Code R50. A rare return reason. State
      law prevents the bank from accepting the Represented Check ("RCK") entry.
    - `stop_payment_on_item_related_to_rck_entry` - Code R52. A rare return reason.
      A stop payment was issued on a Represented Check ("RCK") entry.
    - `stop_payment_on_source_document` - Code R38. A rare return reason. The source
      attached to the ACH, usually an ACH check conversion, includes a stop payment.
    - `timely_original_return` - Code R73. A rare return reason. The bank receiving
      an `untimely_return` believes it was on time.
    - `trace_number_error` - Code R27. A rare return reason. An ACH return's trace
      number does not match an originated ACH.
    - `untimely_dishonored_return` - Code R72. A rare return reason. The dishonored
      return was sent too late.
    - `untimely_return` - Code R68. A rare return reason. The return was sent too
      late.
    """

    trace_number: str
    """A 15 digit number that was generated by the bank that initiated the return.

    The trace number of the return is different than that of the original transfer.
    ACH trace numbers are not unique, but along with the amount and date this number
    can be used to identify the ACH return at the bank that initiated it.
    """

    transaction_id: str
    """The identifier of the Transaction associated with this return."""

    transfer_id: str
    """The identifier of the ACH Transfer associated with this return."""


class Settlement(BaseModel):
    settled_at: datetime.datetime
    """
    When the funds for this transfer have settled at the destination bank at the
    Federal Reserve.
    """


class Submission(BaseModel):
    effective_date: datetime.date
    """The ACH transfer's effective date as sent to the Federal Reserve.

    If a specific date was configured using `preferred_effective_date`, this will
    match that value. Otherwise, it will be the date selected (following the
    specified settlement schedule) at the time the transfer was submitted.
    """

    expected_funds_settlement_at: datetime.datetime
    """When the transfer is expected to settle in the recipient's account.

    Credits may be available sooner, at the receiving banks discretion. The FedACH
    schedule is published
    [here](https://www.frbservices.org/resources/resource-centers/same-day-ach/fedach-processing-schedule.html).
    """

    expected_settlement_schedule: Literal["same_day", "future_dated"]
    """The settlement schedule the transfer is expected to follow.

    This expectation takes into account the `effective_date`, `submitted_at`, and
    the amount of the transfer.

    - `same_day` - The transfer is expected to settle same-day.
    - `future_dated` - The transfer is expected to settle on a future date.
    """

    submitted_at: datetime.datetime
    """When the ACH transfer was sent to FedACH."""

    trace_number: str
    """
    A 15 digit number recorded in the Nacha file and transmitted to the receiving
    bank. Along with the amount, date, and originating routing number, this can be
    used to identify the ACH transfer at the receiving bank. ACH trace numbers are
    not unique, but are
    [used to correlate returns](https://increase.com/documentation/ach-returns#ach-returns).
    """


class ACHTransfer(BaseModel):
    id: str
    """The ACH transfer's identifier."""

    account_id: str
    """The Account to which the transfer belongs."""

    account_number: str
    """The destination account number."""

    acknowledgement: Optional[Acknowledgement] = None
    """
    After the transfer is acknowledged by FedACH, this will contain supplemental
    details. The Federal Reserve sends an acknowledgement message for each file that
    Increase submits.
    """

    addenda: Optional[Addenda] = None
    """Additional information that will be sent to the recipient."""

    amount: int
    """The transfer amount in USD cents.

    A positive amount indicates a credit transfer pushing funds to the receiving
    account. A negative amount indicates a debit transfer pulling funds from the
    receiving account.
    """

    approval: Optional[Approval] = None
    """
    If your account requires approvals for transfers and the transfer was approved,
    this will contain details of the approval.
    """

    cancellation: Optional[Cancellation] = None
    """
    If your account requires approvals for transfers and the transfer was not
    approved, this will contain details of the cancellation.
    """

    company_descriptive_date: Optional[str] = None
    """The description of the date of the transfer."""

    company_discretionary_data: Optional[str] = None
    """The data you chose to associate with the transfer."""

    company_entry_description: Optional[str] = None
    """The description of the transfer you set to be shown to the recipient."""

    company_id: str
    """The company ID associated with the transfer."""

    company_name: Optional[str] = None
    """The name by which the recipient knows you."""

    created_at: datetime.datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    created_by: Optional[CreatedBy] = None
    """What object created the transfer, either via the API or the dashboard."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For ACH transfers this is always equal to `usd`.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    destination_account_holder: Literal["business", "individual", "unknown"]
    """
    The type of entity that owns the account to which the ACH Transfer is being
    sent.

    - `business` - The External Account is owned by a business.
    - `individual` - The External Account is owned by an individual.
    - `unknown` - It's unknown what kind of entity owns the External Account.
    """

    external_account_id: Optional[str] = None
    """The identifier of the External Account the transfer was made to, if any."""

    funding: Literal["checking", "savings", "general_ledger"]
    """The type of the account to which the transfer will be sent.

    - `checking` - A checking account.
    - `savings` - A savings account.
    - `general_ledger` - A bank's general ledger. Uncommon.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    inbound_funds_hold: Optional[InboundFundsHold] = None
    """Increase will sometimes hold the funds for ACH debit transfers.

    If funds are held, this sub-object will contain details of the hold.
    """

    individual_id: Optional[str] = None
    """Your identifier for the transfer recipient."""

    individual_name: Optional[str] = None
    """The name of the transfer recipient.

    This value is information and not verified by the recipient's bank.
    """

    network: Literal["ach"]
    """The transfer's network."""

    notifications_of_change: List[NotificationsOfChange]
    """
    If the receiving bank accepts the transfer but notifies that future transfers
    should use different details, this will contain those details.
    """

    pending_transaction_id: Optional[str] = None
    """The ID for the pending transaction representing the transfer.

    A pending transaction is created when the transfer
    [requires approval](https://increase.com/documentation/transfer-approvals#transfer-approvals)
    by someone else in your organization.
    """

    preferred_effective_date: PreferredEffectiveDate
    """Configuration for how the effective date of the transfer will be set.

    This determines same-day vs future-dated settlement timing. If not set, defaults
    to a `settlement_schedule` of `same_day`. If set, exactly one of the child
    attributes must be set.
    """

    return_: Optional[Return] = FieldInfo(alias="return", default=None)
    """If your transfer is returned, this will contain details of the return."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    settlement: Optional[Settlement] = None
    """
    A subhash containing information about when and how the transfer settled at the
    Federal Reserve.
    """

    standard_entry_class_code: Literal[
        "corporate_credit_or_debit",
        "corporate_trade_exchange",
        "prearranged_payments_and_deposit",
        "internet_initiated",
    ]
    """The Standard Entry Class (SEC) code to use for the transfer.

    - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
    - `corporate_trade_exchange` - Corporate Trade Exchange (CTX).
    - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
    - `internet_initiated` - Internet Initiated (WEB).
    """

    statement_descriptor: str
    """The descriptor that will show on the recipient's bank statement."""

    status: Literal[
        "pending_approval",
        "pending_transfer_session_confirmation",
        "canceled",
        "pending_submission",
        "pending_reviewing",
        "requires_attention",
        "rejected",
        "submitted",
        "returned",
    ]
    """The lifecycle status of the transfer.

    - `pending_approval` - The transfer is pending approval.
    - `pending_transfer_session_confirmation` - The transfer belongs to a Transfer
      Session that is pending confirmation.
    - `canceled` - The transfer has been canceled.
    - `pending_submission` - The transfer is pending submission to the Federal
      Reserve.
    - `pending_reviewing` - The transfer is pending review by Increase.
    - `requires_attention` - The transfer requires attention from an Increase
      operator.
    - `rejected` - The transfer has been rejected.
    - `submitted` - The transfer is complete.
    - `returned` - The transfer has been returned.
    """

    submission: Optional[Submission] = None
    """
    After the transfer is submitted to FedACH, this will contain supplemental
    details. Increase batches transfers and submits a file to the Federal Reserve
    roughly every 30 minutes. The Federal Reserve processes ACH transfers during
    weekdays according to their
    [posted schedule](https://www.frbservices.org/resources/resource-centers/same-day-ach/fedach-processing-schedule.html).
    """

    transaction_id: Optional[str] = None
    """The ID for the transaction funding the transfer."""

    type: Literal["ach_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `ach_transfer`.
    """
