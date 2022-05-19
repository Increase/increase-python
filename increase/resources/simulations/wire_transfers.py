# File generated from our OpenAPI spec by Stainless.

from typing import Union

from ..._types import NOT_GIVEN, Headers, Timeout, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.wire_transfer_simulation import *
from ...types.simulations.wire_transfer_create_inbound_params import (
    WireTransferCreateInboundParams,
)

__all__ = ["WireTransfers", "AsyncWireTransfers"]


class WireTransfers(SyncAPIResource):
    def create_inbound(
        self,
        body: WireTransferCreateInboundParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> WireTransferSimulation:
        """Simulates an inbound Wire transfer to your account."""
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> WireTransferSimulation:
        """Simulates an inbound Wire transfer to your account."""
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/simulations/inbound_wire_transfers",
            body=body,
            options=options,
            cast_to=WireTransferSimulation,
        )
