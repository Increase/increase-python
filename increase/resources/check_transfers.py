# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.check_transfer import *
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
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/check_transfers",
            body=body,
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
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout)
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
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/check_transfers",
            page=SyncPage[CheckTransfer],
            query=query,
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
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/check_transfers",
            body=body,
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
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout)
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
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/check_transfers",
            page=AsyncPage[CheckTransfer],
            query=query,
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
    ) -> CheckTransfer:
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            options=options,
            cast_to=CheckTransfer,
        )
