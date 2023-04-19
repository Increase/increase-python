# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EventSubscriptionCreateParams"]


class EventSubscriptionCreateParams(TypedDict, total=False):
    url: Required[str]
    """The URL you'd like us to send webhooks to."""

    selected_event_category: Literal[
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
    """
    If specified, this subscription will only receive webhooks for Events with the
    specified `category`.
    """

    shared_secret: str
    """The key that will be used to sign webhooks.

    If no value is passed, a random string will be used as default.
    """
