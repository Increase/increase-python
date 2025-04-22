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
from ...types.simulations import digital_wallet_token_request_create_params
from ...types.simulations.digital_wallet_token_request_create_response import DigitalWalletTokenRequestCreateResponse

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

    def create(
        self,
        *,
        card_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DigitalWalletTokenRequestCreateResponse:
        """
        Simulates a user attempting add a [Card](#cards) to a digital wallet such as
        Apple Pay.

        Args:
          card_id: The identifier of the Card to be authorized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/digital_wallet_token_requests",
            body=maybe_transform(
                {"card_id": card_id}, digital_wallet_token_request_create_params.DigitalWalletTokenRequestCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DigitalWalletTokenRequestCreateResponse,
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

    async def create(
        self,
        *,
        card_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DigitalWalletTokenRequestCreateResponse:
        """
        Simulates a user attempting add a [Card](#cards) to a digital wallet such as
        Apple Pay.

        Args:
          card_id: The identifier of the Card to be authorized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/digital_wallet_token_requests",
            body=await async_maybe_transform(
                {"card_id": card_id}, digital_wallet_token_request_create_params.DigitalWalletTokenRequestCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DigitalWalletTokenRequestCreateResponse,
        )


class DigitalWalletTokenRequestsResourceWithRawResponse:
    def __init__(self, digital_wallet_token_requests: DigitalWalletTokenRequestsResource) -> None:
        self._digital_wallet_token_requests = digital_wallet_token_requests

        self.create = to_raw_response_wrapper(
            digital_wallet_token_requests.create,
        )


class AsyncDigitalWalletTokenRequestsResourceWithRawResponse:
    def __init__(self, digital_wallet_token_requests: AsyncDigitalWalletTokenRequestsResource) -> None:
        self._digital_wallet_token_requests = digital_wallet_token_requests

        self.create = async_to_raw_response_wrapper(
            digital_wallet_token_requests.create,
        )


class DigitalWalletTokenRequestsResourceWithStreamingResponse:
    def __init__(self, digital_wallet_token_requests: DigitalWalletTokenRequestsResource) -> None:
        self._digital_wallet_token_requests = digital_wallet_token_requests

        self.create = to_streamed_response_wrapper(
            digital_wallet_token_requests.create,
        )


class AsyncDigitalWalletTokenRequestsResourceWithStreamingResponse:
    def __init__(self, digital_wallet_token_requests: AsyncDigitalWalletTokenRequestsResource) -> None:
        self._digital_wallet_token_requests = digital_wallet_token_requests

        self.create = async_to_streamed_response_wrapper(
            digital_wallet_token_requests.create,
        )
