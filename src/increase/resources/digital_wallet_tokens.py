# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import digital_wallet_token_list_params
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
from ..types.digital_wallet_token import DigitalWalletToken

__all__ = ["DigitalWalletTokensResource", "AsyncDigitalWalletTokensResource"]


class DigitalWalletTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DigitalWalletTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return DigitalWalletTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DigitalWalletTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return DigitalWalletTokensResourceWithStreamingResponse(self)

    def retrieve(
        self,
        digital_wallet_token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DigitalWalletToken:
        """
        Retrieve a Digital Wallet Token

        Args:
          digital_wallet_token_id: The identifier of the Digital Wallet Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not digital_wallet_token_id:
            raise ValueError(
                f"Expected a non-empty value for `digital_wallet_token_id` but received {digital_wallet_token_id!r}"
            )
        return self._get(
            f"/digital_wallet_tokens/{digital_wallet_token_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DigitalWalletToken,
        )

    def list(
        self,
        *,
        card_id: str | NotGiven = NOT_GIVEN,
        created_at: digital_wallet_token_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[DigitalWalletToken]:
        """
        List Digital Wallet Tokens

        Args:
          card_id: Filter Digital Wallet Tokens to ones belonging to the specified Card.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/digital_wallet_tokens",
            page=SyncPage[DigitalWalletToken],
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
                    digital_wallet_token_list_params.DigitalWalletTokenListParams,
                ),
            ),
            model=DigitalWalletToken,
        )


class AsyncDigitalWalletTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDigitalWalletTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDigitalWalletTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDigitalWalletTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncDigitalWalletTokensResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        digital_wallet_token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DigitalWalletToken:
        """
        Retrieve a Digital Wallet Token

        Args:
          digital_wallet_token_id: The identifier of the Digital Wallet Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not digital_wallet_token_id:
            raise ValueError(
                f"Expected a non-empty value for `digital_wallet_token_id` but received {digital_wallet_token_id!r}"
            )
        return await self._get(
            f"/digital_wallet_tokens/{digital_wallet_token_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DigitalWalletToken,
        )

    def list(
        self,
        *,
        card_id: str | NotGiven = NOT_GIVEN,
        created_at: digital_wallet_token_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DigitalWalletToken, AsyncPage[DigitalWalletToken]]:
        """
        List Digital Wallet Tokens

        Args:
          card_id: Filter Digital Wallet Tokens to ones belonging to the specified Card.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/digital_wallet_tokens",
            page=AsyncPage[DigitalWalletToken],
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
                    digital_wallet_token_list_params.DigitalWalletTokenListParams,
                ),
            ),
            model=DigitalWalletToken,
        )


class DigitalWalletTokensResourceWithRawResponse:
    def __init__(self, digital_wallet_tokens: DigitalWalletTokensResource) -> None:
        self._digital_wallet_tokens = digital_wallet_tokens

        self.retrieve = to_raw_response_wrapper(
            digital_wallet_tokens.retrieve,
        )
        self.list = to_raw_response_wrapper(
            digital_wallet_tokens.list,
        )


class AsyncDigitalWalletTokensResourceWithRawResponse:
    def __init__(self, digital_wallet_tokens: AsyncDigitalWalletTokensResource) -> None:
        self._digital_wallet_tokens = digital_wallet_tokens

        self.retrieve = async_to_raw_response_wrapper(
            digital_wallet_tokens.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            digital_wallet_tokens.list,
        )


class DigitalWalletTokensResourceWithStreamingResponse:
    def __init__(self, digital_wallet_tokens: DigitalWalletTokensResource) -> None:
        self._digital_wallet_tokens = digital_wallet_tokens

        self.retrieve = to_streamed_response_wrapper(
            digital_wallet_tokens.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            digital_wallet_tokens.list,
        )


class AsyncDigitalWalletTokensResourceWithStreamingResponse:
    def __init__(self, digital_wallet_tokens: AsyncDigitalWalletTokensResource) -> None:
        self._digital_wallet_tokens = digital_wallet_tokens

        self.retrieve = async_to_streamed_response_wrapper(
            digital_wallet_tokens.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            digital_wallet_tokens.list,
        )
