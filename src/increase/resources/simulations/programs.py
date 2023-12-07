# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ...types import Program
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.simulations import program_create_params

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["Programs", "AsyncPrograms"]


class Programs(SyncAPIResource):
    with_raw_response: ProgramsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = ProgramsWithRawResponse(self)

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
    with_raw_response: AsyncProgramsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncProgramsWithRawResponse(self)

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
        self.create = to_raw_response_wrapper(
            programs.create,
        )


class AsyncProgramsWithRawResponse:
    def __init__(self, programs: AsyncPrograms) -> None:
        self.create = async_to_raw_response_wrapper(
            programs.create,
        )
