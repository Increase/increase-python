# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventSubscription"]


class EventSubscription(BaseModel):
    id: str
    """The event subscription identifier."""

    created_at: datetime
    """The time the event subscription was created."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    oauth_connection_id: Optional[str] = None
    """
    If specified, this subscription will only receive webhooks for Events associated
    with this OAuth Connection.
    """

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
    ] = None
    """
    If specified, this subscription will only receive webhooks for Events with the
    specified `category`.

    - `account.created` - Occurs whenever an Account is created.
    - `account.updated` - Occurs whenever an Account is updated.
    - `account_number.created` - Occurs whenever an Account Number is created.
    - `account_number.updated` - Occurs whenever an Account Number is updated.
    - `account_statement.created` - Occurs whenever an Account Statement is created.
    - `account_transfer.created` - Occurs whenever an Account Transfer is created.
    - `account_transfer.updated` - Occurs whenever an Account Transfer is updated.
    - `ach_prenotification.created` - Occurs whenever an ACH Prenotification is
      created.
    - `ach_prenotification.updated` - Occurs whenever an ACH Prenotification is
      updated.
    - `ach_transfer.created` - Occurs whenever an ACH Transfer is created.
    - `ach_transfer.updated` - Occurs whenever an ACH Transfer is updated.
    - `bookkeeping_account.created` - Occurs whenever a Bookkeeping Account is
      created.
    - `bookkeeping_account.updated` - Occurs whenever a Bookkeeping Account is
      updated.
    - `bookkeeping_entry_set.updated` - Occurs whenever a Bookkeeping Entry Set is
      created.
    - `card.created` - Occurs whenever a Card is created.
    - `card.updated` - Occurs whenever a Card is updated.
    - `card_payment.created` - Occurs whenever a Card Payment is created.
    - `card_payment.updated` - Occurs whenever a Card Payment is updated.
    - `card_profile.created` - Occurs whenever a Card Profile is created.
    - `card_profile.updated` - Occurs whenever a Card Profile is updated.
    - `card_dispute.created` - Occurs whenever a Card Dispute is created.
    - `card_dispute.updated` - Occurs whenever a Card Dispute is updated.
    - `check_deposit.created` - Occurs whenever a Check Deposit is created.
    - `check_deposit.updated` - Occurs whenever a Check Deposit is updated.
    - `check_transfer.created` - Occurs whenever a Check Transfer is created.
    - `check_transfer.updated` - Occurs whenever a Check Transfer is updated.
    - `declined_transaction.created` - Occurs whenever a Declined Transaction is
      created.
    - `digital_card_profile.created` - Occurs whenever a Digital Card Profile is
      created.
    - `digital_card_profile.updated` - Occurs whenever a Digital Card Profile is
      updated.
    - `digital_wallet_token.created` - Occurs whenever a Digital Wallet Token is
      created.
    - `digital_wallet_token.updated` - Occurs whenever a Digital Wallet Token is
      updated.
    - `document.created` - Occurs whenever a Document is created.
    - `entity.created` - Occurs whenever an Entity is created.
    - `entity.updated` - Occurs whenever an Entity is updated.
    - `event_subscription.created` - Occurs whenever an Event Subscription is
      created.
    - `event_subscription.updated` - Occurs whenever an Event Subscription is
      updated.
    - `export.created` - Occurs whenever an Export is created.
    - `export.updated` - Occurs whenever an Export is updated.
    - `external_account.created` - Occurs whenever an External Account is created.
    - `external_account.updated` - Occurs whenever an External Account is updated.
    - `file.created` - Occurs whenever a File is created.
    - `group.updated` - Occurs whenever a Group is updated.
    - `group.heartbeat` - Increase may send webhooks with this category to see if a
      webhook endpoint is working properly.
    - `inbound_ach_transfer.created` - Occurs whenever an Inbound ACH Transfer is
      created.
    - `inbound_ach_transfer.updated` - Occurs whenever an Inbound ACH Transfer is
      updated.
    - `inbound_ach_transfer_return.created` - Occurs whenever an Inbound ACH
      Transfer Return is created.
    - `inbound_ach_transfer_return.updated` - Occurs whenever an Inbound ACH
      Transfer Return is updated.
    - `inbound_check_deposit.created` - Occurs whenever an Inbound Check Deposit is
      created.
    - `inbound_check_deposit.updated` - Occurs whenever an Inbound Check Deposit is
      updated.
    - `inbound_mail_item.created` - Occurs whenever an Inbound Mail Item is created.
    - `inbound_mail_item.updated` - Occurs whenever an Inbound Mail Item is updated.
    - `inbound_real_time_payments_transfer.created` - Occurs whenever an Inbound
      Real-Time Payments Transfer is created.
    - `inbound_real_time_payments_transfer.updated` - Occurs whenever an Inbound
      Real-Time Payments Transfer is updated.
    - `inbound_wire_drawdown_request.created` - Occurs whenever an Inbound Wire
      Drawdown Request is created.
    - `inbound_wire_transfer.created` - Occurs whenever an Inbound Wire Transfer is
      created.
    - `inbound_wire_transfer.updated` - Occurs whenever an Inbound Wire Transfer is
      updated.
    - `intrafi_account_enrollment.created` - Occurs whenever an IntraFi Account
      Enrollment is created.
    - `intrafi_account_enrollment.updated` - Occurs whenever an IntraFi Account
      Enrollment is updated.
    - `intrafi_exclusion.created` - Occurs whenever an IntraFi Exclusion is created.
    - `intrafi_exclusion.updated` - Occurs whenever an IntraFi Exclusion is updated.
    - `lockbox.created` - Occurs whenever a Lockbox is created.
    - `lockbox.updated` - Occurs whenever a Lockbox is updated.
    - `oauth_connection.created` - Occurs whenever an OAuth Connection is created.
    - `oauth_connection.deactivated` - Occurs whenever an OAuth Connection is
      deactivated.
    - `outbound_card_push_transfer.created` - Occurs whenever a Card Push Transfer
      is created.
    - `outbound_card_push_transfer.updated` - Occurs whenever a Card Push Transfer
      is updated.
    - `outbound_card_validation.created` - Occurs whenever a Card Validation is
      created.
    - `outbound_card_validation.updated` - Occurs whenever a Card Validation is
      updated.
    - `card_push_transfer.created` - Occurs whenever a Card Push Transfer is
      created.
    - `card_push_transfer.updated` - Occurs whenever a Card Push Transfer is
      updated.
    - `card_validation.created` - Occurs whenever a Card Validation is created.
    - `card_validation.updated` - Occurs whenever a Card Validation is updated.
    - `pending_transaction.created` - Occurs whenever a Pending Transaction is
      created.
    - `pending_transaction.updated` - Occurs whenever a Pending Transaction is
      updated.
    - `physical_card.created` - Occurs whenever a Physical Card is created.
    - `physical_card.updated` - Occurs whenever a Physical Card is updated.
    - `physical_card_profile.created` - Occurs whenever a Physical Card Profile is
      created.
    - `physical_card_profile.updated` - Occurs whenever a Physical Card Profile is
      updated.
    - `program.created` - Occurs whenever a Program is created.
    - `program.updated` - Occurs whenever a Program is updated.
    - `proof_of_authorization_request.created` - Occurs whenever a Proof of
      Authorization Request is created.
    - `proof_of_authorization_request.updated` - Occurs whenever a Proof of
      Authorization Request is updated.
    - `real_time_decision.card_authorization_requested` - Occurs whenever a
      Real-Time Decision is created in response to a card authorization.
    - `real_time_decision.digital_wallet_token_requested` - Occurs whenever a
      Real-Time Decision is created in response to a digital wallet provisioning
      attempt.
    - `real_time_decision.digital_wallet_authentication_requested` - Occurs whenever
      a Real-Time Decision is created in response to a digital wallet requiring
      two-factor authentication.
    - `real_time_decision.card_authentication_requested` - Occurs whenever a
      Real-Time Decision is created in response to 3DS authentication.
    - `real_time_decision.card_authentication_challenge_requested` - Occurs whenever
      a Real-Time Decision is created in response to 3DS authentication challenges.
    - `real_time_payments_transfer.created` - Occurs whenever a Real-Time Payments
      Transfer is created.
    - `real_time_payments_transfer.updated` - Occurs whenever a Real-Time Payments
      Transfer is updated.
    - `real_time_payments_request_for_payment.created` - Occurs whenever a Real-Time
      Payments Request for Payment is created.
    - `real_time_payments_request_for_payment.updated` - Occurs whenever a Real-Time
      Payments Request for Payment is updated.
    - `swift_transfer.created` - Occurs whenever a Swift Transfer is created.
    - `swift_transfer.updated` - Occurs whenever a Swift Transfer is updated.
    - `transaction.created` - Occurs whenever a Transaction is created.
    - `wire_drawdown_request.created` - Occurs whenever a Wire Drawdown Request is
      created.
    - `wire_drawdown_request.updated` - Occurs whenever a Wire Drawdown Request is
      updated.
    - `wire_transfer.created` - Occurs whenever a Wire Transfer is created.
    - `wire_transfer.updated` - Occurs whenever a Wire Transfer is updated.
    """

    status: Literal["active", "disabled", "deleted", "requires_attention"]
    """This indicates if we'll send notifications to this subscription.

    - `active` - The subscription is active and Events will be delivered normally.
    - `disabled` - The subscription is temporarily disabled and Events will not be
      delivered.
    - `deleted` - The subscription is permanently disabled and Events will not be
      delivered.
    - `requires_attention` - The subscription is temporarily disabled due to
      delivery errors and Events will not be delivered.
    """

    type: Literal["event_subscription"]
    """A constant representing the object's type.

    For this resource it will always be `event_subscription`.
    """

    url: str
    """The webhook url where we'll send notifications."""
