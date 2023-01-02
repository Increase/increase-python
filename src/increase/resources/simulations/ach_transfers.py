# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import Body, Query, Headers
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.ach_transfer import ACHTransfer
from ...types.simulations.ach_transfer_simulation import ACHTransferSimulation

__all__ = ["ACHTransfers", "AsyncACHTransfers"]


class ACHTransfers(SyncAPIResource):
    def create_inbound(
        self,
        *,
        account_number_id: str,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        The transfer may be either a
        credit or a debit depending on if the `amount` is positive or negative. This
        will result in either a Transaction or a Declined Transaction depending on if
        the transfer is allowed.

        Args:
          account_number_id: The identifier of the Account Number the inbound ACH Transfer is for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/simulations/inbound_ach_transfers",
            body={
                "account_number_id": account_number_id,
                "amount": amount,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ACHTransferSimulation,
        )

    def return_(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ACHTransfer:
        """
        Simulates the return of an ACH Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `submitted`.
        """
        return self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/return",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ACHTransfer,
        )

    def submit(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ACHTransfer:
        """Simulates the submission of an ACH Transfer to the Federal Reserve.

        This
        transfer must first have a `status` of `pending_approval` or
        `pending_submission`.
        """
        return self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/submit",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ACHTransfer,
        )


class AsyncACHTransfers(AsyncAPIResource):
    async def create_inbound(
        self,
        *,
        account_number_id: str,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        The transfer may be either a
        credit or a debit depending on if the `amount` is positive or negative. This
        will result in either a Transaction or a Declined Transaction depending on if
        the transfer is allowed.

        Args:
          account_number_id: The identifier of the Account Number the inbound ACH Transfer is for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/simulations/inbound_ach_transfers",
            body={
                "account_number_id": account_number_id,
                "amount": amount,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ACHTransferSimulation,
        )

    async def return_(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ACHTransfer:
        """
        Simulates the return of an ACH Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `submitted`.
        """
        return await self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/return",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ACHTransfer,
        )

    async def submit(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ACHTransfer:
        """Simulates the submission of an ACH Transfer to the Federal Reserve.

        This
        transfer must first have a `status` of `pending_approval` or
        `pending_submission`.
        """
        return await self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/submit",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ACHTransfer,
        )
