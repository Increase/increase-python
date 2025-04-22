# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

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
from ...types.simulations import interest_payment_create_params
from ...types.transaction import Transaction

__all__ = ["InterestPaymentsResource", "AsyncInterestPaymentsResource"]


class InterestPaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InterestPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InterestPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InterestPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InterestPaymentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        accrued_on_account_id: str | NotGiven = NOT_GIVEN,
        period_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        period_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """Simulates an interest payment to your account.

        In production, this happens
        automatically on the first of each month.

        Args:
          account_id: The identifier of the Account the Interest Payment should be paid to is for.

          amount: The interest amount in cents. Must be positive.

          accrued_on_account_id: The identifier of the Account the Interest accrued on. Defaults to `account_id`.

          period_end: The end of the interest period. If not provided, defaults to the current time.

          period_start: The start of the interest period. If not provided, defaults to the current time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/interest_payments",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "accrued_on_account_id": accrued_on_account_id,
                    "period_end": period_end,
                    "period_start": period_start,
                },
                interest_payment_create_params.InterestPaymentCreateParams,
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


class AsyncInterestPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInterestPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInterestPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInterestPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInterestPaymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        accrued_on_account_id: str | NotGiven = NOT_GIVEN,
        period_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        period_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Transaction:
        """Simulates an interest payment to your account.

        In production, this happens
        automatically on the first of each month.

        Args:
          account_id: The identifier of the Account the Interest Payment should be paid to is for.

          amount: The interest amount in cents. Must be positive.

          accrued_on_account_id: The identifier of the Account the Interest accrued on. Defaults to `account_id`.

          period_end: The end of the interest period. If not provided, defaults to the current time.

          period_start: The start of the interest period. If not provided, defaults to the current time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/interest_payments",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "accrued_on_account_id": accrued_on_account_id,
                    "period_end": period_end,
                    "period_start": period_start,
                },
                interest_payment_create_params.InterestPaymentCreateParams,
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


class InterestPaymentsResourceWithRawResponse:
    def __init__(self, interest_payments: InterestPaymentsResource) -> None:
        self._interest_payments = interest_payments

        self.create = to_raw_response_wrapper(
            interest_payments.create,
        )


class AsyncInterestPaymentsResourceWithRawResponse:
    def __init__(self, interest_payments: AsyncInterestPaymentsResource) -> None:
        self._interest_payments = interest_payments

        self.create = async_to_raw_response_wrapper(
            interest_payments.create,
        )


class InterestPaymentsResourceWithStreamingResponse:
    def __init__(self, interest_payments: InterestPaymentsResource) -> None:
        self._interest_payments = interest_payments

        self.create = to_streamed_response_wrapper(
            interest_payments.create,
        )


class AsyncInterestPaymentsResourceWithStreamingResponse:
    def __init__(self, interest_payments: AsyncInterestPaymentsResource) -> None:
        self._interest_payments = interest_payments

        self.create = async_to_streamed_response_wrapper(
            interest_payments.create,
        )
