# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import oauth_connection_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.oauth_connection import OAuthConnection

__all__ = ["OAuthConnectionsResource", "AsyncOAuthConnectionsResource"]


class OAuthConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return OAuthConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return OAuthConnectionsResourceWithStreamingResponse(self)

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
        oauth_application_id: str | NotGiven = NOT_GIVEN,
        status: oauth_connection_list_params.Status | NotGiven = NOT_GIVEN,
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

          oauth_application_id: Filter results to only include OAuth Connections for a specific OAuth
              Application.

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
                        "oauth_application_id": oauth_application_id,
                        "status": status,
                    },
                    oauth_connection_list_params.OAuthConnectionListParams,
                ),
            ),
            model=OAuthConnection,
        )


class AsyncOAuthConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncOAuthConnectionsResourceWithStreamingResponse(self)

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
        oauth_application_id: str | NotGiven = NOT_GIVEN,
        status: oauth_connection_list_params.Status | NotGiven = NOT_GIVEN,
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

          oauth_application_id: Filter results to only include OAuth Connections for a specific OAuth
              Application.

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
                        "oauth_application_id": oauth_application_id,
                        "status": status,
                    },
                    oauth_connection_list_params.OAuthConnectionListParams,
                ),
            ),
            model=OAuthConnection,
        )


class OAuthConnectionsResourceWithRawResponse:
    def __init__(self, oauth_connections: OAuthConnectionsResource) -> None:
        self._oauth_connections = oauth_connections

        self.retrieve = to_raw_response_wrapper(
            oauth_connections.retrieve,
        )
        self.list = to_raw_response_wrapper(
            oauth_connections.list,
        )


class AsyncOAuthConnectionsResourceWithRawResponse:
    def __init__(self, oauth_connections: AsyncOAuthConnectionsResource) -> None:
        self._oauth_connections = oauth_connections

        self.retrieve = async_to_raw_response_wrapper(
            oauth_connections.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            oauth_connections.list,
        )


class OAuthConnectionsResourceWithStreamingResponse:
    def __init__(self, oauth_connections: OAuthConnectionsResource) -> None:
        self._oauth_connections = oauth_connections

        self.retrieve = to_streamed_response_wrapper(
            oauth_connections.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            oauth_connections.list,
        )


class AsyncOAuthConnectionsResourceWithStreamingResponse:
    def __init__(self, oauth_connections: AsyncOAuthConnectionsResource) -> None:
        self._oauth_connections = oauth_connections

        self.retrieve = async_to_streamed_response_wrapper(
            oauth_connections.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            oauth_connections.list,
        )
