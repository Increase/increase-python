# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ...types import AccountTransfer
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["AccountTransfers", "AsyncAccountTransfers"]


class AccountTransfers(SyncAPIResource):
    with_raw_response: AccountTransfersWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = AccountTransfersWithRawResponse(self)

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
    with_raw_response: AsyncAccountTransfersWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncAccountTransfersWithRawResponse(self)

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
        self.complete = to_raw_response_wrapper(
            account_transfers.complete,
        )


class AsyncAccountTransfersWithRawResponse:
    def __init__(self, account_transfers: AsyncAccountTransfers) -> None:
        self.complete = async_to_raw_response_wrapper(
            account_transfers.complete,
        )
