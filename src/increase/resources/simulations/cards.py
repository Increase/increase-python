# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.transaction import Transaction
from ...types.simulations.card_authorization_simulation import (
    CardAuthorizationSimulation,
)

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
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
        return self._post(
            "/simulations/card_authorizations",
            body={
                "amount": amount,
                "card_id": card_id,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CardAuthorizationSimulation,
        )

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
        return self._post(
            "/simulations/card_settlements",
            body={
                "card_id": card_id,
                "pending_transaction_id": pending_transaction_id,
                "amount": amount,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Transaction,
        )


class AsyncCards(AsyncAPIResource):
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
        return await self._post(
            "/simulations/card_authorizations",
            body={
                "amount": amount,
                "card_id": card_id,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CardAuthorizationSimulation,
        )

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
        return await self._post(
            "/simulations/card_settlements",
            body={
                "card_id": card_id,
                "pending_transaction_id": pending_transaction_id,
                "amount": amount,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Transaction,
        )
