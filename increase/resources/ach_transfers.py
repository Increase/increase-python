# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ach_transfer import ACHTransfer
from ..types.ach_transfer_list_params import ACHTransferListParams
from ..types.ach_transfer_create_params import ACHTransferCreateParams

__all__ = ["ACHTransfers", "AsyncACHTransfers"]


class ACHTransfers(SyncAPIResource):
    def create(
        self,
        body: ACHTransferCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/ach_transfers",
            body=body,
            options=options,
            cast_to=ACHTransfer,
        )

    def retrieve(
        self,
        ach_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/ach_transfers/{ach_transfer_id}",
            options=options,
            cast_to=ACHTransfer,
        )

    def list(
        self,
        query: ACHTransferListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ACHTransfer]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/ach_transfers",
            page=SyncPage[ACHTransfer],
            options=options,
            model=ACHTransfer,
        )


class AsyncACHTransfers(AsyncAPIResource):
    async def create(
        self,
        body: ACHTransferCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/ach_transfers",
            body=body,
            options=options,
            cast_to=ACHTransfer,
        )

    async def retrieve(
        self,
        ach_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/ach_transfers/{ach_transfer_id}",
            options=options,
            cast_to=ACHTransfer,
        )

    def list(
        self,
        query: ACHTransferListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ACHTransfer, AsyncPage[ACHTransfer]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/ach_transfers",
            page=AsyncPage[ACHTransfer],
            options=options,
            model=ACHTransfer,
        )
