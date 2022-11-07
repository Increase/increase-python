# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.external_account import ExternalAccount

__all__ = ["ExternalAccounts", "AsyncExternalAccounts"]


class ExternalAccounts(SyncAPIResource):
    def create(
        self,
        *,
        routing_number: str,
        account_number: str,
        funding: Literal["checking", "savings", "other"] | NotGiven = NOT_GIVEN,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExternalAccount:
        """
        Args:
          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          account_number: The account number for the destination account.

          funding: The type of the destination account. Defaults to `checking`.

          description: The name you choose for the Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/external_accounts",
            body={
                "routing_number": routing_number,
                "account_number": account_number,
                "funding": funding,
                "description": description,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExternalAccount,
        )

    def retrieve(
        self,
        external_account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExternalAccount:
        return self._get(
            f"/external_accounts/{external_account_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExternalAccount,
        )

    def update(
        self,
        external_account_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExternalAccount:
        """
        Args:
          description: The description you choose to give the external account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/external_accounts/{external_account_id}",
            body={"description": description},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExternalAccount,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[ExternalAccount]:
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
            "/external_accounts",
            page=SyncPage[ExternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                },
            ),
            model=ExternalAccount,
        )


class AsyncExternalAccounts(AsyncAPIResource):
    async def create(
        self,
        *,
        routing_number: str,
        account_number: str,
        funding: Literal["checking", "savings", "other"] | NotGiven = NOT_GIVEN,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExternalAccount:
        """
        Args:
          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          account_number: The account number for the destination account.

          funding: The type of the destination account. Defaults to `checking`.

          description: The name you choose for the Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/external_accounts",
            body={
                "routing_number": routing_number,
                "account_number": account_number,
                "funding": funding,
                "description": description,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExternalAccount,
        )

    async def retrieve(
        self,
        external_account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExternalAccount:
        return await self._get(
            f"/external_accounts/{external_account_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExternalAccount,
        )

    async def update(
        self,
        external_account_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExternalAccount:
        """
        Args:
          description: The description you choose to give the external account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/external_accounts/{external_account_id}",
            body={"description": description},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ExternalAccount,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[ExternalAccount, AsyncPage[ExternalAccount]]:
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
            "/external_accounts",
            page=AsyncPage[ExternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                },
            ),
            model=ExternalAccount,
        )
