# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.simulations import fee_payment_create_params
from ...types.transaction import Transaction

__all__ = ["FeePaymentsResource", "AsyncFeePaymentsResource"]


class FeePaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeePaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return FeePaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeePaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return FeePaymentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """
        A fee payment is how Increase charges you for technology fees incurred each
        month. In production, these payments will be charged to your program's billing
        account.

        Args:
          account_id: The identifier of the Account to use as the billing account for the fee payment.

          amount: The fee amount in cents. Must be positive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/fee_payments",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                },
                fee_payment_create_params.FeePaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Transaction,
        )


class AsyncFeePaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeePaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeePaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeePaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncFeePaymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """
        A fee payment is how Increase charges you for technology fees incurred each
        month. In production, these payments will be charged to your program's billing
        account.

        Args:
          account_id: The identifier of the Account to use as the billing account for the fee payment.

          amount: The fee amount in cents. Must be positive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/fee_payments",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                },
                fee_payment_create_params.FeePaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Transaction,
        )


class FeePaymentsResourceWithRawResponse:
    def __init__(self, fee_payments: FeePaymentsResource) -> None:
        self._fee_payments = fee_payments

        self.create = to_raw_response_wrapper(
            fee_payments.create,
        )


class AsyncFeePaymentsResourceWithRawResponse:
    def __init__(self, fee_payments: AsyncFeePaymentsResource) -> None:
        self._fee_payments = fee_payments

        self.create = async_to_raw_response_wrapper(
            fee_payments.create,
        )


class FeePaymentsResourceWithStreamingResponse:
    def __init__(self, fee_payments: FeePaymentsResource) -> None:
        self._fee_payments = fee_payments

        self.create = to_streamed_response_wrapper(
            fee_payments.create,
        )


class AsyncFeePaymentsResourceWithStreamingResponse:
    def __init__(self, fee_payments: AsyncFeePaymentsResource) -> None:
        self._fee_payments = fee_payments

        self.create = async_to_streamed_response_wrapper(
            fee_payments.create,
        )
