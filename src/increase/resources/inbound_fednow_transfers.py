# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import inbound_fednow_transfer_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.inbound_fednow_transfer import InboundFednowTransfer

__all__ = ["InboundFednowTransfersResource", "AsyncInboundFednowTransfersResource"]


class InboundFednowTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundFednowTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundFednowTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundFednowTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundFednowTransfersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        inbound_fednow_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundFednowTransfer:
        """
        Retrieve an Inbound FedNow Transfer

        Args:
          inbound_fednow_transfer_id: The identifier of the Inbound FedNow Transfer to get details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_fednow_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_fednow_transfer_id` but received {inbound_fednow_transfer_id!r}"
            )
        return self._get(
            f"/inbound_fednow_transfers/{inbound_fednow_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundFednowTransfer,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        account_number_id: str | Omit = omit,
        created_at: inbound_fednow_transfer_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[InboundFednowTransfer]:
        """
        List Inbound FedNow Transfers

        Args:
          account_id: Filter Inbound FedNow Transfers to those belonging to the specified Account.

          account_number_id: Filter Inbound FedNow Transfers to ones belonging to the specified Account
              Number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_fednow_transfers",
            page=SyncPage[InboundFednowTransfer],
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
                    inbound_fednow_transfer_list_params.InboundFednowTransferListParams,
                ),
            ),
            model=InboundFednowTransfer,
        )


class AsyncInboundFednowTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundFednowTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundFednowTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundFednowTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundFednowTransfersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        inbound_fednow_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundFednowTransfer:
        """
        Retrieve an Inbound FedNow Transfer

        Args:
          inbound_fednow_transfer_id: The identifier of the Inbound FedNow Transfer to get details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_fednow_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_fednow_transfer_id` but received {inbound_fednow_transfer_id!r}"
            )
        return await self._get(
            f"/inbound_fednow_transfers/{inbound_fednow_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundFednowTransfer,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        account_number_id: str | Omit = omit,
        created_at: inbound_fednow_transfer_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InboundFednowTransfer, AsyncPage[InboundFednowTransfer]]:
        """
        List Inbound FedNow Transfers

        Args:
          account_id: Filter Inbound FedNow Transfers to those belonging to the specified Account.

          account_number_id: Filter Inbound FedNow Transfers to ones belonging to the specified Account
              Number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_fednow_transfers",
            page=AsyncPage[InboundFednowTransfer],
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
                    inbound_fednow_transfer_list_params.InboundFednowTransferListParams,
                ),
            ),
            model=InboundFednowTransfer,
        )


class InboundFednowTransfersResourceWithRawResponse:
    def __init__(self, inbound_fednow_transfers: InboundFednowTransfersResource) -> None:
        self._inbound_fednow_transfers = inbound_fednow_transfers

        self.retrieve = to_raw_response_wrapper(
            inbound_fednow_transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inbound_fednow_transfers.list,
        )


class AsyncInboundFednowTransfersResourceWithRawResponse:
    def __init__(self, inbound_fednow_transfers: AsyncInboundFednowTransfersResource) -> None:
        self._inbound_fednow_transfers = inbound_fednow_transfers

        self.retrieve = async_to_raw_response_wrapper(
            inbound_fednow_transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inbound_fednow_transfers.list,
        )


class InboundFednowTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_fednow_transfers: InboundFednowTransfersResource) -> None:
        self._inbound_fednow_transfers = inbound_fednow_transfers

        self.retrieve = to_streamed_response_wrapper(
            inbound_fednow_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inbound_fednow_transfers.list,
        )


class AsyncInboundFednowTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_fednow_transfers: AsyncInboundFednowTransfersResource) -> None:
        self._inbound_fednow_transfers = inbound_fednow_transfers

        self.retrieve = async_to_streamed_response_wrapper(
            inbound_fednow_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_fednow_transfers.list,
        )
