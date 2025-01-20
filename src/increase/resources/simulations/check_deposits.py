# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.check_deposit import CheckDeposit

__all__ = ["CheckDepositsResource", "AsyncCheckDepositsResource"]


class CheckDepositsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckDepositsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CheckDepositsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckDepositsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CheckDepositsResourceWithStreamingResponse(self)

    def reject(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckDeposit:
        """
        Simulates the rejection of a [Check Deposit](#check-deposits) by Increase due to
        factors like poor image quality. This Check Deposit must first have a `status`
        of `pending`.

        Args:
          check_deposit_id: The identifier of the Check Deposit you wish to reject.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return self._post(
            f"/simulations/check_deposits/{check_deposit_id}/reject",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckDeposit,
        )

    def return_(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckDeposit:
        """Simulates the return of a [Check Deposit](#check-deposits).

        This Check Deposit
        must first have a `status` of `submitted`.

        Args:
          check_deposit_id: The identifier of the Check Deposit you wish to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return self._post(
            f"/simulations/check_deposits/{check_deposit_id}/return",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckDeposit,
        )

    def submit(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckDeposit:
        """
        Simulates the submission of a [Check Deposit](#check-deposits) to the Federal
        Reserve. This Check Deposit must first have a `status` of `pending`.

        Args:
          check_deposit_id: The identifier of the Check Deposit you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return self._post(
            f"/simulations/check_deposits/{check_deposit_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckDeposit,
        )


class AsyncCheckDepositsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckDepositsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckDepositsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckDepositsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCheckDepositsResourceWithStreamingResponse(self)

    async def reject(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckDeposit:
        """
        Simulates the rejection of a [Check Deposit](#check-deposits) by Increase due to
        factors like poor image quality. This Check Deposit must first have a `status`
        of `pending`.

        Args:
          check_deposit_id: The identifier of the Check Deposit you wish to reject.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return await self._post(
            f"/simulations/check_deposits/{check_deposit_id}/reject",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckDeposit,
        )

    async def return_(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckDeposit:
        """Simulates the return of a [Check Deposit](#check-deposits).

        This Check Deposit
        must first have a `status` of `submitted`.

        Args:
          check_deposit_id: The identifier of the Check Deposit you wish to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return await self._post(
            f"/simulations/check_deposits/{check_deposit_id}/return",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckDeposit,
        )

    async def submit(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckDeposit:
        """
        Simulates the submission of a [Check Deposit](#check-deposits) to the Federal
        Reserve. This Check Deposit must first have a `status` of `pending`.

        Args:
          check_deposit_id: The identifier of the Check Deposit you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return await self._post(
            f"/simulations/check_deposits/{check_deposit_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckDeposit,
        )


class CheckDepositsResourceWithRawResponse:
    def __init__(self, check_deposits: CheckDepositsResource) -> None:
        self._check_deposits = check_deposits

        self.reject = to_raw_response_wrapper(
            check_deposits.reject,
        )
        self.return_ = to_raw_response_wrapper(
            check_deposits.return_,
        )
        self.submit = to_raw_response_wrapper(
            check_deposits.submit,
        )


class AsyncCheckDepositsResourceWithRawResponse:
    def __init__(self, check_deposits: AsyncCheckDepositsResource) -> None:
        self._check_deposits = check_deposits

        self.reject = async_to_raw_response_wrapper(
            check_deposits.reject,
        )
        self.return_ = async_to_raw_response_wrapper(
            check_deposits.return_,
        )
        self.submit = async_to_raw_response_wrapper(
            check_deposits.submit,
        )


class CheckDepositsResourceWithStreamingResponse:
    def __init__(self, check_deposits: CheckDepositsResource) -> None:
        self._check_deposits = check_deposits

        self.reject = to_streamed_response_wrapper(
            check_deposits.reject,
        )
        self.return_ = to_streamed_response_wrapper(
            check_deposits.return_,
        )
        self.submit = to_streamed_response_wrapper(
            check_deposits.submit,
        )


class AsyncCheckDepositsResourceWithStreamingResponse:
    def __init__(self, check_deposits: AsyncCheckDepositsResource) -> None:
        self._check_deposits = check_deposits

        self.reject = async_to_streamed_response_wrapper(
            check_deposits.reject,
        )
        self.return_ = async_to_streamed_response_wrapper(
            check_deposits.return_,
        )
        self.submit = async_to_streamed_response_wrapper(
            check_deposits.submit,
        )
