# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.transaction import *
from ..types.transaction_list_params import TransactionListParams

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    def retrieve(
        self,
        transaction_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Transaction:
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/transactions/{transaction_id}",
            options=options,
            cast_to=Transaction,
        )

    def list(
        self,
        query: TransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Transaction]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/transactions",
            page=SyncPage[Transaction],
            query=query,
            options=options,
            model=Transaction,
        )


class AsyncTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        transaction_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Transaction:
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/transactions/{transaction_id}",
            options=options,
            cast_to=Transaction,
        )

    def list(
        self,
        query: TransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/transactions",
            page=AsyncPage[Transaction],
            query=query,
            options=options,
            model=Transaction,
        )
