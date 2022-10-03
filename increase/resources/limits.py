# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.limit import Limit
from .._base_client import AsyncPaginator, make_request_options
from ..types.limit_list_params import LimitListParams
from ..types.limit_create_params import LimitCreateParams
from ..types.limit_update_params import LimitUpdateParams

__all__ = ["Limits", "AsyncLimits"]


class Limits(SyncAPIResource):
    def create(
        self,
        body: LimitCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Limit:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/limits",
            body=maybe_transform(body, LimitCreateParams),
            options=options,
            cast_to=Limit,
        )

    def retrieve(
        self,
        limit_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Limit:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/limits/{limit_id}",
            options=options,
            cast_to=Limit,
        )

    def update(
        self,
        limit_id: str,
        body: LimitUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Limit:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/limits/{limit_id}",
            body=maybe_transform(body, LimitUpdateParams),
            options=options,
            cast_to=Limit,
        )

    def list(
        self,
        query: LimitListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Limit]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, LimitListParams))
        return self._get_api_list(
            "/limits",
            page=SyncPage[Limit],
            options=options,
            model=Limit,
        )


class AsyncLimits(AsyncAPIResource):
    async def create(
        self,
        body: LimitCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Limit:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/limits",
            body=maybe_transform(body, LimitCreateParams),
            options=options,
            cast_to=Limit,
        )

    async def retrieve(
        self,
        limit_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Limit:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/limits/{limit_id}",
            options=options,
            cast_to=Limit,
        )

    async def update(
        self,
        limit_id: str,
        body: LimitUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Limit:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/limits/{limit_id}",
            body=maybe_transform(body, LimitUpdateParams),
            options=options,
            cast_to=Limit,
        )

    def list(
        self,
        query: LimitListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Limit, AsyncPage[Limit]]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, LimitListParams))
        return self._get_api_list(
            "/limits",
            page=AsyncPage[Limit],
            options=options,
            model=Limit,
        )
