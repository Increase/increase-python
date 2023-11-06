# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING
from typing_extensions import Literal

import httpx

from ..types import (
    Card,
    CardDetails,
    card_list_params,
    card_create_params,
    card_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import Increase, AsyncIncrease

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    with_raw_response: CardsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = CardsWithRawResponse(self)

    def create(
        self,
        *,
        account_id: str,
        billing_address: card_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        digital_wallet: card_create_params.DigitalWallet | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Card:
        """
        Create a Card

        Args:
          account_id: The Account the card should belong to.

          billing_address: The card's billing address.

          description: The description you choose to give the card.

          digital_wallet: The contact information used in the two-factor steps for digital wallet card
              creation. To add the card to a digital wallet, you may supply an email or phone
              number with this request. Otherwise, subscribe and then action a Real Time
              Decision with the category `digital_wallet_token_requested` or
              `digital_wallet_authentication_requested`.

          entity_id: The Entity the card belongs to. You only need to supply this in rare situations
              when the card is not for the Account holder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/cards",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "billing_address": billing_address,
                    "description": description,
                    "digital_wallet": digital_wallet,
                    "entity_id": entity_id,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )

    def retrieve(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Retrieve a Card

        Args:
          card_id: The identifier of the Card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cards/{card_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def update(
        self,
        card_id: str,
        *,
        billing_address: card_update_params.BillingAddress | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        digital_wallet: card_update_params.DigitalWallet | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Card:
        """
        Update a Card

        Args:
          card_id: The card identifier.

          billing_address: The card's updated billing address.

          description: The description you choose to give the card.

          digital_wallet: The contact information used in the two-factor steps for digital wallet card
              creation. At least one field must be present to complete the digital wallet
              steps.

          entity_id: The Entity the card belongs to. You only need to supply this in rare situations
              when the card is not for the Account holder.

          status: The status to update the Card with.

              - `active` - The card is active.
              - `disabled` - The card is temporarily disabled.
              - `canceled` - The card is permanently canceled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/cards/{card_id}",
            body=maybe_transform(
                {
                    "billing_address": billing_address,
                    "description": description,
                    "digital_wallet": digital_wallet,
                    "entity_id": entity_id,
                    "status": status,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: card_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Card]:
        """
        List Cards

        Args:
          account_id: Filter Cards to ones belonging to the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cards",
            page=SyncPage[Card],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            model=Card,
        )

    def retrieve_sensitive_details(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardDetails:
        """
        Retrieve sensitive details for a Card

        Args:
          card_id: The identifier of the Card to retrieve details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cards/{card_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDetails,
        )


class AsyncCards(AsyncAPIResource):
    with_raw_response: AsyncCardsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCardsWithRawResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        billing_address: card_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        digital_wallet: card_create_params.DigitalWallet | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Card:
        """
        Create a Card

        Args:
          account_id: The Account the card should belong to.

          billing_address: The card's billing address.

          description: The description you choose to give the card.

          digital_wallet: The contact information used in the two-factor steps for digital wallet card
              creation. To add the card to a digital wallet, you may supply an email or phone
              number with this request. Otherwise, subscribe and then action a Real Time
              Decision with the category `digital_wallet_token_requested` or
              `digital_wallet_authentication_requested`.

          entity_id: The Entity the card belongs to. You only need to supply this in rare situations
              when the card is not for the Account holder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/cards",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "billing_address": billing_address,
                    "description": description,
                    "digital_wallet": digital_wallet,
                    "entity_id": entity_id,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )

    async def retrieve(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Retrieve a Card

        Args:
          card_id: The identifier of the Card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cards/{card_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def update(
        self,
        card_id: str,
        *,
        billing_address: card_update_params.BillingAddress | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        digital_wallet: card_update_params.DigitalWallet | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Card:
        """
        Update a Card

        Args:
          card_id: The card identifier.

          billing_address: The card's updated billing address.

          description: The description you choose to give the card.

          digital_wallet: The contact information used in the two-factor steps for digital wallet card
              creation. At least one field must be present to complete the digital wallet
              steps.

          entity_id: The Entity the card belongs to. You only need to supply this in rare situations
              when the card is not for the Account holder.

          status: The status to update the Card with.

              - `active` - The card is active.
              - `disabled` - The card is temporarily disabled.
              - `canceled` - The card is permanently canceled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/cards/{card_id}",
            body=maybe_transform(
                {
                    "billing_address": billing_address,
                    "description": description,
                    "digital_wallet": digital_wallet,
                    "entity_id": entity_id,
                    "status": status,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: card_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Card, AsyncPage[Card]]:
        """
        List Cards

        Args:
          account_id: Filter Cards to ones belonging to the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cards",
            page=AsyncPage[Card],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            model=Card,
        )

    async def retrieve_sensitive_details(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardDetails:
        """
        Retrieve sensitive details for a Card

        Args:
          card_id: The identifier of the Card to retrieve details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cards/{card_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDetails,
        )


class CardsWithRawResponse:
    def __init__(self, cards: Cards) -> None:
        self.create = to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = to_raw_response_wrapper(
            cards.update,
        )
        self.list = to_raw_response_wrapper(
            cards.list,
        )
        self.retrieve_sensitive_details = to_raw_response_wrapper(
            cards.retrieve_sensitive_details,
        )


class AsyncCardsWithRawResponse:
    def __init__(self, cards: AsyncCards) -> None:
        self.create = async_to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            cards.update,
        )
        self.list = async_to_raw_response_wrapper(
            cards.list,
        )
        self.retrieve_sensitive_details = async_to_raw_response_wrapper(
            cards.retrieve_sensitive_details,
        )
