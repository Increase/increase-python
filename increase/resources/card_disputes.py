# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.card_dispute import CardDispute
from ..types.card_dispute_list_params import CardDisputeListParams
from ..types.card_dispute_create_params import CardDisputeCreateParams

__all__ = ["CardDisputes", "AsyncCardDisputes"]


class CardDisputes(SyncAPIResource):
    def create(
        self,
        body: CardDisputeCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CardDispute:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/card_disputes",
            body=body,
            options=options,
            cast_to=CardDispute,
        )

    def retrieve(
        self,
        card_dispute_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CardDispute:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/card_disputes/{card_dispute_id}",
            options=options,
            cast_to=CardDispute,
        )

    def list(
        self,
        query: CardDisputeListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[CardDispute]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/card_disputes",
            page=SyncPage[CardDispute],
            options=options,
            model=CardDispute,
        )


class AsyncCardDisputes(AsyncAPIResource):
    async def create(
        self,
        body: CardDisputeCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CardDispute:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/card_disputes",
            body=body,
            options=options,
            cast_to=CardDispute,
        )

    async def retrieve(
        self,
        card_dispute_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CardDispute:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/card_disputes/{card_dispute_id}",
            options=options,
            cast_to=CardDispute,
        )

    def list(
        self,
        query: CardDisputeListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[CardDispute, AsyncPage[CardDispute]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/card_disputes",
            page=AsyncPage[CardDispute],
            options=options,
            model=CardDispute,
        )
