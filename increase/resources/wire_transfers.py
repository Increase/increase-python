# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.wire_transfer import WireTransfer
from ..types.wire_transfer_list_params import WireTransferListParams
from ..types.wire_transfer_create_params import WireTransferCreateParams

__all__ = ["WireTransfers", "AsyncWireTransfers"]


class WireTransfers(SyncAPIResource):
    def create(
        self,
        body: WireTransferCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/wire_transfers",
            body=body,
            options=options,
            cast_to=WireTransfer,
        )

    def retrieve(
        self,
        wire_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/wire_transfers/{wire_transfer_id}",
            options=options,
            cast_to=WireTransfer,
        )

    def list(
        self,
        query: WireTransferListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[WireTransfer]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/wire_transfers",
            page=SyncPage[WireTransfer],
            options=options,
            model=WireTransfer,
        )

    def reverse(
        self,
        wire_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        """
        Simulates the reversal of an Wire Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `complete`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/reverse",
            options=options,
            cast_to=WireTransfer,
        )

    def submit(
        self,
        wire_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        """Simulates the submission of a Wire Transfer to the Federal Reserve.

        This transfer must first have a `status` of `pending_approval` or
        `pending_creating`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/submit",
            options=options,
            cast_to=WireTransfer,
        )


class AsyncWireTransfers(AsyncAPIResource):
    async def create(
        self,
        body: WireTransferCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/wire_transfers",
            body=body,
            options=options,
            cast_to=WireTransfer,
        )

    async def retrieve(
        self,
        wire_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/wire_transfers/{wire_transfer_id}",
            options=options,
            cast_to=WireTransfer,
        )

    def list(
        self,
        query: WireTransferListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[WireTransfer, AsyncPage[WireTransfer]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/wire_transfers",
            page=AsyncPage[WireTransfer],
            options=options,
            model=WireTransfer,
        )

    async def reverse(
        self,
        wire_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        """
        Simulates the reversal of an Wire Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `complete`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/reverse",
            options=options,
            cast_to=WireTransfer,
        )

    async def submit(
        self,
        wire_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        """Simulates the submission of a Wire Transfer to the Federal Reserve.

        This transfer must first have a `status` of `pending_approval` or
        `pending_creating`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/submit",
            options=options,
            cast_to=WireTransfer,
        )
