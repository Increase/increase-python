# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import Transaction
from ..._types import Body, Query, Headers
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations import card_refund_create_params

__all__ = ["CardRefunds", "AsyncCardRefunds"]


class CardRefunds(SyncAPIResource):
    def create(
        self,
        *,
        transaction_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
        """
        return self._post(
            "/simulations/card_refunds",
            body=maybe_transform({"transaction_id": transaction_id}, card_refund_create_params.CardRefundCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Transaction,
        )


class AsyncCardRefunds(AsyncAPIResource):
    async def create(
        self,
        *,
        transaction_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
        """
        return await self._post(
            "/simulations/card_refunds",
            body=maybe_transform({"transaction_id": transaction_id}, card_refund_create_params.CardRefundCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Transaction,
        )
