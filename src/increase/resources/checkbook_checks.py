# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import checkbook_check_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.checkbook_check import CheckbookCheck

__all__ = ["CheckbookChecksResource", "AsyncCheckbookChecksResource"]


class CheckbookChecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckbookChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CheckbookChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckbookChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CheckbookChecksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        checkbook_check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckbookCheck:
        """
        Retrieve a Checkbook Check

        Args:
          checkbook_check_id: The identifier of the Checkbook Check.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not checkbook_check_id:
            raise ValueError(f"Expected a non-empty value for `checkbook_check_id` but received {checkbook_check_id!r}")
        return self._get(
            path_template("/checkbook_checks/{checkbook_check_id}", checkbook_check_id=checkbook_check_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckbookCheck,
        )

    def list(
        self,
        *,
        account_number_id: str | Omit = omit,
        check_number: int | Omit = omit,
        checkbook_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[CheckbookCheck]:
        """
        List Checkbook Checks

        Args:
          account_number_id: Filter Checkbook Checks to those drawn on the specified Account Number.

          check_number: Filter Checkbook Checks to the one with the specified check number.

          checkbook_id: Filter Checkbook Checks to those belonging to the specified Checkbook.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

              Defaults to `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/checkbook_checks",
            page=SyncPage[CheckbookCheck],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_number_id": account_number_id,
                        "check_number": check_number,
                        "checkbook_id": checkbook_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    checkbook_check_list_params.CheckbookCheckListParams,
                ),
            ),
            model=CheckbookCheck,
        )

    def stop(
        self,
        checkbook_check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckbookCheck:
        """Stop a Checkbook Check.

        A stopped check cannot be deposited.

        Args:
          checkbook_check_id: The identifier of the Checkbook Check to stop.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not checkbook_check_id:
            raise ValueError(f"Expected a non-empty value for `checkbook_check_id` but received {checkbook_check_id!r}")
        return self._post(
            path_template("/checkbook_checks/{checkbook_check_id}/stop", checkbook_check_id=checkbook_check_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckbookCheck,
        )


class AsyncCheckbookChecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckbookChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckbookChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckbookChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCheckbookChecksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        checkbook_check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckbookCheck:
        """
        Retrieve a Checkbook Check

        Args:
          checkbook_check_id: The identifier of the Checkbook Check.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not checkbook_check_id:
            raise ValueError(f"Expected a non-empty value for `checkbook_check_id` but received {checkbook_check_id!r}")
        return await self._get(
            path_template("/checkbook_checks/{checkbook_check_id}", checkbook_check_id=checkbook_check_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckbookCheck,
        )

    def list(
        self,
        *,
        account_number_id: str | Omit = omit,
        check_number: int | Omit = omit,
        checkbook_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CheckbookCheck, AsyncPage[CheckbookCheck]]:
        """
        List Checkbook Checks

        Args:
          account_number_id: Filter Checkbook Checks to those drawn on the specified Account Number.

          check_number: Filter Checkbook Checks to the one with the specified check number.

          checkbook_id: Filter Checkbook Checks to those belonging to the specified Checkbook.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

              Defaults to `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/checkbook_checks",
            page=AsyncPage[CheckbookCheck],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_number_id": account_number_id,
                        "check_number": check_number,
                        "checkbook_id": checkbook_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    checkbook_check_list_params.CheckbookCheckListParams,
                ),
            ),
            model=CheckbookCheck,
        )

    async def stop(
        self,
        checkbook_check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckbookCheck:
        """Stop a Checkbook Check.

        A stopped check cannot be deposited.

        Args:
          checkbook_check_id: The identifier of the Checkbook Check to stop.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not checkbook_check_id:
            raise ValueError(f"Expected a non-empty value for `checkbook_check_id` but received {checkbook_check_id!r}")
        return await self._post(
            path_template("/checkbook_checks/{checkbook_check_id}/stop", checkbook_check_id=checkbook_check_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckbookCheck,
        )


class CheckbookChecksResourceWithRawResponse:
    def __init__(self, checkbook_checks: CheckbookChecksResource) -> None:
        self._checkbook_checks = checkbook_checks

        self.retrieve = to_raw_response_wrapper(
            checkbook_checks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            checkbook_checks.list,
        )
        self.stop = to_raw_response_wrapper(
            checkbook_checks.stop,
        )


class AsyncCheckbookChecksResourceWithRawResponse:
    def __init__(self, checkbook_checks: AsyncCheckbookChecksResource) -> None:
        self._checkbook_checks = checkbook_checks

        self.retrieve = async_to_raw_response_wrapper(
            checkbook_checks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            checkbook_checks.list,
        )
        self.stop = async_to_raw_response_wrapper(
            checkbook_checks.stop,
        )


class CheckbookChecksResourceWithStreamingResponse:
    def __init__(self, checkbook_checks: CheckbookChecksResource) -> None:
        self._checkbook_checks = checkbook_checks

        self.retrieve = to_streamed_response_wrapper(
            checkbook_checks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            checkbook_checks.list,
        )
        self.stop = to_streamed_response_wrapper(
            checkbook_checks.stop,
        )


class AsyncCheckbookChecksResourceWithStreamingResponse:
    def __init__(self, checkbook_checks: AsyncCheckbookChecksResource) -> None:
        self._checkbook_checks = checkbook_checks

        self.retrieve = async_to_streamed_response_wrapper(
            checkbook_checks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            checkbook_checks.list,
        )
        self.stop = async_to_streamed_response_wrapper(
            checkbook_checks.stop,
        )
