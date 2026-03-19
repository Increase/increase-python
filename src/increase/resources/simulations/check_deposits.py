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
from ...types.simulations import check_deposit_submit_params, check_deposit_adjustment_params
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

    def adjustment(
        self,
        check_deposit_id: str,
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
    ) -> CheckDeposit:
        """
        Simulates the creation of a
        [Check Deposit Adjustment](#check-deposit-adjustments) on a
        [Check Deposit](#check-deposits). This Check Deposit must first have a `status`
        of `submitted`.

        Args:
          check_deposit_id: The identifier of the Check Deposit you wish to adjust.

          amount: The adjustment amount in the minor unit of the Check Deposit's currency (e.g.,
              cents). A negative amount means that the funds are being clawed back by the
              other bank and is a debit to your account. Defaults to the negative of the Check
              Deposit amount.

          reason: The reason for the adjustment. Defaults to `non_conforming_item`, which is often
              used for a low quality image that the recipient wasn't able to handle.

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
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return self._post(
            path_template(
                "/simulations/check_deposits/{check_deposit_id}/adjustment", check_deposit_id=check_deposit_id
            ),
            body=maybe_transform(
                {
                    "amount": amount,
                    "reason": reason,
                },
                check_deposit_adjustment_params.CheckDepositAdjustmentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckDeposit,
        )

    def reject(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/simulations/check_deposits/{check_deposit_id}/reject", check_deposit_id=check_deposit_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/simulations/check_deposits/{check_deposit_id}/return", check_deposit_id=check_deposit_id),
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
        scan: check_deposit_submit_params.Scan | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckDeposit:
        """
        Simulates the submission of a [Check Deposit](#check-deposits) to the Federal
        Reserve. This Check Deposit must first have a `status` of `pending`.

        Args:
          check_deposit_id: The identifier of the Check Deposit you wish to submit.

          scan: If set, the simulation will use these values for the check's scanned MICR data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return self._post(
            path_template("/simulations/check_deposits/{check_deposit_id}/submit", check_deposit_id=check_deposit_id),
            body=maybe_transform({"scan": scan}, check_deposit_submit_params.CheckDepositSubmitParams),
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

    async def adjustment(
        self,
        check_deposit_id: str,
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
    ) -> CheckDeposit:
        """
        Simulates the creation of a
        [Check Deposit Adjustment](#check-deposit-adjustments) on a
        [Check Deposit](#check-deposits). This Check Deposit must first have a `status`
        of `submitted`.

        Args:
          check_deposit_id: The identifier of the Check Deposit you wish to adjust.

          amount: The adjustment amount in the minor unit of the Check Deposit's currency (e.g.,
              cents). A negative amount means that the funds are being clawed back by the
              other bank and is a debit to your account. Defaults to the negative of the Check
              Deposit amount.

          reason: The reason for the adjustment. Defaults to `non_conforming_item`, which is often
              used for a low quality image that the recipient wasn't able to handle.

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
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return await self._post(
            path_template(
                "/simulations/check_deposits/{check_deposit_id}/adjustment", check_deposit_id=check_deposit_id
            ),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "reason": reason,
                },
                check_deposit_adjustment_params.CheckDepositAdjustmentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckDeposit,
        )

    async def reject(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/simulations/check_deposits/{check_deposit_id}/reject", check_deposit_id=check_deposit_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/simulations/check_deposits/{check_deposit_id}/return", check_deposit_id=check_deposit_id),
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
        scan: check_deposit_submit_params.Scan | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckDeposit:
        """
        Simulates the submission of a [Check Deposit](#check-deposits) to the Federal
        Reserve. This Check Deposit must first have a `status` of `pending`.

        Args:
          check_deposit_id: The identifier of the Check Deposit you wish to submit.

          scan: If set, the simulation will use these values for the check's scanned MICR data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return await self._post(
            path_template("/simulations/check_deposits/{check_deposit_id}/submit", check_deposit_id=check_deposit_id),
            body=await async_maybe_transform({"scan": scan}, check_deposit_submit_params.CheckDepositSubmitParams),
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

        self.adjustment = to_raw_response_wrapper(
            check_deposits.adjustment,
        )
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

        self.adjustment = async_to_raw_response_wrapper(
            check_deposits.adjustment,
        )
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

        self.adjustment = to_streamed_response_wrapper(
            check_deposits.adjustment,
        )
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

        self.adjustment = async_to_streamed_response_wrapper(
            check_deposits.adjustment,
        )
        self.reject = async_to_streamed_response_wrapper(
            check_deposits.reject,
        )
        self.return_ = async_to_streamed_response_wrapper(
            check_deposits.return_,
        )
        self.submit = async_to_streamed_response_wrapper(
            check_deposits.submit,
        )
