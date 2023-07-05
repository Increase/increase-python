# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ACHPrenotification", "PrenotificationReturn"]


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
