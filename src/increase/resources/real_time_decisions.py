# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import real_time_decision_action_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.real_time_decision import RealTimeDecision

__all__ = ["RealTimeDecisionsResource", "AsyncRealTimeDecisionsResource"]


class RealTimeDecisionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealTimeDecisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return RealTimeDecisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealTimeDecisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return RealTimeDecisionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        real_time_decision_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealTimeDecision:
        """
        Retrieve a Real-Time Decision

        Args:
          real_time_decision_id: The identifier of the Real-Time Decision.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not real_time_decision_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_decision_id` but received {real_time_decision_id!r}"
            )
        return self._get(
            f"/real_time_decisions/{real_time_decision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealTimeDecision,
        )

    def action(
        self,
        real_time_decision_id: str,
        *,
        card_authentication: real_time_decision_action_params.CardAuthentication | NotGiven = NOT_GIVEN,
        card_authentication_challenge: real_time_decision_action_params.CardAuthenticationChallenge
        | NotGiven = NOT_GIVEN,
        card_authorization: real_time_decision_action_params.CardAuthorization | NotGiven = NOT_GIVEN,
        digital_wallet_authentication: real_time_decision_action_params.DigitalWalletAuthentication
        | NotGiven = NOT_GIVEN,
        digital_wallet_token: real_time_decision_action_params.DigitalWalletToken | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RealTimeDecision:
        """
        Action a Real-Time Decision

        Args:
          real_time_decision_id: The identifier of the Real-Time Decision.

          card_authentication: If the Real-Time Decision relates to a 3DS card authentication attempt, this
              object contains your response to the authentication.

          card_authentication_challenge: If the Real-Time Decision relates to 3DS card authentication challenge delivery,
              this object contains your response.

          card_authorization: If the Real-Time Decision relates to a card authorization attempt, this object
              contains your response to the authorization.

          digital_wallet_authentication: If the Real-Time Decision relates to a digital wallet authentication attempt,
              this object contains your response to the authentication.

          digital_wallet_token: If the Real-Time Decision relates to a digital wallet token provisioning
              attempt, this object contains your response to the attempt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not real_time_decision_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_decision_id` but received {real_time_decision_id!r}"
            )
        return self._post(
            f"/real_time_decisions/{real_time_decision_id}/action",
            body=maybe_transform(
                {
                    "card_authentication": card_authentication,
                    "card_authentication_challenge": card_authentication_challenge,
                    "card_authorization": card_authorization,
                    "digital_wallet_authentication": digital_wallet_authentication,
                    "digital_wallet_token": digital_wallet_token,
                },
                real_time_decision_action_params.RealTimeDecisionActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimeDecision,
        )


class AsyncRealTimeDecisionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealTimeDecisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRealTimeDecisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealTimeDecisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncRealTimeDecisionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        real_time_decision_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealTimeDecision:
        """
        Retrieve a Real-Time Decision

        Args:
          real_time_decision_id: The identifier of the Real-Time Decision.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not real_time_decision_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_decision_id` but received {real_time_decision_id!r}"
            )
        return await self._get(
            f"/real_time_decisions/{real_time_decision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealTimeDecision,
        )

    async def action(
        self,
        real_time_decision_id: str,
        *,
        card_authentication: real_time_decision_action_params.CardAuthentication | NotGiven = NOT_GIVEN,
        card_authentication_challenge: real_time_decision_action_params.CardAuthenticationChallenge
        | NotGiven = NOT_GIVEN,
        card_authorization: real_time_decision_action_params.CardAuthorization | NotGiven = NOT_GIVEN,
        digital_wallet_authentication: real_time_decision_action_params.DigitalWalletAuthentication
        | NotGiven = NOT_GIVEN,
        digital_wallet_token: real_time_decision_action_params.DigitalWalletToken | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RealTimeDecision:
        """
        Action a Real-Time Decision

        Args:
          real_time_decision_id: The identifier of the Real-Time Decision.

          card_authentication: If the Real-Time Decision relates to a 3DS card authentication attempt, this
              object contains your response to the authentication.

          card_authentication_challenge: If the Real-Time Decision relates to 3DS card authentication challenge delivery,
              this object contains your response.

          card_authorization: If the Real-Time Decision relates to a card authorization attempt, this object
              contains your response to the authorization.

          digital_wallet_authentication: If the Real-Time Decision relates to a digital wallet authentication attempt,
              this object contains your response to the authentication.

          digital_wallet_token: If the Real-Time Decision relates to a digital wallet token provisioning
              attempt, this object contains your response to the attempt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not real_time_decision_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_decision_id` but received {real_time_decision_id!r}"
            )
        return await self._post(
            f"/real_time_decisions/{real_time_decision_id}/action",
            body=await async_maybe_transform(
                {
                    "card_authentication": card_authentication,
                    "card_authentication_challenge": card_authentication_challenge,
                    "card_authorization": card_authorization,
                    "digital_wallet_authentication": digital_wallet_authentication,
                    "digital_wallet_token": digital_wallet_token,
                },
                real_time_decision_action_params.RealTimeDecisionActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimeDecision,
        )


class RealTimeDecisionsResourceWithRawResponse:
    def __init__(self, real_time_decisions: RealTimeDecisionsResource) -> None:
        self._real_time_decisions = real_time_decisions

        self.retrieve = to_raw_response_wrapper(
            real_time_decisions.retrieve,
        )
        self.action = to_raw_response_wrapper(
            real_time_decisions.action,
        )


class AsyncRealTimeDecisionsResourceWithRawResponse:
    def __init__(self, real_time_decisions: AsyncRealTimeDecisionsResource) -> None:
        self._real_time_decisions = real_time_decisions

        self.retrieve = async_to_raw_response_wrapper(
            real_time_decisions.retrieve,
        )
        self.action = async_to_raw_response_wrapper(
            real_time_decisions.action,
        )


class RealTimeDecisionsResourceWithStreamingResponse:
    def __init__(self, real_time_decisions: RealTimeDecisionsResource) -> None:
        self._real_time_decisions = real_time_decisions

        self.retrieve = to_streamed_response_wrapper(
            real_time_decisions.retrieve,
        )
        self.action = to_streamed_response_wrapper(
            real_time_decisions.action,
        )


class AsyncRealTimeDecisionsResourceWithStreamingResponse:
    def __init__(self, real_time_decisions: AsyncRealTimeDecisionsResource) -> None:
        self._real_time_decisions = real_time_decisions

        self.retrieve = async_to_streamed_response_wrapper(
            real_time_decisions.retrieve,
        )
        self.action = async_to_streamed_response_wrapper(
            real_time_decisions.action,
        )
