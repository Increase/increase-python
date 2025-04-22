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
from ...types.simulations import card_reversal_create_params
from ...types.card_payment import CardPayment

__all__ = ["CardReversalsResource", "AsyncCardReversalsResource"]


class CardReversalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardReversalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardReversalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardReversalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardReversalsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        card_payment_id: str,
        amount: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates the reversal of an authorization by a card acquirer.

        An authorization
        can be partially reversed multiple times, up until the total authorized amount.
        Marks the pending transaction as complete if the authorization is fully
        reversed.

        Args:
          card_payment_id: The identifier of the Card Payment to create a reversal on.

          amount: The amount of the reversal in minor units in the card authorization's currency.
              This defaults to the authorization amount.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_reversals",
            body=maybe_transform(
                {
                    "card_payment_id": card_payment_id,
                    "amount": amount,
                },
                card_reversal_create_params.CardReversalCreateParams,
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


class AsyncCardReversalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardReversalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardReversalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardReversalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardReversalsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        card_payment_id: str,
        amount: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates the reversal of an authorization by a card acquirer.

        An authorization
        can be partially reversed multiple times, up until the total authorized amount.
        Marks the pending transaction as complete if the authorization is fully
        reversed.

        Args:
          card_payment_id: The identifier of the Card Payment to create a reversal on.

          amount: The amount of the reversal in minor units in the card authorization's currency.
              This defaults to the authorization amount.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_reversals",
            body=await async_maybe_transform(
                {
                    "card_payment_id": card_payment_id,
                    "amount": amount,
                },
                card_reversal_create_params.CardReversalCreateParams,
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


class CardReversalsResourceWithRawResponse:
    def __init__(self, card_reversals: CardReversalsResource) -> None:
        self._card_reversals = card_reversals

        self.create = to_raw_response_wrapper(
            card_reversals.create,
        )


class AsyncCardReversalsResourceWithRawResponse:
    def __init__(self, card_reversals: AsyncCardReversalsResource) -> None:
        self._card_reversals = card_reversals

        self.create = async_to_raw_response_wrapper(
            card_reversals.create,
        )


class CardReversalsResourceWithStreamingResponse:
    def __init__(self, card_reversals: CardReversalsResource) -> None:
        self._card_reversals = card_reversals

        self.create = to_streamed_response_wrapper(
            card_reversals.create,
        )


class AsyncCardReversalsResourceWithStreamingResponse:
    def __init__(self, card_reversals: AsyncCardReversalsResource) -> None:
        self._card_reversals = card_reversals

        self.create = async_to_streamed_response_wrapper(
            card_reversals.create,
        )
