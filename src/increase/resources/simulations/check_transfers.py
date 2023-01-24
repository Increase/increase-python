# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import CheckTransfer
from ..._types import Body, Query, Headers
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

__all__ = ["CheckTransfers", "AsyncCheckTransfers"]


class CheckTransfers(SyncAPIResource):
    def deposit(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckTransfer:
        """Simulates a [Check Transfer](#check-transfers) being deposited at a bank.

        This
        transfer must first have a `status` of `mailed`.
        """
        return self._post(
            f"/simulations/check_transfers/{check_transfer_id}/deposit",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckTransfer,
        )

    def mail(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckTransfer:
        """
        Simulates the mailing of a [Check Transfer](#check-transfers), which happens
        once per weekday in production but can be sped up in sandbox. This transfer must
        first have a `status` of `pending_approval` or `pending_submission`.
        """
        return self._post(
            f"/simulations/check_transfers/{check_transfer_id}/mail",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckTransfer,
        )


class AsyncCheckTransfers(AsyncAPIResource):
    async def deposit(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckTransfer:
        """Simulates a [Check Transfer](#check-transfers) being deposited at a bank.

        This
        transfer must first have a `status` of `mailed`.
        """
        return await self._post(
            f"/simulations/check_transfers/{check_transfer_id}/deposit",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckTransfer,
        )

    async def mail(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckTransfer:
        """
        Simulates the mailing of a [Check Transfer](#check-transfers), which happens
        once per weekday in production but can be sped up in sandbox. This transfer must
        first have a `status` of `pending_approval` or `pending_submission`.
        """
        return await self._post(
            f"/simulations/check_transfers/{check_transfer_id}/mail",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckTransfer,
        )
