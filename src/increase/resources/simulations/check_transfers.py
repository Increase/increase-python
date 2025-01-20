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
from ...types.check_transfer import CheckTransfer

__all__ = ["CheckTransfersResource", "AsyncCheckTransfersResource"]


class CheckTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CheckTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CheckTransfersResourceWithStreamingResponse(self)

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
        periodically throughout the day in production but can be sped up in sandbox.
        This transfer must first have a `status` of `pending_approval` or
        `pending_submission`.

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


class AsyncCheckTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCheckTransfersResourceWithStreamingResponse(self)

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
        periodically throughout the day in production but can be sped up in sandbox.
        This transfer must first have a `status` of `pending_approval` or
        `pending_submission`.

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


class CheckTransfersResourceWithRawResponse:
    def __init__(self, check_transfers: CheckTransfersResource) -> None:
        self._check_transfers = check_transfers

        self.mail = to_raw_response_wrapper(
            check_transfers.mail,
        )


class AsyncCheckTransfersResourceWithRawResponse:
    def __init__(self, check_transfers: AsyncCheckTransfersResource) -> None:
        self._check_transfers = check_transfers

        self.mail = async_to_raw_response_wrapper(
            check_transfers.mail,
        )


class CheckTransfersResourceWithStreamingResponse:
    def __init__(self, check_transfers: CheckTransfersResource) -> None:
        self._check_transfers = check_transfers

        self.mail = to_streamed_response_wrapper(
            check_transfers.mail,
        )


class AsyncCheckTransfersResourceWithStreamingResponse:
    def __init__(self, check_transfers: AsyncCheckTransfersResource) -> None:
        self._check_transfers = check_transfers

        self.mail = async_to_streamed_response_wrapper(
            check_transfers.mail,
        )
