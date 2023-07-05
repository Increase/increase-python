# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..types import (
    EventSubscription,
    event_subscription_list_params,
    event_subscription_create_params,
    event_subscription_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["EventSubscriptions", "AsyncEventSubscriptions"]


class EventSubscriptions(SyncAPIResource):
    def create(
        self,
        *,
        url: str,
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
        | NotGiven = NOT_GIVEN,
        shared_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Create an Event Subscription

        Args:
          url: The URL you'd like us to send webhooks to.

          selected_event_category: If specified, this subscription will only receive webhooks for Events with the
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
              - `card.created` - Occurs whenever a Card is created.
              - `card.updated` - Occurs whenever a Card is updated.
              - `card_payment.created` - Occurs whenever a Card Payment is created.
              - `card_payment.updated` - Occurs whenever a Card Payment is updated.
              - `card_dispute.created` - Occurs whenever a Card Dispute is created.
              - `card_dispute.updated` - Occurs whenever a Card Dispute is updated.
              - `check_deposit.created` - Occurs whenever a Check Deposit is created.
              - `check_deposit.updated` - Occurs whenever a Check Deposit is updated.
              - `check_transfer.created` - Occurs whenever a Check Transfer is created.
              - `check_transfer.updated` - Occurs whenever a Check Transfer is updated.
              - `declined_transaction.created` - Occurs whenever a Declined Transaction is
                created.
              - `digital_wallet_token.created` - Occurs whenever a Digital Wallet Token is
                created.
              - `digital_wallet_token.updated` - Occurs whenever a Digital Wallet Token is
                updated.
              - `document.created` - Occurs whenever a Document is created.
              - `entity.created` - Occurs whenever an Entity is created.
              - `entity.updated` - Occurs whenever an Entity is updated.
              - `external_account.created` - Occurs whenever an External Account is created.
              - `file.created` - Occurs whenever a File is created.
              - `group.updated` - Occurs whenever a Group is updated.
              - `group.heartbeat` - Increase may send webhooks with this category to see if a
                webhook endpoint is working properly.
              - `inbound_ach_transfer_return.created` - Occurs whenever an Inbound ACH
                Transfer Return is created.
              - `inbound_ach_transfer_return.updated` - Occurs whenever an Inbound ACH
                Transfer Return is updated.
              - `inbound_wire_drawdown_request.created` - Occurs whenever an Inbound Wire
                Drawdown Request is created.
              - `oauth_connection.created` - Occurs whenever an OAuth Connection is created.
              - `oauth_connection.deactivated` - Occurs whenever an OAuth Connection is
                deactivated.
              - `pending_transaction.created` - Occurs whenever a Pending Transaction is
                created.
              - `pending_transaction.updated` - Occurs whenever a Pending Transaction is
                updated.
              - `real_time_decision.card_authorization_requested` - Occurs whenever a
                Real-Time Decision is created in response to a card authorization.
              - `real_time_decision.digital_wallet_token_requested` - Occurs whenever a
                Real-Time Decision is created in response to a digital wallet provisioning
                attempt.
              - `real_time_decision.digital_wallet_authentication_requested` - Occurs whenever
                a Real-Time Decision is created in response to a digital wallet requiring
                two-factor authentication.
              - `real_time_payments_transfer.created` - Occurs whenever a Real Time Payments
                Transfer is created.
              - `real_time_payments_transfer.updated` - Occurs whenever a Real Time Payments
                Transfer is updated.
              - `real_time_payments_request_for_payment.created` - Occurs whenever a Real Time
                Payments Request for Payment is created.
              - `real_time_payments_request_for_payment.updated` - Occurs whenever a Real Time
                Payments Request for Payment is updated.
              - `transaction.created` - Occurs whenever a Transaction is updated.
              - `wire_drawdown_request.created` - Occurs whenever a Wire Drawdown Request is
                created.
              - `wire_drawdown_request.updated` - Occurs whenever a Wire Drawdown Request is
                updated.
              - `wire_transfer.created` - Occurs whenever a Wire Transfer is created.
              - `wire_transfer.updated` - Occurs whenever a Wire Transfer is updated.

          shared_secret: The key that will be used to sign webhooks. If no value is passed, a random
              string will be used as default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/event_subscriptions",
            body=maybe_transform(
                {
                    "url": url,
                    "selected_event_category": selected_event_category,
                    "shared_secret": shared_secret,
                },
                event_subscription_create_params.EventSubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    def retrieve(
        self,
        event_subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Retrieve an Event Subscription

        Args:
          event_subscription_id: The identifier of the Event Subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/event_subscriptions/{event_subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    def update(
        self,
        event_subscription_id: str,
        *,
        status: Literal["active", "disabled", "deleted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Update an Event Subscription

        Args:
          event_subscription_id: The identifier of the Event Subscription.

          status: The status to update the Event Subscription with.

              - `active` - The subscription is active and Events will be delivered normally.
              - `disabled` - The subscription is temporarily disabled and Events will not be
                delivered.
              - `deleted` - The subscription is permanently disabled and Events will not be
                delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/event_subscriptions/{event_subscription_id}",
            body=maybe_transform({"status": status}, event_subscription_update_params.EventSubscriptionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[EventSubscription]:
        """
        List Event Subscriptions

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/event_subscriptions",
            page=SyncPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    event_subscription_list_params.EventSubscriptionListParams,
                ),
            ),
            model=EventSubscription,
        )


class AsyncEventSubscriptions(AsyncAPIResource):
    async def create(
        self,
        *,
        url: str,
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
        | NotGiven = NOT_GIVEN,
        shared_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Create an Event Subscription

        Args:
          url: The URL you'd like us to send webhooks to.

          selected_event_category: If specified, this subscription will only receive webhooks for Events with the
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
              - `card.created` - Occurs whenever a Card is created.
              - `card.updated` - Occurs whenever a Card is updated.
              - `card_payment.created` - Occurs whenever a Card Payment is created.
              - `card_payment.updated` - Occurs whenever a Card Payment is updated.
              - `card_dispute.created` - Occurs whenever a Card Dispute is created.
              - `card_dispute.updated` - Occurs whenever a Card Dispute is updated.
              - `check_deposit.created` - Occurs whenever a Check Deposit is created.
              - `check_deposit.updated` - Occurs whenever a Check Deposit is updated.
              - `check_transfer.created` - Occurs whenever a Check Transfer is created.
              - `check_transfer.updated` - Occurs whenever a Check Transfer is updated.
              - `declined_transaction.created` - Occurs whenever a Declined Transaction is
                created.
              - `digital_wallet_token.created` - Occurs whenever a Digital Wallet Token is
                created.
              - `digital_wallet_token.updated` - Occurs whenever a Digital Wallet Token is
                updated.
              - `document.created` - Occurs whenever a Document is created.
              - `entity.created` - Occurs whenever an Entity is created.
              - `entity.updated` - Occurs whenever an Entity is updated.
              - `external_account.created` - Occurs whenever an External Account is created.
              - `file.created` - Occurs whenever a File is created.
              - `group.updated` - Occurs whenever a Group is updated.
              - `group.heartbeat` - Increase may send webhooks with this category to see if a
                webhook endpoint is working properly.
              - `inbound_ach_transfer_return.created` - Occurs whenever an Inbound ACH
                Transfer Return is created.
              - `inbound_ach_transfer_return.updated` - Occurs whenever an Inbound ACH
                Transfer Return is updated.
              - `inbound_wire_drawdown_request.created` - Occurs whenever an Inbound Wire
                Drawdown Request is created.
              - `oauth_connection.created` - Occurs whenever an OAuth Connection is created.
              - `oauth_connection.deactivated` - Occurs whenever an OAuth Connection is
                deactivated.
              - `pending_transaction.created` - Occurs whenever a Pending Transaction is
                created.
              - `pending_transaction.updated` - Occurs whenever a Pending Transaction is
                updated.
              - `real_time_decision.card_authorization_requested` - Occurs whenever a
                Real-Time Decision is created in response to a card authorization.
              - `real_time_decision.digital_wallet_token_requested` - Occurs whenever a
                Real-Time Decision is created in response to a digital wallet provisioning
                attempt.
              - `real_time_decision.digital_wallet_authentication_requested` - Occurs whenever
                a Real-Time Decision is created in response to a digital wallet requiring
                two-factor authentication.
              - `real_time_payments_transfer.created` - Occurs whenever a Real Time Payments
                Transfer is created.
              - `real_time_payments_transfer.updated` - Occurs whenever a Real Time Payments
                Transfer is updated.
              - `real_time_payments_request_for_payment.created` - Occurs whenever a Real Time
                Payments Request for Payment is created.
              - `real_time_payments_request_for_payment.updated` - Occurs whenever a Real Time
                Payments Request for Payment is updated.
              - `transaction.created` - Occurs whenever a Transaction is updated.
              - `wire_drawdown_request.created` - Occurs whenever a Wire Drawdown Request is
                created.
              - `wire_drawdown_request.updated` - Occurs whenever a Wire Drawdown Request is
                updated.
              - `wire_transfer.created` - Occurs whenever a Wire Transfer is created.
              - `wire_transfer.updated` - Occurs whenever a Wire Transfer is updated.

          shared_secret: The key that will be used to sign webhooks. If no value is passed, a random
              string will be used as default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/event_subscriptions",
            body=maybe_transform(
                {
                    "url": url,
                    "selected_event_category": selected_event_category,
                    "shared_secret": shared_secret,
                },
                event_subscription_create_params.EventSubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    async def retrieve(
        self,
        event_subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Retrieve an Event Subscription

        Args:
          event_subscription_id: The identifier of the Event Subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/event_subscriptions/{event_subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    async def update(
        self,
        event_subscription_id: str,
        *,
        status: Literal["active", "disabled", "deleted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Update an Event Subscription

        Args:
          event_subscription_id: The identifier of the Event Subscription.

          status: The status to update the Event Subscription with.

              - `active` - The subscription is active and Events will be delivered normally.
              - `disabled` - The subscription is temporarily disabled and Events will not be
                delivered.
              - `deleted` - The subscription is permanently disabled and Events will not be
                delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/event_subscriptions/{event_subscription_id}",
            body=maybe_transform({"status": status}, event_subscription_update_params.EventSubscriptionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EventSubscription, AsyncPage[EventSubscription]]:
        """
        List Event Subscriptions

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/event_subscriptions",
            page=AsyncPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    event_subscription_list_params.EventSubscriptionListParams,
                ),
            ),
            model=EventSubscription,
        )
