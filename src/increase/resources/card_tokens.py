# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import card_token_list_params
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
from ..types.card_token import CardToken
from ..types.card_token_capabilities import CardTokenCapabilities

__all__ = ["CardTokensResource", "AsyncCardTokensResource"]


class CardTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardTokensResourceWithStreamingResponse(self)

    def retrieve(
        self,
        card_token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardToken:
        """
        Retrieve a Card Token

        Args:
          card_token_id: The identifier of the Card Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token_id:
            raise ValueError(f"Expected a non-empty value for `card_token_id` but received {card_token_id!r}")
        return self._get(
            f"/card_tokens/{card_token_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardToken,
        )

    def list(
        self,
        *,
        created_at: card_token_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CardToken]:
        """
        List Card Tokens

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_tokens",
            page=SyncPage[CardToken],
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
                    },
                    card_token_list_params.CardTokenListParams,
                ),
            ),
            model=CardToken,
        )

    def capabilities(
        self,
        card_token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardTokenCapabilities:
        """
        The capabilities of a Card Token describe whether the card can be used for
        specific operations, such as Card Push Transfers. The capabilities can change
        over time based on the issuing bank's configuration of the card range.

        Args:
          card_token_id: The identifier of the Card Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token_id:
            raise ValueError(f"Expected a non-empty value for `card_token_id` but received {card_token_id!r}")
        return self._get(
            f"/card_tokens/{card_token_id}/capabilities",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardTokenCapabilities,
        )


class AsyncCardTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardTokensResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        card_token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardToken:
        """
        Retrieve a Card Token

        Args:
          card_token_id: The identifier of the Card Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token_id:
            raise ValueError(f"Expected a non-empty value for `card_token_id` but received {card_token_id!r}")
        return await self._get(
            f"/card_tokens/{card_token_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardToken,
        )

    def list(
        self,
        *,
        created_at: card_token_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CardToken, AsyncPage[CardToken]]:
        """
        List Card Tokens

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_tokens",
            page=AsyncPage[CardToken],
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
                    },
                    card_token_list_params.CardTokenListParams,
                ),
            ),
            model=CardToken,
        )

    async def capabilities(
        self,
        card_token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardTokenCapabilities:
        """
        The capabilities of a Card Token describe whether the card can be used for
        specific operations, such as Card Push Transfers. The capabilities can change
        over time based on the issuing bank's configuration of the card range.

        Args:
          card_token_id: The identifier of the Card Token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token_id:
            raise ValueError(f"Expected a non-empty value for `card_token_id` but received {card_token_id!r}")
        return await self._get(
            f"/card_tokens/{card_token_id}/capabilities",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardTokenCapabilities,
        )


class CardTokensResourceWithRawResponse:
    def __init__(self, card_tokens: CardTokensResource) -> None:
        self._card_tokens = card_tokens

        self.retrieve = to_raw_response_wrapper(
            card_tokens.retrieve,
        )
        self.list = to_raw_response_wrapper(
            card_tokens.list,
        )
        self.capabilities = to_raw_response_wrapper(
            card_tokens.capabilities,
        )


class AsyncCardTokensResourceWithRawResponse:
    def __init__(self, card_tokens: AsyncCardTokensResource) -> None:
        self._card_tokens = card_tokens

        self.retrieve = async_to_raw_response_wrapper(
            card_tokens.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            card_tokens.list,
        )
        self.capabilities = async_to_raw_response_wrapper(
            card_tokens.capabilities,
        )


class CardTokensResourceWithStreamingResponse:
    def __init__(self, card_tokens: CardTokensResource) -> None:
        self._card_tokens = card_tokens

        self.retrieve = to_streamed_response_wrapper(
            card_tokens.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            card_tokens.list,
        )
        self.capabilities = to_streamed_response_wrapper(
            card_tokens.capabilities,
        )


class AsyncCardTokensResourceWithStreamingResponse:
    def __init__(self, card_tokens: AsyncCardTokensResource) -> None:
        self._card_tokens = card_tokens

        self.retrieve = async_to_streamed_response_wrapper(
            card_tokens.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            card_tokens.list,
        )
        self.capabilities = async_to_streamed_response_wrapper(
            card_tokens.capabilities,
        )
