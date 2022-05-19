# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.pending_transaction import *
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
    ) -> PendingTransaction:
        options = make_request_options(headers, max_retries, timeout)
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
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/pending_transactions",
            page=SyncPage[PendingTransaction],
            query=query,
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
    ) -> PendingTransaction:
        options = make_request_options(headers, max_retries, timeout)
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
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/pending_transactions",
            page=AsyncPage[PendingTransaction],
            query=query,
            options=options,
            model=PendingTransaction,
        )
