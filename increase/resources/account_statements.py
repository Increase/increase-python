# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account_statement import AccountStatement
from ..types.account_statement_list_params import AccountStatementListParams

__all__ = ["AccountStatements", "AsyncAccountStatements"]


class AccountStatements(SyncAPIResource):
    def retrieve(
        self,
        account_statement_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountStatement:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/account_statements/{account_statement_id}",
            options=options,
            cast_to=AccountStatement,
        )

    def list(
        self,
        query: AccountStatementListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[AccountStatement]:
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, AccountStatementListParams)
        )
        return self._get_api_list(
            "/account_statements",
            page=SyncPage[AccountStatement],
            options=options,
            model=AccountStatement,
        )


class AsyncAccountStatements(AsyncAPIResource):
    async def retrieve(
        self,
        account_statement_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountStatement:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/account_statements/{account_statement_id}",
            options=options,
            cast_to=AccountStatement,
        )

    def list(
        self,
        query: AccountStatementListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[AccountStatement, AsyncPage[AccountStatement]]:
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, AccountStatementListParams)
        )
        return self._get_api_list(
            "/account_statements",
            page=AsyncPage[AccountStatement],
            options=options,
            model=AccountStatement,
        )
