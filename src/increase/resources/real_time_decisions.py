# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import real_time_decision_action_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options
from ..types.real_time_decision import RealTimeDecision

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
    ) -> RealTimeDecision:
        return self._get(
            f"/real_time_decisions/{real_time_decision_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=RealTimeDecision,
        )

    def action(
        self,
        real_time_decision_id: str,
        *,
        card_authorization: real_time_decision_action_params.CardAuthorization | NotGiven = NOT_GIVEN,
        digital_wallet_token: real_time_decision_action_params.DigitalWalletToken | NotGiven = NOT_GIVEN,
        digital_wallet_authentication: real_time_decision_action_params.DigitalWalletAuthentication
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> RealTimeDecision:
        """
        Args:
          card_authorization: If the Real-Time Decision relates to a card authorization attempt, this object
              contains your response to the authorization.

          digital_wallet_token: If the Real-Time Decision relates to a digital wallet token provisioning
              attempt, this object contains your response to the attempt.

          digital_wallet_authentication: If the Real-Time Decision relates to a digital wallet authentication attempt,
              this object contains your response to the authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            f"/real_time_decisions/{real_time_decision_id}/action",
            body={
                "card_authorization": card_authorization,
                "digital_wallet_token": digital_wallet_token,
                "digital_wallet_authentication": digital_wallet_authentication,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> RealTimeDecision:
        return await self._get(
            f"/real_time_decisions/{real_time_decision_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=RealTimeDecision,
        )

    async def action(
        self,
        real_time_decision_id: str,
        *,
        card_authorization: real_time_decision_action_params.CardAuthorization | NotGiven = NOT_GIVEN,
        digital_wallet_token: real_time_decision_action_params.DigitalWalletToken | NotGiven = NOT_GIVEN,
        digital_wallet_authentication: real_time_decision_action_params.DigitalWalletAuthentication
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> RealTimeDecision:
        """
        Args:
          card_authorization: If the Real-Time Decision relates to a card authorization attempt, this object
              contains your response to the authorization.

          digital_wallet_token: If the Real-Time Decision relates to a digital wallet token provisioning
              attempt, this object contains your response to the attempt.

          digital_wallet_authentication: If the Real-Time Decision relates to a digital wallet authentication attempt,
              this object contains your response to the authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            f"/real_time_decisions/{real_time_decision_id}/action",
            body={
                "card_authorization": card_authorization,
                "digital_wallet_token": digital_wallet_token,
                "digital_wallet_authentication": digital_wallet_authentication,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=RealTimeDecision,
        )
