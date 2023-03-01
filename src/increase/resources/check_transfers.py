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
        address_line1: str,
        address_line2: str | NotGiven = NOT_GIVEN,
        address_city: str,
        address_state: str,
        address_zip: str,
        return_address: check_transfer_create_params.ReturnAddress | NotGiven = NOT_GIVEN,
        amount: int,
        message: str,
        note: str | NotGiven = NOT_GIVEN,
        recipient_name: str,
        require_approval: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckTransfer:
        """
        Create a Check Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          address_line1: The street address of the check's destination.

          address_line2: The second line of the address of the check's destination.

          address_city: The city of the check's destination.

          address_state: The state of the check's destination.

          address_zip: The postal code of the check's destination.

          return_address: The return address to be printed on the check. If omitted this will default to
              the address of the Entity of the Account used to make the Check Transfer.

          amount: The transfer amount in cents.

          message: The descriptor that will be printed on the memo field on the check.

          note: The descriptor that will be printed on the letter included with the check.

          recipient_name: The name that will be printed on the check.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/check_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "address_line1": address_line1,
                    "address_line2": address_line2,
                    "address_city": address_city,
                    "address_state": address_state,
                    "address_zip": address_zip,
                    "return_address": return_address,
                    "amount": amount,
                    "message": message,
                    "note": note,
                    "recipient_name": recipient_name,
                    "require_approval": require_approval,
                },
                check_transfer_create_params.CheckTransferCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> CheckTransfer:
        """Retrieve a Check Transfer"""
        return self._get(
            f"/check_transfers/{check_transfer_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckTransfer,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: check_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[CheckTransfer]:
        """
        List Check Transfers

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Check Transfers to those that originated from the specified Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/check_transfers",
            page=SyncPage[CheckTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "account_id": account_id,
                        "created_at": created_at,
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
    ) -> CheckTransfer:
        """Approve a Check Transfer"""
        return self._post(
            f"/check_transfers/{check_transfer_id}/approve",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> CheckTransfer:
        """Cancel a pending Check Transfer"""
        return self._post(
            f"/check_transfers/{check_transfer_id}/cancel",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> CheckTransfer:
        """Request a stop payment on a Check Transfer"""
        return self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckTransfer,
        )


class AsyncCheckTransfers(AsyncAPIResource):
    async def create(
        self,
        *,
        account_id: str,
        address_line1: str,
        address_line2: str | NotGiven = NOT_GIVEN,
        address_city: str,
        address_state: str,
        address_zip: str,
        return_address: check_transfer_create_params.ReturnAddress | NotGiven = NOT_GIVEN,
        amount: int,
        message: str,
        note: str | NotGiven = NOT_GIVEN,
        recipient_name: str,
        require_approval: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckTransfer:
        """
        Create a Check Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          address_line1: The street address of the check's destination.

          address_line2: The second line of the address of the check's destination.

          address_city: The city of the check's destination.

          address_state: The state of the check's destination.

          address_zip: The postal code of the check's destination.

          return_address: The return address to be printed on the check. If omitted this will default to
              the address of the Entity of the Account used to make the Check Transfer.

          amount: The transfer amount in cents.

          message: The descriptor that will be printed on the memo field on the check.

          note: The descriptor that will be printed on the letter included with the check.

          recipient_name: The name that will be printed on the check.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/check_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "address_line1": address_line1,
                    "address_line2": address_line2,
                    "address_city": address_city,
                    "address_state": address_state,
                    "address_zip": address_zip,
                    "return_address": return_address,
                    "amount": amount,
                    "message": message,
                    "note": note,
                    "recipient_name": recipient_name,
                    "require_approval": require_approval,
                },
                check_transfer_create_params.CheckTransferCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> CheckTransfer:
        """Retrieve a Check Transfer"""
        return await self._get(
            f"/check_transfers/{check_transfer_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckTransfer,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: check_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[CheckTransfer, AsyncPage[CheckTransfer]]:
        """
        List Check Transfers

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Check Transfers to those that originated from the specified Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/check_transfers",
            page=AsyncPage[CheckTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "account_id": account_id,
                        "created_at": created_at,
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
    ) -> CheckTransfer:
        """Approve a Check Transfer"""
        return await self._post(
            f"/check_transfers/{check_transfer_id}/approve",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> CheckTransfer:
        """Cancel a pending Check Transfer"""
        return await self._post(
            f"/check_transfers/{check_transfer_id}/cancel",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> CheckTransfer:
        """Request a stop payment on a Check Transfer"""
        return await self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckTransfer,
        )
