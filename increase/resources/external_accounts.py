# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.external_account import ExternalAccount
from ..types.external_account_list_params import ExternalAccountListParams
from ..types.external_account_create_params import ExternalAccountCreateParams
from ..types.external_account_update_params import ExternalAccountUpdateParams

__all__ = ["ExternalAccounts", "AsyncExternalAccounts"]


class ExternalAccounts(SyncAPIResource):
    def create(
        self,
        body: ExternalAccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/external_accounts",
            body=maybe_transform(body, ExternalAccountCreateParams),
            options=options,
            cast_to=ExternalAccount,
        )

    def retrieve(
        self,
        external_account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/external_accounts/{external_account_id}",
            options=options,
            cast_to=ExternalAccount,
        )

    def update(
        self,
        external_account_id: str,
        body: ExternalAccountUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/external_accounts/{external_account_id}",
            body=maybe_transform(body, ExternalAccountUpdateParams),
            options=options,
            cast_to=ExternalAccount,
        )

    def list(
        self,
        query: ExternalAccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ExternalAccount]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, ExternalAccountListParams))
        return self._get_api_list(
            "/external_accounts",
            page=SyncPage[ExternalAccount],
            options=options,
            model=ExternalAccount,
        )


class AsyncExternalAccounts(AsyncAPIResource):
    async def create(
        self,
        body: ExternalAccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/external_accounts",
            body=maybe_transform(body, ExternalAccountCreateParams),
            options=options,
            cast_to=ExternalAccount,
        )

    async def retrieve(
        self,
        external_account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/external_accounts/{external_account_id}",
            options=options,
            cast_to=ExternalAccount,
        )

    async def update(
        self,
        external_account_id: str,
        body: ExternalAccountUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ExternalAccount:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/external_accounts/{external_account_id}",
            body=maybe_transform(body, ExternalAccountUpdateParams),
            options=options,
            cast_to=ExternalAccount,
        )

    def list(
        self,
        query: ExternalAccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ExternalAccount, AsyncPage[ExternalAccount]]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, ExternalAccountListParams))
        return self._get_api_list(
            "/external_accounts",
            page=AsyncPage[ExternalAccount],
            options=options,
            model=ExternalAccount,
        )
