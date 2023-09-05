# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InboundACHTransferNotificationOfChangeParams"]


class InboundACHTransferNotificationOfChangeParams(TypedDict, total=False):
    updated_account_number: str
    """The updated account number to send in the notification of change."""

    updated_routing_number: str
    """The updated routing number to send in the notification of change."""
