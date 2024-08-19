# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InboundCheckDepositCreateParams"]


class InboundCheckDepositCreateParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The identifier of the Account Number the Inbound Check Deposit will be against."""

    amount: Required[int]
    """The check amount in cents."""

    check_number: Required[str]
    """The check number on the check to be deposited."""
