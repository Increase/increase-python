# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import program_list_params
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
from ..types.program import Program

__all__ = ["ProgramsResource", "AsyncProgramsResource"]


class ProgramsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProgramsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return ProgramsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProgramsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return ProgramsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        program_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Program:
        """
        Retrieve a Program

        Args:
          program_id: The identifier of the Program to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not program_id:
            raise ValueError(f"Expected a non-empty value for `program_id` but received {program_id!r}")
        return self._get(
            f"/programs/{program_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Program,
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
    ) -> SyncPage[Program]:
        """
        List Programs

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
            "/programs",
            page=SyncPage[Program],
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
                    program_list_params.ProgramListParams,
                ),
            ),
            model=Program,
        )


class AsyncProgramsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProgramsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProgramsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProgramsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncProgramsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        program_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Program:
        """
        Retrieve a Program

        Args:
          program_id: The identifier of the Program to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not program_id:
            raise ValueError(f"Expected a non-empty value for `program_id` but received {program_id!r}")
        return await self._get(
            f"/programs/{program_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Program,
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
    ) -> AsyncPaginator[Program, AsyncPage[Program]]:
        """
        List Programs

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
            "/programs",
            page=AsyncPage[Program],
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
                    program_list_params.ProgramListParams,
                ),
            ),
            model=Program,
        )


class ProgramsResourceWithRawResponse:
    def __init__(self, programs: ProgramsResource) -> None:
        self._programs = programs

        self.retrieve = to_raw_response_wrapper(
            programs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            programs.list,
        )


class AsyncProgramsResourceWithRawResponse:
    def __init__(self, programs: AsyncProgramsResource) -> None:
        self._programs = programs

        self.retrieve = async_to_raw_response_wrapper(
            programs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            programs.list,
        )


class ProgramsResourceWithStreamingResponse:
    def __init__(self, programs: ProgramsResource) -> None:
        self._programs = programs

        self.retrieve = to_streamed_response_wrapper(
            programs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            programs.list,
        )


class AsyncProgramsResourceWithStreamingResponse:
    def __init__(self, programs: AsyncProgramsResource) -> None:
        self._programs = programs

        self.retrieve = async_to_streamed_response_wrapper(
            programs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            programs.list,
        )
