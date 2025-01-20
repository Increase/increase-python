# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import oauth_application_list_params
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
from ..types.oauth_application import OAuthApplication

__all__ = ["OAuthApplicationsResource", "AsyncOAuthApplicationsResource"]


class OAuthApplicationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return OAuthApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return OAuthApplicationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        oauth_application_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OAuthApplication:
        """
        Retrieve an OAuth Application

        Args:
          oauth_application_id: The identifier of the OAuth Application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not oauth_application_id:
            raise ValueError(
                f"Expected a non-empty value for `oauth_application_id` but received {oauth_application_id!r}"
            )
        return self._get(
            f"/oauth_applications/{oauth_application_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthApplication,
        )

    def list(
        self,
        *,
        created_at: oauth_application_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: oauth_application_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[OAuthApplication]:
        """
        List OAuth Applications

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
            "/oauth_applications",
            page=SyncPage[OAuthApplication],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    oauth_application_list_params.OAuthApplicationListParams,
                ),
            ),
            model=OAuthApplication,
        )


class AsyncOAuthApplicationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncOAuthApplicationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        oauth_application_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OAuthApplication:
        """
        Retrieve an OAuth Application

        Args:
          oauth_application_id: The identifier of the OAuth Application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not oauth_application_id:
            raise ValueError(
                f"Expected a non-empty value for `oauth_application_id` but received {oauth_application_id!r}"
            )
        return await self._get(
            f"/oauth_applications/{oauth_application_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthApplication,
        )

    def list(
        self,
        *,
        created_at: oauth_application_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: oauth_application_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OAuthApplication, AsyncPage[OAuthApplication]]:
        """
        List OAuth Applications

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
            "/oauth_applications",
            page=AsyncPage[OAuthApplication],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    oauth_application_list_params.OAuthApplicationListParams,
                ),
            ),
            model=OAuthApplication,
        )


class OAuthApplicationsResourceWithRawResponse:
    def __init__(self, oauth_applications: OAuthApplicationsResource) -> None:
        self._oauth_applications = oauth_applications

        self.retrieve = to_raw_response_wrapper(
            oauth_applications.retrieve,
        )
        self.list = to_raw_response_wrapper(
            oauth_applications.list,
        )


class AsyncOAuthApplicationsResourceWithRawResponse:
    def __init__(self, oauth_applications: AsyncOAuthApplicationsResource) -> None:
        self._oauth_applications = oauth_applications

        self.retrieve = async_to_raw_response_wrapper(
            oauth_applications.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            oauth_applications.list,
        )


class OAuthApplicationsResourceWithStreamingResponse:
    def __init__(self, oauth_applications: OAuthApplicationsResource) -> None:
        self._oauth_applications = oauth_applications

        self.retrieve = to_streamed_response_wrapper(
            oauth_applications.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            oauth_applications.list,
        )


class AsyncOAuthApplicationsResourceWithStreamingResponse:
    def __init__(self, oauth_applications: AsyncOAuthApplicationsResource) -> None:
        self._oauth_applications = oauth_applications

        self.retrieve = async_to_streamed_response_wrapper(
            oauth_applications.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            oauth_applications.list,
        )
