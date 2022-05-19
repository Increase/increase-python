# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.declined_transaction import *
from ..types.declined_transaction_list_params import DeclinedTransactionListParams

__all__ = ["DeclinedTransactions", "AsyncDeclinedTransactions"]


class DeclinedTransactions(SyncAPIResource):
    def retrieve(
        self,
        declined_transaction_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> DeclinedTransaction:
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/declined_transactions/{declined_transaction_id}",
            options=options,
            cast_to=DeclinedTransaction,
        )

    def list(
        self,
        query: DeclinedTransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[DeclinedTransaction]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/declined_transactions",
            page=SyncPage[DeclinedTransaction],
            query=query,
            options=options,
            model=DeclinedTransaction,
        )


class AsyncDeclinedTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        declined_transaction_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> DeclinedTransaction:
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/declined_transactions/{declined_transaction_id}",
            options=options,
            cast_to=DeclinedTransaction,
        )

    def list(
        self,
        query: DeclinedTransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[DeclinedTransaction, AsyncPage[DeclinedTransaction]]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/declined_transactions",
            page=AsyncPage[DeclinedTransaction],
            query=query,
            options=options,
            model=DeclinedTransaction,
        )
