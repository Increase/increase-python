# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import shared
from ..._types import Body, Query, Headers
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

__all__ = ["DigitalWalletTokenRequests", "AsyncDigitalWalletTokenRequests"]


class DigitalWalletTokenRequests(SyncAPIResource):
    def create(
        self,
        *,
        card_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> shared.InboundDigitalWalletTokenRequestSimulationResult:
        """
        Simulates a user attempting add a Card to a digital wallet such as Apple Pay.

        Args:
          card_id: The identifier of the Card to be authorized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/simulations/digital_wallet_token_requests",
            body={"card_id": card_id},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=shared.InboundDigitalWalletTokenRequestSimulationResult,
        )


class AsyncDigitalWalletTokenRequests(AsyncAPIResource):
    async def create(
        self,
        *,
        card_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> shared.InboundDigitalWalletTokenRequestSimulationResult:
        """
        Simulates a user attempting add a Card to a digital wallet such as Apple Pay.

        Args:
          card_id: The identifier of the Card to be authorized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/simulations/digital_wallet_token_requests",
            body={"card_id": card_id},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=shared.InboundDigitalWalletTokenRequestSimulationResult,
        )
