# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    check_transfer_list_params,
    check_transfer_create_params,
    check_transfer_stop_payment_params,
)
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
from ..types.check_transfer import CheckTransfer

__all__ = ["CheckTransfers", "AsyncCheckTransfers"]


class CheckTransfers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckTransfersWithRawResponse:
        return CheckTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckTransfersWithStreamingResponse:
        return CheckTransfersWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        source_account_number_id: str,
        fulfillment_method: Literal["physical_check", "third_party"] | NotGiven = NOT_GIVEN,
        physical_check: check_transfer_create_params.PhysicalCheck | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        third_party: check_transfer_create_params.ThirdParty | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Create a Check Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          amount: The transfer amount in cents.

          source_account_number_id: The identifier of the Account Number from which to send the transfer and print
              on the check.

          fulfillment_method: Whether Increase will print and mail the check or if you will do it yourself.

              - `physical_check` - Increase will print and mail a physical check.
              - `third_party` - Increase will not print a check; you are responsible for
                printing and mailing a check with the provided account number, routing number,
                check number, and amount.

          physical_check: Details relating to the physical check that Increase will print and mail. This
              is required if `fulfillment_method` is equal to `physical_check`. It must not be
              included if any other `fulfillment_method` is provided.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          third_party: Details relating to the custom fulfillment you will perform. This is required if
              `fulfillment_method` is equal to `third_party`. It must not be included if any
              other `fulfillment_method` is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/check_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "source_account_number_id": source_account_number_id,
                    "fulfillment_method": fulfillment_method,
                    "physical_check": physical_check,
                    "require_approval": require_approval,
                    "third_party": third_party,
                },
                check_transfer_create_params.CheckTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )

    def retrieve(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckTransfer:
        """
        Retrieve a Check Transfer

        Args:
          check_transfer_id: The identifier of the Check Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return self._get(
            f"/check_transfers/{check_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: check_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CheckTransfer]:
        """
        List Check Transfers

        Args:
          account_id: Filter Check Transfers to those that originated from the specified Account.

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
            "/check_transfers",
            page=SyncPage[CheckTransfer],
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
                    check_transfer_list_params.CheckTransferListParams,
                ),
            ),
            model=CheckTransfer,
        )

    def approve(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Approve a Check Transfer

        Args:
          check_transfer_id: The identifier of the Check Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return self._post(
            f"/check_transfers/{check_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )

    def cancel(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Cancel a pending Check Transfer

        Args:
          check_transfer_id: The identifier of the pending Check Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return self._post(
            f"/check_transfers/{check_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )

    def stop_payment(
        self,
        check_transfer_id: str,
        *,
        reason: Literal["mail_delivery_failed", "not_authorized", "unknown"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Request a stop payment on a Check Transfer

        Args:
          check_transfer_id: The identifier of the Check Transfer.

          reason: The reason why this transfer should be stopped.

              - `mail_delivery_failed` - The check could not be delivered.
              - `not_authorized` - The check was not authorized.
              - `unknown` - The check was stopped for another reason.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            body=maybe_transform({"reason": reason}, check_transfer_stop_payment_params.CheckTransferStopPaymentParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )


class AsyncCheckTransfers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckTransfersWithRawResponse:
        return AsyncCheckTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckTransfersWithStreamingResponse:
        return AsyncCheckTransfersWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        source_account_number_id: str,
        fulfillment_method: Literal["physical_check", "third_party"] | NotGiven = NOT_GIVEN,
        physical_check: check_transfer_create_params.PhysicalCheck | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        third_party: check_transfer_create_params.ThirdParty | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Create a Check Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          amount: The transfer amount in cents.

          source_account_number_id: The identifier of the Account Number from which to send the transfer and print
              on the check.

          fulfillment_method: Whether Increase will print and mail the check or if you will do it yourself.

              - `physical_check` - Increase will print and mail a physical check.
              - `third_party` - Increase will not print a check; you are responsible for
                printing and mailing a check with the provided account number, routing number,
                check number, and amount.

          physical_check: Details relating to the physical check that Increase will print and mail. This
              is required if `fulfillment_method` is equal to `physical_check`. It must not be
              included if any other `fulfillment_method` is provided.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          third_party: Details relating to the custom fulfillment you will perform. This is required if
              `fulfillment_method` is equal to `third_party`. It must not be included if any
              other `fulfillment_method` is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/check_transfers",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "source_account_number_id": source_account_number_id,
                    "fulfillment_method": fulfillment_method,
                    "physical_check": physical_check,
                    "require_approval": require_approval,
                    "third_party": third_party,
                },
                check_transfer_create_params.CheckTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )

    async def retrieve(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckTransfer:
        """
        Retrieve a Check Transfer

        Args:
          check_transfer_id: The identifier of the Check Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return await self._get(
            f"/check_transfers/{check_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: check_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CheckTransfer, AsyncPage[CheckTransfer]]:
        """
        List Check Transfers

        Args:
          account_id: Filter Check Transfers to those that originated from the specified Account.

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
            "/check_transfers",
            page=AsyncPage[CheckTransfer],
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
                    check_transfer_list_params.CheckTransferListParams,
                ),
            ),
            model=CheckTransfer,
        )

    async def approve(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Approve a Check Transfer

        Args:
          check_transfer_id: The identifier of the Check Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return await self._post(
            f"/check_transfers/{check_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )

    async def cancel(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Cancel a pending Check Transfer

        Args:
          check_transfer_id: The identifier of the pending Check Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return await self._post(
            f"/check_transfers/{check_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )

    async def stop_payment(
        self,
        check_transfer_id: str,
        *,
        reason: Literal["mail_delivery_failed", "not_authorized", "unknown"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Request a stop payment on a Check Transfer

        Args:
          check_transfer_id: The identifier of the Check Transfer.

          reason: The reason why this transfer should be stopped.

              - `mail_delivery_failed` - The check could not be delivered.
              - `not_authorized` - The check was not authorized.
              - `unknown` - The check was stopped for another reason.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not check_transfer_id:
            raise ValueError(f"Expected a non-empty value for `check_transfer_id` but received {check_transfer_id!r}")
        return await self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            body=await async_maybe_transform(
                {"reason": reason}, check_transfer_stop_payment_params.CheckTransferStopPaymentParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )


class CheckTransfersWithRawResponse:
    def __init__(self, check_transfers: CheckTransfers) -> None:
        self._check_transfers = check_transfers

        self.create = _legacy_response.to_raw_response_wrapper(
            check_transfers.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            check_transfers.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            check_transfers.list,
        )
        self.approve = _legacy_response.to_raw_response_wrapper(
            check_transfers.approve,
        )
        self.cancel = _legacy_response.to_raw_response_wrapper(
            check_transfers.cancel,
        )
        self.stop_payment = _legacy_response.to_raw_response_wrapper(
            check_transfers.stop_payment,
        )


class AsyncCheckTransfersWithRawResponse:
    def __init__(self, check_transfers: AsyncCheckTransfers) -> None:
        self._check_transfers = check_transfers

        self.create = _legacy_response.async_to_raw_response_wrapper(
            check_transfers.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            check_transfers.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            check_transfers.list,
        )
        self.approve = _legacy_response.async_to_raw_response_wrapper(
            check_transfers.approve,
        )
        self.cancel = _legacy_response.async_to_raw_response_wrapper(
            check_transfers.cancel,
        )
        self.stop_payment = _legacy_response.async_to_raw_response_wrapper(
            check_transfers.stop_payment,
        )


class CheckTransfersWithStreamingResponse:
    def __init__(self, check_transfers: CheckTransfers) -> None:
        self._check_transfers = check_transfers

        self.create = to_streamed_response_wrapper(
            check_transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            check_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            check_transfers.list,
        )
        self.approve = to_streamed_response_wrapper(
            check_transfers.approve,
        )
        self.cancel = to_streamed_response_wrapper(
            check_transfers.cancel,
        )
        self.stop_payment = to_streamed_response_wrapper(
            check_transfers.stop_payment,
        )


class AsyncCheckTransfersWithStreamingResponse:
    def __init__(self, check_transfers: AsyncCheckTransfers) -> None:
        self._check_transfers = check_transfers

        self.create = async_to_streamed_response_wrapper(
            check_transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            check_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            check_transfers.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            check_transfers.approve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            check_transfers.cancel,
        )
        self.stop_payment = async_to_streamed_response_wrapper(
            check_transfers.stop_payment,
        )
