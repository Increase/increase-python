# File generated from our OpenAPI spec by Stainless.

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ach_tranfer import ACHTranfer
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
    ) -> ACHTranfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/ach_transfers",
            body=body,
            options=options,
            cast_to=ACHTranfer,
        )

    def retrieve(
        self,
        ach_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTranfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/ach_transfers/{ach_transfer_id}",
            options=options,
            cast_to=ACHTranfer,
        )

    def list(
        self,
        query: ACHTransferListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ACHTranfer]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/ach_transfers",
            page=SyncPage[ACHTranfer],
            options=options,
            model=ACHTranfer,
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
    ) -> ACHTranfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/ach_transfers",
            body=body,
            options=options,
            cast_to=ACHTranfer,
        )

    async def retrieve(
        self,
        ach_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHTranfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/ach_transfers/{ach_transfer_id}",
            options=options,
            cast_to=ACHTranfer,
        )

    def list(
        self,
        query: ACHTransferListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ACHTranfer, AsyncPage[ACHTranfer]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/ach_transfers",
            page=AsyncPage[ACHTranfer],
            options=options,
            model=ACHTranfer,
        )
