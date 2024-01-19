# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import InboundWireTransfer
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["InboundWireTransfers", "AsyncInboundWireTransfers"]


class InboundWireTransfers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundWireTransfersWithRawResponse:
        return InboundWireTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundWireTransfersWithStreamingResponse:
        return InboundWireTransfersWithStreamingResponse(self)

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


class AsyncInboundWireTransfers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundWireTransfersWithRawResponse:
        return AsyncInboundWireTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundWireTransfersWithStreamingResponse:
        return AsyncInboundWireTransfersWithStreamingResponse(self)

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


class InboundWireTransfersWithRawResponse:
    def __init__(self, inbound_wire_transfers: InboundWireTransfers) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            inbound_wire_transfers.retrieve,
        )


class AsyncInboundWireTransfersWithRawResponse:
    def __init__(self, inbound_wire_transfers: AsyncInboundWireTransfers) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            inbound_wire_transfers.retrieve,
        )


class InboundWireTransfersWithStreamingResponse:
    def __init__(self, inbound_wire_transfers: InboundWireTransfers) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.retrieve = to_streamed_response_wrapper(
            inbound_wire_transfers.retrieve,
        )


class AsyncInboundWireTransfersWithStreamingResponse:
    def __init__(self, inbound_wire_transfers: AsyncInboundWireTransfers) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.retrieve = async_to_streamed_response_wrapper(
            inbound_wire_transfers.retrieve,
        )
