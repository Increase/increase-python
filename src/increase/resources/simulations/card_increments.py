# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import card_increment_create_params
from ...types.card_payment import CardPayment

__all__ = ["CardIncrementsResource", "AsyncCardIncrementsResource"]


class CardIncrementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardIncrementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardIncrementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardIncrementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardIncrementsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        card_payment_id: str,
        event_subscription_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates the increment of an authorization by a card acquirer.

        An authorization
        can be incremented multiple times.

        Args:
          amount: The amount of the increment in minor units in the card authorization's currency.

          card_payment_id: The identifier of the Card Payment to create a increment on.

          event_subscription_id: The identifier of the Event Subscription to use. If provided, will override the
              default real time event subscription. Because you can only create one real time
              decision event subscription, you can use this field to route events to any
              specified event subscription for testing purposes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_increments",
            body=maybe_transform(
                {
                    "amount": amount,
                    "card_payment_id": card_payment_id,
                    "event_subscription_id": event_subscription_id,
                },
                card_increment_create_params.CardIncrementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )


class AsyncCardIncrementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardIncrementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardIncrementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardIncrementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardIncrementsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        card_payment_id: str,
        event_subscription_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates the increment of an authorization by a card acquirer.

        An authorization
        can be incremented multiple times.

        Args:
          amount: The amount of the increment in minor units in the card authorization's currency.

          card_payment_id: The identifier of the Card Payment to create a increment on.

          event_subscription_id: The identifier of the Event Subscription to use. If provided, will override the
              default real time event subscription. Because you can only create one real time
              decision event subscription, you can use this field to route events to any
              specified event subscription for testing purposes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_increments",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "card_payment_id": card_payment_id,
                    "event_subscription_id": event_subscription_id,
                },
                card_increment_create_params.CardIncrementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )


class CardIncrementsResourceWithRawResponse:
    def __init__(self, card_increments: CardIncrementsResource) -> None:
        self._card_increments = card_increments

        self.create = to_raw_response_wrapper(
            card_increments.create,
        )


class AsyncCardIncrementsResourceWithRawResponse:
    def __init__(self, card_increments: AsyncCardIncrementsResource) -> None:
        self._card_increments = card_increments

        self.create = async_to_raw_response_wrapper(
            card_increments.create,
        )


class CardIncrementsResourceWithStreamingResponse:
    def __init__(self, card_increments: CardIncrementsResource) -> None:
        self._card_increments = card_increments

        self.create = to_streamed_response_wrapper(
            card_increments.create,
        )


class AsyncCardIncrementsResourceWithStreamingResponse:
    def __init__(self, card_increments: AsyncCardIncrementsResource) -> None:
        self._card_increments = card_increments

        self.create = async_to_streamed_response_wrapper(
            card_increments.create,
        )
