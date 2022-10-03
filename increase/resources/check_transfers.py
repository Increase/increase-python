# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.check_transfer import CheckTransfer
from ..types.check_transfer_list_params import CheckTransferListParams
from ..types.check_transfer_create_params import CheckTransferCreateParams

__all__ = ["CheckTransfers", "AsyncCheckTransfers"]


class CheckTransfers(SyncAPIResource):
    def create(
        self,
        body: CheckTransferCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/check_transfers",
            body=maybe_transform(body, CheckTransferCreateParams),
            options=options,
            cast_to=CheckTransfer,
        )

    def retrieve(
        self,
        check_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/check_transfers/{check_transfer_id}",
            options=options,
            cast_to=CheckTransfer,
        )

    def list(
        self,
        query: CheckTransferListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[CheckTransfer]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, CheckTransferListParams))
        return self._get_api_list(
            "/check_transfers",
            page=SyncPage[CheckTransfer],
            options=options,
            model=CheckTransfer,
        )

    def stop_payment(
        self,
        check_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            options=options,
            cast_to=CheckTransfer,
        )


class AsyncCheckTransfers(AsyncAPIResource):
    async def create(
        self,
        body: CheckTransferCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/check_transfers",
            body=maybe_transform(body, CheckTransferCreateParams),
            options=options,
            cast_to=CheckTransfer,
        )

    async def retrieve(
        self,
        check_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/check_transfers/{check_transfer_id}",
            options=options,
            cast_to=CheckTransfer,
        )

    def list(
        self,
        query: CheckTransferListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[CheckTransfer, AsyncPage[CheckTransfer]]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, CheckTransferListParams))
        return self._get_api_list(
            "/check_transfers",
            page=AsyncPage[CheckTransfer],
            options=options,
            model=CheckTransfer,
        )

    async def stop_payment(
        self,
        check_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            options=options,
            cast_to=CheckTransfer,
        )
