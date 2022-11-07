# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..types import card_list_params, card_create_params, card_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.card import Card
from .._base_client import AsyncPaginator, make_request_options
from ..types.card_details import CardDetails

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    def create(
        self,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        billing_address: card_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Card:
        """
        Args:
          account_id: The Account the card should belong to.

          description: The description you choose to give the card.

          billing_address: The card's billing address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/cards",
            body={
                "account_id": account_id,
                "description": description,
                "billing_address": billing_address,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> Card:
        return self._get(
            f"/cards/{card_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Card,
        )

    def update(
        self,
        card_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        billing_address: card_update_params.BillingAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Card:
        """
        Args:
          description: The description you choose to give the card.

          status: The status to update the Card with.

          billing_address: The card's updated billing address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/cards/{card_id}",
            body={
                "description": description,
                "status": status,
                "billing_address": billing_address,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Card,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: card_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[Card]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Cards to ones belonging to the specified Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/cards",
            page=SyncPage[Card],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "created_at": created_at,
                },
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
    ) -> CardDetails:
        return self._get(
            f"/cards/{card_id}/details",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CardDetails,
        )


class AsyncCards(AsyncAPIResource):
    async def create(
        self,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        billing_address: card_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Card:
        """
        Args:
          account_id: The Account the card should belong to.

          description: The description you choose to give the card.

          billing_address: The card's billing address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/cards",
            body={
                "account_id": account_id,
                "description": description,
                "billing_address": billing_address,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> Card:
        return await self._get(
            f"/cards/{card_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Card,
        )

    async def update(
        self,
        card_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        billing_address: card_update_params.BillingAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Card:
        """
        Args:
          description: The description you choose to give the card.

          status: The status to update the Card with.

          billing_address: The card's updated billing address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/cards/{card_id}",
            body={
                "description": description,
                "status": status,
                "billing_address": billing_address,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Card,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: card_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[Card, AsyncPage[Card]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Cards to ones belonging to the specified Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/cards",
            page=AsyncPage[Card],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "created_at": created_at,
                },
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
    ) -> CardDetails:
        return await self._get(
            f"/cards/{card_id}/details",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CardDetails,
        )
