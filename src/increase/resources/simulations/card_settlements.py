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
from ...types.simulations import card_settlement_create_params
from ...types.transaction import Transaction

__all__ = ["CardSettlementsResource", "AsyncCardSettlementsResource"]


class CardSettlementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardSettlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardSettlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardSettlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardSettlementsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        card_id: str,
        pending_transaction_id: str,
        amount: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """Simulates the settlement of an authorization by a card acquirer.

        After a card
        authorization is created, the merchant will eventually send a settlement. This
        simulates that event, which may occur many days after the purchase in
        production. The amount settled can be different from the amount originally
        authorized, for example, when adding a tip to a restaurant bill.

        Args:
          card_id: The identifier of the Card to create a settlement on.

          pending_transaction_id: The identifier of the Pending Transaction for the Card Authorization you wish to
              settle.

          amount: The amount to be settled. This defaults to the amount of the Pending Transaction
              being settled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_settlements",
            body=maybe_transform(
                {
                    "card_id": card_id,
                    "pending_transaction_id": pending_transaction_id,
                    "amount": amount,
                },
                card_settlement_create_params.CardSettlementCreateParams,
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


class AsyncCardSettlementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardSettlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardSettlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardSettlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardSettlementsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        card_id: str,
        pending_transaction_id: str,
        amount: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """Simulates the settlement of an authorization by a card acquirer.

        After a card
        authorization is created, the merchant will eventually send a settlement. This
        simulates that event, which may occur many days after the purchase in
        production. The amount settled can be different from the amount originally
        authorized, for example, when adding a tip to a restaurant bill.

        Args:
          card_id: The identifier of the Card to create a settlement on.

          pending_transaction_id: The identifier of the Pending Transaction for the Card Authorization you wish to
              settle.

          amount: The amount to be settled. This defaults to the amount of the Pending Transaction
              being settled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_settlements",
            body=await async_maybe_transform(
                {
                    "card_id": card_id,
                    "pending_transaction_id": pending_transaction_id,
                    "amount": amount,
                },
                card_settlement_create_params.CardSettlementCreateParams,
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


class CardSettlementsResourceWithRawResponse:
    def __init__(self, card_settlements: CardSettlementsResource) -> None:
        self._card_settlements = card_settlements

        self.create = to_raw_response_wrapper(
            card_settlements.create,
        )


class AsyncCardSettlementsResourceWithRawResponse:
    def __init__(self, card_settlements: AsyncCardSettlementsResource) -> None:
        self._card_settlements = card_settlements

        self.create = async_to_raw_response_wrapper(
            card_settlements.create,
        )


class CardSettlementsResourceWithStreamingResponse:
    def __init__(self, card_settlements: CardSettlementsResource) -> None:
        self._card_settlements = card_settlements

        self.create = to_streamed_response_wrapper(
            card_settlements.create,
        )


class AsyncCardSettlementsResourceWithStreamingResponse:
    def __init__(self, card_settlements: AsyncCardSettlementsResource) -> None:
        self._card_settlements = card_settlements

        self.create = async_to_streamed_response_wrapper(
            card_settlements.create,
        )
