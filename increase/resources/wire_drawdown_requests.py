# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.wire_drawdown_request import WireDrawdownRequest
from ..types.wire_drawdown_request_list_params import WireDrawdownRequestListParams
from ..types.wire_drawdown_request_create_params import WireDrawdownRequestCreateParams

__all__ = ["WireDrawdownRequests", "AsyncWireDrawdownRequests"]


class WireDrawdownRequests(SyncAPIResource):
    def create(
        self,
        body: WireDrawdownRequestCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireDrawdownRequest:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/wire_drawdown_requests",
            body=maybe_transform(body, WireDrawdownRequestCreateParams),
            options=options,
            cast_to=WireDrawdownRequest,
        )

    def retrieve(
        self,
        wire_drawdown_request_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireDrawdownRequest:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/wire_drawdown_requests/{wire_drawdown_request_id}",
            options=options,
            cast_to=WireDrawdownRequest,
        )

    def list(
        self,
        query: WireDrawdownRequestListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[WireDrawdownRequest]:
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, WireDrawdownRequestListParams)
        )
        return self._get_api_list(
            "/wire_drawdown_requests",
            page=SyncPage[WireDrawdownRequest],
            options=options,
            model=WireDrawdownRequest,
        )


class AsyncWireDrawdownRequests(AsyncAPIResource):
    async def create(
        self,
        body: WireDrawdownRequestCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireDrawdownRequest:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/wire_drawdown_requests",
            body=maybe_transform(body, WireDrawdownRequestCreateParams),
            options=options,
            cast_to=WireDrawdownRequest,
        )

    async def retrieve(
        self,
        wire_drawdown_request_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireDrawdownRequest:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/wire_drawdown_requests/{wire_drawdown_request_id}",
            options=options,
            cast_to=WireDrawdownRequest,
        )

    def list(
        self,
        query: WireDrawdownRequestListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[WireDrawdownRequest, AsyncPage[WireDrawdownRequest]]:
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, WireDrawdownRequestListParams)
        )
        return self._get_api_list(
            "/wire_drawdown_requests",
            page=AsyncPage[WireDrawdownRequest],
            options=options,
            model=WireDrawdownRequest,
        )
