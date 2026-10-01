# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    real_time_payments_requests_for_payment_list_params,
    real_time_payments_requests_for_payment_cancel_params,
    real_time_payments_requests_for_payment_create_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.real_time_payments_request_for_payment import RealTimePaymentsRequestForPayment

__all__ = ["RealTimePaymentsRequestsForPaymentResource", "AsyncRealTimePaymentsRequestsForPaymentResource"]


class RealTimePaymentsRequestsForPaymentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealTimePaymentsRequestsForPaymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return RealTimePaymentsRequestsForPaymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealTimePaymentsRequestsForPaymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return RealTimePaymentsRequestsForPaymentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        debtor: real_time_payments_requests_for_payment_create_params.Debtor,
        debtor_account_number: str,
        debtor_routing_number: str,
        expires_at: Union[str, datetime],
        requested_execution_at: Union[str, datetime],
        unstructured_remittance_information: str,
        creditor_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsRequestForPayment:
        """
        Create a Real-Time Payments Request for Payment

        Args:
          account_number_id: The identifier of the Account Number where the funds will land.

          amount: The requested amount in USD cents. Must be positive.

          debtor: Details of the person being requested to pay.

          debtor_account_number: The debtor's account number, which the funds will be requested from.

          debtor_routing_number: The debtor's American Bankers' Association (ABA) Routing Transit Number (RTN).

          expires_at: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time after which
              the request for payment is no longer valid. After this time the debtor's bank
              should no longer allow the debtor to pay it. Must not be before
              `requested_execution_at`.

          requested_execution_at: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time by which
              you are requesting the payment to be made.

          unstructured_remittance_information: Unstructured information that will show on the recipient's bank statement.

          creditor_name: The name of the creditor requesting the payment. If not provided, defaults to
              the name of the account's entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/real_time_payments_requests_for_payment",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "debtor": debtor,
                    "debtor_account_number": debtor_account_number,
                    "debtor_routing_number": debtor_routing_number,
                    "expires_at": expires_at,
                    "requested_execution_at": requested_execution_at,
                    "unstructured_remittance_information": unstructured_remittance_information,
                    "creditor_name": creditor_name,
                },
                real_time_payments_requests_for_payment_create_params.RealTimePaymentsRequestsForPaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimePaymentsRequestForPayment,
        )

    def retrieve(
        self,
        real_time_payments_request_for_payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealTimePaymentsRequestForPayment:
        """
        Retrieve a Real-Time Payments Request for Payment

        Args:
          real_time_payments_request_for_payment_id: The identifier of the Real-Time Payments Request for Payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not real_time_payments_request_for_payment_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_payments_request_for_payment_id` but received {real_time_payments_request_for_payment_id!r}"
            )
        return self._get(
            path_template(
                "/real_time_payments_requests_for_payment/{real_time_payments_request_for_payment_id}",
                real_time_payments_request_for_payment_id=real_time_payments_request_for_payment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealTimePaymentsRequestForPayment,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: real_time_payments_requests_for_payment_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[RealTimePaymentsRequestForPayment]:
        """
        List Real-Time Payments Requests for Payment

        Args:
          account_id: Filter Real-Time Payments Requests for Payment to those destined to the
              specified Account.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

              Defaults to `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/real_time_payments_requests_for_payment",
            page=SyncPage[RealTimePaymentsRequestForPayment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    real_time_payments_requests_for_payment_list_params.RealTimePaymentsRequestsForPaymentListParams,
                ),
            ),
            model=RealTimePaymentsRequestForPayment,
        )

    def cancel(
        self,
        real_time_payments_request_for_payment_id: str,
        *,
        additional_information: str | Omit = omit,
        reason: Literal["requested_by_customer", "paid_by_other_means", "duplicate", "wrong_amount"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsRequestForPayment:
        """
        Cancels a Real-Time Payments Request for Payment that is still awaiting payment.

        Args:
          real_time_payments_request_for_payment_id: The identifier of the Real-Time Payments Request for Payment to cancel.

          additional_information: Additional information about the cancellation to pass on to the recipient bank.

          reason: The reason the request for payment is being canceled. Defaults to
              `requested_by_customer`.

              - `requested_by_customer` - The creditor no longer wants to be paid. Corresponds
                to the Real-Time Payments reason code `CUST`.
              - `paid_by_other_means` - The requested payment has already been made through
                another channel. Corresponds to the Real-Time Payments reason code `UPAY`.
              - `duplicate` - The request for payment duplicated another request for payment.
                Corresponds to the Real-Time Payments reason code `DUPL`.
              - `wrong_amount` - The request for payment was sent for the wrong amount.
                Corresponds to the Real-Time Payments reason code `AM09`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not real_time_payments_request_for_payment_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_payments_request_for_payment_id` but received {real_time_payments_request_for_payment_id!r}"
            )
        return self._post(
            path_template(
                "/real_time_payments_requests_for_payment/{real_time_payments_request_for_payment_id}/cancel",
                real_time_payments_request_for_payment_id=real_time_payments_request_for_payment_id,
            ),
            body=maybe_transform(
                {
                    "additional_information": additional_information,
                    "reason": reason,
                },
                real_time_payments_requests_for_payment_cancel_params.RealTimePaymentsRequestsForPaymentCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimePaymentsRequestForPayment,
        )


class AsyncRealTimePaymentsRequestsForPaymentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealTimePaymentsRequestsForPaymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRealTimePaymentsRequestsForPaymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealTimePaymentsRequestsForPaymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncRealTimePaymentsRequestsForPaymentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        debtor: real_time_payments_requests_for_payment_create_params.Debtor,
        debtor_account_number: str,
        debtor_routing_number: str,
        expires_at: Union[str, datetime],
        requested_execution_at: Union[str, datetime],
        unstructured_remittance_information: str,
        creditor_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsRequestForPayment:
        """
        Create a Real-Time Payments Request for Payment

        Args:
          account_number_id: The identifier of the Account Number where the funds will land.

          amount: The requested amount in USD cents. Must be positive.

          debtor: Details of the person being requested to pay.

          debtor_account_number: The debtor's account number, which the funds will be requested from.

          debtor_routing_number: The debtor's American Bankers' Association (ABA) Routing Transit Number (RTN).

          expires_at: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time after which
              the request for payment is no longer valid. After this time the debtor's bank
              should no longer allow the debtor to pay it. Must not be before
              `requested_execution_at`.

          requested_execution_at: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time by which
              you are requesting the payment to be made.

          unstructured_remittance_information: Unstructured information that will show on the recipient's bank statement.

          creditor_name: The name of the creditor requesting the payment. If not provided, defaults to
              the name of the account's entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/real_time_payments_requests_for_payment",
            body=await async_maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "debtor": debtor,
                    "debtor_account_number": debtor_account_number,
                    "debtor_routing_number": debtor_routing_number,
                    "expires_at": expires_at,
                    "requested_execution_at": requested_execution_at,
                    "unstructured_remittance_information": unstructured_remittance_information,
                    "creditor_name": creditor_name,
                },
                real_time_payments_requests_for_payment_create_params.RealTimePaymentsRequestsForPaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimePaymentsRequestForPayment,
        )

    async def retrieve(
        self,
        real_time_payments_request_for_payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealTimePaymentsRequestForPayment:
        """
        Retrieve a Real-Time Payments Request for Payment

        Args:
          real_time_payments_request_for_payment_id: The identifier of the Real-Time Payments Request for Payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not real_time_payments_request_for_payment_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_payments_request_for_payment_id` but received {real_time_payments_request_for_payment_id!r}"
            )
        return await self._get(
            path_template(
                "/real_time_payments_requests_for_payment/{real_time_payments_request_for_payment_id}",
                real_time_payments_request_for_payment_id=real_time_payments_request_for_payment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealTimePaymentsRequestForPayment,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: real_time_payments_requests_for_payment_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RealTimePaymentsRequestForPayment, AsyncPage[RealTimePaymentsRequestForPayment]]:
        """
        List Real-Time Payments Requests for Payment

        Args:
          account_id: Filter Real-Time Payments Requests for Payment to those destined to the
              specified Account.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

              Defaults to `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/real_time_payments_requests_for_payment",
            page=AsyncPage[RealTimePaymentsRequestForPayment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    real_time_payments_requests_for_payment_list_params.RealTimePaymentsRequestsForPaymentListParams,
                ),
            ),
            model=RealTimePaymentsRequestForPayment,
        )

    async def cancel(
        self,
        real_time_payments_request_for_payment_id: str,
        *,
        additional_information: str | Omit = omit,
        reason: Literal["requested_by_customer", "paid_by_other_means", "duplicate", "wrong_amount"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsRequestForPayment:
        """
        Cancels a Real-Time Payments Request for Payment that is still awaiting payment.

        Args:
          real_time_payments_request_for_payment_id: The identifier of the Real-Time Payments Request for Payment to cancel.

          additional_information: Additional information about the cancellation to pass on to the recipient bank.

          reason: The reason the request for payment is being canceled. Defaults to
              `requested_by_customer`.

              - `requested_by_customer` - The creditor no longer wants to be paid. Corresponds
                to the Real-Time Payments reason code `CUST`.
              - `paid_by_other_means` - The requested payment has already been made through
                another channel. Corresponds to the Real-Time Payments reason code `UPAY`.
              - `duplicate` - The request for payment duplicated another request for payment.
                Corresponds to the Real-Time Payments reason code `DUPL`.
              - `wrong_amount` - The request for payment was sent for the wrong amount.
                Corresponds to the Real-Time Payments reason code `AM09`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not real_time_payments_request_for_payment_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_payments_request_for_payment_id` but received {real_time_payments_request_for_payment_id!r}"
            )
        return await self._post(
            path_template(
                "/real_time_payments_requests_for_payment/{real_time_payments_request_for_payment_id}/cancel",
                real_time_payments_request_for_payment_id=real_time_payments_request_for_payment_id,
            ),
            body=await async_maybe_transform(
                {
                    "additional_information": additional_information,
                    "reason": reason,
                },
                real_time_payments_requests_for_payment_cancel_params.RealTimePaymentsRequestsForPaymentCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimePaymentsRequestForPayment,
        )


class RealTimePaymentsRequestsForPaymentResourceWithRawResponse:
    def __init__(self, real_time_payments_requests_for_payment: RealTimePaymentsRequestsForPaymentResource) -> None:
        self._real_time_payments_requests_for_payment = real_time_payments_requests_for_payment

        self.create = to_raw_response_wrapper(
            real_time_payments_requests_for_payment.create,
        )
        self.retrieve = to_raw_response_wrapper(
            real_time_payments_requests_for_payment.retrieve,
        )
        self.list = to_raw_response_wrapper(
            real_time_payments_requests_for_payment.list,
        )
        self.cancel = to_raw_response_wrapper(
            real_time_payments_requests_for_payment.cancel,
        )


class AsyncRealTimePaymentsRequestsForPaymentResourceWithRawResponse:
    def __init__(
        self, real_time_payments_requests_for_payment: AsyncRealTimePaymentsRequestsForPaymentResource
    ) -> None:
        self._real_time_payments_requests_for_payment = real_time_payments_requests_for_payment

        self.create = async_to_raw_response_wrapper(
            real_time_payments_requests_for_payment.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            real_time_payments_requests_for_payment.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            real_time_payments_requests_for_payment.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            real_time_payments_requests_for_payment.cancel,
        )


class RealTimePaymentsRequestsForPaymentResourceWithStreamingResponse:
    def __init__(self, real_time_payments_requests_for_payment: RealTimePaymentsRequestsForPaymentResource) -> None:
        self._real_time_payments_requests_for_payment = real_time_payments_requests_for_payment

        self.create = to_streamed_response_wrapper(
            real_time_payments_requests_for_payment.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            real_time_payments_requests_for_payment.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            real_time_payments_requests_for_payment.list,
        )
        self.cancel = to_streamed_response_wrapper(
            real_time_payments_requests_for_payment.cancel,
        )


class AsyncRealTimePaymentsRequestsForPaymentResourceWithStreamingResponse:
    def __init__(
        self, real_time_payments_requests_for_payment: AsyncRealTimePaymentsRequestsForPaymentResource
    ) -> None:
        self._real_time_payments_requests_for_payment = real_time_payments_requests_for_payment

        self.create = async_to_streamed_response_wrapper(
            real_time_payments_requests_for_payment.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            real_time_payments_requests_for_payment.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            real_time_payments_requests_for_payment.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            real_time_payments_requests_for_payment.cancel,
        )
