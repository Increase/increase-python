# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account import *
from ..types.account_list_params import AccountListParams
from ..types.account_create_params import AccountCreateParams

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    def create(
        self,
        body: AccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/accounts",
            body=body,
            options=options,
            cast_to=Account,
        )

    def retrieve(
        self,
        account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/accounts/{account_id}",
            options=options,
            cast_to=Account,
        )

    def list(
        self,
        query: AccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Account]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/accounts",
            page=SyncPage[Account],
            query=query,
            options=options,
            model=Account,
        )

    def close(
        self,
        account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            f"/accounts/{account_id}/close",
            options=options,
            cast_to=Account,
        )


class AsyncAccounts(AsyncAPIResource):
    async def create(
        self,
        body: AccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/accounts",
            body=body,
            options=options,
            cast_to=Account,
        )

    async def retrieve(
        self,
        account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/accounts/{account_id}",
            options=options,
            cast_to=Account,
        )

    def list(
        self,
        query: AccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Account, AsyncPage[Account]]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/accounts",
            page=AsyncPage[Account],
            query=query,
            options=options,
            model=Account,
        )

    async def close(
        self,
        account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/accounts/{account_id}/close",
            options=options,
            cast_to=Account,
        )
