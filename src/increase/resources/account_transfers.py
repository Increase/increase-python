# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..types import (
    AccountTransfer,
    account_transfer_list_params,
    account_transfer_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import Increase, AsyncIncrease

__all__ = ["AccountTransfers", "AsyncAccountTransfers"]


class AccountTransfers(SyncAPIResource):
    with_raw_response: AccountTransfersWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = AccountTransfersWithRawResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        description: str,
        destination_account_id: str,
        require_approval: bool | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          unique_identifier: A unique identifier you choose for the transfer. Reusing this identifier for
              another transfer will result in an error. You can query for the transfer
              associated with this identifier using the List endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                    "unique_identifier": unique_identifier,
                },
                account_transfer_create_params.AccountTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AccountTransfer:
        """
        Retrieve an Account Transfer

        Args:
          account_transfer_id: The identifier of the Account Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/account_transfers/{account_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: account_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[AccountTransfer]:
        """
        List Account Transfers

        Args:
          account_id: Filter Account Transfers to those that originated from the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          unique_identifier: Filter Account Transfers to the one with the specified unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/account_transfers",
            page=SyncPage[AccountTransfer],
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
                        "unique_identifier": unique_identifier,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountTransfer:
        """
        Approve an Account Transfer

        Args:
          account_transfer_id: The identifier of the Account Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/account_transfers/{account_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountTransfer:
        """
        Cancel an Account Transfer

        Args:
          account_transfer_id: The identifier of the pending Account Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/account_transfers/{account_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountTransfer,
        )


class AsyncAccountTransfers(AsyncAPIResource):
    with_raw_response: AsyncAccountTransfersWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncAccountTransfersWithRawResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        description: str,
        destination_account_id: str,
        require_approval: bool | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          unique_identifier: A unique identifier you choose for the transfer. Reusing this identifier for
              another transfer will result in an error. You can query for the transfer
              associated with this identifier using the List endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                    "unique_identifier": unique_identifier,
                },
                account_transfer_create_params.AccountTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AccountTransfer:
        """
        Retrieve an Account Transfer

        Args:
          account_transfer_id: The identifier of the Account Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/account_transfers/{account_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: account_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AccountTransfer, AsyncPage[AccountTransfer]]:
        """
        List Account Transfers

        Args:
          account_id: Filter Account Transfers to those that originated from the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          unique_identifier: Filter Account Transfers to the one with the specified unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/account_transfers",
            page=AsyncPage[AccountTransfer],
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
                        "unique_identifier": unique_identifier,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountTransfer:
        """
        Approve an Account Transfer

        Args:
          account_transfer_id: The identifier of the Account Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/account_transfers/{account_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountTransfer:
        """
        Cancel an Account Transfer

        Args:
          account_transfer_id: The identifier of the pending Account Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/account_transfers/{account_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountTransfer,
        )


class AccountTransfersWithRawResponse:
    def __init__(self, account_transfers: AccountTransfers) -> None:
        self.create = to_raw_response_wrapper(
            account_transfers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            account_transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            account_transfers.list,
        )
        self.approve = to_raw_response_wrapper(
            account_transfers.approve,
        )
        self.cancel = to_raw_response_wrapper(
            account_transfers.cancel,
        )


class AsyncAccountTransfersWithRawResponse:
    def __init__(self, account_transfers: AsyncAccountTransfers) -> None:
        self.create = async_to_raw_response_wrapper(
            account_transfers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            account_transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            account_transfers.list,
        )
        self.approve = async_to_raw_response_wrapper(
            account_transfers.approve,
        )
        self.cancel = async_to_raw_response_wrapper(
            account_transfers.cancel,
        )
