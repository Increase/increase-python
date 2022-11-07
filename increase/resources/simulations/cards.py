# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload

from ..._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from ..._utils import required_args
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.transaction import Transaction
from ...types.simulations.card_authorize_params import CardAuthorizeParams
from ...types.simulations.card_settlement_params import CardSettlementParams
from ...types.simulations.card_authorization_simulation import (
    CardAuthorizationSimulation,
)

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    @overload
    def authorize(
        self,
        *,
        amount: int,
        card_id: str,
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
    ) -> CardAuthorizationSimulation:
        """
        Simulates activity on a Card.

        Args:
          amount: The authorization amount in cents.

          card_id: The identifier of the Card to be authorized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def authorize(
        self,
        body: CardAuthorizeParams,
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
    ) -> CardAuthorizationSimulation:
        """Simulates activity on a Card."""
        ...

    @required_args(["body"], ["amount", "card_id"])
    def authorize(
        self,
        body: CardAuthorizeParams | None = None,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        card_id: str | NotGiven = NOT_GIVEN,
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
    ) -> CardAuthorizationSimulation:
        """
        Simulates activity on a Card.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          amount: The authorization amount in cents.

          card_id: The identifier of the Card to be authorized.

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
            # with the standard CardAuthorizeParams type.
            body = cast(
                Any,
                {
                    "amount": amount,
                    "card_id": card_id,
                },
            )

        return self._post(
            "/simulations/card_authorizations",
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
            cast_to=CardAuthorizationSimulation,
        )

    @overload
    def settlement(
        self,
        *,
        card_id: str,
        pending_transaction_id: str,
        amount: int | NotGiven = NOT_GIVEN,
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
    ) -> Transaction:
        """
        Simulates the settlement of an authorization by a card acquirer.

        Args:
          card_id: The identifier of the Card to create a settlement on.

          pending_transaction_id: The identifier of the Pending Transaction for the Card Authorization you wish to
              settle.

          amount: The amount to be settled. This defaults to the amount of the Pending Transaction
              being settled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def settlement(
        self,
        body: CardSettlementParams,
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
    ) -> Transaction:
        """Simulates the settlement of an authorization by a card acquirer."""
        ...

    @required_args(["body"], ["card_id", "pending_transaction_id"])
    def settlement(
        self,
        body: CardSettlementParams | None = None,
        *,
        card_id: str | NotGiven = NOT_GIVEN,
        pending_transaction_id: str | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
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
    ) -> Transaction:
        """
        Simulates the settlement of an authorization by a card acquirer.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          card_id: The identifier of the Card to create a settlement on.

          pending_transaction_id: The identifier of the Pending Transaction for the Card Authorization you wish to
              settle.

          amount: The amount to be settled. This defaults to the amount of the Pending Transaction
              being settled.

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
            # with the standard CardSettlementParams type.
            body = cast(
                Any,
                {
                    "card_id": card_id,
                    "pending_transaction_id": pending_transaction_id,
                    "amount": amount,
                },
            )

        return self._post(
            "/simulations/card_settlements",
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
            cast_to=Transaction,
        )


class AsyncCards(AsyncAPIResource):
    @overload
    async def authorize(
        self,
        *,
        amount: int,
        card_id: str,
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
    ) -> CardAuthorizationSimulation:
        """
        Simulates activity on a Card.

        Args:
          amount: The authorization amount in cents.

          card_id: The identifier of the Card to be authorized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def authorize(
        self,
        body: CardAuthorizeParams,
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
    ) -> CardAuthorizationSimulation:
        """Simulates activity on a Card."""
        ...

    @required_args(["body"], ["amount", "card_id"])
    async def authorize(
        self,
        body: CardAuthorizeParams | None = None,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        card_id: str | NotGiven = NOT_GIVEN,
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
    ) -> CardAuthorizationSimulation:
        """
        Simulates activity on a Card.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          amount: The authorization amount in cents.

          card_id: The identifier of the Card to be authorized.

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
            # with the standard CardAuthorizeParams type.
            body = cast(
                Any,
                {
                    "amount": amount,
                    "card_id": card_id,
                },
            )

        return await self._post(
            "/simulations/card_authorizations",
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
            cast_to=CardAuthorizationSimulation,
        )

    @overload
    async def settlement(
        self,
        *,
        card_id: str,
        pending_transaction_id: str,
        amount: int | NotGiven = NOT_GIVEN,
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
    ) -> Transaction:
        """
        Simulates the settlement of an authorization by a card acquirer.

        Args:
          card_id: The identifier of the Card to create a settlement on.

          pending_transaction_id: The identifier of the Pending Transaction for the Card Authorization you wish to
              settle.

          amount: The amount to be settled. This defaults to the amount of the Pending Transaction
              being settled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def settlement(
        self,
        body: CardSettlementParams,
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
    ) -> Transaction:
        """Simulates the settlement of an authorization by a card acquirer."""
        ...

    @required_args(["body"], ["card_id", "pending_transaction_id"])
    async def settlement(
        self,
        body: CardSettlementParams | None = None,
        *,
        card_id: str | NotGiven = NOT_GIVEN,
        pending_transaction_id: str | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
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
    ) -> Transaction:
        """
        Simulates the settlement of an authorization by a card acquirer.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          card_id: The identifier of the Card to create a settlement on.

          pending_transaction_id: The identifier of the Pending Transaction for the Card Authorization you wish to
              settle.

          amount: The amount to be settled. This defaults to the amount of the Pending Transaction
              being settled.

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
            # with the standard CardSettlementParams type.
            body = cast(
                Any,
                {
                    "card_id": card_id,
                    "pending_transaction_id": pending_transaction_id,
                    "amount": amount,
                },
            )

        return await self._post(
            "/simulations/card_settlements",
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
            cast_to=Transaction,
        )
