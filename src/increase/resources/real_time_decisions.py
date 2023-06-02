# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import RealTimeDecision, real_time_decision_action_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["RealTimeDecisions", "AsyncRealTimeDecisions"]


class RealTimeDecisions(SyncAPIResource):
    def retrieve(
        self,
        real_time_decision_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    async def retrieve(
        self,
        real_time_decision_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
