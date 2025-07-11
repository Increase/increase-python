# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.program import Program
from ...types.simulations import program_create_params

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

    def create(
        self,
        *,
        name: str,
        bank: Literal[
            "blue_ridge_bank", "core_bank", "first_internet_bank", "global_innovations_bank", "grasshopper_bank"
        ]
        | NotGiven = NOT_GIVEN,
        reserve_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Program:
        """Simulates a [Program](#programs) being created in your group.

        By default, your
        group has one program called Commercial Banking. Note that when your group
        operates more than one program, `program_id` is a required field when creating
        accounts.

        Args:
          name: The name of the program being added.

          bank: The bank for the program's accounts, defaults to First Internet Bank.

              - `blue_ridge_bank` - Blue Ridge Bank, N.A.
              - `core_bank` - Core Bank
              - `first_internet_bank` - First Internet Bank of Indiana
              - `global_innovations_bank` - Global Innovations Bank
              - `grasshopper_bank` - Grasshopper Bank

          reserve_account_id: The identifier of the Account the Program should be added to is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/programs",
            body=maybe_transform(
                {
                    "name": name,
                    "bank": bank,
                    "reserve_account_id": reserve_account_id,
                },
                program_create_params.ProgramCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Program,
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

    async def create(
        self,
        *,
        name: str,
        bank: Literal[
            "blue_ridge_bank", "core_bank", "first_internet_bank", "global_innovations_bank", "grasshopper_bank"
        ]
        | NotGiven = NOT_GIVEN,
        reserve_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Program:
        """Simulates a [Program](#programs) being created in your group.

        By default, your
        group has one program called Commercial Banking. Note that when your group
        operates more than one program, `program_id` is a required field when creating
        accounts.

        Args:
          name: The name of the program being added.

          bank: The bank for the program's accounts, defaults to First Internet Bank.

              - `blue_ridge_bank` - Blue Ridge Bank, N.A.
              - `core_bank` - Core Bank
              - `first_internet_bank` - First Internet Bank of Indiana
              - `global_innovations_bank` - Global Innovations Bank
              - `grasshopper_bank` - Grasshopper Bank

          reserve_account_id: The identifier of the Account the Program should be added to is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/programs",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "bank": bank,
                    "reserve_account_id": reserve_account_id,
                },
                program_create_params.ProgramCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Program,
        )


class ProgramsResourceWithRawResponse:
    def __init__(self, programs: ProgramsResource) -> None:
        self._programs = programs

        self.create = to_raw_response_wrapper(
            programs.create,
        )


class AsyncProgramsResourceWithRawResponse:
    def __init__(self, programs: AsyncProgramsResource) -> None:
        self._programs = programs

        self.create = async_to_raw_response_wrapper(
            programs.create,
        )


class ProgramsResourceWithStreamingResponse:
    def __init__(self, programs: ProgramsResource) -> None:
        self._programs = programs

        self.create = to_streamed_response_wrapper(
            programs.create,
        )


class AsyncProgramsResourceWithStreamingResponse:
    def __init__(self, programs: AsyncProgramsResource) -> None:
        self._programs = programs

        self.create = async_to_streamed_response_wrapper(
            programs.create,
        )
