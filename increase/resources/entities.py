# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.entity import *
from ..types.entity_list_params import EntityListParams
from ..types.entity_create_person_params import EntityCreatePersonParams
from ..types.entity_create_corporation_params import EntityCreateCorporationParams

__all__ = ["Entities", "AsyncEntities"]


class Entities(SyncAPIResource):
    def retrieve(
        self,
        entity_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Entity:
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/entities/{entity_id}",
            options=options,
            cast_to=Entity,
        )

    def list(
        self,
        query: EntityListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Entity]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/entities",
            page=SyncPage[Entity],
            query=query,
            options=options,
            model=Entity,
        )

    def create_corporation(
        self,
        body: EntityCreateCorporationParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Entity:
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/entities/corporations",
            body=body,
            options=options,
            cast_to=Entity,
        )

    def create_person(
        self,
        body: EntityCreatePersonParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Entity:
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/entities/natural_people",
            body=body,
            options=options,
            cast_to=Entity,
        )


class AsyncEntities(AsyncAPIResource):
    async def retrieve(
        self,
        entity_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Entity:
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/entities/{entity_id}",
            options=options,
            cast_to=Entity,
        )

    def list(
        self,
        query: EntityListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Entity, AsyncPage[Entity]]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/entities",
            page=AsyncPage[Entity],
            query=query,
            options=options,
            model=Entity,
        )

    async def create_corporation(
        self,
        body: EntityCreateCorporationParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Entity:
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/entities/corporations",
            body=body,
            options=options,
            cast_to=Entity,
        )

    async def create_person(
        self,
        body: EntityCreatePersonParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Entity:
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/entities/natural_people",
            body=body,
            options=options,
            cast_to=Entity,
        )
