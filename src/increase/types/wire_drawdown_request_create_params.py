# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WireDrawdownRequestCreateParams"]


class WireDrawdownRequestCreateParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The Account Number to which the recipient should send funds."""

    amount: Required[int]
    """The amount requested from the recipient, in USD cents."""

    message_to_recipient: Required[str]
    """A message the recipient will see as part of the request."""

    recipient_account_number: Required[str]
    """The drawdown request's recipient's account number."""

    recipient_name: Required[str]
    """The drawdown request's recipient's name."""

    recipient_routing_number: Required[str]
    """The drawdown request's recipient's routing number."""

    originator_address_line1: str
    """The drawdown request originator's address line 1.

    This is only necessary if you're requesting a payment to a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    originator_address_line2: str
    """The drawdown request originator's address line 2.

    This is only necessary if you're requesting a payment to a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    originator_address_line3: str
    """The drawdown request originator's address line 3.

    This is only necessary if you're requesting a payment to a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    originator_name: str
    """The drawdown request originator's name.

    This is only necessary if you're requesting a payment to a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    recipient_address_line1: str
    """Line 1 of the drawdown request's recipient's address."""

    recipient_address_line2: str
    """Line 2 of the drawdown request's recipient's address."""

    recipient_address_line3: str
    """Line 3 of the drawdown request's recipient's address."""
