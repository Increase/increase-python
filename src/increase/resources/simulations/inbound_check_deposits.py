# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import inbound_check_deposit_create_params, inbound_check_deposit_adjustment_params
from ...types.inbound_check_deposit import InboundCheckDeposit

__all__ = ["InboundCheckDepositsResource", "AsyncInboundCheckDepositsResource"]


class InboundCheckDepositsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundCheckDepositsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundCheckDepositsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundCheckDepositsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundCheckDepositsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        check_number: str,
        payee_name_analysis: Literal["name_matches", "does_not_match", "not_evaluated"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> InboundCheckDeposit:
        """Simulates an Inbound Check Deposit against your account.

        This imitates someone
        depositing a check at their bank that was issued from your account. It may or
        may not be associated with a Check Transfer. Increase will evaluate the Inbound
        Check Deposit as we would in production and either create a Transaction or a
        Declined Transaction as a result. You can inspect the resulting Inbound Check
        Deposit object to see the result.

        Args:
          account_number_id: The identifier of the Account Number the Inbound Check Deposit will be against.

          amount: The check amount in cents.

          check_number: The check number on the check to be deposited.

          payee_name_analysis: Simulate the outcome of
              [payee name checking](https://increase.com/documentation/positive-pay#payee-name-mismatches).
              Defaults to `not_evaluated`.

              - `name_matches` - The details on the check match the recipient name of the
                check transfer.
              - `does_not_match` - The details on the check do not match the recipient name of
                the check transfer.
              - `not_evaluated` - The payee name analysis was not evaluated.

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
                    "payee_name_analysis": payee_name_analysis,
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

    def adjustment(
        self,
        inbound_check_deposit_id: str,
        *,
        amount: int | Omit = omit,
        reason: Literal["late_return", "wrong_payee_credit", "adjusted_amount", "non_conforming_item", "paid"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> InboundCheckDeposit:
        """Simulates an adjustment on an Inbound Check Deposit.

        The Inbound Check Deposit
        must have a `status` of `accepted`.

        Args:
          inbound_check_deposit_id: The identifier of the Inbound Check Deposit to adjust.

          amount: The adjustment amount in cents. Defaults to the amount of the Inbound Check
              Deposit.

          reason: The reason for the adjustment. Defaults to `wrong_payee_credit`.

              - `late_return` - The return was initiated too late and the receiving
                institution has responded with a Late Return Claim.
              - `wrong_payee_credit` - The check was deposited to the wrong payee and the
                depositing institution has reimbursed the funds with a Wrong Payee Credit.
              - `adjusted_amount` - The check was deposited with a different amount than what
                was written on the check.
              - `non_conforming_item` - The recipient was not able to process the check. This
                usually happens for e.g., low quality images.
              - `paid` - The check has already been deposited elsewhere and so this is a
                duplicate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not inbound_check_deposit_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_check_deposit_id` but received {inbound_check_deposit_id!r}"
            )
        return self._post(
            path_template(
                "/simulations/inbound_check_deposits/{inbound_check_deposit_id}/adjustment",
                inbound_check_deposit_id=inbound_check_deposit_id,
            ),
            body=maybe_transform(
                {
                    "amount": amount,
                    "reason": reason,
                },
                inbound_check_deposit_adjustment_params.InboundCheckDepositAdjustmentParams,
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


class AsyncInboundCheckDepositsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundCheckDepositsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundCheckDepositsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundCheckDepositsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundCheckDepositsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        check_number: str,
        payee_name_analysis: Literal["name_matches", "does_not_match", "not_evaluated"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> InboundCheckDeposit:
        """Simulates an Inbound Check Deposit against your account.

        This imitates someone
        depositing a check at their bank that was issued from your account. It may or
        may not be associated with a Check Transfer. Increase will evaluate the Inbound
        Check Deposit as we would in production and either create a Transaction or a
        Declined Transaction as a result. You can inspect the resulting Inbound Check
        Deposit object to see the result.

        Args:
          account_number_id: The identifier of the Account Number the Inbound Check Deposit will be against.

          amount: The check amount in cents.

          check_number: The check number on the check to be deposited.

          payee_name_analysis: Simulate the outcome of
              [payee name checking](https://increase.com/documentation/positive-pay#payee-name-mismatches).
              Defaults to `not_evaluated`.

              - `name_matches` - The details on the check match the recipient name of the
                check transfer.
              - `does_not_match` - The details on the check do not match the recipient name of
                the check transfer.
              - `not_evaluated` - The payee name analysis was not evaluated.

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
                    "payee_name_analysis": payee_name_analysis,
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

    async def adjustment(
        self,
        inbound_check_deposit_id: str,
        *,
        amount: int | Omit = omit,
        reason: Literal["late_return", "wrong_payee_credit", "adjusted_amount", "non_conforming_item", "paid"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> InboundCheckDeposit:
        """Simulates an adjustment on an Inbound Check Deposit.

        The Inbound Check Deposit
        must have a `status` of `accepted`.

        Args:
          inbound_check_deposit_id: The identifier of the Inbound Check Deposit to adjust.

          amount: The adjustment amount in cents. Defaults to the amount of the Inbound Check
              Deposit.

          reason: The reason for the adjustment. Defaults to `wrong_payee_credit`.

              - `late_return` - The return was initiated too late and the receiving
                institution has responded with a Late Return Claim.
              - `wrong_payee_credit` - The check was deposited to the wrong payee and the
                depositing institution has reimbursed the funds with a Wrong Payee Credit.
              - `adjusted_amount` - The check was deposited with a different amount than what
                was written on the check.
              - `non_conforming_item` - The recipient was not able to process the check. This
                usually happens for e.g., low quality images.
              - `paid` - The check has already been deposited elsewhere and so this is a
                duplicate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not inbound_check_deposit_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_check_deposit_id` but received {inbound_check_deposit_id!r}"
            )
        return await self._post(
            path_template(
                "/simulations/inbound_check_deposits/{inbound_check_deposit_id}/adjustment",
                inbound_check_deposit_id=inbound_check_deposit_id,
            ),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "reason": reason,
                },
                inbound_check_deposit_adjustment_params.InboundCheckDepositAdjustmentParams,
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


class InboundCheckDepositsResourceWithRawResponse:
    def __init__(self, inbound_check_deposits: InboundCheckDepositsResource) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.create = to_raw_response_wrapper(
            inbound_check_deposits.create,
        )
        self.adjustment = to_raw_response_wrapper(
            inbound_check_deposits.adjustment,
        )


class AsyncInboundCheckDepositsResourceWithRawResponse:
    def __init__(self, inbound_check_deposits: AsyncInboundCheckDepositsResource) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.create = async_to_raw_response_wrapper(
            inbound_check_deposits.create,
        )
        self.adjustment = async_to_raw_response_wrapper(
            inbound_check_deposits.adjustment,
        )


class InboundCheckDepositsResourceWithStreamingResponse:
    def __init__(self, inbound_check_deposits: InboundCheckDepositsResource) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.create = to_streamed_response_wrapper(
            inbound_check_deposits.create,
        )
        self.adjustment = to_streamed_response_wrapper(
            inbound_check_deposits.adjustment,
        )


class AsyncInboundCheckDepositsResourceWithStreamingResponse:
    def __init__(self, inbound_check_deposits: AsyncInboundCheckDepositsResource) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.create = async_to_streamed_response_wrapper(
            inbound_check_deposits.create,
        )
        self.adjustment = async_to_streamed_response_wrapper(
            inbound_check_deposits.adjustment,
        )
