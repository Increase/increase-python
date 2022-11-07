# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import pending_transaction_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.pending_transaction import PendingTransaction

__all__ = ["PendingTransactions", "AsyncPendingTransactions"]


class PendingTransactions(SyncAPIResource):
    def retrieve(
        self,
        pending_transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> PendingTransaction:
        return self._get(
            f"/pending_transactions/{pending_transaction_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=PendingTransaction,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        route_id: str | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        status: pending_transaction_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[PendingTransaction]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter pending transactions to those belonging to the specified Account.

          route_id: Filter pending transactions to those belonging to the specified Route.

          source_id: Filter pending transactions to those caused by the specified source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/pending_transactions",
            page=SyncPage[PendingTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "route_id": route_id,
                    "source_id": source_id,
                    "status": status,
                },
            ),
            model=PendingTransaction,
        )


class AsyncPendingTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        pending_transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> PendingTransaction:
        return await self._get(
            f"/pending_transactions/{pending_transaction_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=PendingTransaction,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        route_id: str | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        status: pending_transaction_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[PendingTransaction, AsyncPage[PendingTransaction]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter pending transactions to those belonging to the specified Account.

          route_id: Filter pending transactions to those belonging to the specified Route.

          source_id: Filter pending transactions to those caused by the specified source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/pending_transactions",
            page=AsyncPage[PendingTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "route_id": route_id,
                    "source_id": source_id,
                    "status": status,
                },
            ),
            model=PendingTransaction,
        )
