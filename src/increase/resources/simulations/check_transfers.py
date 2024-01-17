# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ...types import CheckTransfer
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)

__all__ = ["CheckTransfers", "AsyncCheckTransfers"]


class CheckTransfers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckTransfersWithRawResponse:
        return CheckTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckTransfersWithStreamingResponse:
        return CheckTransfersWithStreamingResponse(self)

    def deposit(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """Simulates a [Check Transfer](#check-transfers) being deposited at a bank.

        This
        transfer must first have a `status` of `mailed`.

        Args:
          check_transfer_id: The identifier of the Check Transfer you wish to mark deposited.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return self._post(
            f"/simulations/check_transfers/{check_transfer_id}/deposit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )

    def mail(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Simulates the mailing of a [Check Transfer](#check-transfers), which happens
        once per weekday in production but can be sped up in sandbox. This transfer must
        first have a `status` of `pending_approval` or `pending_submission`.

        Args:
          check_transfer_id: The identifier of the Check Transfer you wish to mail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return self._post(
            f"/simulations/check_transfers/{check_transfer_id}/mail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )


class AsyncCheckTransfers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckTransfersWithRawResponse:
        return AsyncCheckTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckTransfersWithStreamingResponse:
        return AsyncCheckTransfersWithStreamingResponse(self)

    async def deposit(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """Simulates a [Check Transfer](#check-transfers) being deposited at a bank.

        This
        transfer must first have a `status` of `mailed`.

        Args:
          check_transfer_id: The identifier of the Check Transfer you wish to mark deposited.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return await self._post(
            f"/simulations/check_transfers/{check_transfer_id}/deposit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )

    async def mail(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Simulates the mailing of a [Check Transfer](#check-transfers), which happens
        once per weekday in production but can be sped up in sandbox. This transfer must
        first have a `status` of `pending_approval` or `pending_submission`.

        Args:
          check_transfer_id: The identifier of the Check Transfer you wish to mail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return await self._post(
            f"/simulations/check_transfers/{check_transfer_id}/mail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )


class CheckTransfersWithRawResponse:
    def __init__(self, check_transfers: CheckTransfers) -> None:
        self._check_transfers = check_transfers

        self.deposit = _legacy_response.to_raw_response_wrapper(
            check_transfers.deposit,
        )
        self.mail = _legacy_response.to_raw_response_wrapper(
            check_transfers.mail,
        )


class AsyncCheckTransfersWithRawResponse:
    def __init__(self, check_transfers: AsyncCheckTransfers) -> None:
        self._check_transfers = check_transfers

        self.deposit = _legacy_response.async_to_raw_response_wrapper(
            check_transfers.deposit,
        )
        self.mail = _legacy_response.async_to_raw_response_wrapper(
            check_transfers.mail,
        )


class CheckTransfersWithStreamingResponse:
    def __init__(self, check_transfers: CheckTransfers) -> None:
        self._check_transfers = check_transfers

        self.deposit = to_streamed_response_wrapper(
            check_transfers.deposit,
        )
        self.mail = to_streamed_response_wrapper(
            check_transfers.mail,
        )


class AsyncCheckTransfersWithStreamingResponse:
    def __init__(self, check_transfers: AsyncCheckTransfers) -> None:
        self._check_transfers = check_transfers

        self.deposit = async_to_streamed_response_wrapper(
            check_transfers.deposit,
        )
        self.mail = async_to_streamed_response_wrapper(
            check_transfers.mail,
        )
