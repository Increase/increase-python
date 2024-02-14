# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import CardDispute, card_dispute_list_params, card_dispute_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["CardDisputes", "AsyncCardDisputes"]


class CardDisputes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardDisputesWithRawResponse:
        return CardDisputesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardDisputesWithStreamingResponse:
        return CardDisputesWithStreamingResponse(self)

    def create(
        self,
        *,
        disputed_transaction_id: str,
        explanation: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        Create a Card Dispute

        Args:
          disputed_transaction_id: The Transaction you wish to dispute. This Transaction must have a `source_type`
              of `card_settlement`.

          explanation: Why you are disputing this Transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/card_disputes",
            body=maybe_transform(
                {
                    "disputed_transaction_id": disputed_transaction_id,
                    "explanation": explanation,
                },
                card_dispute_create_params.CardDisputeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )

    def retrieve(
        self,
        card_dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardDispute:
        """
        Retrieve a Card Dispute

        Args:
          card_dispute_id: The identifier of the Card Dispute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_dispute_id:
            raise ValueError(f"Expected a non-empty value for `card_dispute_id` but received {card_dispute_id!r}")
        return self._get(
            f"/card_disputes/{card_dispute_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDispute,
        )

    def list(
        self,
        *,
        created_at: card_dispute_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: card_dispute_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CardDispute]:
        """
        List Card Disputes

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
            "/card_disputes",
            page=SyncPage[CardDispute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    card_dispute_list_params.CardDisputeListParams,
                ),
            ),
            model=CardDispute,
        )


class AsyncCardDisputes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardDisputesWithRawResponse:
        return AsyncCardDisputesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardDisputesWithStreamingResponse:
        return AsyncCardDisputesWithStreamingResponse(self)

    async def create(
        self,
        *,
        disputed_transaction_id: str,
        explanation: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        Create a Card Dispute

        Args:
          disputed_transaction_id: The Transaction you wish to dispute. This Transaction must have a `source_type`
              of `card_settlement`.

          explanation: Why you are disputing this Transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/card_disputes",
            body=maybe_transform(
                {
                    "disputed_transaction_id": disputed_transaction_id,
                    "explanation": explanation,
                },
                card_dispute_create_params.CardDisputeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )

    async def retrieve(
        self,
        card_dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardDispute:
        """
        Retrieve a Card Dispute

        Args:
          card_dispute_id: The identifier of the Card Dispute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_dispute_id:
            raise ValueError(f"Expected a non-empty value for `card_dispute_id` but received {card_dispute_id!r}")
        return await self._get(
            f"/card_disputes/{card_dispute_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDispute,
        )

    def list(
        self,
        *,
        created_at: card_dispute_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: card_dispute_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CardDispute, AsyncPage[CardDispute]]:
        """
        List Card Disputes

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
            "/card_disputes",
            page=AsyncPage[CardDispute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    card_dispute_list_params.CardDisputeListParams,
                ),
            ),
            model=CardDispute,
        )


class CardDisputesWithRawResponse:
    def __init__(self, card_disputes: CardDisputes) -> None:
        self._card_disputes = card_disputes

        self.create = _legacy_response.to_raw_response_wrapper(
            card_disputes.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            card_disputes.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            card_disputes.list,
        )


class AsyncCardDisputesWithRawResponse:
    def __init__(self, card_disputes: AsyncCardDisputes) -> None:
        self._card_disputes = card_disputes

        self.create = _legacy_response.async_to_raw_response_wrapper(
            card_disputes.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            card_disputes.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            card_disputes.list,
        )


class CardDisputesWithStreamingResponse:
    def __init__(self, card_disputes: CardDisputes) -> None:
        self._card_disputes = card_disputes

        self.create = to_streamed_response_wrapper(
            card_disputes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            card_disputes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            card_disputes.list,
        )


class AsyncCardDisputesWithStreamingResponse:
    def __init__(self, card_disputes: AsyncCardDisputes) -> None:
        self._card_disputes = card_disputes

        self.create = async_to_streamed_response_wrapper(
            card_disputes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            card_disputes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            card_disputes.list,
        )
