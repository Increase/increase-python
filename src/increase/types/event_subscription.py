# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventSubscription"]


class EventSubscription(BaseModel):
    created_at: datetime
    """The time the event subscription was created."""

    id: str
    """The event subscription identifier."""

    selected_event_category: Optional[
        Literal[
            "account.created",
            "account.updated",
            "account_number.created",
            "account_number.updated",
            "account_statement.created",
            "account_transfer.created",
            "account_transfer.updated",
            "ach_prenotification.created",
            "ach_prenotification.updated",
            "ach_transfer.created",
            "ach_transfer.updated",
            "card.created",
            "card.updated",
            "card_payment.created",
            "card_payment.updated",
            "card_dispute.created",
            "card_dispute.updated",
            "check_deposit.created",
            "check_deposit.updated",
            "check_transfer.created",
            "check_transfer.updated",
            "declined_transaction.created",
            "digital_wallet_token.created",
            "digital_wallet_token.updated",
            "document.created",
            "entity.created",
            "entity.updated",
            "external_account.created",
            "file.created",
            "group.updated",
            "group.heartbeat",
            "inbound_ach_transfer_return.created",
            "inbound_ach_transfer_return.updated",
            "inbound_wire_drawdown_request.created",
            "oauth_connection.created",
            "oauth_connection.deactivated",
            "pending_transaction.created",
            "pending_transaction.updated",
            "real_time_decision.card_authorization_requested",
            "real_time_decision.digital_wallet_token_requested",
            "real_time_decision.digital_wallet_authentication_requested",
            "real_time_payments_transfer.created",
            "real_time_payments_transfer.updated",
            "real_time_payments_request_for_payment.created",
            "real_time_payments_request_for_payment.updated",
            "transaction.created",
            "wire_drawdown_request.created",
            "wire_drawdown_request.updated",
            "wire_transfer.created",
            "wire_transfer.updated",
        ]
    ]
    """
    If specified, this subscription will only receive webhooks for Events with the
    specified `category`.
    """

    shared_secret: str
    """The key that will be used to sign webhooks."""

    status: Literal["active", "disabled", "deleted", "requires_attention"]
    """This indicates if we'll send notifications to this subscription."""

    type: Literal["event_subscription"]
    """A constant representing the object's type.

    For this resource it will always be `event_subscription`.
    """

    url: str
    """The webhook url where we'll send notifications."""
