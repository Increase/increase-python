# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.event_subscription import EventSubscription

__all__ = ["EventSubscriptions", "AsyncEventSubscriptions"]


class EventSubscriptions(SyncAPIResource):
    def create(
        self,
        *,
        url: str,
        shared_secret: str | NotGiven = NOT_GIVEN,
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
            "card_dispute.created",
            "card_dispute.updated",
            "check_deposit.created",
            "check_deposit.updated",
            "check_transfer.created",
            "check_transfer.updated",
            "declined_transaction.created",
            "document.created",
            "entity.created",
            "entity.updated",
            "external_account.created",
            "file.created",
            "group.updated",
            "group.heartbeat",
            "oauth_connection.created",
            "oauth_connection.deactivated",
            "pending_transaction.created",
            "pending_transaction.updated",
            "real_time_decision.card_authorization_requested",
            "real_time_decision.digital_wallet_token_requested",
            "real_time_decision.digital_wallet_authentication_requested",
            "real_time_payments_transfer.created",
            "real_time_payments_transfer.updated",
            "transaction.created",
            "wire_drawdown_request.created",
            "wire_drawdown_request.updated",
            "wire_transfer.created",
            "wire_transfer.updated",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> EventSubscription:
        """
        Args:
          url: The URL you'd like us to send webhooks to.

          shared_secret: The key that will be used to sign webhooks. If no value is passed, a random
              string will be used as default.

          selected_event_category: If specified, this subscription will only receive webhooks for Events with the
              specified `category`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/event_subscriptions",
            body={
                "url": url,
                "shared_secret": shared_secret,
                "selected_event_category": selected_event_category,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> EventSubscription:
        return self._get(
            f"/event_subscriptions/{event_subscription_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> EventSubscription:
        """
        Args:
          status: The status to update the Event Subscription with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/event_subscriptions/{event_subscription_id}",
            body={"status": status},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> SyncPage[EventSubscription]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/event_subscriptions",
            page=SyncPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                },
            ),
            model=EventSubscription,
        )


class AsyncEventSubscriptions(AsyncAPIResource):
    async def create(
        self,
        *,
        url: str,
        shared_secret: str | NotGiven = NOT_GIVEN,
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
            "card_dispute.created",
            "card_dispute.updated",
            "check_deposit.created",
            "check_deposit.updated",
            "check_transfer.created",
            "check_transfer.updated",
            "declined_transaction.created",
            "document.created",
            "entity.created",
            "entity.updated",
            "external_account.created",
            "file.created",
            "group.updated",
            "group.heartbeat",
            "oauth_connection.created",
            "oauth_connection.deactivated",
            "pending_transaction.created",
            "pending_transaction.updated",
            "real_time_decision.card_authorization_requested",
            "real_time_decision.digital_wallet_token_requested",
            "real_time_decision.digital_wallet_authentication_requested",
            "real_time_payments_transfer.created",
            "real_time_payments_transfer.updated",
            "transaction.created",
            "wire_drawdown_request.created",
            "wire_drawdown_request.updated",
            "wire_transfer.created",
            "wire_transfer.updated",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> EventSubscription:
        """
        Args:
          url: The URL you'd like us to send webhooks to.

          shared_secret: The key that will be used to sign webhooks. If no value is passed, a random
              string will be used as default.

          selected_event_category: If specified, this subscription will only receive webhooks for Events with the
              specified `category`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/event_subscriptions",
            body={
                "url": url,
                "shared_secret": shared_secret,
                "selected_event_category": selected_event_category,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> EventSubscription:
        return await self._get(
            f"/event_subscriptions/{event_subscription_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> EventSubscription:
        """
        Args:
          status: The status to update the Event Subscription with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/event_subscriptions/{event_subscription_id}",
            body={"status": status},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> AsyncPaginator[EventSubscription, AsyncPage[EventSubscription]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/event_subscriptions",
            page=AsyncPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                },
            ),
            model=EventSubscription,
        )
