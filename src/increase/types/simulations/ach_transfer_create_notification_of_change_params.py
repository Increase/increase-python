# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ACHTransferCreateNotificationOfChangeParams"]


class ACHTransferCreateNotificationOfChangeParams(TypedDict, total=False):
    corrected_account_funding: Literal["checking", "savings", "general_ledger"]
    """The corrected account funding type.

    - `checking` - A checking account.
    - `savings` - A savings account.
    - `general_ledger` - A bank's general ledger. Uncommon.
    """

    corrected_account_number: str
    """The corrected account number."""

    corrected_individual_id: str
    """The corrected individual identifier."""

    corrected_routing_number: str
    """The corrected routing number."""
