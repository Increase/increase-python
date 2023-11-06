# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ...types import Transaction
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.simulations import card_refund_create_params

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["CardRefunds", "AsyncCardRefunds"]


class CardRefunds(SyncAPIResource):
    with_raw_response: CardRefundsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = CardRefundsWithRawResponse(self)

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


class AsyncCardRefunds(AsyncAPIResource):
    with_raw_response: AsyncCardRefundsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCardRefundsWithRawResponse(self)

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


class CardRefundsWithRawResponse:
    def __init__(self, card_refunds: CardRefunds) -> None:
        self.create = to_raw_response_wrapper(
            card_refunds.create,
        )


class AsyncCardRefundsWithRawResponse:
    def __init__(self, card_refunds: AsyncCardRefunds) -> None:
        self.create = async_to_raw_response_wrapper(
            card_refunds.create,
        )
