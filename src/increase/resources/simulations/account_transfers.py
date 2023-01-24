# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import AccountTransfer
from ..._types import Body, Query, Headers
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

__all__ = ["AccountTransfers", "AsyncAccountTransfers"]


class AccountTransfers(SyncAPIResource):
    def complete(
        self,
        account_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountTransfer:
        """
        If your account is configured to require approval for each transfer, this
        endpoint simulates the approval of an [Account Transfer](#account-transfers).
        You can also approve sandbox Account Transfers in the dashboard. This transfer
        must first have a `status` of `pending_approval`.
        """
        return self._post(
            f"/simulations/account_transfers/{account_transfer_id}/complete",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountTransfer,
        )


class AsyncAccountTransfers(AsyncAPIResource):
    async def complete(
        self,
        account_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountTransfer:
        """
        If your account is configured to require approval for each transfer, this
        endpoint simulates the approval of an [Account Transfer](#account-transfers).
        You can also approve sandbox Account Transfers in the dashboard. This transfer
        must first have a `status` of `pending_approval`.
        """
        return await self._post(
            f"/simulations/account_transfers/{account_transfer_id}/complete",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountTransfer,
        )
