# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Export",
    "AccountStatementBai2",
    "AccountStatementOfx",
    "AccountStatementOfxCreatedAt",
    "AccountVerificationLetter",
    "BalanceCsv",
    "BalanceCsvCreatedAt",
    "BookkeepingAccountBalanceCsv",
    "BookkeepingAccountBalanceCsvCreatedAt",
    "DailyAccountBalanceCsv",
    "DashboardTableCsv",
    "EntityCsv",
    "FeeCsv",
    "FeeCsvCreatedAt",
    "Form1099Int",
    "Form1099Misc",
    "FundingInstructions",
    "Result",
    "TransactionCsv",
    "TransactionCsvCreatedAt",
    "VendorCsv",
    "VoidedCheck",
    "VoidedCheckPayer",
]


class AccountStatementBai2(BaseModel):
    """Details of the account statement BAI2 export.

    This field will be present when the `category` is equal to `account_statement_bai2`.
    """

    account_id: Optional[str] = None
    """Filter results by Account."""

    effective_date: Optional[date] = None
    """The date for which to retrieve the balance."""

    program_id: Optional[str] = None
    """Filter results by Program."""


class AccountStatementOfxCreatedAt(BaseModel):
    """Filter transactions by their created date."""

    after: Optional[datetime] = None
    """Filter results to transactions created after this time."""

    before: Optional[datetime] = None
    """Filter results to transactions created before this time."""


class AccountStatementOfx(BaseModel):
    """Details of the account statement OFX export.

    This field will be present when the `category` is equal to `account_statement_ofx`.
    """

    account_id: str
    """The Account to create a statement for."""

    created_at: Optional[AccountStatementOfxCreatedAt] = None
    """Filter transactions by their created date."""


class AccountVerificationLetter(BaseModel):
    """Details of the account verification letter export.

    This field will be present when the `category` is equal to `account_verification_letter`.
    """

    account_number_id: str
    """The Account Number to create a letter for."""

    balance_date: Optional[date] = None
    """The date of the balance to include in the letter."""


class BalanceCsvCreatedAt(BaseModel):
    """Filter balances by their created date."""

    after: Optional[datetime] = None
    """Filter balances created after this time."""

    before: Optional[datetime] = None
    """Filter balances created before this time."""


class BalanceCsv(BaseModel):
    """Details of the balance CSV export.

    This field will be present when the `category` is equal to `balance_csv`.
    """

    account_id: Optional[str] = None
    """Filter results by Account."""

    created_at: Optional[BalanceCsvCreatedAt] = None
    """Filter balances by their created date."""


class BookkeepingAccountBalanceCsvCreatedAt(BaseModel):
    """Filter balances by their created date."""

    after: Optional[datetime] = None
    """Filter balances created after this time."""

    before: Optional[datetime] = None
    """Filter balances created before this time."""


class BookkeepingAccountBalanceCsv(BaseModel):
    """Details of the bookkeeping account balance CSV export.

    This field will be present when the `category` is equal to `bookkeeping_account_balance_csv`.
    """

    bookkeeping_account_id: Optional[str] = None
    """Filter results by Bookkeeping Account."""

    created_at: Optional[BookkeepingAccountBalanceCsvCreatedAt] = None
    """Filter balances by their created date."""


class DailyAccountBalanceCsv(BaseModel):
    """Details of the daily account balance CSV export.

    This field will be present when the `category` is equal to `daily_account_balance_csv`.
    """

    account_id: Optional[str] = None
    """Filter results by Account."""

    on_or_after_date: Optional[date] = None
    """Filter balances on or after this date."""

    on_or_before_date: Optional[date] = None
    """Filter balances on or before this date."""


class DashboardTableCsv(BaseModel):
    """Details of the dashboard table CSV export.

    This field will be present when the `category` is equal to `dashboard_table_csv`.
    """

    pass


class EntityCsv(BaseModel):
    """Details of the entity CSV export.

    This field will be present when the `category` is equal to `entity_csv`.
    """

    pass


class FeeCsvCreatedAt(BaseModel):
    """Filter fees by their created date.

    The time range must not include any fees that are part of an open fee statement.
    """

    after: Optional[datetime] = None
    """Filter fees created after this time."""

    before: Optional[datetime] = None
    """Filter fees created before this time."""


class FeeCsv(BaseModel):
    """Details of the fee CSV export.

    This field will be present when the `category` is equal to `fee_csv`.
    """

    created_at: Optional[FeeCsvCreatedAt] = None
    """Filter fees by their created date.

    The time range must not include any fees that are part of an open fee statement.
    """


class Form1099Int(BaseModel):
    """Details of the Form 1099-INT export.

    This field will be present when the `category` is equal to `form_1099_int`.
    """

    account_id: str
    """The Account the tax form is for."""

    corrected: bool
    """Whether the tax form is a corrected form."""

    description: str
    """A description of the tax form."""

    year: int
    """The tax year for the tax form."""


class Form1099Misc(BaseModel):
    """Details of the Form 1099-MISC export.

    This field will be present when the `category` is equal to `form_1099_misc`.
    """

    account_id: str
    """The Account the tax form is for."""

    corrected: bool
    """Whether the tax form is a corrected form."""

    year: int
    """The tax year for the tax form."""


class FundingInstructions(BaseModel):
    """Details of the funding instructions export.

    This field will be present when the `category` is equal to `funding_instructions`.
    """

    account_number_id: str
    """The Account Number to create funding instructions for."""


class Result(BaseModel):
    """The result of the Export.

    This will be present when the Export's status transitions to `complete`.
    """

    file_id: str
    """The File containing the contents of the Export."""


class TransactionCsvCreatedAt(BaseModel):
    """Filter transactions by their created date."""

    after: Optional[datetime] = None
    """Filter transactions created after this time."""

    before: Optional[datetime] = None
    """Filter transactions created before this time."""


class TransactionCsv(BaseModel):
    """Details of the transaction CSV export.

    This field will be present when the `category` is equal to `transaction_csv`.
    """

    account_id: Optional[str] = None
    """Filter results by Account."""

    created_at: Optional[TransactionCsvCreatedAt] = None
    """Filter transactions by their created date."""


class VendorCsv(BaseModel):
    """Details of the vendor CSV export.

    This field will be present when the `category` is equal to `vendor_csv`.
    """

    pass


class VoidedCheckPayer(BaseModel):
    line: str
    """The contents of the line."""


class VoidedCheck(BaseModel):
    """Details of the voided check export.

    This field will be present when the `category` is equal to `voided_check`.
    """

    account_number_id: str
    """The Account Number for the voided check."""

    payer: List[VoidedCheckPayer]
    """The payer information printed on the check."""


class Export(BaseModel):
    """Exports are generated files.

    Some exports can contain a lot of data, like a CSV of your transactions. Others can be a single document, like a tax form. Since they can take a while, they are generated asynchronously. We send a webhook when they are ready. For more information, please read our [Exports documentation](https://increase.com/documentation/exports).
    """

    id: str
    """The Export identifier."""

    account_statement_bai2: Optional[AccountStatementBai2] = None
    """Details of the account statement BAI2 export.

    This field will be present when the `category` is equal to
    `account_statement_bai2`.
    """

    account_statement_ofx: Optional[AccountStatementOfx] = None
    """Details of the account statement OFX export.

    This field will be present when the `category` is equal to
    `account_statement_ofx`.
    """

    account_verification_letter: Optional[AccountVerificationLetter] = None
    """Details of the account verification letter export.

    This field will be present when the `category` is equal to
    `account_verification_letter`.
    """

    balance_csv: Optional[BalanceCsv] = None
    """Details of the balance CSV export.

    This field will be present when the `category` is equal to `balance_csv`.
    """

    bookkeeping_account_balance_csv: Optional[BookkeepingAccountBalanceCsv] = None
    """Details of the bookkeeping account balance CSV export.

    This field will be present when the `category` is equal to
    `bookkeeping_account_balance_csv`.
    """

    category: Literal[
        "account_statement_ofx",
        "account_statement_bai2",
        "transaction_csv",
        "balance_csv",
        "bookkeeping_account_balance_csv",
        "entity_csv",
        "vendor_csv",
        "dashboard_table_csv",
        "account_verification_letter",
        "funding_instructions",
        "form_1099_int",
        "form_1099_misc",
        "fee_csv",
        "voided_check",
        "daily_account_balance_csv",
    ]
    """The category of the Export.

    We may add additional possible values for this enum over time; your application
    should be able to handle that gracefully.

    - `account_statement_ofx` - Export an Open Financial Exchange (OFX) file of
      transactions and balances for a given time range and Account.
    - `account_statement_bai2` - Export a BAI2 file of transactions and balances for
      a given date and optional Account.
    - `transaction_csv` - Export a CSV of all transactions for a given time range.
    - `balance_csv` - Export a CSV of account balances for the dates in a given
      range.
    - `bookkeeping_account_balance_csv` - Export a CSV of bookkeeping account
      balances for the dates in a given range.
    - `entity_csv` - Export a CSV of entities with a given status.
    - `vendor_csv` - Export a CSV of vendors added to the third-party risk
      management dashboard.
    - `dashboard_table_csv` - Certain dashboard tables are available as CSV exports.
      This export cannot be created via the API.
    - `account_verification_letter` - A PDF of an account verification letter.
    - `funding_instructions` - A PDF of funding instructions.
    - `form_1099_int` - A PDF of an Internal Revenue Service Form 1099-INT.
    - `form_1099_misc` - A PDF of an Internal Revenue Service Form 1099-MISC.
    - `fee_csv` - Export a CSV of fees. The time range must not include any fees
      that are part of an open fee statement.
    - `voided_check` - A PDF of a voided check.
    - `daily_account_balance_csv` - Export a CSV of daily account balances with
      starting and ending balances for a given date range.
    """

    created_at: datetime
    """The time the Export was created."""

    daily_account_balance_csv: Optional[DailyAccountBalanceCsv] = None
    """Details of the daily account balance CSV export.

    This field will be present when the `category` is equal to
    `daily_account_balance_csv`.
    """

    dashboard_table_csv: Optional[DashboardTableCsv] = None
    """Details of the dashboard table CSV export.

    This field will be present when the `category` is equal to
    `dashboard_table_csv`.
    """

    entity_csv: Optional[EntityCsv] = None
    """Details of the entity CSV export.

    This field will be present when the `category` is equal to `entity_csv`.
    """

    fee_csv: Optional[FeeCsv] = None
    """Details of the fee CSV export.

    This field will be present when the `category` is equal to `fee_csv`.
    """

    form_1099_int: Optional[Form1099Int] = None
    """Details of the Form 1099-INT export.

    This field will be present when the `category` is equal to `form_1099_int`.
    """

    form_1099_misc: Optional[Form1099Misc] = None
    """Details of the Form 1099-MISC export.

    This field will be present when the `category` is equal to `form_1099_misc`.
    """

    funding_instructions: Optional[FundingInstructions] = None
    """Details of the funding instructions export.

    This field will be present when the `category` is equal to
    `funding_instructions`.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    result: Optional[Result] = None
    """The result of the Export.

    This will be present when the Export's status transitions to `complete`.
    """

    status: Literal["pending", "complete", "failed"]
    """The status of the Export.

    - `pending` - Increase is generating the export.
    - `complete` - The export has been successfully generated.
    - `failed` - The export failed to generate. Increase will reach out to you to
      resolve the issue.
    """

    transaction_csv: Optional[TransactionCsv] = None
    """Details of the transaction CSV export.

    This field will be present when the `category` is equal to `transaction_csv`.
    """

    type: Literal["export"]
    """A constant representing the object's type.

    For this resource it will always be `export`.
    """

    vendor_csv: Optional[VendorCsv] = None
    """Details of the vendor CSV export.

    This field will be present when the `category` is equal to `vendor_csv`.
    """

    voided_check: Optional[VoidedCheck] = None
    """Details of the voided check export.

    This field will be present when the `category` is equal to `voided_check`.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
