# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import inbound_mail_item_list_params
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
from ..types.inbound_mail_item import InboundMailItem

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

    def retrieve(
        self,
        inbound_mail_item_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundMailItem:
        """
        Retrieve an Inbound Mail Item

        Args:
          inbound_mail_item_id: The identifier of the Inbound Mail Item to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_mail_item_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_mail_item_id` but received {inbound_mail_item_id!r}"
            )
        return self._get(
            f"/inbound_mail_items/{inbound_mail_item_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundMailItem,
        )

    def list(
        self,
        *,
        created_at: inbound_mail_item_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        lockbox_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InboundMailItem]:
        """
        List Inbound Mail Items

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          lockbox_id: Filter Inbound Mail Items to ones sent to the provided Lockbox.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_mail_items",
            page=SyncPage[InboundMailItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                        "lockbox_id": lockbox_id,
                    },
                    inbound_mail_item_list_params.InboundMailItemListParams,
                ),
            ),
            model=InboundMailItem,
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

    async def retrieve(
        self,
        inbound_mail_item_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundMailItem:
        """
        Retrieve an Inbound Mail Item

        Args:
          inbound_mail_item_id: The identifier of the Inbound Mail Item to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_mail_item_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_mail_item_id` but received {inbound_mail_item_id!r}"
            )
        return await self._get(
            f"/inbound_mail_items/{inbound_mail_item_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundMailItem,
        )

    def list(
        self,
        *,
        created_at: inbound_mail_item_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        lockbox_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InboundMailItem, AsyncPage[InboundMailItem]]:
        """
        List Inbound Mail Items

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          lockbox_id: Filter Inbound Mail Items to ones sent to the provided Lockbox.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_mail_items",
            page=AsyncPage[InboundMailItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                        "lockbox_id": lockbox_id,
                    },
                    inbound_mail_item_list_params.InboundMailItemListParams,
                ),
            ),
            model=InboundMailItem,
        )


class InboundMailItemsResourceWithRawResponse:
    def __init__(self, inbound_mail_items: InboundMailItemsResource) -> None:
        self._inbound_mail_items = inbound_mail_items

        self.retrieve = to_raw_response_wrapper(
            inbound_mail_items.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inbound_mail_items.list,
        )


class AsyncInboundMailItemsResourceWithRawResponse:
    def __init__(self, inbound_mail_items: AsyncInboundMailItemsResource) -> None:
        self._inbound_mail_items = inbound_mail_items

        self.retrieve = async_to_raw_response_wrapper(
            inbound_mail_items.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inbound_mail_items.list,
        )


class InboundMailItemsResourceWithStreamingResponse:
    def __init__(self, inbound_mail_items: InboundMailItemsResource) -> None:
        self._inbound_mail_items = inbound_mail_items

        self.retrieve = to_streamed_response_wrapper(
            inbound_mail_items.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inbound_mail_items.list,
        )


class AsyncInboundMailItemsResourceWithStreamingResponse:
    def __init__(self, inbound_mail_items: AsyncInboundMailItemsResource) -> None:
        self._inbound_mail_items = inbound_mail_items

        self.retrieve = async_to_streamed_response_wrapper(
            inbound_mail_items.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_mail_items.list,
        )
