# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account_number import *
from ..types.account_number_list_params import AccountNumberListParams
from ..types.account_number_create_params import AccountNumberCreateParams
from ..types.account_number_update_params import AccountNumberUpdateParams

__all__ = ["AccountNumbers", "AsyncAccountNumbers"]


class AccountNumbers(SyncAPIResource):
    def create(
        self,
        body: AccountNumberCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountNumber:
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/account_numbers",
            body=body,
            options=options,
            cast_to=AccountNumber,
        )

    def retrieve(
        self,
        account_number_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountNumber:
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/account_numbers/{account_number_id}",
            options=options,
            cast_to=AccountNumber,
        )

    def update(
        self,
        account_number_id: str,
        body: AccountNumberUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountNumber:
        options = make_request_options(headers, max_retries, timeout)
        return self._patch(
            f"/account_numbers/{account_number_id}",
            body=body,
            options=options,
            cast_to=AccountNumber,
        )

    def list(
        self,
        query: AccountNumberListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[AccountNumber]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/account_numbers",
            page=SyncPage[AccountNumber],
            query=query,
            options=options,
            model=AccountNumber,
        )


class AsyncAccountNumbers(AsyncAPIResource):
    async def create(
        self,
        body: AccountNumberCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountNumber:
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/account_numbers",
            body=body,
            options=options,
            cast_to=AccountNumber,
        )

    async def retrieve(
        self,
        account_number_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountNumber:
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/account_numbers/{account_number_id}",
            options=options,
            cast_to=AccountNumber,
        )

    async def update(
        self,
        account_number_id: str,
        body: AccountNumberUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountNumber:
        options = make_request_options(headers, max_retries, timeout)
        return await self._patch(
            f"/account_numbers/{account_number_id}",
            body=body,
            options=options,
            cast_to=AccountNumber,
        )

    def list(
        self,
        query: AccountNumberListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[AccountNumber, AsyncPage[AccountNumber]]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/account_numbers",
            page=AsyncPage[AccountNumber],
            query=query,
            options=options,
            model=AccountNumber,
        )
