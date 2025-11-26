# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import fednow_transfer_list_params, fednow_transfer_create_params
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
from ..types.fednow_transfer import FednowTransfer

__all__ = ["FednowTransfersResource", "AsyncFednowTransfersResource"]


class FednowTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FednowTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return FednowTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FednowTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return FednowTransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        creditor_name: str,
        debtor_name: str,
        source_account_number_id: str,
        unstructured_remittance_information: str,
        account_number: str | Omit = omit,
        creditor_address: fednow_transfer_create_params.CreditorAddress | Omit = omit,
        debtor_address: fednow_transfer_create_params.DebtorAddress | Omit = omit,
        external_account_id: str | Omit = omit,
        require_approval: bool | Omit = omit,
        routing_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FednowTransfer:
        """
        Create a FedNow Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          amount: The amount, in minor units, to send to the creditor.

          creditor_name: The creditor's name.

          debtor_name: The debtor's name.

          source_account_number_id: The Account Number to include in the transfer as the debtor's account number.

          unstructured_remittance_information: Unstructured remittance information to include in the transfer.

          account_number: The creditor's account number.

          creditor_address: The creditor's address.

          debtor_address: The debtor's address.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The creditor's bank account routing number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/fednow_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "creditor_name": creditor_name,
                    "debtor_name": debtor_name,
                    "source_account_number_id": source_account_number_id,
                    "unstructured_remittance_information": unstructured_remittance_information,
                    "account_number": account_number,
                    "creditor_address": creditor_address,
                    "debtor_address": debtor_address,
                    "external_account_id": external_account_id,
                    "require_approval": require_approval,
                    "routing_number": routing_number,
                },
                fednow_transfer_create_params.FednowTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FednowTransfer,
        )

    def retrieve(
        self,
        fednow_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FednowTransfer:
        """
        Retrieve a FedNow Transfer

        Args:
          fednow_transfer_id: The identifier of the FedNow Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fednow_transfer_id:
            raise ValueError(f"Expected a non-empty value for `fednow_transfer_id` but received {fednow_transfer_id!r}")
        return self._get(
            f"/fednow_transfers/{fednow_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FednowTransfer,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: fednow_transfer_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        external_account_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: fednow_transfer_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[FednowTransfer]:
        """
        List FedNow Transfers

        Args:
          account_id: Filter FedNow Transfers to those that originated from the specified Account.

          cursor: Return the page of entries after this one.

          external_account_id: Filter FedNow Transfers to those made to the specified External Account.

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
            "/fednow_transfers",
            page=SyncPage[FednowTransfer],
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
                        "status": status,
                    },
                    fednow_transfer_list_params.FednowTransferListParams,
                ),
            ),
            model=FednowTransfer,
        )

    def approve(
        self,
        fednow_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FednowTransfer:
        """
        Approve a FedNow Transfer

        Args:
          fednow_transfer_id: The identifier of the FedNow Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not fednow_transfer_id:
            raise ValueError(f"Expected a non-empty value for `fednow_transfer_id` but received {fednow_transfer_id!r}")
        return self._post(
            f"/fednow_transfers/{fednow_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FednowTransfer,
        )

    def cancel(
        self,
        fednow_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FednowTransfer:
        """
        Cancel a pending FedNow Transfer

        Args:
          fednow_transfer_id: The identifier of the pending FedNow Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not fednow_transfer_id:
            raise ValueError(f"Expected a non-empty value for `fednow_transfer_id` but received {fednow_transfer_id!r}")
        return self._post(
            f"/fednow_transfers/{fednow_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FednowTransfer,
        )


class AsyncFednowTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFednowTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFednowTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFednowTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncFednowTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        creditor_name: str,
        debtor_name: str,
        source_account_number_id: str,
        unstructured_remittance_information: str,
        account_number: str | Omit = omit,
        creditor_address: fednow_transfer_create_params.CreditorAddress | Omit = omit,
        debtor_address: fednow_transfer_create_params.DebtorAddress | Omit = omit,
        external_account_id: str | Omit = omit,
        require_approval: bool | Omit = omit,
        routing_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FednowTransfer:
        """
        Create a FedNow Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          amount: The amount, in minor units, to send to the creditor.

          creditor_name: The creditor's name.

          debtor_name: The debtor's name.

          source_account_number_id: The Account Number to include in the transfer as the debtor's account number.

          unstructured_remittance_information: Unstructured remittance information to include in the transfer.

          account_number: The creditor's account number.

          creditor_address: The creditor's address.

          debtor_address: The debtor's address.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The creditor's bank account routing number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/fednow_transfers",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "creditor_name": creditor_name,
                    "debtor_name": debtor_name,
                    "source_account_number_id": source_account_number_id,
                    "unstructured_remittance_information": unstructured_remittance_information,
                    "account_number": account_number,
                    "creditor_address": creditor_address,
                    "debtor_address": debtor_address,
                    "external_account_id": external_account_id,
                    "require_approval": require_approval,
                    "routing_number": routing_number,
                },
                fednow_transfer_create_params.FednowTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FednowTransfer,
        )

    async def retrieve(
        self,
        fednow_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FednowTransfer:
        """
        Retrieve a FedNow Transfer

        Args:
          fednow_transfer_id: The identifier of the FedNow Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fednow_transfer_id:
            raise ValueError(f"Expected a non-empty value for `fednow_transfer_id` but received {fednow_transfer_id!r}")
        return await self._get(
            f"/fednow_transfers/{fednow_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FednowTransfer,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: fednow_transfer_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        external_account_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: fednow_transfer_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FednowTransfer, AsyncPage[FednowTransfer]]:
        """
        List FedNow Transfers

        Args:
          account_id: Filter FedNow Transfers to those that originated from the specified Account.

          cursor: Return the page of entries after this one.

          external_account_id: Filter FedNow Transfers to those made to the specified External Account.

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
            "/fednow_transfers",
            page=AsyncPage[FednowTransfer],
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
                        "status": status,
                    },
                    fednow_transfer_list_params.FednowTransferListParams,
                ),
            ),
            model=FednowTransfer,
        )

    async def approve(
        self,
        fednow_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FednowTransfer:
        """
        Approve a FedNow Transfer

        Args:
          fednow_transfer_id: The identifier of the FedNow Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not fednow_transfer_id:
            raise ValueError(f"Expected a non-empty value for `fednow_transfer_id` but received {fednow_transfer_id!r}")
        return await self._post(
            f"/fednow_transfers/{fednow_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FednowTransfer,
        )

    async def cancel(
        self,
        fednow_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FednowTransfer:
        """
        Cancel a pending FedNow Transfer

        Args:
          fednow_transfer_id: The identifier of the pending FedNow Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not fednow_transfer_id:
            raise ValueError(f"Expected a non-empty value for `fednow_transfer_id` but received {fednow_transfer_id!r}")
        return await self._post(
            f"/fednow_transfers/{fednow_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FednowTransfer,
        )


class FednowTransfersResourceWithRawResponse:
    def __init__(self, fednow_transfers: FednowTransfersResource) -> None:
        self._fednow_transfers = fednow_transfers

        self.create = to_raw_response_wrapper(
            fednow_transfers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            fednow_transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            fednow_transfers.list,
        )
        self.approve = to_raw_response_wrapper(
            fednow_transfers.approve,
        )
        self.cancel = to_raw_response_wrapper(
            fednow_transfers.cancel,
        )


class AsyncFednowTransfersResourceWithRawResponse:
    def __init__(self, fednow_transfers: AsyncFednowTransfersResource) -> None:
        self._fednow_transfers = fednow_transfers

        self.create = async_to_raw_response_wrapper(
            fednow_transfers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            fednow_transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            fednow_transfers.list,
        )
        self.approve = async_to_raw_response_wrapper(
            fednow_transfers.approve,
        )
        self.cancel = async_to_raw_response_wrapper(
            fednow_transfers.cancel,
        )


class FednowTransfersResourceWithStreamingResponse:
    def __init__(self, fednow_transfers: FednowTransfersResource) -> None:
        self._fednow_transfers = fednow_transfers

        self.create = to_streamed_response_wrapper(
            fednow_transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            fednow_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            fednow_transfers.list,
        )
        self.approve = to_streamed_response_wrapper(
            fednow_transfers.approve,
        )
        self.cancel = to_streamed_response_wrapper(
            fednow_transfers.cancel,
        )


class AsyncFednowTransfersResourceWithStreamingResponse:
    def __init__(self, fednow_transfers: AsyncFednowTransfersResource) -> None:
        self._fednow_transfers = fednow_transfers

        self.create = async_to_streamed_response_wrapper(
            fednow_transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            fednow_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            fednow_transfers.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            fednow_transfers.approve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            fednow_transfers.cancel,
        )
