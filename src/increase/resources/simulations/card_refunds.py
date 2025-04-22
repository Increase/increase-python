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
from ...types.simulations import card_refund_create_params
from ...types.transaction import Transaction

__all__ = ["CardRefundsResource", "AsyncCardRefundsResource"]


class CardRefundsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardRefundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardRefundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardRefundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardRefundsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        transaction_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """Simulates refunding a card transaction.

        The full value of the original sandbox
        transaction is refunded.

        Args:
          transaction_id: The identifier for the Transaction to refund. The Transaction's source must have
              a category of card_settlement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_refunds",
            body=maybe_transform({"transaction_id": transaction_id}, card_refund_create_params.CardRefundCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Transaction,
        )


class AsyncCardRefundsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardRefundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardRefundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardRefundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardRefundsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        transaction_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """Simulates refunding a card transaction.

        The full value of the original sandbox
        transaction is refunded.

        Args:
          transaction_id: The identifier for the Transaction to refund. The Transaction's source must have
              a category of card_settlement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_refunds",
            body=await async_maybe_transform(
                {"transaction_id": transaction_id}, card_refund_create_params.CardRefundCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Transaction,
        )


class CardRefundsResourceWithRawResponse:
    def __init__(self, card_refunds: CardRefundsResource) -> None:
        self._card_refunds = card_refunds

        self.create = to_raw_response_wrapper(
            card_refunds.create,
        )


class AsyncCardRefundsResourceWithRawResponse:
    def __init__(self, card_refunds: AsyncCardRefundsResource) -> None:
        self._card_refunds = card_refunds

        self.create = async_to_raw_response_wrapper(
            card_refunds.create,
        )


class CardRefundsResourceWithStreamingResponse:
    def __init__(self, card_refunds: CardRefundsResource) -> None:
        self._card_refunds = card_refunds

        self.create = to_streamed_response_wrapper(
            card_refunds.create,
        )


class AsyncCardRefundsResourceWithStreamingResponse:
    def __init__(self, card_refunds: AsyncCardRefundsResource) -> None:
        self._card_refunds = card_refunds

        self.create = async_to_streamed_response_wrapper(
            card_refunds.create,
        )
