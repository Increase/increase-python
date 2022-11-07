# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import wire_transfer_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.wire_transfer import WireTransfer

__all__ = ["WireTransfers", "AsyncWireTransfers"]


class WireTransfers(SyncAPIResource):
    def create(
        self,
        *,
        account_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        amount: int,
        message_to_recipient: str,
        beneficiary_name: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> WireTransfer:
        """
        Args:
          account_id: The identifier for the account that will send the transfer.

          account_number: The account number for the destination account.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          amount: The transfer amount in cents.

          message_to_recipient: The message that will show on the recipient's bank statement.

          beneficiary_name: The beneficiary's name.

          beneficiary_address_line1: The beneficiary's address line 1.

          beneficiary_address_line2: The beneficiary's address line 2.

          beneficiary_address_line3: The beneficiary's address line 3.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/wire_transfers",
            body={
                "account_id": account_id,
                "account_number": account_number,
                "routing_number": routing_number,
                "external_account_id": external_account_id,
                "amount": amount,
                "message_to_recipient": message_to_recipient,
                "beneficiary_name": beneficiary_name,
                "beneficiary_address_line1": beneficiary_address_line1,
                "beneficiary_address_line2": beneficiary_address_line2,
                "beneficiary_address_line3": beneficiary_address_line3,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> WireTransfer:
        return self._get(
            f"/wire_transfers/{wire_transfer_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=WireTransfer,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        created_at: wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[WireTransfer]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Wire Transfers to those belonging to the specified Account.

          external_account_id: Filter Wire Transfers to those made to the specified External Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/wire_transfers",
            page=SyncPage[WireTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "external_account_id": external_account_id,
                    "created_at": created_at,
                },
            ),
            model=WireTransfer,
        )

    def reverse(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> WireTransfer:
        """
        Simulates the reversal of an Wire Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `complete`.
        """
        return self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/reverse",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=WireTransfer,
        )

    def submit(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> WireTransfer:
        """Simulates the submission of a Wire Transfer to the Federal Reserve.

        This
        transfer must first have a `status` of `pending_approval` or `pending_creating`.
        """
        return self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/submit",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=WireTransfer,
        )


class AsyncWireTransfers(AsyncAPIResource):
    async def create(
        self,
        *,
        account_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        amount: int,
        message_to_recipient: str,
        beneficiary_name: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> WireTransfer:
        """
        Args:
          account_id: The identifier for the account that will send the transfer.

          account_number: The account number for the destination account.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          amount: The transfer amount in cents.

          message_to_recipient: The message that will show on the recipient's bank statement.

          beneficiary_name: The beneficiary's name.

          beneficiary_address_line1: The beneficiary's address line 1.

          beneficiary_address_line2: The beneficiary's address line 2.

          beneficiary_address_line3: The beneficiary's address line 3.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/wire_transfers",
            body={
                "account_id": account_id,
                "account_number": account_number,
                "routing_number": routing_number,
                "external_account_id": external_account_id,
                "amount": amount,
                "message_to_recipient": message_to_recipient,
                "beneficiary_name": beneficiary_name,
                "beneficiary_address_line1": beneficiary_address_line1,
                "beneficiary_address_line2": beneficiary_address_line2,
                "beneficiary_address_line3": beneficiary_address_line3,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> WireTransfer:
        return await self._get(
            f"/wire_transfers/{wire_transfer_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=WireTransfer,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        created_at: wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[WireTransfer, AsyncPage[WireTransfer]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Wire Transfers to those belonging to the specified Account.

          external_account_id: Filter Wire Transfers to those made to the specified External Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/wire_transfers",
            page=AsyncPage[WireTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "external_account_id": external_account_id,
                    "created_at": created_at,
                },
            ),
            model=WireTransfer,
        )

    async def reverse(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> WireTransfer:
        """
        Simulates the reversal of an Wire Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `complete`.
        """
        return await self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/reverse",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=WireTransfer,
        )

    async def submit(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> WireTransfer:
        """Simulates the submission of a Wire Transfer to the Federal Reserve.

        This
        transfer must first have a `status` of `pending_approval` or `pending_creating`.
        """
        return await self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/submit",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=WireTransfer,
        )
