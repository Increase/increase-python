# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountTransferCreateParams"]


class AccountTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in the minor unit of the account currency.

    For dollars, for example, this is cents.
    """

    description: Required[str]
    """The description you choose to give the transfer."""

    destination_account_id: Required[str]
    """The identifier for the account that will receive the transfer."""

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    unique_identifier: str
    """A unique identifier you choose for the transfer.

    Reusing this identifer for another transfer will result in an error. You can
    query for the transfer associated with this identifier using the List endpoint.
    """
