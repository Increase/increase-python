# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import check_transfer_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.check_transfer import CheckTransfer

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
        amount: int,
        message: str,
        recipient_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckTransfer:
        """
        Args:
          account_id: The identifier for the account that will send the transfer.

          address_line1: The street address of the check's destination.

          address_line2: The second line of the address of the check's destination.

          address_city: The city of the check's destination.

          address_state: The state of the check's destination.

          address_zip: The postal code of the check's destination.

          amount: The transfer amount in cents.

          message: The descriptor that will be printed on the check.

          recipient_name: The name that will be printed on the check.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/check_transfers",
            body={
                "account_id": account_id,
                "address_line1": address_line1,
                "address_line2": address_line2,
                "address_city": address_city,
                "address_state": address_state,
                "address_zip": address_zip,
                "amount": amount,
                "message": message,
                "recipient_name": recipient_name,
            },
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
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "created_at": created_at,
                },
            ),
            model=CheckTransfer,
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
        amount: int,
        message: str,
        recipient_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckTransfer:
        """
        Args:
          account_id: The identifier for the account that will send the transfer.

          address_line1: The street address of the check's destination.

          address_line2: The second line of the address of the check's destination.

          address_city: The city of the check's destination.

          address_state: The state of the check's destination.

          address_zip: The postal code of the check's destination.

          amount: The transfer amount in cents.

          message: The descriptor that will be printed on the check.

          recipient_name: The name that will be printed on the check.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/check_transfers",
            body={
                "account_id": account_id,
                "address_line1": address_line1,
                "address_line2": address_line2,
                "address_city": address_city,
                "address_state": address_state,
                "address_zip": address_zip,
                "amount": amount,
                "message": message,
                "recipient_name": recipient_name,
            },
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
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "created_at": created_at,
                },
            ),
            model=CheckTransfer,
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
        return await self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckTransfer,
        )
