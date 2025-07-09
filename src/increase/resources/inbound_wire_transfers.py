# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import inbound_wire_transfer_list_params, inbound_wire_transfer_reverse_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.inbound_wire_transfer import InboundWireTransfer

__all__ = ["InboundWireTransfersResource", "AsyncInboundWireTransfersResource"]


class InboundWireTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundWireTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundWireTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundWireTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundWireTransfersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        inbound_wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundWireTransfer:
        """
        Retrieve an Inbound Wire Transfer

        Args:
          inbound_wire_transfer_id: The identifier of the Inbound Wire Transfer to get details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_wire_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_wire_transfer_id` but received {inbound_wire_transfer_id!r}"
            )
        return self._get(
            f"/inbound_wire_transfers/{inbound_wire_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundWireTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        account_number_id: str | NotGiven = NOT_GIVEN,
        created_at: inbound_wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: inbound_wire_transfer_list_params.Status | NotGiven = NOT_GIVEN,
        wire_drawdown_request_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InboundWireTransfer]:
        """
        List Inbound Wire Transfers

        Args:
          account_id: Filter Inbound Wire Transfers to ones belonging to the specified Account.

          account_number_id: Filter Inbound Wire Transfers to ones belonging to the specified Account Number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          wire_drawdown_request_id: Filter Inbound Wire Transfers to ones belonging to the specified Wire Drawdown
              Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_wire_transfers",
            page=SyncPage[InboundWireTransfer],
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
                        "status": status,
                        "wire_drawdown_request_id": wire_drawdown_request_id,
                    },
                    inbound_wire_transfer_list_params.InboundWireTransferListParams,
                ),
            ),
            model=InboundWireTransfer,
        )

    def reverse(
        self,
        inbound_wire_transfer_id: str,
        *,
        reason: Literal["duplicate", "creditor_request"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundWireTransfer:
        """
        Reverse an Inbound Wire Transfer

        Args:
          inbound_wire_transfer_id: The identifier of the Inbound Wire Transfer to reverse.

          reason: Reason for the reversal.

              - `duplicate` - The inbound wire transfer was a duplicate.
              - `creditor_request` - The recipient of the wire transfer requested the funds be
                returned to the sender.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not inbound_wire_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_wire_transfer_id` but received {inbound_wire_transfer_id!r}"
            )
        return self._post(
            f"/inbound_wire_transfers/{inbound_wire_transfer_id}/reverse",
            body=maybe_transform(
                {"reason": reason}, inbound_wire_transfer_reverse_params.InboundWireTransferReverseParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundWireTransfer,
        )


class AsyncInboundWireTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundWireTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundWireTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundWireTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundWireTransfersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        inbound_wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundWireTransfer:
        """
        Retrieve an Inbound Wire Transfer

        Args:
          inbound_wire_transfer_id: The identifier of the Inbound Wire Transfer to get details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_wire_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_wire_transfer_id` but received {inbound_wire_transfer_id!r}"
            )
        return await self._get(
            f"/inbound_wire_transfers/{inbound_wire_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundWireTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        account_number_id: str | NotGiven = NOT_GIVEN,
        created_at: inbound_wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: inbound_wire_transfer_list_params.Status | NotGiven = NOT_GIVEN,
        wire_drawdown_request_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InboundWireTransfer, AsyncPage[InboundWireTransfer]]:
        """
        List Inbound Wire Transfers

        Args:
          account_id: Filter Inbound Wire Transfers to ones belonging to the specified Account.

          account_number_id: Filter Inbound Wire Transfers to ones belonging to the specified Account Number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          wire_drawdown_request_id: Filter Inbound Wire Transfers to ones belonging to the specified Wire Drawdown
              Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_wire_transfers",
            page=AsyncPage[InboundWireTransfer],
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
                        "status": status,
                        "wire_drawdown_request_id": wire_drawdown_request_id,
                    },
                    inbound_wire_transfer_list_params.InboundWireTransferListParams,
                ),
            ),
            model=InboundWireTransfer,
        )

    async def reverse(
        self,
        inbound_wire_transfer_id: str,
        *,
        reason: Literal["duplicate", "creditor_request"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundWireTransfer:
        """
        Reverse an Inbound Wire Transfer

        Args:
          inbound_wire_transfer_id: The identifier of the Inbound Wire Transfer to reverse.

          reason: Reason for the reversal.

              - `duplicate` - The inbound wire transfer was a duplicate.
              - `creditor_request` - The recipient of the wire transfer requested the funds be
                returned to the sender.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not inbound_wire_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_wire_transfer_id` but received {inbound_wire_transfer_id!r}"
            )
        return await self._post(
            f"/inbound_wire_transfers/{inbound_wire_transfer_id}/reverse",
            body=await async_maybe_transform(
                {"reason": reason}, inbound_wire_transfer_reverse_params.InboundWireTransferReverseParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundWireTransfer,
        )


class InboundWireTransfersResourceWithRawResponse:
    def __init__(self, inbound_wire_transfers: InboundWireTransfersResource) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.retrieve = to_raw_response_wrapper(
            inbound_wire_transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inbound_wire_transfers.list,
        )
        self.reverse = to_raw_response_wrapper(
            inbound_wire_transfers.reverse,
        )


class AsyncInboundWireTransfersResourceWithRawResponse:
    def __init__(self, inbound_wire_transfers: AsyncInboundWireTransfersResource) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.retrieve = async_to_raw_response_wrapper(
            inbound_wire_transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inbound_wire_transfers.list,
        )
        self.reverse = async_to_raw_response_wrapper(
            inbound_wire_transfers.reverse,
        )


class InboundWireTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_wire_transfers: InboundWireTransfersResource) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.retrieve = to_streamed_response_wrapper(
            inbound_wire_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inbound_wire_transfers.list,
        )
        self.reverse = to_streamed_response_wrapper(
            inbound_wire_transfers.reverse,
        )


class AsyncInboundWireTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_wire_transfers: AsyncInboundWireTransfersResource) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.retrieve = async_to_streamed_response_wrapper(
            inbound_wire_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_wire_transfers.list,
        )
        self.reverse = async_to_streamed_response_wrapper(
            inbound_wire_transfers.reverse,
        )
