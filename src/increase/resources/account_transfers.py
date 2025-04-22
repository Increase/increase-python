# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import account_transfer_list_params, account_transfer_create_params
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
from ..types.account_transfer import AccountTransfer

__all__ = ["AccountTransfersResource", "AsyncAccountTransfersResource"]


class AccountTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AccountTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AccountTransfersResourceWithStreamingResponse(self)

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not account_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `account_transfer_id` but received {account_transfer_id!r}"
            )
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
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[AccountTransfer]:
        """
        List Account Transfers

        Args:
          account_id: Filter Account Transfers to those that originated from the specified Account.

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
                        "idempotency_key": idempotency_key,
                        "limit": limit,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not account_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `account_transfer_id` but received {account_transfer_id!r}"
            )
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not account_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `account_transfer_id` but received {account_transfer_id!r}"
            )
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


class AsyncAccountTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncAccountTransfersResourceWithStreamingResponse(self)

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/account_transfers",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "description": description,
                    "destination_account_id": destination_account_id,
                    "require_approval": require_approval,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not account_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `account_transfer_id` but received {account_transfer_id!r}"
            )
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
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AccountTransfer, AsyncPage[AccountTransfer]]:
        """
        List Account Transfers

        Args:
          account_id: Filter Account Transfers to those that originated from the specified Account.

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
                        "idempotency_key": idempotency_key,
                        "limit": limit,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not account_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `account_transfer_id` but received {account_transfer_id!r}"
            )
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not account_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `account_transfer_id` but received {account_transfer_id!r}"
            )
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


class AccountTransfersResourceWithRawResponse:
    def __init__(self, account_transfers: AccountTransfersResource) -> None:
        self._account_transfers = account_transfers

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


class AsyncAccountTransfersResourceWithRawResponse:
    def __init__(self, account_transfers: AsyncAccountTransfersResource) -> None:
        self._account_transfers = account_transfers

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


class AccountTransfersResourceWithStreamingResponse:
    def __init__(self, account_transfers: AccountTransfersResource) -> None:
        self._account_transfers = account_transfers

        self.create = to_streamed_response_wrapper(
            account_transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            account_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            account_transfers.list,
        )
        self.approve = to_streamed_response_wrapper(
            account_transfers.approve,
        )
        self.cancel = to_streamed_response_wrapper(
            account_transfers.cancel,
        )


class AsyncAccountTransfersResourceWithStreamingResponse:
    def __init__(self, account_transfers: AsyncAccountTransfersResource) -> None:
        self._account_transfers = account_transfers

        self.create = async_to_streamed_response_wrapper(
            account_transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            account_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            account_transfers.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            account_transfers.approve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            account_transfers.cancel,
        )
