# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ACHPrenotification", "NotificationsOfChange", "PrenotificationReturn"]


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
    ]
    """The type of change that occurred.

    - `incorrect_account_number` - The account number was incorrect.
    - `incorrect_routing_number` - The routing number was incorrect.
    - `incorrect_routing_number_and_account_number` - Both the routing number and
      the account number were incorrect.
    - `incorrect_transaction_code` - The transaction code was incorrect.
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
    """

    corrected_data: str
    """The corrected data."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the notification occurred.
    """


class PrenotificationReturn(BaseModel):
    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Prenotification was returned.
    """

    return_reason_code: str
    """Why the Prenotification was returned."""


class ACHPrenotification(BaseModel):
    id: str
    """The ACH Prenotification's identifier."""

    account_number: str
    """The destination account number."""

    addendum: Optional[str]
    """Additional information for the recipient."""

    company_descriptive_date: Optional[str]
    """The description of the date of the notification."""

    company_discretionary_data: Optional[str]
    """Optional data associated with the notification."""

    company_entry_description: Optional[str]
    """The description of the notification."""

    company_name: Optional[str]
    """The name by which you know the company."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the prenotification was created.
    """

    credit_debit_indicator: Optional[Literal["credit", "debit"]]
    """If the notification is for a future credit or debit.

    - `credit` - The Prenotification is for an anticipated credit.
    - `debit` - The Prenotification is for an anticipated debit.
    """

    effective_date: Optional[datetime]
    """
    The effective date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    notifications_of_change: List[NotificationsOfChange]
    """
    If the receiving bank notifies that future transfers should use different
    details, this will contain those details.
    """

    prenotification_return: Optional[PrenotificationReturn]
    """If your prenotification is returned, this will contain details of the return."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    status: Literal["pending_submitting", "requires_attention", "returned", "submitted"]
    """The lifecycle status of the ACH Prenotification.

    - `pending_submitting` - The Prenotification is pending submission.
    - `requires_attention` - The Prenotification requires attention.
    - `returned` - The Prenotification has been returned.
    - `submitted` - The Prentification is complete.
    """

    type: Literal["ach_prenotification"]
    """A constant representing the object's type.

    For this resource it will always be `ach_prenotification`.
    """
