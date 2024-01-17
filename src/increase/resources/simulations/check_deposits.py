# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ...types import CheckDeposit
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)

__all__ = ["CheckDeposits", "AsyncCheckDeposits"]


class CheckDeposits(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckDepositsWithRawResponse:
        return CheckDepositsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckDepositsWithStreamingResponse:
        return CheckDepositsWithStreamingResponse(self)

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


class AsyncCheckDeposits(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckDepositsWithRawResponse:
        return AsyncCheckDepositsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckDepositsWithStreamingResponse:
        return AsyncCheckDepositsWithStreamingResponse(self)

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


class CheckDepositsWithRawResponse:
    def __init__(self, check_deposits: CheckDeposits) -> None:
        self._check_deposits = check_deposits

        self.reject = _legacy_response.to_raw_response_wrapper(
            check_deposits.reject,
        )
        self.return_ = _legacy_response.to_raw_response_wrapper(
            check_deposits.return_,
        )
        self.submit = _legacy_response.to_raw_response_wrapper(
            check_deposits.submit,
        )


class AsyncCheckDepositsWithRawResponse:
    def __init__(self, check_deposits: AsyncCheckDeposits) -> None:
        self._check_deposits = check_deposits

        self.reject = _legacy_response.async_to_raw_response_wrapper(
            check_deposits.reject,
        )
        self.return_ = _legacy_response.async_to_raw_response_wrapper(
            check_deposits.return_,
        )
        self.submit = _legacy_response.async_to_raw_response_wrapper(
            check_deposits.submit,
        )


class CheckDepositsWithStreamingResponse:
    def __init__(self, check_deposits: CheckDeposits) -> None:
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


class AsyncCheckDepositsWithStreamingResponse:
    def __init__(self, check_deposits: AsyncCheckDeposits) -> None:
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
