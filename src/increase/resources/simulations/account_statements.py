# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import Body, Query, Headers
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.account_statement import AccountStatement

__all__ = ["AccountStatements", "AsyncAccountStatements"]


class AccountStatements(SyncAPIResource):
    def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountStatement:
        """
        Simulates an Account Statement being created for an account.

        Args:
          account_id: The identifier of the Account the statement is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/simulations/account_statements",
            body={"account_id": account_id},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountStatement,
        )


class AsyncAccountStatements(AsyncAPIResource):
    async def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountStatement:
        """
        Simulates an Account Statement being created for an account.

        Args:
          account_id: The identifier of the Account the statement is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/simulations/account_statements",
            body={"account_id": account_id},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountStatement,
        )
