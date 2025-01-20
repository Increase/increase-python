# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import (
    real_time_payments_request_for_payment_list_params,
    real_time_payments_request_for_payment_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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

__all__ = ["RealTimePaymentsRequestForPaymentsResource", "AsyncRealTimePaymentsRequestForPaymentsResource"]


class RealTimePaymentsRequestForPaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealTimePaymentsRequestForPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return RealTimePaymentsRequestForPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealTimePaymentsRequestForPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return RealTimePaymentsRequestForPaymentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        debtor: real_time_payments_request_for_payment_create_params.Debtor,
        destination_account_number_id: str,
        expires_at: Union[str, date],
        remittance_information: str,
        source_account_number: str,
        source_routing_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsRequestForPayment:
        """
        Create a Real-Time Payments Request for Payment

        Args:
          amount: The requested amount in USD cents. Must be positive.

          debtor: Details of the person being requested to pay.

          destination_account_number_id: The identifier of the Account Number where the funds will land.

          expires_at: The expiration time for this request, in UTC. The requestee will not be able to
              pay after this date.

          remittance_information: Unstructured information that will show on the requestee's bank statement.

          source_account_number: The account number the funds will be requested from.

          source_routing_number: The requestee's American Bankers' Association (ABA) Routing Transit Number
              (RTN).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/real_time_payments_request_for_payments",
            body=maybe_transform(
                {
                    "amount": amount,
                    "debtor": debtor,
                    "destination_account_number_id": destination_account_number_id,
                    "expires_at": expires_at,
                    "remittance_information": remittance_information,
                    "source_account_number": source_account_number,
                    "source_routing_number": source_routing_number,
                },
                real_time_payments_request_for_payment_create_params.RealTimePaymentsRequestForPaymentCreateParams,
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
        request_for_payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealTimePaymentsRequestForPayment:
        """
        Retrieve a Real-Time Payments Request for Payment

        Args:
          request_for_payment_id: The identifier of the Real-Time Payments Request for Payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_for_payment_id:
            raise ValueError(
                f"Expected a non-empty value for `request_for_payment_id` but received {request_for_payment_id!r}"
            )
        return self._get(
            f"/real_time_payments_request_for_payments/{request_for_payment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealTimePaymentsRequestForPayment,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: real_time_payments_request_for_payment_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[RealTimePaymentsRequestForPayment]:
        """
        List Real-Time Payments Request for Payments

        Args:
          account_id: Filter Real-Time Payments Request for Payments to those destined to the
              specified Account.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/real_time_payments_request_for_payments",
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
                    real_time_payments_request_for_payment_list_params.RealTimePaymentsRequestForPaymentListParams,
                ),
            ),
            model=RealTimePaymentsRequestForPayment,
        )


class AsyncRealTimePaymentsRequestForPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealTimePaymentsRequestForPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRealTimePaymentsRequestForPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealTimePaymentsRequestForPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncRealTimePaymentsRequestForPaymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        debtor: real_time_payments_request_for_payment_create_params.Debtor,
        destination_account_number_id: str,
        expires_at: Union[str, date],
        remittance_information: str,
        source_account_number: str,
        source_routing_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsRequestForPayment:
        """
        Create a Real-Time Payments Request for Payment

        Args:
          amount: The requested amount in USD cents. Must be positive.

          debtor: Details of the person being requested to pay.

          destination_account_number_id: The identifier of the Account Number where the funds will land.

          expires_at: The expiration time for this request, in UTC. The requestee will not be able to
              pay after this date.

          remittance_information: Unstructured information that will show on the requestee's bank statement.

          source_account_number: The account number the funds will be requested from.

          source_routing_number: The requestee's American Bankers' Association (ABA) Routing Transit Number
              (RTN).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/real_time_payments_request_for_payments",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "debtor": debtor,
                    "destination_account_number_id": destination_account_number_id,
                    "expires_at": expires_at,
                    "remittance_information": remittance_information,
                    "source_account_number": source_account_number,
                    "source_routing_number": source_routing_number,
                },
                real_time_payments_request_for_payment_create_params.RealTimePaymentsRequestForPaymentCreateParams,
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
        request_for_payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealTimePaymentsRequestForPayment:
        """
        Retrieve a Real-Time Payments Request for Payment

        Args:
          request_for_payment_id: The identifier of the Real-Time Payments Request for Payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_for_payment_id:
            raise ValueError(
                f"Expected a non-empty value for `request_for_payment_id` but received {request_for_payment_id!r}"
            )
        return await self._get(
            f"/real_time_payments_request_for_payments/{request_for_payment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealTimePaymentsRequestForPayment,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: real_time_payments_request_for_payment_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RealTimePaymentsRequestForPayment, AsyncPage[RealTimePaymentsRequestForPayment]]:
        """
        List Real-Time Payments Request for Payments

        Args:
          account_id: Filter Real-Time Payments Request for Payments to those destined to the
              specified Account.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/real_time_payments_request_for_payments",
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
                    real_time_payments_request_for_payment_list_params.RealTimePaymentsRequestForPaymentListParams,
                ),
            ),
            model=RealTimePaymentsRequestForPayment,
        )


class RealTimePaymentsRequestForPaymentsResourceWithRawResponse:
    def __init__(self, real_time_payments_request_for_payments: RealTimePaymentsRequestForPaymentsResource) -> None:
        self._real_time_payments_request_for_payments = real_time_payments_request_for_payments

        self.create = to_raw_response_wrapper(
            real_time_payments_request_for_payments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            real_time_payments_request_for_payments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            real_time_payments_request_for_payments.list,
        )


class AsyncRealTimePaymentsRequestForPaymentsResourceWithRawResponse:
    def __init__(
        self, real_time_payments_request_for_payments: AsyncRealTimePaymentsRequestForPaymentsResource
    ) -> None:
        self._real_time_payments_request_for_payments = real_time_payments_request_for_payments

        self.create = async_to_raw_response_wrapper(
            real_time_payments_request_for_payments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            real_time_payments_request_for_payments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            real_time_payments_request_for_payments.list,
        )


class RealTimePaymentsRequestForPaymentsResourceWithStreamingResponse:
    def __init__(self, real_time_payments_request_for_payments: RealTimePaymentsRequestForPaymentsResource) -> None:
        self._real_time_payments_request_for_payments = real_time_payments_request_for_payments

        self.create = to_streamed_response_wrapper(
            real_time_payments_request_for_payments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            real_time_payments_request_for_payments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            real_time_payments_request_for_payments.list,
        )


class AsyncRealTimePaymentsRequestForPaymentsResourceWithStreamingResponse:
    def __init__(
        self, real_time_payments_request_for_payments: AsyncRealTimePaymentsRequestForPaymentsResource
    ) -> None:
        self._real_time_payments_request_for_payments = real_time_payments_request_for_payments

        self.create = async_to_streamed_response_wrapper(
            real_time_payments_request_for_payments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            real_time_payments_request_for_payments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            real_time_payments_request_for_payments.list,
        )
