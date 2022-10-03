# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.pending_transaction import PendingTransaction
from ..types.pending_transaction_list_params import PendingTransactionListParams

__all__ = ["PendingTransactions", "AsyncPendingTransactions"]


class PendingTransactions(SyncAPIResource):
    def retrieve(
        self,
        pending_transaction_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PendingTransaction:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/pending_transactions/{pending_transaction_id}",
            options=options,
            cast_to=PendingTransaction,
        )

    def list(
        self,
        query: PendingTransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[PendingTransaction]:
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, PendingTransactionListParams)
        )
        return self._get_api_list(
            "/pending_transactions",
            page=SyncPage[PendingTransaction],
            options=options,
            model=PendingTransaction,
        )


class AsyncPendingTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        pending_transaction_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PendingTransaction:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/pending_transactions/{pending_transaction_id}",
            options=options,
            cast_to=PendingTransaction,
        )

    def list(
        self,
        query: PendingTransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[PendingTransaction, AsyncPage[PendingTransaction]]:
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, PendingTransactionListParams)
        )
        return self._get_api_list(
            "/pending_transactions",
            page=AsyncPage[PendingTransaction],
            options=options,
            model=PendingTransaction,
        )
