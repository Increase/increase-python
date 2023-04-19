# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    associated_object_id: str
    """The identifier of the object that generated this Event."""

    associated_object_type: str
    """The type of the object that generated this Event."""

    category: Literal[
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
    """The category of the Event.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.
    """

    created_at: datetime
    """The time the Event was created."""

    id: str
    """The Event identifier."""

    type: Literal["event"]
    """A constant representing the object's type.

    For this resource it will always be `event`.
    """
