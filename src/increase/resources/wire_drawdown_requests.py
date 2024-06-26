# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import wire_drawdown_request_list_params, wire_drawdown_request_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.wire_drawdown_request import WireDrawdownRequest

__all__ = ["WireDrawdownRequests", "AsyncWireDrawdownRequests"]


class WireDrawdownRequests(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WireDrawdownRequestsWithRawResponse:
        return WireDrawdownRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WireDrawdownRequestsWithStreamingResponse:
        return WireDrawdownRequestsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        message_to_recipient: str,
        recipient_account_number: str,
        recipient_name: str,
        recipient_routing_number: str,
        originator_address_line1: str | NotGiven = NOT_GIVEN,
        originator_address_line2: str | NotGiven = NOT_GIVEN,
        originator_address_line3: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        recipient_address_line1: str | NotGiven = NOT_GIVEN,
        recipient_address_line2: str | NotGiven = NOT_GIVEN,
        recipient_address_line3: str | NotGiven = NOT_GIVEN,
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
          account_number_id: The Account Number to which the recipient should send funds.

          amount: The amount requested from the recipient, in cents.

          message_to_recipient: A message the recipient will see as part of the request.

          recipient_account_number: The drawdown request's recipient's account number.

          recipient_name: The drawdown request's recipient's name.

          recipient_routing_number: The drawdown request's recipient's routing number.

          originator_address_line1: The drawdown request originator's address line 1. This is only necessary if
              you're requesting a payment to a commingled account. Otherwise, we'll use the
              associated entity's details.

          originator_address_line2: The drawdown request originator's address line 2. This is only necessary if
              you're requesting a payment to a commingled account. Otherwise, we'll use the
              associated entity's details.

          originator_address_line3: The drawdown request originator's address line 3. This is only necessary if
              you're requesting a payment to a commingled account. Otherwise, we'll use the
              associated entity's details.

          originator_name: The drawdown request originator's name. This is only necessary if you're
              requesting a payment to a commingled account. Otherwise, we'll use the
              associated entity's details.

          recipient_address_line1: Line 1 of the drawdown request's recipient's address.

          recipient_address_line2: Line 2 of the drawdown request's recipient's address.

          recipient_address_line3: Line 3 of the drawdown request's recipient's address.

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
                    "message_to_recipient": message_to_recipient,
                    "recipient_account_number": recipient_account_number,
                    "recipient_name": recipient_name,
                    "recipient_routing_number": recipient_routing_number,
                    "originator_address_line1": originator_address_line1,
                    "originator_address_line2": originator_address_line2,
                    "originator_address_line3": originator_address_line3,
                    "originator_name": originator_name,
                    "recipient_address_line1": recipient_address_line1,
                    "recipient_address_line2": recipient_address_line2,
                    "recipient_address_line3": recipient_address_line3,
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
        status: Literal["pending_submission", "pending_response", "fulfilled", "refused"] | NotGiven = NOT_GIVEN,
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

          status: Filter Wire Drawdown Requests for those with the specified status.

              - `pending_submission` - The drawdown request is queued to be submitted to
                Fedwire.
              - `pending_response` - The drawdown request has been sent and the recipient
                should respond in some way.
              - `fulfilled` - The drawdown request has been fulfilled by the recipient.
              - `refused` - The drawdown request has been refused by the recipient.

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


class AsyncWireDrawdownRequests(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWireDrawdownRequestsWithRawResponse:
        return AsyncWireDrawdownRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWireDrawdownRequestsWithStreamingResponse:
        return AsyncWireDrawdownRequestsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        message_to_recipient: str,
        recipient_account_number: str,
        recipient_name: str,
        recipient_routing_number: str,
        originator_address_line1: str | NotGiven = NOT_GIVEN,
        originator_address_line2: str | NotGiven = NOT_GIVEN,
        originator_address_line3: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        recipient_address_line1: str | NotGiven = NOT_GIVEN,
        recipient_address_line2: str | NotGiven = NOT_GIVEN,
        recipient_address_line3: str | NotGiven = NOT_GIVEN,
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
          account_number_id: The Account Number to which the recipient should send funds.

          amount: The amount requested from the recipient, in cents.

          message_to_recipient: A message the recipient will see as part of the request.

          recipient_account_number: The drawdown request's recipient's account number.

          recipient_name: The drawdown request's recipient's name.

          recipient_routing_number: The drawdown request's recipient's routing number.

          originator_address_line1: The drawdown request originator's address line 1. This is only necessary if
              you're requesting a payment to a commingled account. Otherwise, we'll use the
              associated entity's details.

          originator_address_line2: The drawdown request originator's address line 2. This is only necessary if
              you're requesting a payment to a commingled account. Otherwise, we'll use the
              associated entity's details.

          originator_address_line3: The drawdown request originator's address line 3. This is only necessary if
              you're requesting a payment to a commingled account. Otherwise, we'll use the
              associated entity's details.

          originator_name: The drawdown request originator's name. This is only necessary if you're
              requesting a payment to a commingled account. Otherwise, we'll use the
              associated entity's details.

          recipient_address_line1: Line 1 of the drawdown request's recipient's address.

          recipient_address_line2: Line 2 of the drawdown request's recipient's address.

          recipient_address_line3: Line 3 of the drawdown request's recipient's address.

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
                    "message_to_recipient": message_to_recipient,
                    "recipient_account_number": recipient_account_number,
                    "recipient_name": recipient_name,
                    "recipient_routing_number": recipient_routing_number,
                    "originator_address_line1": originator_address_line1,
                    "originator_address_line2": originator_address_line2,
                    "originator_address_line3": originator_address_line3,
                    "originator_name": originator_name,
                    "recipient_address_line1": recipient_address_line1,
                    "recipient_address_line2": recipient_address_line2,
                    "recipient_address_line3": recipient_address_line3,
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
        status: Literal["pending_submission", "pending_response", "fulfilled", "refused"] | NotGiven = NOT_GIVEN,
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

          status: Filter Wire Drawdown Requests for those with the specified status.

              - `pending_submission` - The drawdown request is queued to be submitted to
                Fedwire.
              - `pending_response` - The drawdown request has been sent and the recipient
                should respond in some way.
              - `fulfilled` - The drawdown request has been fulfilled by the recipient.
              - `refused` - The drawdown request has been refused by the recipient.

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


class WireDrawdownRequestsWithRawResponse:
    def __init__(self, wire_drawdown_requests: WireDrawdownRequests) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.create = _legacy_response.to_raw_response_wrapper(
            wire_drawdown_requests.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            wire_drawdown_requests.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            wire_drawdown_requests.list,
        )


class AsyncWireDrawdownRequestsWithRawResponse:
    def __init__(self, wire_drawdown_requests: AsyncWireDrawdownRequests) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.create = _legacy_response.async_to_raw_response_wrapper(
            wire_drawdown_requests.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            wire_drawdown_requests.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            wire_drawdown_requests.list,
        )


class WireDrawdownRequestsWithStreamingResponse:
    def __init__(self, wire_drawdown_requests: WireDrawdownRequests) -> None:
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


class AsyncWireDrawdownRequestsWithStreamingResponse:
    def __init__(self, wire_drawdown_requests: AsyncWireDrawdownRequests) -> None:
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
