# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import Program, program_list_params
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

__all__ = ["Programs", "AsyncPrograms"]


class Programs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProgramsWithRawResponse:
        return ProgramsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProgramsWithStreamingResponse:
        return ProgramsWithStreamingResponse(self)

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


class AsyncPrograms(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProgramsWithRawResponse:
        return AsyncProgramsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProgramsWithStreamingResponse:
        return AsyncProgramsWithStreamingResponse(self)

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


class ProgramsWithRawResponse:
    def __init__(self, programs: Programs) -> None:
        self._programs = programs

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            programs.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            programs.list,
        )


class AsyncProgramsWithRawResponse:
    def __init__(self, programs: AsyncPrograms) -> None:
        self._programs = programs

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            programs.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            programs.list,
        )


class ProgramsWithStreamingResponse:
    def __init__(self, programs: Programs) -> None:
        self._programs = programs

        self.retrieve = to_streamed_response_wrapper(
            programs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            programs.list,
        )


class AsyncProgramsWithStreamingResponse:
    def __init__(self, programs: AsyncPrograms) -> None:
        self._programs = programs

        self.retrieve = async_to_streamed_response_wrapper(
            programs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            programs.list,
        )
