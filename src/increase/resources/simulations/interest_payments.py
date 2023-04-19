# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations import (
    InterestPaymentSimulationResult,
    interest_payment_create_params,
)

__all__ = ["InterestPayments", "AsyncInterestPayments"]


class InterestPayments(SyncAPIResource):
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InterestPaymentSimulationResult:
        """Simulates an interest payment to your account.

        In production, this happens
        automatically on the first of each month.

        Args:
          account_id: The identifier of the Account Number the Interest Payment is for.

          amount: The interest amount in cents. Must be positive.

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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InterestPaymentSimulationResult:
        """Simulates an interest payment to your account.

        In production, this happens
        automatically on the first of each month.

        Args:
          account_id: The identifier of the Account Number the Interest Payment is for.

          amount: The interest amount in cents. Must be positive.

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
