# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ACHTransferCreateInboundParams"]


class ACHTransferCreateInboundParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The identifier of the Account Number the inbound ACH Transfer is for."""

    amount: Required[int]
    """The transfer amount in cents.

    A positive amount originates a credit transfer pushing funds to the receiving
    account. A negative amount originates a debit transfer pulling funds from the
    receiving account.
    """

    company_descriptive_date: str
    """The description of the date of the transfer."""

    company_discretionary_data: str
    """Data associated with the transfer set by the sender."""

    company_entry_description: str
    """The description of the transfer set by the sender."""

    company_id: str
    """The sender's company id."""

    company_name: str
    """The name of the sender."""

    resolve_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time at which the transfer should be resolved.

    If not provided will resolve immediately.
    """
