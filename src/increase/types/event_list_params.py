# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventListParams", "Category", "CreatedAt"]


class EventListParams(TypedDict, total=False):
    associated_object_id: str
    """Filter Events to those belonging to the object with the provided identifier."""

    category: Category

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """


_CategoryReservedKeywords = TypedDict(
    "_CategoryReservedKeywords",
    {
        "in": List[
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
                "bookkeeping_account.created",
                "bookkeeping_account.updated",
                "bookkeeping_entry_set.updated",
                "card.created",
                "card.updated",
                "card_payment.created",
                "card_payment.updated",
                "card_profile.created",
                "card_profile.updated",
                "card_dispute.created",
                "card_dispute.updated",
                "check_deposit.created",
                "check_deposit.updated",
                "check_transfer.created",
                "check_transfer.updated",
                "declined_transaction.created",
                "digital_card_profile.created",
                "digital_card_profile.updated",
                "digital_wallet_token.created",
                "digital_wallet_token.updated",
                "document.created",
                "entity.created",
                "entity.updated",
                "event_subscription.created",
                "event_subscription.updated",
                "export.created",
                "export.updated",
                "external_account.created",
                "external_account.updated",
                "file.created",
                "group.updated",
                "group.heartbeat",
                "inbound_ach_transfer.created",
                "inbound_ach_transfer.updated",
                "inbound_ach_transfer_return.created",
                "inbound_ach_transfer_return.updated",
                "inbound_check_deposit.created",
                "inbound_check_deposit.updated",
                "inbound_mail_item.created",
                "inbound_mail_item.updated",
                "inbound_real_time_payments_transfer.created",
                "inbound_real_time_payments_transfer.updated",
                "inbound_wire_drawdown_request.created",
                "inbound_wire_transfer.created",
                "inbound_wire_transfer.updated",
                "intrafi_account_enrollment.created",
                "intrafi_account_enrollment.updated",
                "intrafi_exclusion.created",
                "intrafi_exclusion.updated",
                "legacy_card_dispute.created",
                "legacy_card_dispute.updated",
                "lockbox.created",
                "lockbox.updated",
                "oauth_connection.created",
                "oauth_connection.deactivated",
                "outbound_card_push_transfer.created",
                "outbound_card_push_transfer.updated",
                "outbound_card_validation.created",
                "outbound_card_validation.updated",
                "card_push_transfer.created",
                "card_push_transfer.updated",
                "card_validation.created",
                "card_validation.updated",
                "pending_transaction.created",
                "pending_transaction.updated",
                "physical_card.created",
                "physical_card.updated",
                "physical_card_profile.created",
                "physical_card_profile.updated",
                "program.created",
                "program.updated",
                "proof_of_authorization_request.created",
                "proof_of_authorization_request.updated",
                "real_time_decision.card_authorization_requested",
                "real_time_decision.digital_wallet_token_requested",
                "real_time_decision.digital_wallet_authentication_requested",
                "real_time_decision.card_authentication_requested",
                "real_time_decision.card_authentication_challenge_requested",
                "real_time_payments_transfer.created",
                "real_time_payments_transfer.updated",
                "real_time_payments_request_for_payment.created",
                "real_time_payments_request_for_payment.updated",
                "swift_transfer.created",
                "swift_transfer.updated",
                "transaction.created",
                "wire_drawdown_request.created",
                "wire_drawdown_request.updated",
                "wire_transfer.created",
                "wire_transfer.updated",
            ]
        ],
    },
    total=False,
)


class Category(_CategoryReservedKeywords, total=False):
    pass


class CreatedAt(TypedDict, total=False):
    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    on_or_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or after this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """

    on_or_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or before this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """
