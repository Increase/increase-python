# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import (
    AccountTransfer,
    account_transfer_list_params,
    account_transfer_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["AccountTransfers", "AsyncAccountTransfers"]


class AccountTransfers(SyncAPIResource):
    def create(
        self,
        *,
        account_id: str,
        amount: int,
        description: str,
        destination_account_id: str,
        require_approval: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountTransfer:
        """
        Create an Account Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          amount: The transfer amount in the minor unit of the account currency. For dollars, for
              example, this is cents.

          description: The description you choose to give the transfer.

          destination_account_id: The identifier for the account that will receive the transfer.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/account_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "description": description,
                    "destination_account_id": destination_account_id,
                    "require_approval": require_approval,
                },
                account_transfer_create_params.AccountTransferCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountTransfer,
        )

    def retrieve(
        self,
        account_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountTransfer:
        """Retrieve an Account Transfer"""
        return self._get(
            f"/account_transfers/{account_transfer_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: account_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[AccountTransfer]:
        """
        List Account Transfers

        Args:
          account_id: Filter Account Transfers to those that originated from the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/account_transfers",
            page=SyncPage[AccountTransfer],
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
                    account_transfer_list_params.AccountTransferListParams,
                ),
            ),
            model=AccountTransfer,
        )

    def approve(
        self,
        account_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountTransfer:
        """Approve an Account Transfer"""
        return self._post(
            f"/account_transfers/{account_transfer_id}/approve",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountTransfer,
        )

    def cancel(
        self,
        account_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountTransfer:
        """Cancel an Account Transfer"""
        return self._post(
            f"/account_transfers/{account_transfer_id}/cancel",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountTransfer,
        )


class AsyncAccountTransfers(AsyncAPIResource):
    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        description: str,
        destination_account_id: str,
        require_approval: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountTransfer:
        """
        Create an Account Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          amount: The transfer amount in the minor unit of the account currency. For dollars, for
              example, this is cents.

          description: The description you choose to give the transfer.

          destination_account_id: The identifier for the account that will receive the transfer.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/account_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "description": description,
                    "destination_account_id": destination_account_id,
                    "require_approval": require_approval,
                },
                account_transfer_create_params.AccountTransferCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountTransfer,
        )

    async def retrieve(
        self,
        account_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountTransfer:
        """Retrieve an Account Transfer"""
        return await self._get(
            f"/account_transfers/{account_transfer_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: account_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[AccountTransfer, AsyncPage[AccountTransfer]]:
        """
        List Account Transfers

        Args:
          account_id: Filter Account Transfers to those that originated from the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/account_transfers",
            page=AsyncPage[AccountTransfer],
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
                    account_transfer_list_params.AccountTransferListParams,
                ),
            ),
            model=AccountTransfer,
        )

    async def approve(
        self,
        account_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountTransfer:
        """Approve an Account Transfer"""
        return await self._post(
            f"/account_transfers/{account_transfer_id}/approve",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountTransfer,
        )

    async def cancel(
        self,
        account_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountTransfer:
        """Cancel an Account Transfer"""
        return await self._post(
            f"/account_transfers/{account_transfer_id}/cancel",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountTransfer,
        )
