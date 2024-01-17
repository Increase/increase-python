# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.simulations import InterestPaymentSimulationResult, interest_payment_create_params

__all__ = ["InterestPayments", "AsyncInterestPayments"]


class InterestPayments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InterestPaymentsWithRawResponse:
        return InterestPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InterestPaymentsWithStreamingResponse:
        return InterestPaymentsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        period_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        period_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InterestPaymentSimulationResult:
        """Simulates an interest payment to your account.

        In production, this happens
        automatically on the first of each month.

        Args:
          account_id: The identifier of the Account Number the Interest Payment is for.

          amount: The interest amount in cents. Must be positive.

          period_end: The end of the interest period. If not provided, defaults to the current time.

          period_start: The start of the interest period. If not provided, defaults to the current time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/interest_payment",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
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
            cast_to=InterestPaymentSimulationResult,
        )


class AsyncInterestPayments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInterestPaymentsWithRawResponse:
        return AsyncInterestPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInterestPaymentsWithStreamingResponse:
        return AsyncInterestPaymentsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        period_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        period_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InterestPaymentSimulationResult:
        """Simulates an interest payment to your account.

        In production, this happens
        automatically on the first of each month.

        Args:
          account_id: The identifier of the Account Number the Interest Payment is for.

          amount: The interest amount in cents. Must be positive.

          period_end: The end of the interest period. If not provided, defaults to the current time.

          period_start: The start of the interest period. If not provided, defaults to the current time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/interest_payment",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
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
            cast_to=InterestPaymentSimulationResult,
        )


class InterestPaymentsWithRawResponse:
    def __init__(self, interest_payments: InterestPayments) -> None:
        self._interest_payments = interest_payments

        self.create = _legacy_response.to_raw_response_wrapper(
            interest_payments.create,
        )


class AsyncInterestPaymentsWithRawResponse:
    def __init__(self, interest_payments: AsyncInterestPayments) -> None:
        self._interest_payments = interest_payments

        self.create = _legacy_response.async_to_raw_response_wrapper(
            interest_payments.create,
        )


class InterestPaymentsWithStreamingResponse:
    def __init__(self, interest_payments: InterestPayments) -> None:
        self._interest_payments = interest_payments

        self.create = to_streamed_response_wrapper(
            interest_payments.create,
        )


class AsyncInterestPaymentsWithStreamingResponse:
    def __init__(self, interest_payments: AsyncInterestPayments) -> None:
        self._interest_payments = interest_payments

        self.create = async_to_streamed_response_wrapper(
            interest_payments.create,
        )
