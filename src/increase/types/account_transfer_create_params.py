# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountTransferCreateParams"]


class AccountTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the originating Account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in the minor unit of the account currency.

    For dollars, for example, this is cents.
    """

    description: Required[str]
    """
    An internal-facing description for the transfer for display in the API and
    dashboard. This will also show in the description of the created Transactions.
    """

    destination_account_id: Required[str]
    """The identifier for the destination Account that will receive the transfer."""

    require_approval: bool
    """Whether the transfer should require explicit approval via the dashboard or API.

    For more information, see
    [Transfer Approvals](/documentation/transfer-approvals).
    """
