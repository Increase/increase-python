# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional

from ..._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.wire_transfer_simulation import WireTransferSimulation
from ...types.simulations.wire_transfer_create_inbound_params import (
    WireTransferCreateInboundParams,
)

if TYPE_CHECKING:
    pass

__all__ = ["WireTransfers", "AsyncWireTransfers"]


class WireTransfers(SyncAPIResource):
    def create_inbound(
        self,
        body: WireTransferCreateInboundParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransferSimulation:
        """Simulates an inbound Wire transfer to your account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/simulations/inbound_wire_transfers",
            body=body,
            options=options,
            cast_to=WireTransferSimulation,
        )


class AsyncWireTransfers(AsyncAPIResource):
    async def create_inbound(
        self,
        body: WireTransferCreateInboundParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransferSimulation:
        """Simulates an inbound Wire transfer to your account."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/simulations/inbound_wire_transfers",
            body=body,
            options=options,
            cast_to=WireTransferSimulation,
        )
