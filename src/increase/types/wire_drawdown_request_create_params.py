# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WireDrawdownRequestCreateParams"]


class WireDrawdownRequestCreateParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The Account Number to which the recipient should send funds."""

    amount: Required[int]
    """The amount requested from the recipient, in cents."""

    message_to_recipient: Required[str]
    """A message the recipient will see as part of the request."""

    recipient_account_number: Required[str]
    """The drawdown request's recipient's account number."""

    recipient_name: Required[str]
    """The drawdown request's recipient's name."""

    recipient_routing_number: Required[str]
    """The drawdown request's recipient's routing number."""

    recipient_address_line1: str
    """Line 1 of the drawdown request's recipient's address."""

    recipient_address_line2: str
    """Line 2 of the drawdown request's recipient's address."""

    recipient_address_line3: str
    """Line 3 of the drawdown request's recipient's address."""
