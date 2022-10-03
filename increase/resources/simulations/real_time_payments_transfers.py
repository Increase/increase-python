# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from ..._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.real_time_payments_transfer_create_inbound_params import (
    RealTimePaymentsTransferCreateInboundParams,
)
from ...types.simulations.inbound_real_time_payments_transfer_simulation_result import (
    InboundRealTimePaymentsTransferSimulationResult,
)

__all__ = ["RealTimePaymentsTransfers", "AsyncRealTimePaymentsTransfers"]


class RealTimePaymentsTransfers(SyncAPIResource):
    def create_inbound(
        self,
        body: RealTimePaymentsTransferCreateInboundParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> InboundRealTimePaymentsTransferSimulationResult:
        """Simulates an inbound Real Time Payments transfer to your account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/simulations/inbound_real_time_payments_transfers",
            body=maybe_transform(body, RealTimePaymentsTransferCreateInboundParams),
            options=options,
            cast_to=InboundRealTimePaymentsTransferSimulationResult,
        )


class AsyncRealTimePaymentsTransfers(AsyncAPIResource):
    async def create_inbound(
        self,
        body: RealTimePaymentsTransferCreateInboundParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> InboundRealTimePaymentsTransferSimulationResult:
        """Simulates an inbound Real Time Payments transfer to your account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/simulations/inbound_real_time_payments_transfers",
            body=maybe_transform(body, RealTimePaymentsTransferCreateInboundParams),
            options=options,
            cast_to=InboundRealTimePaymentsTransferSimulationResult,
        )
