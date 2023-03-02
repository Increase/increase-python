# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import CheckDeposit
from ..._types import Body, Query, Headers
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

__all__ = ["CheckDeposits", "AsyncCheckDeposits"]


class CheckDeposits(SyncAPIResource):
    def reject(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckDeposit:
        """
        Simulates the rejection of a [Check Deposit](#check-deposits) by Increase due to
        factors like poor image quality. This Check Deposit must first have a `status`
        of `pending`.
        """
        return self._post(
            f"/simulations/check_deposits/{check_deposit_id}/reject",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckDeposit,
        )

    def return_(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckDeposit:
        """Simulates the return of a [Check Deposit](#check-deposits).

        This Check Deposit
        must first have a `status` of `submitted`.
        """
        return self._post(
            f"/simulations/check_deposits/{check_deposit_id}/return",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckDeposit,
        )

    def submit(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckDeposit:
        """
        Simulates the submission of a [Check Deposit](#check-deposits) to the Federal
        Reserve. This Check Deposit must first have a `status` of `pending`.
        """
        return self._post(
            f"/simulations/check_deposits/{check_deposit_id}/submit",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckDeposit,
        )


class AsyncCheckDeposits(AsyncAPIResource):
    async def reject(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckDeposit:
        """
        Simulates the rejection of a [Check Deposit](#check-deposits) by Increase due to
        factors like poor image quality. This Check Deposit must first have a `status`
        of `pending`.
        """
        return await self._post(
            f"/simulations/check_deposits/{check_deposit_id}/reject",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckDeposit,
        )

    async def return_(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckDeposit:
        """Simulates the return of a [Check Deposit](#check-deposits).

        This Check Deposit
        must first have a `status` of `submitted`.
        """
        return await self._post(
            f"/simulations/check_deposits/{check_deposit_id}/return",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckDeposit,
        )

    async def submit(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CheckDeposit:
        """
        Simulates the submission of a [Check Deposit](#check-deposits) to the Federal
        Reserve. This Check Deposit must first have a `status` of `pending`.
        """
        return await self._post(
            f"/simulations/check_deposits/{check_deposit_id}/submit",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CheckDeposit,
        )
