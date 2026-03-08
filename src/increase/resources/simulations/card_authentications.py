# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.simulations import card_authentication_create_params, card_authentication_challenge_attempts_params
from ...types.card_payment import CardPayment

__all__ = ["CardAuthenticationsResource", "AsyncCardAuthenticationsResource"]


class CardAuthenticationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardAuthenticationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardAuthenticationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardAuthenticationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardAuthenticationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        card_id: str,
        category: Literal["payment_authentication", "non_payment_authentication"] | Omit = omit,
        device_channel: Literal["app", "browser", "three_ds_requestor_initiated"] | Omit = omit,
        merchant_acceptor_id: str | Omit = omit,
        merchant_category_code: str | Omit = omit,
        merchant_country: str | Omit = omit,
        merchant_name: str | Omit = omit,
        purchase_amount: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates a Card Authentication attempt on a [Card](#cards).

        The attempt always
        results in a [Card Payment](#card_payments) being created, either with a status
        that allows further action or a terminal failed status.

        Args:
          card_id: The identifier of the Card to be authorized.

          category: The category of the card authentication attempt.

              - `payment_authentication` - The authentication attempt is for a payment.
              - `non_payment_authentication` - The authentication attempt is not for a
                payment.

          device_channel: The device channel of the card authentication attempt.

              - `app` - The authentication attempt was made from an app.
              - `browser` - The authentication attempt was made from a browser.
              - `three_ds_requestor_initiated` - The authentication attempt was initiated by
                the 3DS Requestor.

          merchant_acceptor_id: The merchant identifier (commonly abbreviated as MID) of the merchant the card
              is transacting with.

          merchant_category_code: The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
              card is transacting with.

          merchant_country: The country the merchant resides in.

          merchant_name: The name of the merchant

          purchase_amount: The purchase amount in cents.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_authentications",
            body=maybe_transform(
                {
                    "card_id": card_id,
                    "category": category,
                    "device_channel": device_channel,
                    "merchant_acceptor_id": merchant_acceptor_id,
                    "merchant_category_code": merchant_category_code,
                    "merchant_country": merchant_country,
                    "merchant_name": merchant_name,
                    "purchase_amount": purchase_amount,
                },
                card_authentication_create_params.CardAuthenticationCreateParams,
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

    def challenge_attempts(
        self,
        card_payment_id: str,
        *,
        one_time_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates an attempt at a Card Authentication Challenge.

        This updates the
        `card_authentications` object under the [Card Payment](#card_payments). You can
        also attempt the challenge by navigating to
        https://dashboard.increase.com/card_authentication_simulation/:card_payment_id.

        Args:
          card_payment_id: The identifier of the Card Payment to be challenged.

          one_time_code: The one-time code to be validated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_payment_id:
            raise ValueError(f"Expected a non-empty value for `card_payment_id` but received {card_payment_id!r}")
        return self._post(
            f"/simulations/card_authentications/{card_payment_id}/challenge_attempts",
            body=maybe_transform(
                {"one_time_code": one_time_code},
                card_authentication_challenge_attempts_params.CardAuthenticationChallengeAttemptsParams,
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

    def challenges(
        self,
        card_payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """
        Simulates starting a Card Authentication Challenge for an existing Card
        Authentication. This updates the `card_authentications` object under the
        [Card Payment](#card_payments). To attempt the challenge, use the
        `/simulations/card_authentications/:card_payment_id/challenge_attempts` endpoint
        or navigate to
        https://dashboard.increase.com/card_authentication_simulation/:card_payment_id.

        Args:
          card_payment_id: The identifier of the Card Payment to be challenged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_payment_id:
            raise ValueError(f"Expected a non-empty value for `card_payment_id` but received {card_payment_id!r}")
        return self._post(
            f"/simulations/card_authentications/{card_payment_id}/challenges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )


class AsyncCardAuthenticationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardAuthenticationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardAuthenticationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardAuthenticationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardAuthenticationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        card_id: str,
        category: Literal["payment_authentication", "non_payment_authentication"] | Omit = omit,
        device_channel: Literal["app", "browser", "three_ds_requestor_initiated"] | Omit = omit,
        merchant_acceptor_id: str | Omit = omit,
        merchant_category_code: str | Omit = omit,
        merchant_country: str | Omit = omit,
        merchant_name: str | Omit = omit,
        purchase_amount: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates a Card Authentication attempt on a [Card](#cards).

        The attempt always
        results in a [Card Payment](#card_payments) being created, either with a status
        that allows further action or a terminal failed status.

        Args:
          card_id: The identifier of the Card to be authorized.

          category: The category of the card authentication attempt.

              - `payment_authentication` - The authentication attempt is for a payment.
              - `non_payment_authentication` - The authentication attempt is not for a
                payment.

          device_channel: The device channel of the card authentication attempt.

              - `app` - The authentication attempt was made from an app.
              - `browser` - The authentication attempt was made from a browser.
              - `three_ds_requestor_initiated` - The authentication attempt was initiated by
                the 3DS Requestor.

          merchant_acceptor_id: The merchant identifier (commonly abbreviated as MID) of the merchant the card
              is transacting with.

          merchant_category_code: The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
              card is transacting with.

          merchant_country: The country the merchant resides in.

          merchant_name: The name of the merchant

          purchase_amount: The purchase amount in cents.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_authentications",
            body=await async_maybe_transform(
                {
                    "card_id": card_id,
                    "category": category,
                    "device_channel": device_channel,
                    "merchant_acceptor_id": merchant_acceptor_id,
                    "merchant_category_code": merchant_category_code,
                    "merchant_country": merchant_country,
                    "merchant_name": merchant_name,
                    "purchase_amount": purchase_amount,
                },
                card_authentication_create_params.CardAuthenticationCreateParams,
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

    async def challenge_attempts(
        self,
        card_payment_id: str,
        *,
        one_time_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates an attempt at a Card Authentication Challenge.

        This updates the
        `card_authentications` object under the [Card Payment](#card_payments). You can
        also attempt the challenge by navigating to
        https://dashboard.increase.com/card_authentication_simulation/:card_payment_id.

        Args:
          card_payment_id: The identifier of the Card Payment to be challenged.

          one_time_code: The one-time code to be validated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_payment_id:
            raise ValueError(f"Expected a non-empty value for `card_payment_id` but received {card_payment_id!r}")
        return await self._post(
            f"/simulations/card_authentications/{card_payment_id}/challenge_attempts",
            body=await async_maybe_transform(
                {"one_time_code": one_time_code},
                card_authentication_challenge_attempts_params.CardAuthenticationChallengeAttemptsParams,
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

    async def challenges(
        self,
        card_payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """
        Simulates starting a Card Authentication Challenge for an existing Card
        Authentication. This updates the `card_authentications` object under the
        [Card Payment](#card_payments). To attempt the challenge, use the
        `/simulations/card_authentications/:card_payment_id/challenge_attempts` endpoint
        or navigate to
        https://dashboard.increase.com/card_authentication_simulation/:card_payment_id.

        Args:
          card_payment_id: The identifier of the Card Payment to be challenged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_payment_id:
            raise ValueError(f"Expected a non-empty value for `card_payment_id` but received {card_payment_id!r}")
        return await self._post(
            f"/simulations/card_authentications/{card_payment_id}/challenges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )


class CardAuthenticationsResourceWithRawResponse:
    def __init__(self, card_authentications: CardAuthenticationsResource) -> None:
        self._card_authentications = card_authentications

        self.create = to_raw_response_wrapper(
            card_authentications.create,
        )
        self.challenge_attempts = to_raw_response_wrapper(
            card_authentications.challenge_attempts,
        )
        self.challenges = to_raw_response_wrapper(
            card_authentications.challenges,
        )


class AsyncCardAuthenticationsResourceWithRawResponse:
    def __init__(self, card_authentications: AsyncCardAuthenticationsResource) -> None:
        self._card_authentications = card_authentications

        self.create = async_to_raw_response_wrapper(
            card_authentications.create,
        )
        self.challenge_attempts = async_to_raw_response_wrapper(
            card_authentications.challenge_attempts,
        )
        self.challenges = async_to_raw_response_wrapper(
            card_authentications.challenges,
        )


class CardAuthenticationsResourceWithStreamingResponse:
    def __init__(self, card_authentications: CardAuthenticationsResource) -> None:
        self._card_authentications = card_authentications

        self.create = to_streamed_response_wrapper(
            card_authentications.create,
        )
        self.challenge_attempts = to_streamed_response_wrapper(
            card_authentications.challenge_attempts,
        )
        self.challenges = to_streamed_response_wrapper(
            card_authentications.challenges,
        )


class AsyncCardAuthenticationsResourceWithStreamingResponse:
    def __init__(self, card_authentications: AsyncCardAuthenticationsResource) -> None:
        self._card_authentications = card_authentications

        self.create = async_to_streamed_response_wrapper(
            card_authentications.create,
        )
        self.challenge_attempts = async_to_streamed_response_wrapper(
            card_authentications.challenge_attempts,
        )
        self.challenges = async_to_streamed_response_wrapper(
            card_authentications.challenges,
        )
