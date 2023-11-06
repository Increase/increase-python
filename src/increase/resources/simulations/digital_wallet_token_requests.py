# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.simulations import (
    DigitalWalletTokenRequestCreateResponse,
    digital_wallet_token_request_create_params,
)

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["DigitalWalletTokenRequests", "AsyncDigitalWalletTokenRequests"]


class DigitalWalletTokenRequests(SyncAPIResource):
    with_raw_response: DigitalWalletTokenRequestsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = DigitalWalletTokenRequestsWithRawResponse(self)

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


class AsyncDigitalWalletTokenRequests(AsyncAPIResource):
    with_raw_response: AsyncDigitalWalletTokenRequestsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncDigitalWalletTokenRequestsWithRawResponse(self)

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


class DigitalWalletTokenRequestsWithRawResponse:
    def __init__(self, digital_wallet_token_requests: DigitalWalletTokenRequests) -> None:
        self.create = to_raw_response_wrapper(
            digital_wallet_token_requests.create,
        )


class AsyncDigitalWalletTokenRequestsWithRawResponse:
    def __init__(self, digital_wallet_token_requests: AsyncDigitalWalletTokenRequests) -> None:
        self.create = async_to_raw_response_wrapper(
            digital_wallet_token_requests.create,
        )
