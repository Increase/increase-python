# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import event_subscription_list_params, event_subscription_create_params, event_subscription_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.event_subscription import EventSubscription

__all__ = ["EventSubscriptionsResource", "AsyncEventSubscriptionsResource"]


class EventSubscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return EventSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return EventSubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        oauth_connection_id: str | Omit = omit,
        selected_event_categories: Iterable[event_subscription_create_params.SelectedEventCategory] | Omit = omit,
        shared_secret: str | Omit = omit,
        status: Literal["active", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Create an Event Subscription

        Args:
          url: The URL you'd like us to send webhooks to.

          oauth_connection_id: If specified, this subscription will only receive webhooks for Events associated
              with the specified OAuth Connection.

          selected_event_categories: If specified, this subscription will only receive webhooks for Events with the
              specified `category`. If specifying a Real-Time Decision event category, only
              one Event Category can be specified for the Event Subscription.

          shared_secret: The key that will be used to sign webhooks. If no value is passed, a random
              string will be used as default.

          status: The status of the event subscription. Defaults to `active` if not specified.

              - `active` - The subscription is active and Events will be delivered normally.
              - `disabled` - The subscription is temporarily disabled and Events will not be
                delivered.

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
                    "oauth_connection_id": oauth_connection_id,
                    "selected_event_categories": selected_event_categories,
                    "shared_secret": shared_secret,
                    "status": status,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if not event_subscription_id:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_id` but received {event_subscription_id!r}"
            )
        return self._get(
            path_template("/event_subscriptions/{event_subscription_id}", event_subscription_id=event_subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    def update(
        self,
        event_subscription_id: str,
        *,
        status: Literal["active", "disabled", "deleted"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if not event_subscription_id:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_id` but received {event_subscription_id!r}"
            )
        return self._patch(
            path_template("/event_subscriptions/{event_subscription_id}", event_subscription_id=event_subscription_id),
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
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[EventSubscription]:
        """
        List Event Subscriptions

        Args:
          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

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
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    event_subscription_list_params.EventSubscriptionListParams,
                ),
            ),
            model=EventSubscription,
        )


class AsyncEventSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncEventSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        oauth_connection_id: str | Omit = omit,
        selected_event_categories: Iterable[event_subscription_create_params.SelectedEventCategory] | Omit = omit,
        shared_secret: str | Omit = omit,
        status: Literal["active", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Create an Event Subscription

        Args:
          url: The URL you'd like us to send webhooks to.

          oauth_connection_id: If specified, this subscription will only receive webhooks for Events associated
              with the specified OAuth Connection.

          selected_event_categories: If specified, this subscription will only receive webhooks for Events with the
              specified `category`. If specifying a Real-Time Decision event category, only
              one Event Category can be specified for the Event Subscription.

          shared_secret: The key that will be used to sign webhooks. If no value is passed, a random
              string will be used as default.

          status: The status of the event subscription. Defaults to `active` if not specified.

              - `active` - The subscription is active and Events will be delivered normally.
              - `disabled` - The subscription is temporarily disabled and Events will not be
                delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/event_subscriptions",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "oauth_connection_id": oauth_connection_id,
                    "selected_event_categories": selected_event_categories,
                    "shared_secret": shared_secret,
                    "status": status,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if not event_subscription_id:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_id` but received {event_subscription_id!r}"
            )
        return await self._get(
            path_template("/event_subscriptions/{event_subscription_id}", event_subscription_id=event_subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    async def update(
        self,
        event_subscription_id: str,
        *,
        status: Literal["active", "disabled", "deleted"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if not event_subscription_id:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_id` but received {event_subscription_id!r}"
            )
        return await self._patch(
            path_template("/event_subscriptions/{event_subscription_id}", event_subscription_id=event_subscription_id),
            body=await async_maybe_transform(
                {"status": status}, event_subscription_update_params.EventSubscriptionUpdateParams
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

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EventSubscription, AsyncPage[EventSubscription]]:
        """
        List Event Subscriptions

        Args:
          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

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
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    event_subscription_list_params.EventSubscriptionListParams,
                ),
            ),
            model=EventSubscription,
        )


class EventSubscriptionsResourceWithRawResponse:
    def __init__(self, event_subscriptions: EventSubscriptionsResource) -> None:
        self._event_subscriptions = event_subscriptions

        self.create = to_raw_response_wrapper(
            event_subscriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            event_subscriptions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            event_subscriptions.update,
        )
        self.list = to_raw_response_wrapper(
            event_subscriptions.list,
        )


class AsyncEventSubscriptionsResourceWithRawResponse:
    def __init__(self, event_subscriptions: AsyncEventSubscriptionsResource) -> None:
        self._event_subscriptions = event_subscriptions

        self.create = async_to_raw_response_wrapper(
            event_subscriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            event_subscriptions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            event_subscriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            event_subscriptions.list,
        )


class EventSubscriptionsResourceWithStreamingResponse:
    def __init__(self, event_subscriptions: EventSubscriptionsResource) -> None:
        self._event_subscriptions = event_subscriptions

        self.create = to_streamed_response_wrapper(
            event_subscriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            event_subscriptions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            event_subscriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            event_subscriptions.list,
        )


class AsyncEventSubscriptionsResourceWithStreamingResponse:
    def __init__(self, event_subscriptions: AsyncEventSubscriptionsResource) -> None:
        self._event_subscriptions = event_subscriptions

        self.create = async_to_streamed_response_wrapper(
            event_subscriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            event_subscriptions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            event_subscriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            event_subscriptions.list,
        )
