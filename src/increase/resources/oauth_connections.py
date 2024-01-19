# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import OAuthConnection, oauth_connection_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["OAuthConnections", "AsyncOAuthConnections"]


class OAuthConnections(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthConnectionsWithRawResponse:
        return OAuthConnectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthConnectionsWithStreamingResponse:
        return OAuthConnectionsWithStreamingResponse(self)

    def retrieve(
        self,
        oauth_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OAuthConnection:
        """
        Retrieve an OAuth Connection

        Args:
          oauth_connection_id: The identifier of the OAuth Connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not oauth_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `oauth_connection_id` but received {oauth_connection_id!r}"
            )
        return self._get(
            f"/oauth_connections/{oauth_connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthConnection,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[OAuthConnection]:
        """
        List OAuth Connections

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/oauth_connections",
            page=SyncPage[OAuthConnection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    oauth_connection_list_params.OAuthConnectionListParams,
                ),
            ),
            model=OAuthConnection,
        )


class AsyncOAuthConnections(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthConnectionsWithRawResponse:
        return AsyncOAuthConnectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthConnectionsWithStreamingResponse:
        return AsyncOAuthConnectionsWithStreamingResponse(self)

    async def retrieve(
        self,
        oauth_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OAuthConnection:
        """
        Retrieve an OAuth Connection

        Args:
          oauth_connection_id: The identifier of the OAuth Connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not oauth_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `oauth_connection_id` but received {oauth_connection_id!r}"
            )
        return await self._get(
            f"/oauth_connections/{oauth_connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthConnection,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OAuthConnection, AsyncPage[OAuthConnection]]:
        """
        List OAuth Connections

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/oauth_connections",
            page=AsyncPage[OAuthConnection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    oauth_connection_list_params.OAuthConnectionListParams,
                ),
            ),
            model=OAuthConnection,
        )


class OAuthConnectionsWithRawResponse:
    def __init__(self, oauth_connections: OAuthConnections) -> None:
        self._oauth_connections = oauth_connections

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            oauth_connections.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            oauth_connections.list,
        )


class AsyncOAuthConnectionsWithRawResponse:
    def __init__(self, oauth_connections: AsyncOAuthConnections) -> None:
        self._oauth_connections = oauth_connections

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            oauth_connections.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            oauth_connections.list,
        )


class OAuthConnectionsWithStreamingResponse:
    def __init__(self, oauth_connections: OAuthConnections) -> None:
        self._oauth_connections = oauth_connections

        self.retrieve = to_streamed_response_wrapper(
            oauth_connections.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            oauth_connections.list,
        )


class AsyncOAuthConnectionsWithStreamingResponse:
    def __init__(self, oauth_connections: AsyncOAuthConnections) -> None:
        self._oauth_connections = oauth_connections

        self.retrieve = async_to_streamed_response_wrapper(
            oauth_connections.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            oauth_connections.list,
        )
