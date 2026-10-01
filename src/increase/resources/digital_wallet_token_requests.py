# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import digital_wallet_token_request_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.digital_wallet_token_request import DigitalWalletTokenRequest

__all__ = ["DigitalWalletTokenRequestsResource", "AsyncDigitalWalletTokenRequestsResource"]


class DigitalWalletTokenRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DigitalWalletTokenRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return DigitalWalletTokenRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DigitalWalletTokenRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return DigitalWalletTokenRequestsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        digital_wallet_token_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DigitalWalletTokenRequest:
        """
        Retrieve a Digital Wallet Token Request

        Args:
          digital_wallet_token_request_id: The identifier of the Digital Wallet Token Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not digital_wallet_token_request_id:
            raise ValueError(
                f"Expected a non-empty value for `digital_wallet_token_request_id` but received {digital_wallet_token_request_id!r}"
            )
        return self._get(
            path_template(
                "/digital_wallet_token_requests/{digital_wallet_token_request_id}",
                digital_wallet_token_request_id=digital_wallet_token_request_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DigitalWalletTokenRequest,
        )

    def list(
        self,
        *,
        card_id: str | Omit = omit,
        created_at: digital_wallet_token_request_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[DigitalWalletTokenRequest]:
        """
        List Digital Wallet Token Requests

        Args:
          card_id: Filter Digital Wallet Token Requests to ones for the specified Card.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

              Defaults to `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/digital_wallet_token_requests",
            page=SyncPage[DigitalWalletTokenRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "card_id": card_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    digital_wallet_token_request_list_params.DigitalWalletTokenRequestListParams,
                ),
            ),
            model=DigitalWalletTokenRequest,
        )


class AsyncDigitalWalletTokenRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDigitalWalletTokenRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDigitalWalletTokenRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDigitalWalletTokenRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncDigitalWalletTokenRequestsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        digital_wallet_token_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DigitalWalletTokenRequest:
        """
        Retrieve a Digital Wallet Token Request

        Args:
          digital_wallet_token_request_id: The identifier of the Digital Wallet Token Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not digital_wallet_token_request_id:
            raise ValueError(
                f"Expected a non-empty value for `digital_wallet_token_request_id` but received {digital_wallet_token_request_id!r}"
            )
        return await self._get(
            path_template(
                "/digital_wallet_token_requests/{digital_wallet_token_request_id}",
                digital_wallet_token_request_id=digital_wallet_token_request_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DigitalWalletTokenRequest,
        )

    def list(
        self,
        *,
        card_id: str | Omit = omit,
        created_at: digital_wallet_token_request_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DigitalWalletTokenRequest, AsyncPage[DigitalWalletTokenRequest]]:
        """
        List Digital Wallet Token Requests

        Args:
          card_id: Filter Digital Wallet Token Requests to ones for the specified Card.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

              Defaults to `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/digital_wallet_token_requests",
            page=AsyncPage[DigitalWalletTokenRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "card_id": card_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    digital_wallet_token_request_list_params.DigitalWalletTokenRequestListParams,
                ),
            ),
            model=DigitalWalletTokenRequest,
        )


class DigitalWalletTokenRequestsResourceWithRawResponse:
    def __init__(self, digital_wallet_token_requests: DigitalWalletTokenRequestsResource) -> None:
        self._digital_wallet_token_requests = digital_wallet_token_requests

        self.retrieve = to_raw_response_wrapper(
            digital_wallet_token_requests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            digital_wallet_token_requests.list,
        )


class AsyncDigitalWalletTokenRequestsResourceWithRawResponse:
    def __init__(self, digital_wallet_token_requests: AsyncDigitalWalletTokenRequestsResource) -> None:
        self._digital_wallet_token_requests = digital_wallet_token_requests

        self.retrieve = async_to_raw_response_wrapper(
            digital_wallet_token_requests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            digital_wallet_token_requests.list,
        )


class DigitalWalletTokenRequestsResourceWithStreamingResponse:
    def __init__(self, digital_wallet_token_requests: DigitalWalletTokenRequestsResource) -> None:
        self._digital_wallet_token_requests = digital_wallet_token_requests

        self.retrieve = to_streamed_response_wrapper(
            digital_wallet_token_requests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            digital_wallet_token_requests.list,
        )


class AsyncDigitalWalletTokenRequestsResourceWithStreamingResponse:
    def __init__(self, digital_wallet_token_requests: AsyncDigitalWalletTokenRequestsResource) -> None:
        self._digital_wallet_token_requests = digital_wallet_token_requests

        self.retrieve = async_to_streamed_response_wrapper(
            digital_wallet_token_requests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            digital_wallet_token_requests.list,
        )
