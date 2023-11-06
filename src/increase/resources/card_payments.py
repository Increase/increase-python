# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..types import CardPayment, card_payment_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import Increase, AsyncIncrease

__all__ = ["CardPayments", "AsyncCardPayments"]


class CardPayments(SyncAPIResource):
    with_raw_response: CardPaymentsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = CardPaymentsWithRawResponse(self)

    def retrieve(
        self,
        card_payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardPayment:
        """
        Retrieve a Card Payment

        Args:
          card_payment_id: The identifier of the Card Payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/card_payments/{card_payment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardPayment,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        card_id: str | NotGiven = NOT_GIVEN,
        created_at: card_payment_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CardPayment]:
        """
        List Card Payments

        Args:
          account_id: Filter Card Payments to ones belonging to the specified Account.

          card_id: Filter Card Payments to ones belonging to the specified Card.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_payments",
            page=SyncPage[CardPayment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "card_id": card_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    card_payment_list_params.CardPaymentListParams,
                ),
            ),
            model=CardPayment,
        )


class AsyncCardPayments(AsyncAPIResource):
    with_raw_response: AsyncCardPaymentsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCardPaymentsWithRawResponse(self)

    async def retrieve(
        self,
        card_payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardPayment:
        """
        Retrieve a Card Payment

        Args:
          card_payment_id: The identifier of the Card Payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/card_payments/{card_payment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardPayment,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        card_id: str | NotGiven = NOT_GIVEN,
        created_at: card_payment_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CardPayment, AsyncPage[CardPayment]]:
        """
        List Card Payments

        Args:
          account_id: Filter Card Payments to ones belonging to the specified Account.

          card_id: Filter Card Payments to ones belonging to the specified Card.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_payments",
            page=AsyncPage[CardPayment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "card_id": card_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    card_payment_list_params.CardPaymentListParams,
                ),
            ),
            model=CardPayment,
        )


class CardPaymentsWithRawResponse:
    def __init__(self, card_payments: CardPayments) -> None:
        self.retrieve = to_raw_response_wrapper(
            card_payments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            card_payments.list,
        )


class AsyncCardPaymentsWithRawResponse:
    def __init__(self, card_payments: AsyncCardPayments) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            card_payments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            card_payments.list,
        )
