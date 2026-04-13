# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.simulations import card_purchase_supplement_create_params
from ...types.card_purchase_supplement import CardPurchaseSupplement

__all__ = ["CardPurchaseSupplementsResource", "AsyncCardPurchaseSupplementsResource"]


class CardPurchaseSupplementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardPurchaseSupplementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardPurchaseSupplementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardPurchaseSupplementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardPurchaseSupplementsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        transaction_id: str,
        invoice: card_purchase_supplement_create_params.Invoice | Omit = omit,
        line_items: Iterable[card_purchase_supplement_create_params.LineItem] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardPurchaseSupplement:
        """
        Simulates the creation of a Card Purchase Supplement (Level 3 data) for a card
        settlement. This happens asynchronously in production when Visa sends enhanced
        transaction data about a purchase.

        Args:
          transaction_id: The identifier of the Transaction to create a Card Purchase Supplement for. The
              Transaction must have a source of type `card_settlement`.

          invoice: Invoice-level information about the payment.

          line_items: Line item information, such as individual products purchased.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_purchase_supplements",
            body=maybe_transform(
                {
                    "transaction_id": transaction_id,
                    "invoice": invoice,
                    "line_items": line_items,
                },
                card_purchase_supplement_create_params.CardPurchaseSupplementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPurchaseSupplement,
        )


class AsyncCardPurchaseSupplementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardPurchaseSupplementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardPurchaseSupplementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardPurchaseSupplementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardPurchaseSupplementsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        transaction_id: str,
        invoice: card_purchase_supplement_create_params.Invoice | Omit = omit,
        line_items: Iterable[card_purchase_supplement_create_params.LineItem] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardPurchaseSupplement:
        """
        Simulates the creation of a Card Purchase Supplement (Level 3 data) for a card
        settlement. This happens asynchronously in production when Visa sends enhanced
        transaction data about a purchase.

        Args:
          transaction_id: The identifier of the Transaction to create a Card Purchase Supplement for. The
              Transaction must have a source of type `card_settlement`.

          invoice: Invoice-level information about the payment.

          line_items: Line item information, such as individual products purchased.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_purchase_supplements",
            body=await async_maybe_transform(
                {
                    "transaction_id": transaction_id,
                    "invoice": invoice,
                    "line_items": line_items,
                },
                card_purchase_supplement_create_params.CardPurchaseSupplementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPurchaseSupplement,
        )


class CardPurchaseSupplementsResourceWithRawResponse:
    def __init__(self, card_purchase_supplements: CardPurchaseSupplementsResource) -> None:
        self._card_purchase_supplements = card_purchase_supplements

        self.create = to_raw_response_wrapper(
            card_purchase_supplements.create,
        )


class AsyncCardPurchaseSupplementsResourceWithRawResponse:
    def __init__(self, card_purchase_supplements: AsyncCardPurchaseSupplementsResource) -> None:
        self._card_purchase_supplements = card_purchase_supplements

        self.create = async_to_raw_response_wrapper(
            card_purchase_supplements.create,
        )


class CardPurchaseSupplementsResourceWithStreamingResponse:
    def __init__(self, card_purchase_supplements: CardPurchaseSupplementsResource) -> None:
        self._card_purchase_supplements = card_purchase_supplements

        self.create = to_streamed_response_wrapper(
            card_purchase_supplements.create,
        )


class AsyncCardPurchaseSupplementsResourceWithStreamingResponse:
    def __init__(self, card_purchase_supplements: AsyncCardPurchaseSupplementsResource) -> None:
        self._card_purchase_supplements = card_purchase_supplements

        self.create = async_to_streamed_response_wrapper(
            card_purchase_supplements.create,
        )
