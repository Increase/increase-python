# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ...types import Program
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.simulations import program_create_params

__all__ = ["Programs", "AsyncPrograms"]


class Programs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProgramsWithRawResponse:
        return ProgramsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProgramsWithStreamingResponse:
        return ProgramsWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Program:
        """Simulates a program being created in your group.

        By default, your group has one
        program called Commercial Banking. Note that when your group operates more than
        one program, `program_id` is a required field when creating accounts.

        Args:
          name: The name of the program being added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/programs",
            body=maybe_transform({"name": name}, program_create_params.ProgramCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Program,
        )


class AsyncPrograms(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProgramsWithRawResponse:
        return AsyncProgramsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProgramsWithStreamingResponse:
        return AsyncProgramsWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Program:
        """Simulates a program being created in your group.

        By default, your group has one
        program called Commercial Banking. Note that when your group operates more than
        one program, `program_id` is a required field when creating accounts.

        Args:
          name: The name of the program being added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/programs",
            body=maybe_transform({"name": name}, program_create_params.ProgramCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Program,
        )


class ProgramsWithRawResponse:
    def __init__(self, programs: Programs) -> None:
        self._programs = programs

        self.create = _legacy_response.to_raw_response_wrapper(
            programs.create,
        )


class AsyncProgramsWithRawResponse:
    def __init__(self, programs: AsyncPrograms) -> None:
        self._programs = programs

        self.create = _legacy_response.async_to_raw_response_wrapper(
            programs.create,
        )


class ProgramsWithStreamingResponse:
    def __init__(self, programs: Programs) -> None:
        self._programs = programs

        self.create = to_streamed_response_wrapper(
            programs.create,
        )


class AsyncProgramsWithStreamingResponse:
    def __init__(self, programs: AsyncPrograms) -> None:
        self._programs = programs

        self.create = async_to_streamed_response_wrapper(
            programs.create,
        )
