# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..types import CardPurchaseSupplement, card_purchase_supplement_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import Increase, AsyncIncrease

__all__ = ["CardPurchaseSupplements", "AsyncCardPurchaseSupplements"]


class CardPurchaseSupplements(SyncAPIResource):
    with_raw_response: CardPurchaseSupplementsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = CardPurchaseSupplementsWithRawResponse(self)

    def retrieve(
        self,
        card_purchase_supplement_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardPurchaseSupplement:
        """
        Retrieve a Card Purchase Supplement

        Args:
          card_purchase_supplement_id: The identifier of the Card Purchase Supplement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/card_purchase_supplements/{card_purchase_supplement_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardPurchaseSupplement,
        )

    def list(
        self,
        *,
        card_payment_id: str | NotGiven = NOT_GIVEN,
        created_at: card_purchase_supplement_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CardPurchaseSupplement]:
        """
        List Card Purchase Supplements

        Args:
          card_payment_id: Filter Card Purchase Supplements to ones belonging to the specified Card
              Payment.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_purchase_supplements",
            page=SyncPage[CardPurchaseSupplement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "card_payment_id": card_payment_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    card_purchase_supplement_list_params.CardPurchaseSupplementListParams,
                ),
            ),
            model=CardPurchaseSupplement,
        )


class AsyncCardPurchaseSupplements(AsyncAPIResource):
    with_raw_response: AsyncCardPurchaseSupplementsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCardPurchaseSupplementsWithRawResponse(self)

    async def retrieve(
        self,
        card_purchase_supplement_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardPurchaseSupplement:
        """
        Retrieve a Card Purchase Supplement

        Args:
          card_purchase_supplement_id: The identifier of the Card Purchase Supplement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/card_purchase_supplements/{card_purchase_supplement_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardPurchaseSupplement,
        )

    def list(
        self,
        *,
        card_payment_id: str | NotGiven = NOT_GIVEN,
        created_at: card_purchase_supplement_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CardPurchaseSupplement, AsyncPage[CardPurchaseSupplement]]:
        """
        List Card Purchase Supplements

        Args:
          card_payment_id: Filter Card Purchase Supplements to ones belonging to the specified Card
              Payment.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_purchase_supplements",
            page=AsyncPage[CardPurchaseSupplement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "card_payment_id": card_payment_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    card_purchase_supplement_list_params.CardPurchaseSupplementListParams,
                ),
            ),
            model=CardPurchaseSupplement,
        )


class CardPurchaseSupplementsWithRawResponse:
    def __init__(self, card_purchase_supplements: CardPurchaseSupplements) -> None:
        self.retrieve = to_raw_response_wrapper(
            card_purchase_supplements.retrieve,
        )
        self.list = to_raw_response_wrapper(
            card_purchase_supplements.list,
        )


class AsyncCardPurchaseSupplementsWithRawResponse:
    def __init__(self, card_purchase_supplements: AsyncCardPurchaseSupplements) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            card_purchase_supplements.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            card_purchase_supplements.list,
        )
