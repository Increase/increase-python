# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountStatementCreateParams"]


class AccountStatementCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier of the Account the statement is for."""
