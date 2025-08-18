# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import wire_drawdown_request_list_params, wire_drawdown_request_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.wire_drawdown_request import WireDrawdownRequest

__all__ = ["WireDrawdownRequestsResource", "AsyncWireDrawdownRequestsResource"]


class WireDrawdownRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WireDrawdownRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return WireDrawdownRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WireDrawdownRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return WireDrawdownRequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        creditor_address: wire_drawdown_request_create_params.CreditorAddress,
        creditor_name: str,
        debtor_address: wire_drawdown_request_create_params.DebtorAddress,
        debtor_name: str,
        unstructured_remittance_information: str,
        debtor_account_number: str | NotGiven = NOT_GIVEN,
        debtor_external_account_id: str | NotGiven = NOT_GIVEN,
        debtor_routing_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireDrawdownRequest:
        """
        Create a Wire Drawdown Request

        Args:
          account_number_id: The Account Number to which the debtor should send funds.

          amount: The amount requested from the debtor, in USD cents.

          creditor_address: The creditor's address.

          creditor_name: The creditor's name.

          debtor_address: The debtor's address.

          debtor_name: The debtor's name.

          unstructured_remittance_information: Remittance information the debtor will see as part of the request.

          debtor_account_number: The debtor's account number.

          debtor_external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `debtor_account_number` and `debtor_routing_number` must be absent.

          debtor_routing_number: The debtor's routing number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/wire_drawdown_requests",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "creditor_address": creditor_address,
                    "creditor_name": creditor_name,
                    "debtor_address": debtor_address,
                    "debtor_name": debtor_name,
                    "unstructured_remittance_information": unstructured_remittance_information,
                    "debtor_account_number": debtor_account_number,
                    "debtor_external_account_id": debtor_external_account_id,
                    "debtor_routing_number": debtor_routing_number,
                },
                wire_drawdown_request_create_params.WireDrawdownRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireDrawdownRequest,
        )

    def retrieve(
        self,
        wire_drawdown_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WireDrawdownRequest:
        """
        Retrieve a Wire Drawdown Request

        Args:
          wire_drawdown_request_id: The identifier of the Wire Drawdown Request to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `wire_drawdown_request_id` but received {wire_drawdown_request_id!r}"
            )
        return self._get(
            f"/wire_drawdown_requests/{wire_drawdown_request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireDrawdownRequest,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: wire_drawdown_request_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[WireDrawdownRequest]:
        """
        List Wire Drawdown Requests

        Args:
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
            "/wire_drawdown_requests",
            page=SyncPage[WireDrawdownRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    wire_drawdown_request_list_params.WireDrawdownRequestListParams,
                ),
            ),
            model=WireDrawdownRequest,
        )


class AsyncWireDrawdownRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWireDrawdownRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWireDrawdownRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWireDrawdownRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncWireDrawdownRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        creditor_address: wire_drawdown_request_create_params.CreditorAddress,
        creditor_name: str,
        debtor_address: wire_drawdown_request_create_params.DebtorAddress,
        debtor_name: str,
        unstructured_remittance_information: str,
        debtor_account_number: str | NotGiven = NOT_GIVEN,
        debtor_external_account_id: str | NotGiven = NOT_GIVEN,
        debtor_routing_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireDrawdownRequest:
        """
        Create a Wire Drawdown Request

        Args:
          account_number_id: The Account Number to which the debtor should send funds.

          amount: The amount requested from the debtor, in USD cents.

          creditor_address: The creditor's address.

          creditor_name: The creditor's name.

          debtor_address: The debtor's address.

          debtor_name: The debtor's name.

          unstructured_remittance_information: Remittance information the debtor will see as part of the request.

          debtor_account_number: The debtor's account number.

          debtor_external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `debtor_account_number` and `debtor_routing_number` must be absent.

          debtor_routing_number: The debtor's routing number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/wire_drawdown_requests",
            body=await async_maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "creditor_address": creditor_address,
                    "creditor_name": creditor_name,
                    "debtor_address": debtor_address,
                    "debtor_name": debtor_name,
                    "unstructured_remittance_information": unstructured_remittance_information,
                    "debtor_account_number": debtor_account_number,
                    "debtor_external_account_id": debtor_external_account_id,
                    "debtor_routing_number": debtor_routing_number,
                },
                wire_drawdown_request_create_params.WireDrawdownRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireDrawdownRequest,
        )

    async def retrieve(
        self,
        wire_drawdown_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WireDrawdownRequest:
        """
        Retrieve a Wire Drawdown Request

        Args:
          wire_drawdown_request_id: The identifier of the Wire Drawdown Request to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `wire_drawdown_request_id` but received {wire_drawdown_request_id!r}"
            )
        return await self._get(
            f"/wire_drawdown_requests/{wire_drawdown_request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireDrawdownRequest,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: wire_drawdown_request_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WireDrawdownRequest, AsyncPage[WireDrawdownRequest]]:
        """
        List Wire Drawdown Requests

        Args:
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
            "/wire_drawdown_requests",
            page=AsyncPage[WireDrawdownRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    wire_drawdown_request_list_params.WireDrawdownRequestListParams,
                ),
            ),
            model=WireDrawdownRequest,
        )


class WireDrawdownRequestsResourceWithRawResponse:
    def __init__(self, wire_drawdown_requests: WireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.create = to_raw_response_wrapper(
            wire_drawdown_requests.create,
        )
        self.retrieve = to_raw_response_wrapper(
            wire_drawdown_requests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            wire_drawdown_requests.list,
        )


class AsyncWireDrawdownRequestsResourceWithRawResponse:
    def __init__(self, wire_drawdown_requests: AsyncWireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.create = async_to_raw_response_wrapper(
            wire_drawdown_requests.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            wire_drawdown_requests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            wire_drawdown_requests.list,
        )


class WireDrawdownRequestsResourceWithStreamingResponse:
    def __init__(self, wire_drawdown_requests: WireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.create = to_streamed_response_wrapper(
            wire_drawdown_requests.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            wire_drawdown_requests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            wire_drawdown_requests.list,
        )


class AsyncWireDrawdownRequestsResourceWithStreamingResponse:
    def __init__(self, wire_drawdown_requests: AsyncWireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.create = async_to_streamed_response_wrapper(
            wire_drawdown_requests.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            wire_drawdown_requests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            wire_drawdown_requests.list,
        )
