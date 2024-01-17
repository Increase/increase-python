# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import RealTimeDecision, real_time_decision_action_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["RealTimeDecisions", "AsyncRealTimeDecisions"]


class RealTimeDecisions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealTimeDecisionsWithRawResponse:
        return RealTimeDecisionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealTimeDecisionsWithStreamingResponse:
        return RealTimeDecisionsWithStreamingResponse(self)

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


class AsyncRealTimeDecisions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealTimeDecisionsWithRawResponse:
        return AsyncRealTimeDecisionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealTimeDecisionsWithStreamingResponse:
        return AsyncRealTimeDecisionsWithStreamingResponse(self)

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
            body=maybe_transform(
                {
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


class RealTimeDecisionsWithRawResponse:
    def __init__(self, real_time_decisions: RealTimeDecisions) -> None:
        self._real_time_decisions = real_time_decisions

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            real_time_decisions.retrieve,
        )
        self.action = _legacy_response.to_raw_response_wrapper(
            real_time_decisions.action,
        )


class AsyncRealTimeDecisionsWithRawResponse:
    def __init__(self, real_time_decisions: AsyncRealTimeDecisions) -> None:
        self._real_time_decisions = real_time_decisions

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            real_time_decisions.retrieve,
        )
        self.action = _legacy_response.async_to_raw_response_wrapper(
            real_time_decisions.action,
        )


class RealTimeDecisionsWithStreamingResponse:
    def __init__(self, real_time_decisions: RealTimeDecisions) -> None:
        self._real_time_decisions = real_time_decisions

        self.retrieve = to_streamed_response_wrapper(
            real_time_decisions.retrieve,
        )
        self.action = to_streamed_response_wrapper(
            real_time_decisions.action,
        )


class AsyncRealTimeDecisionsWithStreamingResponse:
    def __init__(self, real_time_decisions: AsyncRealTimeDecisions) -> None:
        self._real_time_decisions = real_time_decisions

        self.retrieve = async_to_streamed_response_wrapper(
            real_time_decisions.retrieve,
        )
        self.action = async_to_streamed_response_wrapper(
            real_time_decisions.action,
        )
