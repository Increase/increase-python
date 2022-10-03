# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from ..._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.ach_transfer import ACHTransfer
from ...types.simulations.ach_transfer_simulation import ACHTransferSimulation
from ...types.simulations.ach_transfer_create_inbound_params import (
    ACHTransferCreateInboundParams,
)

__all__ = ["ACHTransfers", "AsyncACHTransfers"]


class ACHTransfers(SyncAPIResource):
    def create_inbound(
        self,
        body: ACHTransferCreateInboundParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        The transfer may be either a credit or a debit depending on if the `amount` is
        positive or negative. This will result in either a Transaction or a Declined
        Transaction depending on if the transfer is allowed.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/simulations/inbound_ach_transfers",
            body=maybe_transform(body, ACHTransferCreateInboundParams),
            options=options,
            cast_to=ACHTransferSimulation,
        )

    def return_(
        self,
        ach_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTransfer:
        """
        Simulates the return of an ACH Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `submitted`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/return",
            options=options,
            cast_to=ACHTransfer,
        )

    def submit(
        self,
        ach_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTransfer:
        """Simulates the submission of an ACH Transfer to the Federal Reserve.

        This transfer must first have a `status` of `pending_approval` or
        `pending_submission`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/submit",
            options=options,
            cast_to=ACHTransfer,
        )


class AsyncACHTransfers(AsyncAPIResource):
    async def create_inbound(
        self,
        body: ACHTransferCreateInboundParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        The transfer may be either a credit or a debit depending on if the `amount` is
        positive or negative. This will result in either a Transaction or a Declined
        Transaction depending on if the transfer is allowed.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/simulations/inbound_ach_transfers",
            body=maybe_transform(body, ACHTransferCreateInboundParams),
            options=options,
            cast_to=ACHTransferSimulation,
        )

    async def return_(
        self,
        ach_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTransfer:
        """
        Simulates the return of an ACH Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `submitted`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/return",
            options=options,
            cast_to=ACHTransfer,
        )

    async def submit(
        self,
        ach_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTransfer:
        """Simulates the submission of an ACH Transfer to the Federal Reserve.

        This transfer must first have a `status` of `pending_approval` or
        `pending_submission`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/submit",
            options=options,
            cast_to=ACHTransfer,
        )
