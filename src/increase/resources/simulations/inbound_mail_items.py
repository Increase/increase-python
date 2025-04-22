# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.simulations import inbound_mail_item_create_params
from ...types.inbound_mail_item import InboundMailItem

__all__ = ["InboundMailItemsResource", "AsyncInboundMailItemsResource"]


class InboundMailItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundMailItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundMailItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundMailItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundMailItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        lockbox_id: str,
        contents_file_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundMailItem:
        """
        Simulates an inbound mail item to your account, as if someone had mailed a
        physical check to one of your account's Lockboxes.

        Args:
          amount: The amount of the check to be simulated, in cents.

          lockbox_id: The identifier of the Lockbox to simulate inbound mail to.

          contents_file_id: The file containing the PDF contents. If not present, a default check image file
              will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/inbound_mail_items",
            body=maybe_transform(
                {
                    "amount": amount,
                    "lockbox_id": lockbox_id,
                    "contents_file_id": contents_file_id,
                },
                inbound_mail_item_create_params.InboundMailItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundMailItem,
        )


class AsyncInboundMailItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundMailItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundMailItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundMailItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundMailItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        lockbox_id: str,
        contents_file_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundMailItem:
        """
        Simulates an inbound mail item to your account, as if someone had mailed a
        physical check to one of your account's Lockboxes.

        Args:
          amount: The amount of the check to be simulated, in cents.

          lockbox_id: The identifier of the Lockbox to simulate inbound mail to.

          contents_file_id: The file containing the PDF contents. If not present, a default check image file
              will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/inbound_mail_items",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "lockbox_id": lockbox_id,
                    "contents_file_id": contents_file_id,
                },
                inbound_mail_item_create_params.InboundMailItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundMailItem,
        )


class InboundMailItemsResourceWithRawResponse:
    def __init__(self, inbound_mail_items: InboundMailItemsResource) -> None:
        self._inbound_mail_items = inbound_mail_items

        self.create = to_raw_response_wrapper(
            inbound_mail_items.create,
        )


class AsyncInboundMailItemsResourceWithRawResponse:
    def __init__(self, inbound_mail_items: AsyncInboundMailItemsResource) -> None:
        self._inbound_mail_items = inbound_mail_items

        self.create = async_to_raw_response_wrapper(
            inbound_mail_items.create,
        )


class InboundMailItemsResourceWithStreamingResponse:
    def __init__(self, inbound_mail_items: InboundMailItemsResource) -> None:
        self._inbound_mail_items = inbound_mail_items

        self.create = to_streamed_response_wrapper(
            inbound_mail_items.create,
        )


class AsyncInboundMailItemsResourceWithStreamingResponse:
    def __init__(self, inbound_mail_items: AsyncInboundMailItemsResource) -> None:
        self._inbound_mail_items = inbound_mail_items

        self.create = async_to_streamed_response_wrapper(
            inbound_mail_items.create,
        )
