# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import card_dispute_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.card_dispute import CardDispute

__all__ = ["CardDisputes", "AsyncCardDisputes"]


class CardDisputes(SyncAPIResource):
    def create(
        self,
        *,
        disputed_transaction_id: str,
        explanation: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CardDispute:
        """Args:
          disputed_transaction_id: The Transaction you wish to dispute.

        This Transaction must have a `source_type`
              of `card_settlement`.

          explanation: Why you are disputing this Transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/card_disputes",
            body={
                "disputed_transaction_id": disputed_transaction_id,
                "explanation": explanation,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CardDispute,
        )

    def retrieve(
        self,
        card_dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CardDispute:
        return self._get(
            f"/card_disputes/{card_dispute_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CardDispute,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        created_at: card_dispute_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        status: card_dispute_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[CardDispute]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/card_disputes",
            page=SyncPage[CardDispute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "created_at": created_at,
                    "status": status,
                },
            ),
            model=CardDispute,
        )


class AsyncCardDisputes(AsyncAPIResource):
    async def create(
        self,
        *,
        disputed_transaction_id: str,
        explanation: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CardDispute:
        """Args:
          disputed_transaction_id: The Transaction you wish to dispute.

        This Transaction must have a `source_type`
              of `card_settlement`.

          explanation: Why you are disputing this Transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/card_disputes",
            body={
                "disputed_transaction_id": disputed_transaction_id,
                "explanation": explanation,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CardDispute,
        )

    async def retrieve(
        self,
        card_dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CardDispute:
        return await self._get(
            f"/card_disputes/{card_dispute_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CardDispute,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        created_at: card_dispute_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        status: card_dispute_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[CardDispute, AsyncPage[CardDispute]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/card_disputes",
            page=AsyncPage[CardDispute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "created_at": created_at,
                    "status": status,
                },
            ),
            model=CardDispute,
        )
