# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

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
from ...types.card_token import CardToken
from ...types.simulations import card_token_create_params

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

    def create(
        self,
        *,
        capabilities: Iterable[card_token_create_params.Capability] | NotGiven = NOT_GIVEN,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        last4: str | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        primary_account_number_length: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardToken:
        """
        Simulates tokenizing a card in the sandbox environment.

        Args:
          capabilities: The capabilities of the outbound card token.

          expiration: The expiration date of the card.

          last4: The last 4 digits of the card number.

          prefix: The prefix of the card number, usually the first 8 digits.

          primary_account_number_length: The total length of the card number, including prefix and last4.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_tokens",
            body=maybe_transform(
                {
                    "capabilities": capabilities,
                    "expiration": expiration,
                    "last4": last4,
                    "prefix": prefix,
                    "primary_account_number_length": primary_account_number_length,
                },
                card_token_create_params.CardTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardToken,
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

    async def create(
        self,
        *,
        capabilities: Iterable[card_token_create_params.Capability] | NotGiven = NOT_GIVEN,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        last4: str | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        primary_account_number_length: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardToken:
        """
        Simulates tokenizing a card in the sandbox environment.

        Args:
          capabilities: The capabilities of the outbound card token.

          expiration: The expiration date of the card.

          last4: The last 4 digits of the card number.

          prefix: The prefix of the card number, usually the first 8 digits.

          primary_account_number_length: The total length of the card number, including prefix and last4.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_tokens",
            body=await async_maybe_transform(
                {
                    "capabilities": capabilities,
                    "expiration": expiration,
                    "last4": last4,
                    "prefix": prefix,
                    "primary_account_number_length": primary_account_number_length,
                },
                card_token_create_params.CardTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardToken,
        )


class CardTokensResourceWithRawResponse:
    def __init__(self, card_tokens: CardTokensResource) -> None:
        self._card_tokens = card_tokens

        self.create = to_raw_response_wrapper(
            card_tokens.create,
        )


class AsyncCardTokensResourceWithRawResponse:
    def __init__(self, card_tokens: AsyncCardTokensResource) -> None:
        self._card_tokens = card_tokens

        self.create = async_to_raw_response_wrapper(
            card_tokens.create,
        )


class CardTokensResourceWithStreamingResponse:
    def __init__(self, card_tokens: CardTokensResource) -> None:
        self._card_tokens = card_tokens

        self.create = to_streamed_response_wrapper(
            card_tokens.create,
        )


class AsyncCardTokensResourceWithStreamingResponse:
    def __init__(self, card_tokens: AsyncCardTokensResource) -> None:
        self._card_tokens = card_tokens

        self.create = async_to_streamed_response_wrapper(
            card_tokens.create,
        )
