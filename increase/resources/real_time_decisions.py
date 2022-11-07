# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload

from ..types import real_time_decision_action_params
from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options
from ..types.real_time_decision import RealTimeDecision
from ..types.real_time_decision_action_params import RealTimeDecisionActionParams

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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> RealTimeDecision:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/real_time_decisions/{real_time_decision_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=RealTimeDecision,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    def action(
        self,
        real_time_decision_id: str,
        body: RealTimeDecisionActionParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> RealTimeDecision:
        ...

    def action(
        self,
        real_time_decision_id: str,
        body: RealTimeDecisionActionParams | None = None,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> RealTimeDecision:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard RealTimeDecisionActionParams type.
            body = cast(
                Any,
                {
                    "card_authorization": card_authorization,
                    "digital_wallet_token": digital_wallet_token,
                    "digital_wallet_authentication": digital_wallet_authentication,
                },
            )

        return self._post(
            f"/real_time_decisions/{real_time_decision_id}/action",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> RealTimeDecision:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/real_time_decisions/{real_time_decision_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=RealTimeDecision,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    async def action(
        self,
        real_time_decision_id: str,
        body: RealTimeDecisionActionParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> RealTimeDecision:
        ...

    async def action(
        self,
        real_time_decision_id: str,
        body: RealTimeDecisionActionParams | None = None,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> RealTimeDecision:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard RealTimeDecisionActionParams type.
            body = cast(
                Any,
                {
                    "card_authorization": card_authorization,
                    "digital_wallet_token": digital_wallet_token,
                    "digital_wallet_authentication": digital_wallet_authentication,
                },
            )

        return await self._post(
            f"/real_time_decisions/{real_time_decision_id}/action",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=RealTimeDecision,
        )
