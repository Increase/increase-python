# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "InboundACHTransfer",
    "Acceptance",
    "Addenda",
    "AddendaFreeform",
    "AddendaFreeformEntry",
    "Decline",
    "InternationalAddenda",
    "NotificationOfChange",
    "Settlement",
    "TransferReturn",
]


class Acceptance(BaseModel):
    accepted_at: datetime
    """The time at which the transfer was accepted."""

    transaction_id: str
    """The id of the transaction for the accepted transfer."""


class AddendaFreeformEntry(BaseModel):
    payment_related_information: str
    """The payment related information passed in the addendum."""


class AddendaFreeform(BaseModel):
    entries: List[AddendaFreeformEntry]
    """Each entry represents an addendum received from the originator."""


class Addenda(BaseModel):
    category: Literal["freeform"]
    """The type of addendum.

    - `freeform` - Unstructured addendum.
    """

    freeform: Optional[AddendaFreeform] = None
    """Unstructured `payment_related_information` passed through by the originator."""


class Decline(BaseModel):
    declined_at: datetime
    """The time at which the transfer was declined."""

    declined_transaction_id: str
    """The id of the transaction for the declined transfer."""

    reason: Literal[
        "ach_route_canceled",
        "ach_route_disabled",
        "breaches_limit",
        "entity_not_active",
        "group_locked",
        "transaction_not_allowed",
        "user_initiated",
        "insufficient_funds",
        "returned_per_odfi_request",
        "authorization_revoked_by_customer",
        "payment_stopped",
        "customer_advised_unauthorized_improper_ineligible_or_incomplete",
        "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
        "beneficiary_or_account_holder_deceased",
        "credit_entry_refused_by_receiver",
        "duplicate_entry",
        "corporate_customer_advised_not_authorized",
    ]
    """The reason for the transfer decline.

    - `ach_route_canceled` - The account number is canceled.
    - `ach_route_disabled` - The account number is disabled.
    - `breaches_limit` - The transaction would cause an Increase limit to be
      exceeded.
    - `entity_not_active` - The account's entity is not active.
    - `group_locked` - Your account is inactive.
    - `transaction_not_allowed` - The transaction is not allowed per Increase's
      terms.
    - `user_initiated` - Your integration declined this transfer via the API.
    - `insufficient_funds` - Your account contains insufficient funds.
    - `returned_per_odfi_request` - The originating financial institution asked for
      this transfer to be returned. The receiving bank is complying with the
      request.
    - `authorization_revoked_by_customer` - The customer no longer authorizes this
      transaction.
    - `payment_stopped` - The customer asked for the payment to be stopped.
    - `customer_advised_unauthorized_improper_ineligible_or_incomplete` - The
      customer advises that the debit was unauthorized.
    - `representative_payee_deceased_or_unable_to_continue_in_that_capacity` - The
      payee is deceased.
    - `beneficiary_or_account_holder_deceased` - The account holder is deceased.
    - `credit_entry_refused_by_receiver` - The customer refused a credit entry.
    - `duplicate_entry` - The account holder identified this transaction as a
      duplicate.
    - `corporate_customer_advised_not_authorized` - The corporate customer no longer
      authorizes this transaction.
    """


class InternationalAddenda(BaseModel):
    destination_country_code: str
    """
    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the destination country.
    """

    destination_currency_code: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code for the
    destination bank account.
    """

    foreign_exchange_indicator: Literal["fixed_to_variable", "variable_to_fixed", "fixed_to_fixed"]
    """A description of how the foreign exchange rate was calculated.

    - `fixed_to_variable` - The originator chose an amount in their own currency.
      The settled amount in USD was converted using the exchange rate.
    - `variable_to_fixed` - The originator chose an amount to settle in USD. The
      originator's amount was variable; known only after the foreign exchange
      conversion.
    - `fixed_to_fixed` - The amount was originated and settled as a fixed amount in
      USD. There is no foreign exchange conversion.
    """

    foreign_exchange_reference: Optional[str] = None
    """
    Depending on the `foreign_exchange_reference_indicator`, an exchange rate or a
    reference to a well-known rate.
    """

    foreign_exchange_reference_indicator: Literal["foreign_exchange_rate", "foreign_exchange_reference_number", "blank"]
    """
    An instruction of how to interpret the `foreign_exchange_reference` field for
    this Transaction.

    - `foreign_exchange_rate` - The ACH file contains a foreign exchange rate.
    - `foreign_exchange_reference_number` - The ACH file contains a reference to a
      well-known foreign exchange rate.
    - `blank` - There is no foreign exchange for this transfer, so the
      `foreign_exchange_reference` field is blank.
    """

    foreign_payment_amount: int
    """The amount in the minor unit of the foreign payment currency.

    For dollars, for example, this is cents.
    """

    foreign_trace_number: Optional[str] = None
    """A reference number in the foreign banking infrastructure."""

    international_transaction_type_code: Literal[
        "annuity",
        "business_or_commercial",
        "deposit",
        "loan",
        "miscellaneous",
        "mortgage",
        "pension",
        "remittance",
        "rent_or_lease",
        "salary_or_payroll",
        "tax",
        "accounts_receivable",
        "back_office_conversion",
        "machine_transfer",
        "point_of_purchase",
        "point_of_sale",
        "represented_check",
        "shared_network_transaction",
        "telphone_initiated",
        "internet_initiated",
    ]
    """The type of transfer. Set by the originator.

    - `annuity` - Sent as `ANN` in the Nacha file.
    - `business_or_commercial` - Sent as `BUS` in the Nacha file.
    - `deposit` - Sent as `DEP` in the Nacha file.
    - `loan` - Sent as `LOA` in the Nacha file.
    - `miscellaneous` - Sent as `MIS` in the Nacha file.
    - `mortgage` - Sent as `MOR` in the Nacha file.
    - `pension` - Sent as `PEN` in the Nacha file.
    - `remittance` - Sent as `REM` in the Nacha file.
    - `rent_or_lease` - Sent as `RLS` in the Nacha file.
    - `salary_or_payroll` - Sent as `SAL` in the Nacha file.
    - `tax` - Sent as `TAX` in the Nacha file.
    - `accounts_receivable` - Sent as `ARC` in the Nacha file.
    - `back_office_conversion` - Sent as `BOC` in the Nacha file.
    - `machine_transfer` - Sent as `MTE` in the Nacha file.
    - `point_of_purchase` - Sent as `POP` in the Nacha file.
    - `point_of_sale` - Sent as `POS` in the Nacha file.
    - `represented_check` - Sent as `RCK` in the Nacha file.
    - `shared_network_transaction` - Sent as `SHR` in the Nacha file.
    - `telphone_initiated` - Sent as `TEL` in the Nacha file.
    - `internet_initiated` - Sent as `WEB` in the Nacha file.
    """

    originating_currency_code: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code for the
    originating bank account.
    """

    originating_depository_financial_institution_branch_country: str
    """
    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the originating branch country.
    """

    originating_depository_financial_institution_id: str
    """An identifier for the originating bank.

    One of an International Bank Account Number (IBAN) bank identifier, SWIFT Bank
    Identification Code (BIC), or a domestic identifier like a US Routing Number.
    """

    originating_depository_financial_institution_id_qualifier: Literal[
        "national_clearing_system_number", "bic_code", "iban"
    ]
    """
    An instruction of how to interpret the
    `originating_depository_financial_institution_id` field for this Transaction.

    - `national_clearing_system_number` - A domestic clearing system number. In the
      US, for example, this is the American Banking Association (ABA) routing
      number.
    - `bic_code` - The SWIFT Bank Identifier Code (BIC) of the bank.
    - `iban` - An International Bank Account Number.
    """

    originating_depository_financial_institution_name: str
    """The name of the originating bank.

    Sometimes this will refer to an American bank and obscure the correspondent
    foreign bank.
    """

    originator_city: str
    """A portion of the originator address. This may be incomplete."""

    originator_country: str
    """A portion of the originator address.

    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the originator country.
    """

    originator_identification: str
    """An identifier for the originating company.

    This is generally stable across multiple ACH transfers.
    """

    originator_name: str
    """Either the name of the originator or an intermediary money transmitter."""

    originator_postal_code: Optional[str] = None
    """A portion of the originator address. This may be incomplete."""

    originator_state_or_province: Optional[str] = None
    """A portion of the originator address. This may be incomplete."""

    originator_street_address: str
    """A portion of the originator address. This may be incomplete."""

    payment_related_information: Optional[str] = None
    """A description field set by the originator."""

    payment_related_information2: Optional[str] = None
    """A description field set by the originator."""

    receiver_city: str
    """A portion of the receiver address. This may be incomplete."""

    receiver_country: str
    """A portion of the receiver address.

    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the receiver country.
    """

    receiver_identification_number: Optional[str] = None
    """An identification number the originator uses for the receiver."""

    receiver_postal_code: Optional[str] = None
    """A portion of the receiver address. This may be incomplete."""

    receiver_state_or_province: Optional[str] = None
    """A portion of the receiver address. This may be incomplete."""

    receiver_street_address: str
    """A portion of the receiver address. This may be incomplete."""

    receiving_company_or_individual_name: str
    """The name of the receiver of the transfer. This is not verified by Increase."""

    receiving_depository_financial_institution_country: str
    """
    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the receiving bank country.
    """

    receiving_depository_financial_institution_id: str
    """An identifier for the receiving bank.

    One of an International Bank Account Number (IBAN) bank identifier, SWIFT Bank
    Identification Code (BIC), or a domestic identifier like a US Routing Number.
    """

    receiving_depository_financial_institution_id_qualifier: Literal[
        "national_clearing_system_number", "bic_code", "iban"
    ]
    """
    An instruction of how to interpret the
    `receiving_depository_financial_institution_id` field for this Transaction.

    - `national_clearing_system_number` - A domestic clearing system number. In the
      US, for example, this is the American Banking Association (ABA) routing
      number.
    - `bic_code` - The SWIFT Bank Identifier Code (BIC) of the bank.
    - `iban` - An International Bank Account Number.
    """

    receiving_depository_financial_institution_name: str
    """The name of the receiving bank, as set by the sending financial institution."""


class NotificationOfChange(BaseModel):
    updated_account_number: Optional[str] = None
    """The new account number provided in the notification of change."""

    updated_routing_number: Optional[str] = None
    """The new account number provided in the notification of change."""


class Settlement(BaseModel):
    settled_at: datetime
    """
    When the funds for this transfer settle at the recipient bank at the Federal
    Reserve.
    """

    settlement_schedule: Literal["same_day", "future_dated"]
    """The settlement schedule this transfer follows.

    - `same_day` - The transfer is expected to settle same-day.
    - `future_dated` - The transfer is expected to settle on a future date.
    """


class TransferReturn(BaseModel):
    reason: Literal[
        "insufficient_funds",
        "returned_per_odfi_request",
        "authorization_revoked_by_customer",
        "payment_stopped",
        "customer_advised_unauthorized_improper_ineligible_or_incomplete",
        "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
        "beneficiary_or_account_holder_deceased",
        "credit_entry_refused_by_receiver",
        "duplicate_entry",
        "corporate_customer_advised_not_authorized",
    ]
    """The reason for the transfer return.

    - `insufficient_funds` - The customer's account has insufficient funds. This
      reason is only allowed for debits. The Nacha return code is R01.
    - `returned_per_odfi_request` - The originating financial institution asked for
      this transfer to be returned. The receiving bank is complying with the
      request. The Nacha return code is R06.
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

    returned_at: datetime
    """The time at which the transfer was returned."""

    transaction_id: str
    """The id of the transaction for the returned transfer."""


class InboundACHTransfer(BaseModel):
    id: str
    """The inbound ACH transfer's identifier."""

    acceptance: Optional[Acceptance] = None
    """If your transfer is accepted, this will contain details of the acceptance."""

    account_id: str
    """The Account to which the transfer belongs."""

    account_number_id: str
    """The identifier of the Account Number to which this transfer was sent."""

    addenda: Optional[Addenda] = None
    """Additional information sent from the originator."""

    amount: int
    """The transfer amount in USD cents."""

    automatically_resolves_at: datetime
    """The time at which the transfer will be automatically resolved."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the inbound ACH transfer was created.
    """

    decline: Optional[Decline] = None
    """If your transfer is declined, this will contain details of the decline."""

    direction: Literal["credit", "debit"]
    """The direction of the transfer.

    - `credit` - Credit
    - `debit` - Debit
    """

    effective_date: date
    """The effective date of the transfer.

    This is sent by the sending bank and is a factor in determining funds
    availability.
    """

    international_addenda: Optional[InternationalAddenda] = None
    """
    If the Inbound ACH Transfer has a Standard Entry Class Code of IAT, this will
    contain fields pertaining to the International ACH Transaction.
    """

    notification_of_change: Optional[NotificationOfChange] = None
    """
    If you initiate a notification of change in response to the transfer, this will
    contain its details.
    """

    originator_company_descriptive_date: Optional[str] = None
    """The descriptive date of the transfer."""

    originator_company_discretionary_data: Optional[str] = None
    """The additional information included with the transfer."""

    originator_company_entry_description: str
    """The description of the transfer."""

    originator_company_id: str
    """The id of the company that initiated the transfer."""

    originator_company_name: str
    """The name of the company that initiated the transfer."""

    originator_routing_number: str
    """
    The American Banking Association (ABA) routing number of the bank originating
    the transfer.
    """

    receiver_id_number: Optional[str] = None
    """The id of the receiver of the transfer."""

    receiver_name: Optional[str] = None
    """The name of the receiver of the transfer."""

    settlement: Settlement
    """
    A subhash containing information about when and how the transfer settled at the
    Federal Reserve.
    """

    standard_entry_class_code: Literal[
        "corporate_credit_or_debit",
        "corporate_trade_exchange",
        "prearranged_payments_and_deposit",
        "internet_initiated",
        "point_of_sale",
        "telephone_initiated",
        "customer_initiated",
        "accounts_receivable",
        "machine_transfer",
        "shared_network_transaction",
        "represented_check",
        "back_office_conversion",
        "point_of_purchase",
        "check_truncation",
        "destroyed_check",
        "international_ach_transaction",
    ]
    """The Standard Entry Class (SEC) code of the transfer.

    - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
    - `corporate_trade_exchange` - Corporate Trade Exchange (CTX).
    - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
    - `internet_initiated` - Internet Initiated (WEB).
    - `point_of_sale` - Point of Sale (POS).
    - `telephone_initiated` - Telephone Initiated (TEL).
    - `customer_initiated` - Customer Initiated (CIE).
    - `accounts_receivable` - Accounts Receivable (ARC).
    - `machine_transfer` - Machine Transfer (MTE).
    - `shared_network_transaction` - Shared Network Transaction (SHR).
    - `represented_check` - Represented Check (RCK).
    - `back_office_conversion` - Back Office Conversion (BOC).
    - `point_of_purchase` - Point of Purchase (POP).
    - `check_truncation` - Check Truncation (TRC).
    - `destroyed_check` - Destroyed Check (XCK).
    - `international_ach_transaction` - International ACH Transaction (IAT).
    """

    status: Literal["pending", "declined", "accepted", "returned"]
    """The status of the transfer.

    - `pending` - The Inbound ACH Transfer is awaiting action, will transition
      automatically if no action is taken.
    - `declined` - The Inbound ACH Transfer has been declined.
    - `accepted` - The Inbound ACH Transfer is accepted.
    - `returned` - The Inbound ACH Transfer has been returned.
    """

    trace_number: str
    """A 15 digit number set by the sending bank and transmitted to the receiving bank.

    Along with the amount, date, and originating routing number, this can be used to
    identify the ACH transfer. ACH trace numbers are not unique, but are
    [used to correlate returns](https://increase.com/documentation/ach-returns#ach-returns).
    """

    transfer_return: Optional[TransferReturn] = None
    """If your transfer is returned, this will contain details of the return."""

    type: Literal["inbound_ach_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_ach_transfer`.
    """
