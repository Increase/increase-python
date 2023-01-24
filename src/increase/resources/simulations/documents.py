# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import Document
from ..._types import Body, Query, Headers
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

__all__ = ["Documents", "AsyncDocuments"]


class Documents(SyncAPIResource):
    def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Document:
        """
        Simulates an tax document being created for an account.

        Args:
          account_id: The identifier of the Account the tax document is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/simulations/documents",
            body={"account_id": account_id},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Document,
        )


class AsyncDocuments(AsyncAPIResource):
    async def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Document:
        """
        Simulates an tax document being created for an account.

        Args:
          account_id: The identifier of the Account the tax document is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/simulations/documents",
            body={"account_id": account_id},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Document,
        )
