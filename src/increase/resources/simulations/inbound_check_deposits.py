# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.simulations import inbound_check_deposit_create_params
from ...types.inbound_check_deposit import InboundCheckDeposit

__all__ = ["InboundCheckDeposits", "AsyncInboundCheckDeposits"]


class InboundCheckDeposits(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundCheckDepositsWithRawResponse:
        return InboundCheckDepositsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundCheckDepositsWithStreamingResponse:
        return InboundCheckDepositsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        check_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundCheckDeposit:
        """Simulates an Inbound Check Deposit against your account.

        This imitates someone
        depositing a check at their bank that was issued from your account. It may or
        may not be associated with a Check Transfer. Increase will evaluate the Check
        Deposit as we would in production and either create a Transaction or a Declined
        Transaction as a result. You can inspect the resulting Inbound Check Deposit
        object to see the result.

        Args:
          account_number_id: The identifier of the Account Number the Inbound Check Deposit will be against.

          amount: The check amount in cents.

          check_number: The check number on the check to be deposited.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/inbound_check_deposits",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "check_number": check_number,
                },
                inbound_check_deposit_create_params.InboundCheckDepositCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundCheckDeposit,
        )


class AsyncInboundCheckDeposits(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundCheckDepositsWithRawResponse:
        return AsyncInboundCheckDepositsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundCheckDepositsWithStreamingResponse:
        return AsyncInboundCheckDepositsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        check_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundCheckDeposit:
        """Simulates an Inbound Check Deposit against your account.

        This imitates someone
        depositing a check at their bank that was issued from your account. It may or
        may not be associated with a Check Transfer. Increase will evaluate the Check
        Deposit as we would in production and either create a Transaction or a Declined
        Transaction as a result. You can inspect the resulting Inbound Check Deposit
        object to see the result.

        Args:
          account_number_id: The identifier of the Account Number the Inbound Check Deposit will be against.

          amount: The check amount in cents.

          check_number: The check number on the check to be deposited.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/inbound_check_deposits",
            body=await async_maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "check_number": check_number,
                },
                inbound_check_deposit_create_params.InboundCheckDepositCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundCheckDeposit,
        )


class InboundCheckDepositsWithRawResponse:
    def __init__(self, inbound_check_deposits: InboundCheckDeposits) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.create = _legacy_response.to_raw_response_wrapper(
            inbound_check_deposits.create,
        )


class AsyncInboundCheckDepositsWithRawResponse:
    def __init__(self, inbound_check_deposits: AsyncInboundCheckDeposits) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.create = _legacy_response.async_to_raw_response_wrapper(
            inbound_check_deposits.create,
        )


class InboundCheckDepositsWithStreamingResponse:
    def __init__(self, inbound_check_deposits: InboundCheckDeposits) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.create = to_streamed_response_wrapper(
            inbound_check_deposits.create,
        )


class AsyncInboundCheckDepositsWithStreamingResponse:
    def __init__(self, inbound_check_deposits: AsyncInboundCheckDeposits) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.create = async_to_streamed_response_wrapper(
            inbound_check_deposits.create,
        )
