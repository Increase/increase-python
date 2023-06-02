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
