# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import swift_transfer_list_params, swift_transfer_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.swift_transfer import SwiftTransfer

__all__ = ["SwiftTransfersResource", "AsyncSwiftTransfersResource"]


class SwiftTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SwiftTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return SwiftTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SwiftTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return SwiftTransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        account_number: str,
        bank_identification_code: str,
        creditor_address: swift_transfer_create_params.CreditorAddress,
        creditor_name: str,
        debtor_address: swift_transfer_create_params.DebtorAddress,
        debtor_name: str,
        instructed_amount: int,
        instructed_currency: Literal["USD"],
        source_account_number_id: str,
        unstructured_remittance_information: str,
        require_approval: bool | Omit = omit,
        routing_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SwiftTransfer:
        """
        Create a Swift Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          account_number: The creditor's account number.

          bank_identification_code: The bank identification code (BIC) of the creditor. If it ends with the
              three-character branch code, this must be 11 characters long. Otherwise this
              must be 8 characters and the branch code will be assumed to be `XXX`.

          creditor_address: The creditor's address.

          creditor_name: The creditor's name.

          debtor_address: The debtor's address.

          debtor_name: The debtor's name.

          instructed_amount: The amount, in minor units of `instructed_currency`, to send to the creditor.

          instructed_currency: The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of the
              instructed amount.

              - `USD` - United States Dollar

          source_account_number_id: The Account Number to include in the transfer as the debtor's account number.

          unstructured_remittance_information: Unstructured remittance information to include in the transfer.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The creditor's bank account routing or transit number. Required in certain
              countries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/swift_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "account_number": account_number,
                    "bank_identification_code": bank_identification_code,
                    "creditor_address": creditor_address,
                    "creditor_name": creditor_name,
                    "debtor_address": debtor_address,
                    "debtor_name": debtor_name,
                    "instructed_amount": instructed_amount,
                    "instructed_currency": instructed_currency,
                    "source_account_number_id": source_account_number_id,
                    "unstructured_remittance_information": unstructured_remittance_information,
                    "require_approval": require_approval,
                    "routing_number": routing_number,
                },
                swift_transfer_create_params.SwiftTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SwiftTransfer,
        )

    def retrieve(
        self,
        swift_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwiftTransfer:
        """
        Retrieve a Swift Transfer

        Args:
          swift_transfer_id: The identifier of the Swift Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not swift_transfer_id:
            raise ValueError(f"Expected a non-empty value for `swift_transfer_id` but received {swift_transfer_id!r}")
        return self._get(
            f"/swift_transfers/{swift_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwiftTransfer,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: swift_transfer_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: swift_transfer_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[SwiftTransfer]:
        """
        List Swift Transfers

        Args:
          account_id: Filter Swift Transfers to those that originated from the specified Account.

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
            "/swift_transfers",
            page=SyncPage[SwiftTransfer],
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
                        "status": status,
                    },
                    swift_transfer_list_params.SwiftTransferListParams,
                ),
            ),
            model=SwiftTransfer,
        )

    def approve(
        self,
        swift_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SwiftTransfer:
        """
        Approve a Swift Transfer

        Args:
          swift_transfer_id: The identifier of the Swift Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not swift_transfer_id:
            raise ValueError(f"Expected a non-empty value for `swift_transfer_id` but received {swift_transfer_id!r}")
        return self._post(
            f"/swift_transfers/{swift_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SwiftTransfer,
        )

    def cancel(
        self,
        swift_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SwiftTransfer:
        """
        Cancel a pending Swift Transfer

        Args:
          swift_transfer_id: The identifier of the pending Swift Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not swift_transfer_id:
            raise ValueError(f"Expected a non-empty value for `swift_transfer_id` but received {swift_transfer_id!r}")
        return self._post(
            f"/swift_transfers/{swift_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SwiftTransfer,
        )


class AsyncSwiftTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSwiftTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSwiftTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSwiftTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncSwiftTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        account_number: str,
        bank_identification_code: str,
        creditor_address: swift_transfer_create_params.CreditorAddress,
        creditor_name: str,
        debtor_address: swift_transfer_create_params.DebtorAddress,
        debtor_name: str,
        instructed_amount: int,
        instructed_currency: Literal["USD"],
        source_account_number_id: str,
        unstructured_remittance_information: str,
        require_approval: bool | Omit = omit,
        routing_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SwiftTransfer:
        """
        Create a Swift Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          account_number: The creditor's account number.

          bank_identification_code: The bank identification code (BIC) of the creditor. If it ends with the
              three-character branch code, this must be 11 characters long. Otherwise this
              must be 8 characters and the branch code will be assumed to be `XXX`.

          creditor_address: The creditor's address.

          creditor_name: The creditor's name.

          debtor_address: The debtor's address.

          debtor_name: The debtor's name.

          instructed_amount: The amount, in minor units of `instructed_currency`, to send to the creditor.

          instructed_currency: The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of the
              instructed amount.

              - `USD` - United States Dollar

          source_account_number_id: The Account Number to include in the transfer as the debtor's account number.

          unstructured_remittance_information: Unstructured remittance information to include in the transfer.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The creditor's bank account routing or transit number. Required in certain
              countries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/swift_transfers",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "account_number": account_number,
                    "bank_identification_code": bank_identification_code,
                    "creditor_address": creditor_address,
                    "creditor_name": creditor_name,
                    "debtor_address": debtor_address,
                    "debtor_name": debtor_name,
                    "instructed_amount": instructed_amount,
                    "instructed_currency": instructed_currency,
                    "source_account_number_id": source_account_number_id,
                    "unstructured_remittance_information": unstructured_remittance_information,
                    "require_approval": require_approval,
                    "routing_number": routing_number,
                },
                swift_transfer_create_params.SwiftTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SwiftTransfer,
        )

    async def retrieve(
        self,
        swift_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwiftTransfer:
        """
        Retrieve a Swift Transfer

        Args:
          swift_transfer_id: The identifier of the Swift Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not swift_transfer_id:
            raise ValueError(f"Expected a non-empty value for `swift_transfer_id` but received {swift_transfer_id!r}")
        return await self._get(
            f"/swift_transfers/{swift_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwiftTransfer,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: swift_transfer_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: swift_transfer_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SwiftTransfer, AsyncPage[SwiftTransfer]]:
        """
        List Swift Transfers

        Args:
          account_id: Filter Swift Transfers to those that originated from the specified Account.

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
            "/swift_transfers",
            page=AsyncPage[SwiftTransfer],
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
                        "status": status,
                    },
                    swift_transfer_list_params.SwiftTransferListParams,
                ),
            ),
            model=SwiftTransfer,
        )

    async def approve(
        self,
        swift_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SwiftTransfer:
        """
        Approve a Swift Transfer

        Args:
          swift_transfer_id: The identifier of the Swift Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not swift_transfer_id:
            raise ValueError(f"Expected a non-empty value for `swift_transfer_id` but received {swift_transfer_id!r}")
        return await self._post(
            f"/swift_transfers/{swift_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SwiftTransfer,
        )

    async def cancel(
        self,
        swift_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SwiftTransfer:
        """
        Cancel a pending Swift Transfer

        Args:
          swift_transfer_id: The identifier of the pending Swift Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not swift_transfer_id:
            raise ValueError(f"Expected a non-empty value for `swift_transfer_id` but received {swift_transfer_id!r}")
        return await self._post(
            f"/swift_transfers/{swift_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SwiftTransfer,
        )


class SwiftTransfersResourceWithRawResponse:
    def __init__(self, swift_transfers: SwiftTransfersResource) -> None:
        self._swift_transfers = swift_transfers

        self.create = to_raw_response_wrapper(
            swift_transfers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            swift_transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            swift_transfers.list,
        )
        self.approve = to_raw_response_wrapper(
            swift_transfers.approve,
        )
        self.cancel = to_raw_response_wrapper(
            swift_transfers.cancel,
        )


class AsyncSwiftTransfersResourceWithRawResponse:
    def __init__(self, swift_transfers: AsyncSwiftTransfersResource) -> None:
        self._swift_transfers = swift_transfers

        self.create = async_to_raw_response_wrapper(
            swift_transfers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            swift_transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            swift_transfers.list,
        )
        self.approve = async_to_raw_response_wrapper(
            swift_transfers.approve,
        )
        self.cancel = async_to_raw_response_wrapper(
            swift_transfers.cancel,
        )


class SwiftTransfersResourceWithStreamingResponse:
    def __init__(self, swift_transfers: SwiftTransfersResource) -> None:
        self._swift_transfers = swift_transfers

        self.create = to_streamed_response_wrapper(
            swift_transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            swift_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            swift_transfers.list,
        )
        self.approve = to_streamed_response_wrapper(
            swift_transfers.approve,
        )
        self.cancel = to_streamed_response_wrapper(
            swift_transfers.cancel,
        )


class AsyncSwiftTransfersResourceWithStreamingResponse:
    def __init__(self, swift_transfers: AsyncSwiftTransfersResource) -> None:
        self._swift_transfers = swift_transfers

        self.create = async_to_streamed_response_wrapper(
            swift_transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            swift_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            swift_transfers.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            swift_transfers.approve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            swift_transfers.cancel,
        )
