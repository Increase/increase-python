# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InboundCheckDepositCreateParams"]


class InboundCheckDepositCreateParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The identifier of the Account Number the Inbound Check Deposit will be against."""

    amount: Required[int]
    """The check amount in cents."""

    check_number: Required[str]
    """The check number on the check to be deposited."""

    payee_name_analysis: Literal["name_matches", "does_not_match", "not_evaluated"]
    """
    Simulate the outcome of
    [payee name checking](https://increase.com/documentation/positive-pay#payee-name-mismatches).
    Defaults to `not_evaluated`.

    - `name_matches` - The details on the check match the recipient name of the
      check transfer.
    - `does_not_match` - The details on the check do not match the recipient name of
      the check transfer.
    - `not_evaluated` - The payee name analysis was not evaluated.
    """
