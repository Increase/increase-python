# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import inbound_real_time_payments_transfer_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.inbound_real_time_payments_transfer import InboundRealTimePaymentsTransfer

__all__ = ["InboundRealTimePaymentsTransfersResource", "AsyncInboundRealTimePaymentsTransfersResource"]


class InboundRealTimePaymentsTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundRealTimePaymentsTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundRealTimePaymentsTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundRealTimePaymentsTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundRealTimePaymentsTransfersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        inbound_real_time_payments_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundRealTimePaymentsTransfer:
        """
        Retrieve an Inbound Real-Time Payments Transfer

        Args:
          inbound_real_time_payments_transfer_id: The identifier of the Inbound Real-Time Payments Transfer to get details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_real_time_payments_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_real_time_payments_transfer_id` but received {inbound_real_time_payments_transfer_id!r}"
            )
        return self._get(
            f"/inbound_real_time_payments_transfers/{inbound_real_time_payments_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundRealTimePaymentsTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        account_number_id: str | NotGiven = NOT_GIVEN,
        created_at: inbound_real_time_payments_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InboundRealTimePaymentsTransfer]:
        """
        List Inbound Real-Time Payments Transfers

        Args:
          account_id: Filter Inbound Real-Time Payments Transfers to those belonging to the specified
              Account.

          account_number_id: Filter Inbound Real-Time Payments Transfers to ones belonging to the specified
              Account Number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_real_time_payments_transfers",
            page=SyncPage[InboundRealTimePaymentsTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "account_number_id": account_number_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    inbound_real_time_payments_transfer_list_params.InboundRealTimePaymentsTransferListParams,
                ),
            ),
            model=InboundRealTimePaymentsTransfer,
        )


class AsyncInboundRealTimePaymentsTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        inbound_real_time_payments_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundRealTimePaymentsTransfer:
        """
        Retrieve an Inbound Real-Time Payments Transfer

        Args:
          inbound_real_time_payments_transfer_id: The identifier of the Inbound Real-Time Payments Transfer to get details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_real_time_payments_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_real_time_payments_transfer_id` but received {inbound_real_time_payments_transfer_id!r}"
            )
        return await self._get(
            f"/inbound_real_time_payments_transfers/{inbound_real_time_payments_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundRealTimePaymentsTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        account_number_id: str | NotGiven = NOT_GIVEN,
        created_at: inbound_real_time_payments_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InboundRealTimePaymentsTransfer, AsyncPage[InboundRealTimePaymentsTransfer]]:
        """
        List Inbound Real-Time Payments Transfers

        Args:
          account_id: Filter Inbound Real-Time Payments Transfers to those belonging to the specified
              Account.

          account_number_id: Filter Inbound Real-Time Payments Transfers to ones belonging to the specified
              Account Number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_real_time_payments_transfers",
            page=AsyncPage[InboundRealTimePaymentsTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "account_number_id": account_number_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    inbound_real_time_payments_transfer_list_params.InboundRealTimePaymentsTransferListParams,
                ),
            ),
            model=InboundRealTimePaymentsTransfer,
        )


class InboundRealTimePaymentsTransfersResourceWithRawResponse:
    def __init__(self, inbound_real_time_payments_transfers: InboundRealTimePaymentsTransfersResource) -> None:
        self._inbound_real_time_payments_transfers = inbound_real_time_payments_transfers

        self.retrieve = to_raw_response_wrapper(
            inbound_real_time_payments_transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inbound_real_time_payments_transfers.list,
        )


class AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse:
    def __init__(self, inbound_real_time_payments_transfers: AsyncInboundRealTimePaymentsTransfersResource) -> None:
        self._inbound_real_time_payments_transfers = inbound_real_time_payments_transfers

        self.retrieve = async_to_raw_response_wrapper(
            inbound_real_time_payments_transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inbound_real_time_payments_transfers.list,
        )


class InboundRealTimePaymentsTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_real_time_payments_transfers: InboundRealTimePaymentsTransfersResource) -> None:
        self._inbound_real_time_payments_transfers = inbound_real_time_payments_transfers

        self.retrieve = to_streamed_response_wrapper(
            inbound_real_time_payments_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inbound_real_time_payments_transfers.list,
        )


class AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_real_time_payments_transfers: AsyncInboundRealTimePaymentsTransfersResource) -> None:
        self._inbound_real_time_payments_transfers = inbound_real_time_payments_transfers

        self.retrieve = async_to_streamed_response_wrapper(
            inbound_real_time_payments_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_real_time_payments_transfers.list,
        )
