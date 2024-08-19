# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import card_authorization_create_params
from ...types.simulations.card_authorization_create_response import CardAuthorizationCreateResponse

__all__ = ["CardAuthorizationsResource", "AsyncCardAuthorizationsResource"]


class CardAuthorizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardAuthorizationsResourceWithRawResponse:
        return CardAuthorizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardAuthorizationsResourceWithStreamingResponse:
        return CardAuthorizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        card_id: str | NotGiven = NOT_GIVEN,
        digital_wallet_token_id: str | NotGiven = NOT_GIVEN,
        event_subscription_id: str | NotGiven = NOT_GIVEN,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        merchant_category_code: str | NotGiven = NOT_GIVEN,
        merchant_city: str | NotGiven = NOT_GIVEN,
        merchant_country: str | NotGiven = NOT_GIVEN,
        merchant_descriptor: str | NotGiven = NOT_GIVEN,
        physical_card_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardAuthorizationCreateResponse:
        """Simulates a purchase authorization on a [Card](#cards).

        Depending on the balance
        available to the card and the `amount` submitted, the authorization activity
        will result in a [Pending Transaction](#pending-transactions) of type
        `card_authorization` or a [Declined Transaction](#declined-transactions) of type
        `card_decline`. You can pass either a Card id or a
        [Digital Wallet Token](#digital-wallet-tokens) id to simulate the two different
        ways purchases can be made.

        Args:
          amount: The authorization amount in cents.

          card_id: The identifier of the Card to be authorized.

          digital_wallet_token_id: The identifier of the Digital Wallet Token to be authorized.

          event_subscription_id: The identifier of the Event Subscription to use. If provided, will override the
              default real time event subscription. Because you can only create one real time
              decision event subscription, you can use this field to route events to any
              specified event subscription for testing purposes.

          merchant_acceptor_id: The merchant identifier (commonly abbreviated as MID) of the merchant the card
              is transacting with.

          merchant_category_code: The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
              card is transacting with.

          merchant_city: The city the merchant resides in.

          merchant_country: The country the merchant resides in.

          merchant_descriptor: The merchant descriptor of the merchant the card is transacting with.

          physical_card_id: The identifier of the Physical Card to be authorized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_authorizations",
            body=maybe_transform(
                {
                    "amount": amount,
                    "card_id": card_id,
                    "digital_wallet_token_id": digital_wallet_token_id,
                    "event_subscription_id": event_subscription_id,
                    "merchant_acceptor_id": merchant_acceptor_id,
                    "merchant_category_code": merchant_category_code,
                    "merchant_city": merchant_city,
                    "merchant_country": merchant_country,
                    "merchant_descriptor": merchant_descriptor,
                    "physical_card_id": physical_card_id,
                },
                card_authorization_create_params.CardAuthorizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardAuthorizationCreateResponse,
        )


class AsyncCardAuthorizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardAuthorizationsResourceWithRawResponse:
        return AsyncCardAuthorizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardAuthorizationsResourceWithStreamingResponse:
        return AsyncCardAuthorizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        card_id: str | NotGiven = NOT_GIVEN,
        digital_wallet_token_id: str | NotGiven = NOT_GIVEN,
        event_subscription_id: str | NotGiven = NOT_GIVEN,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        merchant_category_code: str | NotGiven = NOT_GIVEN,
        merchant_city: str | NotGiven = NOT_GIVEN,
        merchant_country: str | NotGiven = NOT_GIVEN,
        merchant_descriptor: str | NotGiven = NOT_GIVEN,
        physical_card_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardAuthorizationCreateResponse:
        """Simulates a purchase authorization on a [Card](#cards).

        Depending on the balance
        available to the card and the `amount` submitted, the authorization activity
        will result in a [Pending Transaction](#pending-transactions) of type
        `card_authorization` or a [Declined Transaction](#declined-transactions) of type
        `card_decline`. You can pass either a Card id or a
        [Digital Wallet Token](#digital-wallet-tokens) id to simulate the two different
        ways purchases can be made.

        Args:
          amount: The authorization amount in cents.

          card_id: The identifier of the Card to be authorized.

          digital_wallet_token_id: The identifier of the Digital Wallet Token to be authorized.

          event_subscription_id: The identifier of the Event Subscription to use. If provided, will override the
              default real time event subscription. Because you can only create one real time
              decision event subscription, you can use this field to route events to any
              specified event subscription for testing purposes.

          merchant_acceptor_id: The merchant identifier (commonly abbreviated as MID) of the merchant the card
              is transacting with.

          merchant_category_code: The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
              card is transacting with.

          merchant_city: The city the merchant resides in.

          merchant_country: The country the merchant resides in.

          merchant_descriptor: The merchant descriptor of the merchant the card is transacting with.

          physical_card_id: The identifier of the Physical Card to be authorized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_authorizations",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "card_id": card_id,
                    "digital_wallet_token_id": digital_wallet_token_id,
                    "event_subscription_id": event_subscription_id,
                    "merchant_acceptor_id": merchant_acceptor_id,
                    "merchant_category_code": merchant_category_code,
                    "merchant_city": merchant_city,
                    "merchant_country": merchant_country,
                    "merchant_descriptor": merchant_descriptor,
                    "physical_card_id": physical_card_id,
                },
                card_authorization_create_params.CardAuthorizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardAuthorizationCreateResponse,
        )


class CardAuthorizationsResourceWithRawResponse:
    def __init__(self, card_authorizations: CardAuthorizationsResource) -> None:
        self._card_authorizations = card_authorizations

        self.create = to_raw_response_wrapper(
            card_authorizations.create,
        )


class AsyncCardAuthorizationsResourceWithRawResponse:
    def __init__(self, card_authorizations: AsyncCardAuthorizationsResource) -> None:
        self._card_authorizations = card_authorizations

        self.create = async_to_raw_response_wrapper(
            card_authorizations.create,
        )


class CardAuthorizationsResourceWithStreamingResponse:
    def __init__(self, card_authorizations: CardAuthorizationsResource) -> None:
        self._card_authorizations = card_authorizations

        self.create = to_streamed_response_wrapper(
            card_authorizations.create,
        )


class AsyncCardAuthorizationsResourceWithStreamingResponse:
    def __init__(self, card_authorizations: AsyncCardAuthorizationsResource) -> None:
        self._card_authorizations = card_authorizations

        self.create = async_to_streamed_response_wrapper(
            card_authorizations.create,
        )
