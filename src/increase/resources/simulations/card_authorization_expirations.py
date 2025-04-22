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
from ...types.simulations import card_authorization_expiration_create_params
from ...types.card_payment import CardPayment

__all__ = ["CardAuthorizationExpirationsResource", "AsyncCardAuthorizationExpirationsResource"]


class CardAuthorizationExpirationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardAuthorizationExpirationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardAuthorizationExpirationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardAuthorizationExpirationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardAuthorizationExpirationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        card_payment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """
        Simulates expiring a Card Authorization immediately.

        Args:
          card_payment_id: The identifier of the Card Payment to expire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_authorization_expirations",
            body=maybe_transform(
                {"card_payment_id": card_payment_id},
                card_authorization_expiration_create_params.CardAuthorizationExpirationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )


class AsyncCardAuthorizationExpirationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardAuthorizationExpirationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardAuthorizationExpirationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardAuthorizationExpirationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardAuthorizationExpirationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        card_payment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """
        Simulates expiring a Card Authorization immediately.

        Args:
          card_payment_id: The identifier of the Card Payment to expire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_authorization_expirations",
            body=await async_maybe_transform(
                {"card_payment_id": card_payment_id},
                card_authorization_expiration_create_params.CardAuthorizationExpirationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )


class CardAuthorizationExpirationsResourceWithRawResponse:
    def __init__(self, card_authorization_expirations: CardAuthorizationExpirationsResource) -> None:
        self._card_authorization_expirations = card_authorization_expirations

        self.create = to_raw_response_wrapper(
            card_authorization_expirations.create,
        )


class AsyncCardAuthorizationExpirationsResourceWithRawResponse:
    def __init__(self, card_authorization_expirations: AsyncCardAuthorizationExpirationsResource) -> None:
        self._card_authorization_expirations = card_authorization_expirations

        self.create = async_to_raw_response_wrapper(
            card_authorization_expirations.create,
        )


class CardAuthorizationExpirationsResourceWithStreamingResponse:
    def __init__(self, card_authorization_expirations: CardAuthorizationExpirationsResource) -> None:
        self._card_authorization_expirations = card_authorization_expirations

        self.create = to_streamed_response_wrapper(
            card_authorization_expirations.create,
        )


class AsyncCardAuthorizationExpirationsResourceWithStreamingResponse:
    def __init__(self, card_authorization_expirations: AsyncCardAuthorizationExpirationsResource) -> None:
        self._card_authorization_expirations = card_authorization_expirations

        self.create = async_to_streamed_response_wrapper(
            card_authorization_expirations.create,
        )
