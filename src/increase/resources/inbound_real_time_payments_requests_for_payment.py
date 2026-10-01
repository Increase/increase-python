# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import inbound_real_time_payments_requests_for_payment_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.inbound_real_time_payments_request_for_payment import InboundRealTimePaymentsRequestForPayment

__all__ = [
    "InboundRealTimePaymentsRequestsForPaymentResource",
    "AsyncInboundRealTimePaymentsRequestsForPaymentResource",
]


class InboundRealTimePaymentsRequestsForPaymentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundRealTimePaymentsRequestsForPaymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundRealTimePaymentsRequestsForPaymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundRealTimePaymentsRequestsForPaymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundRealTimePaymentsRequestsForPaymentResourceWithStreamingResponse(self)

    def retrieve(
        self,
        inbound_real_time_payments_request_for_payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundRealTimePaymentsRequestForPayment:
        """
        Retrieve an Inbound Real-Time Payments Request for Payment

        Args:
          inbound_real_time_payments_request_for_payment_id: The identifier of the Inbound Real-Time Payments Request for Payment to get
              details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_real_time_payments_request_for_payment_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_real_time_payments_request_for_payment_id` but received {inbound_real_time_payments_request_for_payment_id!r}"
            )
        return self._get(
            path_template(
                "/inbound_real_time_payments_requests_for_payment/{inbound_real_time_payments_request_for_payment_id}",
                inbound_real_time_payments_request_for_payment_id=inbound_real_time_payments_request_for_payment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundRealTimePaymentsRequestForPayment,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        account_number_id: str | Omit = omit,
        created_at: inbound_real_time_payments_requests_for_payment_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[InboundRealTimePaymentsRequestForPayment]:
        """
        List Inbound Real-Time Payments Requests for Payment

        Args:
          account_id: Filter Inbound Real-Time Payments Requests for Payment to those belonging to the
              specified Account.

          account_number_id: Filter Inbound Real-Time Payments Requests for Payment to ones belonging to the
              specified Account Number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

              Defaults to `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_real_time_payments_requests_for_payment",
            page=SyncPage[InboundRealTimePaymentsRequestForPayment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "account_number_id": account_number_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    inbound_real_time_payments_requests_for_payment_list_params.InboundRealTimePaymentsRequestsForPaymentListParams,
                ),
            ),
            model=InboundRealTimePaymentsRequestForPayment,
        )


class AsyncInboundRealTimePaymentsRequestsForPaymentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundRealTimePaymentsRequestsForPaymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundRealTimePaymentsRequestsForPaymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundRealTimePaymentsRequestsForPaymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundRealTimePaymentsRequestsForPaymentResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        inbound_real_time_payments_request_for_payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundRealTimePaymentsRequestForPayment:
        """
        Retrieve an Inbound Real-Time Payments Request for Payment

        Args:
          inbound_real_time_payments_request_for_payment_id: The identifier of the Inbound Real-Time Payments Request for Payment to get
              details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_real_time_payments_request_for_payment_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_real_time_payments_request_for_payment_id` but received {inbound_real_time_payments_request_for_payment_id!r}"
            )
        return await self._get(
            path_template(
                "/inbound_real_time_payments_requests_for_payment/{inbound_real_time_payments_request_for_payment_id}",
                inbound_real_time_payments_request_for_payment_id=inbound_real_time_payments_request_for_payment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundRealTimePaymentsRequestForPayment,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        account_number_id: str | Omit = omit,
        created_at: inbound_real_time_payments_requests_for_payment_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InboundRealTimePaymentsRequestForPayment, AsyncPage[InboundRealTimePaymentsRequestForPayment]]:
        """
        List Inbound Real-Time Payments Requests for Payment

        Args:
          account_id: Filter Inbound Real-Time Payments Requests for Payment to those belonging to the
              specified Account.

          account_number_id: Filter Inbound Real-Time Payments Requests for Payment to ones belonging to the
              specified Account Number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

              Defaults to `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_real_time_payments_requests_for_payment",
            page=AsyncPage[InboundRealTimePaymentsRequestForPayment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "account_number_id": account_number_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    inbound_real_time_payments_requests_for_payment_list_params.InboundRealTimePaymentsRequestsForPaymentListParams,
                ),
            ),
            model=InboundRealTimePaymentsRequestForPayment,
        )


class InboundRealTimePaymentsRequestsForPaymentResourceWithRawResponse:
    def __init__(
        self, inbound_real_time_payments_requests_for_payment: InboundRealTimePaymentsRequestsForPaymentResource
    ) -> None:
        self._inbound_real_time_payments_requests_for_payment = inbound_real_time_payments_requests_for_payment

        self.retrieve = to_raw_response_wrapper(
            inbound_real_time_payments_requests_for_payment.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inbound_real_time_payments_requests_for_payment.list,
        )


class AsyncInboundRealTimePaymentsRequestsForPaymentResourceWithRawResponse:
    def __init__(
        self, inbound_real_time_payments_requests_for_payment: AsyncInboundRealTimePaymentsRequestsForPaymentResource
    ) -> None:
        self._inbound_real_time_payments_requests_for_payment = inbound_real_time_payments_requests_for_payment

        self.retrieve = async_to_raw_response_wrapper(
            inbound_real_time_payments_requests_for_payment.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inbound_real_time_payments_requests_for_payment.list,
        )


class InboundRealTimePaymentsRequestsForPaymentResourceWithStreamingResponse:
    def __init__(
        self, inbound_real_time_payments_requests_for_payment: InboundRealTimePaymentsRequestsForPaymentResource
    ) -> None:
        self._inbound_real_time_payments_requests_for_payment = inbound_real_time_payments_requests_for_payment

        self.retrieve = to_streamed_response_wrapper(
            inbound_real_time_payments_requests_for_payment.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inbound_real_time_payments_requests_for_payment.list,
        )


class AsyncInboundRealTimePaymentsRequestsForPaymentResourceWithStreamingResponse:
    def __init__(
        self, inbound_real_time_payments_requests_for_payment: AsyncInboundRealTimePaymentsRequestsForPaymentResource
    ) -> None:
        self._inbound_real_time_payments_requests_for_payment = inbound_real_time_payments_requests_for_payment

        self.retrieve = async_to_streamed_response_wrapper(
            inbound_real_time_payments_requests_for_payment.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_real_time_payments_requests_for_payment.list,
        )
