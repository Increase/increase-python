# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import Transaction
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations import (
    CardAuthorizationSimulation,
    card_authorize_params,
    card_settlement_params,
)

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    def authorize(
        self,
        *,
        amount: int,
        card_id: str | NotGiven = NOT_GIVEN,
        digital_wallet_token_id: str | NotGiven = NOT_GIVEN,
        event_subscription_id: str | NotGiven = NOT_GIVEN,
        physical_card_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardAuthorizationSimulation:
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
                    "physical_card_id": physical_card_id,
                },
                card_authorize_params.CardAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """Simulates the settlement of an authorization by a card acquirer.

        After a card
        authorization is created, the merchant will eventually send a settlement. This
        simulates that event, which may occur many days after the purchase in
        production. The amount settled can be different from the amount originally
        authorized, for example, when adding a tip to a restaurant bill.

        Args:
          card_id: The identifier of the Card to create a settlement on.

          pending_transaction_id: The identifier of the Pending Transaction for the Card Authorization you wish to
              settle.

          amount: The amount to be settled. This defaults to the amount of the Pending Transaction
              being settled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_settlements",
            body=maybe_transform(
                {
                    "card_id": card_id,
                    "pending_transaction_id": pending_transaction_id,
                    "amount": amount,
                },
                card_settlement_params.CardSettlementParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Transaction,
        )


class AsyncCards(AsyncAPIResource):
    async def authorize(
        self,
        *,
        amount: int,
        card_id: str | NotGiven = NOT_GIVEN,
        digital_wallet_token_id: str | NotGiven = NOT_GIVEN,
        event_subscription_id: str | NotGiven = NOT_GIVEN,
        physical_card_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardAuthorizationSimulation:
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

          physical_card_id: The identifier of the Physical Card to be authorized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_authorizations",
            body=maybe_transform(
                {
                    "amount": amount,
                    "card_id": card_id,
                    "digital_wallet_token_id": digital_wallet_token_id,
                    "event_subscription_id": event_subscription_id,
                    "physical_card_id": physical_card_id,
                },
                card_authorize_params.CardAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """Simulates the settlement of an authorization by a card acquirer.

        After a card
        authorization is created, the merchant will eventually send a settlement. This
        simulates that event, which may occur many days after the purchase in
        production. The amount settled can be different from the amount originally
        authorized, for example, when adding a tip to a restaurant bill.

        Args:
          card_id: The identifier of the Card to create a settlement on.

          pending_transaction_id: The identifier of the Pending Transaction for the Card Authorization you wish to
              settle.

          amount: The amount to be settled. This defaults to the amount of the Pending Transaction
              being settled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_settlements",
            body=maybe_transform(
                {
                    "card_id": card_id,
                    "pending_transaction_id": pending_transaction_id,
                    "amount": amount,
                },
                card_settlement_params.CardSettlementParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Transaction,
        )
