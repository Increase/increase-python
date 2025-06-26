# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import wire_transfer_list_params, wire_transfer_create_params
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
from ..types.wire_transfer import WireTransfer

__all__ = ["WireTransfersResource", "AsyncWireTransfersResource"]


class WireTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WireTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return WireTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WireTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return WireTransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        beneficiary_name: str,
        message_to_recipient: str,
        account_number: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        inbound_wire_drawdown_request_id: str | NotGiven = NOT_GIVEN,
        originator_address_line1: str | NotGiven = NOT_GIVEN,
        originator_address_line2: str | NotGiven = NOT_GIVEN,
        originator_address_line3: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        source_account_number_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Create a Wire Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          amount: The transfer amount in USD cents.

          beneficiary_name: The beneficiary's name.

          message_to_recipient: The message that will show on the recipient's bank statement.

          account_number: The account number for the destination account.

          beneficiary_address_line1: The beneficiary's address line 1.

          beneficiary_address_line2: The beneficiary's address line 2.

          beneficiary_address_line3: The beneficiary's address line 3.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          inbound_wire_drawdown_request_id: The ID of an Inbound Wire Drawdown Request in response to which this transfer is
              being sent.

          originator_address_line1: The originator's address line 1. This is only necessary if you're transferring
              from a commingled account. Otherwise, we'll use the associated entity's details.

          originator_address_line2: The originator's address line 2. This is only necessary if you're transferring
              from a commingled account. Otherwise, we'll use the associated entity's details.

          originator_address_line3: The originator's address line 3. This is only necessary if you're transferring
              from a commingled account. Otherwise, we'll use the associated entity's details.

          originator_name: The originator's name. This is only necessary if you're transferring from a
              commingled account. Otherwise, we'll use the associated entity's details.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          source_account_number_id: The ID of an Account Number that will be passed to the wire's recipient

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/wire_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "beneficiary_name": beneficiary_name,
                    "message_to_recipient": message_to_recipient,
                    "account_number": account_number,
                    "beneficiary_address_line1": beneficiary_address_line1,
                    "beneficiary_address_line2": beneficiary_address_line2,
                    "beneficiary_address_line3": beneficiary_address_line3,
                    "external_account_id": external_account_id,
                    "inbound_wire_drawdown_request_id": inbound_wire_drawdown_request_id,
                    "originator_address_line1": originator_address_line1,
                    "originator_address_line2": originator_address_line2,
                    "originator_address_line3": originator_address_line3,
                    "originator_name": originator_name,
                    "require_approval": require_approval,
                    "routing_number": routing_number,
                    "source_account_number_id": source_account_number_id,
                },
                wire_transfer_create_params.WireTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    def retrieve(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WireTransfer:
        """
        Retrieve a Wire Transfer

        Args:
          wire_transfer_id: The identifier of the Wire Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wire_transfer_id:
            raise ValueError(f"Expected a non-empty value for `wire_transfer_id` but received {wire_transfer_id!r}")
        return self._get(
            f"/wire_transfers/{wire_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[WireTransfer]:
        """
        List Wire Transfers

        Args:
          account_id: Filter Wire Transfers to those belonging to the specified Account.

          cursor: Return the page of entries after this one.

          external_account_id: Filter Wire Transfers to those made to the specified External Account.

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
            "/wire_transfers",
            page=SyncPage[WireTransfer],
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
                        "external_account_id": external_account_id,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    wire_transfer_list_params.WireTransferListParams,
                ),
            ),
            model=WireTransfer,
        )

    def approve(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Approve a Wire Transfer

        Args:
          wire_transfer_id: The identifier of the Wire Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_transfer_id:
            raise ValueError(f"Expected a non-empty value for `wire_transfer_id` but received {wire_transfer_id!r}")
        return self._post(
            f"/wire_transfers/{wire_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    def cancel(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Cancel a pending Wire Transfer

        Args:
          wire_transfer_id: The identifier of the pending Wire Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_transfer_id:
            raise ValueError(f"Expected a non-empty value for `wire_transfer_id` but received {wire_transfer_id!r}")
        return self._post(
            f"/wire_transfers/{wire_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )


class AsyncWireTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWireTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWireTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWireTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncWireTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        beneficiary_name: str,
        message_to_recipient: str,
        account_number: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        inbound_wire_drawdown_request_id: str | NotGiven = NOT_GIVEN,
        originator_address_line1: str | NotGiven = NOT_GIVEN,
        originator_address_line2: str | NotGiven = NOT_GIVEN,
        originator_address_line3: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        source_account_number_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Create a Wire Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          amount: The transfer amount in USD cents.

          beneficiary_name: The beneficiary's name.

          message_to_recipient: The message that will show on the recipient's bank statement.

          account_number: The account number for the destination account.

          beneficiary_address_line1: The beneficiary's address line 1.

          beneficiary_address_line2: The beneficiary's address line 2.

          beneficiary_address_line3: The beneficiary's address line 3.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          inbound_wire_drawdown_request_id: The ID of an Inbound Wire Drawdown Request in response to which this transfer is
              being sent.

          originator_address_line1: The originator's address line 1. This is only necessary if you're transferring
              from a commingled account. Otherwise, we'll use the associated entity's details.

          originator_address_line2: The originator's address line 2. This is only necessary if you're transferring
              from a commingled account. Otherwise, we'll use the associated entity's details.

          originator_address_line3: The originator's address line 3. This is only necessary if you're transferring
              from a commingled account. Otherwise, we'll use the associated entity's details.

          originator_name: The originator's name. This is only necessary if you're transferring from a
              commingled account. Otherwise, we'll use the associated entity's details.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          source_account_number_id: The ID of an Account Number that will be passed to the wire's recipient

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/wire_transfers",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "beneficiary_name": beneficiary_name,
                    "message_to_recipient": message_to_recipient,
                    "account_number": account_number,
                    "beneficiary_address_line1": beneficiary_address_line1,
                    "beneficiary_address_line2": beneficiary_address_line2,
                    "beneficiary_address_line3": beneficiary_address_line3,
                    "external_account_id": external_account_id,
                    "inbound_wire_drawdown_request_id": inbound_wire_drawdown_request_id,
                    "originator_address_line1": originator_address_line1,
                    "originator_address_line2": originator_address_line2,
                    "originator_address_line3": originator_address_line3,
                    "originator_name": originator_name,
                    "require_approval": require_approval,
                    "routing_number": routing_number,
                    "source_account_number_id": source_account_number_id,
                },
                wire_transfer_create_params.WireTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    async def retrieve(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WireTransfer:
        """
        Retrieve a Wire Transfer

        Args:
          wire_transfer_id: The identifier of the Wire Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wire_transfer_id:
            raise ValueError(f"Expected a non-empty value for `wire_transfer_id` but received {wire_transfer_id!r}")
        return await self._get(
            f"/wire_transfers/{wire_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WireTransfer, AsyncPage[WireTransfer]]:
        """
        List Wire Transfers

        Args:
          account_id: Filter Wire Transfers to those belonging to the specified Account.

          cursor: Return the page of entries after this one.

          external_account_id: Filter Wire Transfers to those made to the specified External Account.

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
            "/wire_transfers",
            page=AsyncPage[WireTransfer],
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
                        "external_account_id": external_account_id,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    wire_transfer_list_params.WireTransferListParams,
                ),
            ),
            model=WireTransfer,
        )

    async def approve(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Approve a Wire Transfer

        Args:
          wire_transfer_id: The identifier of the Wire Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_transfer_id:
            raise ValueError(f"Expected a non-empty value for `wire_transfer_id` but received {wire_transfer_id!r}")
        return await self._post(
            f"/wire_transfers/{wire_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    async def cancel(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Cancel a pending Wire Transfer

        Args:
          wire_transfer_id: The identifier of the pending Wire Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_transfer_id:
            raise ValueError(f"Expected a non-empty value for `wire_transfer_id` but received {wire_transfer_id!r}")
        return await self._post(
            f"/wire_transfers/{wire_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )


class WireTransfersResourceWithRawResponse:
    def __init__(self, wire_transfers: WireTransfersResource) -> None:
        self._wire_transfers = wire_transfers

        self.create = to_raw_response_wrapper(
            wire_transfers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            wire_transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            wire_transfers.list,
        )
        self.approve = to_raw_response_wrapper(
            wire_transfers.approve,
        )
        self.cancel = to_raw_response_wrapper(
            wire_transfers.cancel,
        )


class AsyncWireTransfersResourceWithRawResponse:
    def __init__(self, wire_transfers: AsyncWireTransfersResource) -> None:
        self._wire_transfers = wire_transfers

        self.create = async_to_raw_response_wrapper(
            wire_transfers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            wire_transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            wire_transfers.list,
        )
        self.approve = async_to_raw_response_wrapper(
            wire_transfers.approve,
        )
        self.cancel = async_to_raw_response_wrapper(
            wire_transfers.cancel,
        )


class WireTransfersResourceWithStreamingResponse:
    def __init__(self, wire_transfers: WireTransfersResource) -> None:
        self._wire_transfers = wire_transfers

        self.create = to_streamed_response_wrapper(
            wire_transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            wire_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            wire_transfers.list,
        )
        self.approve = to_streamed_response_wrapper(
            wire_transfers.approve,
        )
        self.cancel = to_streamed_response_wrapper(
            wire_transfers.cancel,
        )


class AsyncWireTransfersResourceWithStreamingResponse:
    def __init__(self, wire_transfers: AsyncWireTransfersResource) -> None:
        self._wire_transfers = wire_transfers

        self.create = async_to_streamed_response_wrapper(
            wire_transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            wire_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            wire_transfers.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            wire_transfers.approve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            wire_transfers.cancel,
        )
