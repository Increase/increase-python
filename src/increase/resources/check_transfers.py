# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import (
    CheckTransfer,
    check_transfer_list_params,
    check_transfer_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["CheckTransfers", "AsyncCheckTransfers"]


class CheckTransfers(SyncAPIResource):
    def create(
        self,
        *,
        account_id: str,
        address_city: str,
        address_line1: str,
        address_state: str,
        address_zip: str,
        amount: int,
        message: str,
        recipient_name: str,
        address_line2: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        return_address: check_transfer_create_params.ReturnAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Create a Check Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          address_city: The city of the check's destination.

          address_line1: The street address of the check's destination.

          address_state: The state of the check's destination.

          address_zip: The postal code of the check's destination.

          amount: The transfer amount in cents.

          message: The descriptor that will be printed on the memo field on the check.

          recipient_name: The name that will be printed on the check.

          address_line2: The second line of the address of the check's destination.

          note: The descriptor that will be printed on the letter included with the check.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          return_address: The return address to be printed on the check. If omitted this will default to
              the address of the Entity of the Account used to make the Check Transfer.

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
                    "address_city": address_city,
                    "address_line1": address_line1,
                    "address_state": address_state,
                    "address_zip": address_zip,
                    "amount": amount,
                    "message": message,
                    "recipient_name": recipient_name,
                    "address_line2": address_line2,
                    "note": note,
                    "require_approval": require_approval,
                    "return_address": return_address,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CheckTransfer]:
        """
        List Check Transfers

        Args:
          account_id: Filter Check Transfers to those that originated from the specified Account.

          cursor: Return the page of entries after this one.

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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Request a stop payment on a Check Transfer

        Args:
          check_transfer_id: The identifier of the Check Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
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
    async def create(
        self,
        *,
        account_id: str,
        address_city: str,
        address_line1: str,
        address_state: str,
        address_zip: str,
        amount: int,
        message: str,
        recipient_name: str,
        address_line2: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        return_address: check_transfer_create_params.ReturnAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Create a Check Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          address_city: The city of the check's destination.

          address_line1: The street address of the check's destination.

          address_state: The state of the check's destination.

          address_zip: The postal code of the check's destination.

          amount: The transfer amount in cents.

          message: The descriptor that will be printed on the memo field on the check.

          recipient_name: The name that will be printed on the check.

          address_line2: The second line of the address of the check's destination.

          note: The descriptor that will be printed on the letter included with the check.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          return_address: The return address to be printed on the check. If omitted this will default to
              the address of the Entity of the Account used to make the Check Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/check_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "address_city": address_city,
                    "address_line1": address_line1,
                    "address_state": address_state,
                    "address_zip": address_zip,
                    "amount": amount,
                    "message": message,
                    "recipient_name": recipient_name,
                    "address_line2": address_line2,
                    "note": note,
                    "require_approval": require_approval,
                    "return_address": return_address,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CheckTransfer, AsyncPage[CheckTransfer]]:
        """
        List Check Transfers

        Args:
          account_id: Filter Check Transfers to those that originated from the specified Account.

          cursor: Return the page of entries after this one.

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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckTransfer:
        """
        Request a stop payment on a Check Transfer

        Args:
          check_transfer_id: The identifier of the Check Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckTransfer,
        )
