# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account_transfer import AccountTransfer
from ..types.account_transfer_list_params import AccountTransferListParams
from ..types.account_transfer_create_params import AccountTransferCreateParams

__all__ = ["AccountTransfers", "AsyncAccountTransfers"]


class AccountTransfers(SyncAPIResource):
    def create(
        self,
        body: AccountTransferCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/account_transfers",
            body=maybe_transform(body, AccountTransferCreateParams),
            options=options,
            cast_to=AccountTransfer,
        )

    def retrieve(
        self,
        account_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/account_transfers/{account_transfer_id}",
            options=options,
            cast_to=AccountTransfer,
        )

    def list(
        self,
        query: AccountTransferListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[AccountTransfer]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, AccountTransferListParams))
        return self._get_api_list(
            "/account_transfers",
            page=SyncPage[AccountTransfer],
            options=options,
            model=AccountTransfer,
        )


class AsyncAccountTransfers(AsyncAPIResource):
    async def create(
        self,
        body: AccountTransferCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/account_transfers",
            body=maybe_transform(body, AccountTransferCreateParams),
            options=options,
            cast_to=AccountTransfer,
        )

    async def retrieve(
        self,
        account_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountTransfer:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/account_transfers/{account_transfer_id}",
            options=options,
            cast_to=AccountTransfer,
        )

    def list(
        self,
        query: AccountTransferListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[AccountTransfer, AsyncPage[AccountTransfer]]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, AccountTransferListParams))
        return self._get_api_list(
            "/account_transfers",
            page=AsyncPage[AccountTransfer],
            options=options,
            model=AccountTransfer,
        )
