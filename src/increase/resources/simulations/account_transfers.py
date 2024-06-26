# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.account_transfer import AccountTransfer

__all__ = ["AccountTransfers", "AsyncAccountTransfers"]


class AccountTransfers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountTransfersWithRawResponse:
        return AccountTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountTransfersWithStreamingResponse:
        return AccountTransfersWithStreamingResponse(self)

    def complete(
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
        If your account is configured to require approval for each transfer, this
        endpoint simulates the approval of an [Account Transfer](#account-transfers).
        You can also approve sandbox Account Transfers in the dashboard. This transfer
        must first have a `status` of `pending_approval`.

        Args:
          account_transfer_id: The identifier of the Account Transfer you wish to complete.

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
            f"/simulations/account_transfers/{account_transfer_id}/complete",
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
    @cached_property
    def with_raw_response(self) -> AsyncAccountTransfersWithRawResponse:
        return AsyncAccountTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountTransfersWithStreamingResponse:
        return AsyncAccountTransfersWithStreamingResponse(self)

    async def complete(
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
        If your account is configured to require approval for each transfer, this
        endpoint simulates the approval of an [Account Transfer](#account-transfers).
        You can also approve sandbox Account Transfers in the dashboard. This transfer
        must first have a `status` of `pending_approval`.

        Args:
          account_transfer_id: The identifier of the Account Transfer you wish to complete.

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
            f"/simulations/account_transfers/{account_transfer_id}/complete",
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
        self._account_transfers = account_transfers

        self.complete = _legacy_response.to_raw_response_wrapper(
            account_transfers.complete,
        )


class AsyncAccountTransfersWithRawResponse:
    def __init__(self, account_transfers: AsyncAccountTransfers) -> None:
        self._account_transfers = account_transfers

        self.complete = _legacy_response.async_to_raw_response_wrapper(
            account_transfers.complete,
        )


class AccountTransfersWithStreamingResponse:
    def __init__(self, account_transfers: AccountTransfers) -> None:
        self._account_transfers = account_transfers

        self.complete = to_streamed_response_wrapper(
            account_transfers.complete,
        )


class AsyncAccountTransfersWithStreamingResponse:
    def __init__(self, account_transfers: AsyncAccountTransfers) -> None:
        self._account_transfers = account_transfers

        self.complete = async_to_streamed_response_wrapper(
            account_transfers.complete,
        )
