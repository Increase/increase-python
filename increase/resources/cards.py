# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.card import *
from .._base_client import AsyncPaginator, make_request_options
from ..types.card_detail import *
from ..types.card_list_params import CardListParams
from ..types.card_create_params import CardCreateParams
from ..types.card_update_params import CardUpdateParams

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    def create(
        self,
        body: CardCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/cards",
            body=body,
            options=options,
            cast_to=Card,
        )

    def retrieve(
        self,
        card_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/cards/{card_id}",
            options=options,
            cast_to=Card,
        )

    def update(
        self,
        card_id: str,
        body: CardUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        options = make_request_options(headers, max_retries, timeout)
        return self._patch(
            f"/cards/{card_id}",
            body=body,
            options=options,
            cast_to=Card,
        )

    def list(
        self,
        query: CardListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Card]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/cards",
            page=SyncPage[Card],
            query=query,
            options=options,
            model=Card,
        )

    def retrieve_sensitive_details(
        self,
        card_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CardDetails:
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/cards/{card_id}/details",
            options=options,
            cast_to=CardDetails,
        )


class AsyncCards(AsyncAPIResource):
    async def create(
        self,
        body: CardCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/cards",
            body=body,
            options=options,
            cast_to=Card,
        )

    async def retrieve(
        self,
        card_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/cards/{card_id}",
            options=options,
            cast_to=Card,
        )

    async def update(
        self,
        card_id: str,
        body: CardUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        options = make_request_options(headers, max_retries, timeout)
        return await self._patch(
            f"/cards/{card_id}",
            body=body,
            options=options,
            cast_to=Card,
        )

    def list(
        self,
        query: CardListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Card, AsyncPage[Card]]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/cards",
            page=AsyncPage[Card],
            query=query,
            options=options,
            model=Card,
        )

    async def retrieve_sensitive_details(
        self,
        card_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CardDetails:
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/cards/{card_id}/details",
            options=options,
            cast_to=CardDetails,
        )
