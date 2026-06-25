# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ACHTransferCreateParams",
    "Addenda",
    "AddendaFreeform",
    "AddendaFreeformEntry",
    "AddendaPaymentOrderRemittanceAdvice",
    "AddendaPaymentOrderRemittanceAdviceInvoice",
    "PreferredEffectiveDate",
]


class ACHTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Increase identifier for the account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in USD cents.

    A positive amount originates a credit transfer pushing funds to the receiving
    account. A negative amount originates a debit transfer pulling funds from the
    receiving account.
    """

    statement_descriptor: Required[str]
    """A description you choose to give the transfer.

    This will be saved with the transfer details, displayed in the dashboard, and
    returned by the API. If `individual_name` and `company_name` are not explicitly
    set by this API, the `statement_descriptor` will be sent in those fields to the
    receiving bank to help the customer recognize the transfer. You are highly
    encouraged to pass `individual_name` and `company_name` instead of relying on
    this fallback.
    """

    account_number: str
    """The receiver's account number.

    For credit transfers (positive `amount`) this is the account that funds will be
    sent to. For debit transfers (negative `amount`) this is the account that funds
    will be pulled from.
    """

    addenda: Addenda
    """Additional information passed through to the receiving bank with the transfer.

    Most ACH transfers do not need this. Only set this if your recipient has asked
    for addendum data, typically unstructured remittance information. Corporate
    Trade Exchange (CTX) flows can carry structured X12 remittance advice instead.
    """

    company_descriptive_date: str
    """
    A description of the transfer date (typically `YYMMDD`), sent in the company
    batch header. This value is informational and does not affect funds movement,
    settlement timing, or returns. Only set this if your recipient has asked for it.
    """

    company_discretionary_data: str
    """Custom data sent in the company batch header.

    This value is informational and does not affect funds movement, settlement
    timing, or returns. Most ACH transfers do not need this. Only set this if your
    recipient has asked for it.
    """

    company_entry_description: str
    """A short description sent in the company batch header.

    Most receivers do not surface this. Only set this if your recipient has asked
    for a specific value or if Nacha mandates one for your Standard Entry Class
    (SEC) code and use case. For example, Prearranged Payment and Deposit (PPD)
    payroll credits must use `PAYROLL`, and reversals must use `REVERSAL`.
    """

    company_name: str
    """The name by which the recipient knows you, sent in the company batch header.

    We recommend setting this on every transfer; if you do not, we fall back to the
    ACH company name configured on your account.
    """

    destination_account_holder: Literal["business", "individual", "unknown"]
    """The type of entity that owns the receiver's account.

    - `business` - The External Account is owned by a business.
    - `individual` - The External Account is owned by an individual.
    - `unknown` - It's unknown what kind of entity owns the External Account.
    """

    external_account_id: str
    """The ID of an External Account to initiate a transfer to.

    If this parameter is provided, `account_number`, `routing_number`, and `funding`
    must be absent.
    """

    funding: Literal["checking", "savings", "loan", "general_ledger"]
    """The type of the receiver's bank account.

    - `checking` - A checking account.
    - `savings` - A savings account.
    - `loan` - A loan account used in a lender-borrower relationship. Uncommon.
    - `general_ledger` - A bank's general ledger. Uncommon.
    """

    individual_id: str
    """Your internal identifier for the transfer recipient.

    This value is informational and not verified by the recipient's bank. Most
    callers can leave this unset.
    """

    individual_name: str
    """The name of the transfer recipient.

    This value is informational and not verified by the recipient's bank.
    """

    preferred_effective_date: PreferredEffectiveDate
    """Configuration for how the effective date of the transfer will be set.

    This determines same-day vs future-dated settlement timing. If not set, defaults
    to a `settlement_schedule` of `same_day`. If set, exactly one of the child
    attributes must be set.
    """

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    routing_number: str
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) of the
    receiver's bank.
    """

    standard_entry_class_code: Literal[
        "corporate_credit_or_debit",
        "corporate_trade_exchange",
        "prearranged_payments_and_deposit",
        "internet_initiated",
    ]
    """
    The
    [Standard Entry Class (SEC) code](/documentation/ach-standard-entry-class-codes)
    to use for the transfer. If not provided, the default is
    `corporate_credit_or_debit`.

    - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD) is used for
      business-to-business payments.
    - `corporate_trade_exchange` - Corporate Trade Exchange (CTX) allows for
      including extensive remittance information with business-to-business payments.
    - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD)
      is used for credits or debits originated by an organization to a consumer,
      such as payroll direct deposits.
    - `internet_initiated` - Internet Initiated (WEB) is used for consumer payments
      initiated or authorized via the Internet. Debits can only be initiated by
      non-consumers to debit a consumer’s account. Credits can only be used for
      consumer to consumer transactions.
    """

    transaction_timing: Literal["synchronous", "asynchronous"]
    """The timing of the transaction.

    - `synchronous` - A Transaction will be created immediately.
    - `asynchronous` - A Transaction will be created when the funds settle at the
      Federal Reserve.
    """


class AddendaFreeformEntry(TypedDict, total=False):
    payment_related_information: Required[str]
    """The payment related information passed in the addendum."""


class AddendaFreeform(TypedDict, total=False):
    """Unstructured `payment_related_information` passed through with the transfer.

    Required if and only if `category` is `freeform`.
    """

    entries: Required[Iterable[AddendaFreeformEntry]]
    """Each entry represents an addendum sent with the transfer.

    Sending more than one addendum is only supported for transfers with
    `standard_entry_class_code` of `corporate_trade_exchange` (CTX).
    """


class AddendaPaymentOrderRemittanceAdviceInvoice(TypedDict, total=False):
    invoice_number: Required[str]
    """The invoice number for this reference, determined in advance with the receiver."""

    paid_amount: Required[int]
    """The amount that was paid for this invoice in the minor unit of its currency.

    For dollars, for example, this is cents.
    """


class AddendaPaymentOrderRemittanceAdvice(TypedDict, total=False):
    """Structured ASC X12 820 remittance advice records.

    Please reach out to [support@increase.com](mailto:support@increase.com) for more information. Required if and only if `category` is `payment_order_remittance_advice`.
    """

    invoices: Required[Iterable[AddendaPaymentOrderRemittanceAdviceInvoice]]
    """ASC X12 RMR records for this specific transfer."""


class Addenda(TypedDict, total=False):
    """Additional information passed through to the receiving bank with the transfer.

    Most ACH transfers do not need this. Only set this if your recipient has asked for addendum data, typically unstructured remittance information. Corporate Trade Exchange (CTX) flows can carry structured X12 remittance advice instead.
    """

    category: Required[Literal["freeform", "payment_order_remittance_advice"]]
    """The type of addenda to pass with the transfer.

    - `freeform` - Unstructured `payment_related_information` passed through with
      the transfer.
    - `payment_order_remittance_advice` - Structured ASC X12 820 remittance advice
      records. Please reach out to
      [support@increase.com](mailto:support@increase.com) for more information.
    """

    freeform: AddendaFreeform
    """Unstructured `payment_related_information` passed through with the transfer.

    Required if and only if `category` is `freeform`.
    """

    payment_order_remittance_advice: AddendaPaymentOrderRemittanceAdvice
    """Structured ASC X12 820 remittance advice records.

    Please reach out to [support@increase.com](mailto:support@increase.com) for more
    information. Required if and only if `category` is
    `payment_order_remittance_advice`.
    """


class PreferredEffectiveDate(TypedDict, total=False):
    """Configuration for how the effective date of the transfer will be set.

    This determines same-day vs future-dated settlement timing. If not set, defaults to a `settlement_schedule` of `same_day`. If set, exactly one of the child attributes must be set.
    """

    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """
    A specific date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format to
    use as the effective date when submitting this transfer.
    """

    settlement_schedule: Literal["same_day", "future_dated"]
    """A schedule by which Increase will choose an effective date for the transfer.

    - `same_day` - The chosen effective date will be the same as the ACH processing
      date on which the transfer is submitted. This is necessary, but not sufficient
      for the transfer to be settled same-day: it must also be submitted before the
      last same-day cutoff and be less than or equal to $1,000,000.00.
    - `future_dated` - The chosen effective date will be the business day following
      the ACH processing date on which the transfer is submitted. The transfer will
      be settled on that future day.
    """
