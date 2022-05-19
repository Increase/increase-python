# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.event import *
from .._base_client import AsyncPaginator, make_request_options
from ..types.event_list_params import EventListParams

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    def retrieve(
        self,
        event_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Event:
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/events/{event_id}",
            options=options,
            cast_to=Event,
        )

    def list(
        self,
        query: EventListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Event]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/events",
            page=SyncPage[Event],
            query=query,
            options=options,
            model=Event,
        )


class AsyncEvents(AsyncAPIResource):
    async def retrieve(
        self,
        event_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Event:
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/events/{event_id}",
            options=options,
            cast_to=Event,
        )

    def list(
        self,
        query: EventListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Event, AsyncPage[Event]]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/events",
            page=AsyncPage[Event],
            query=query,
            options=options,
            model=Event,
        )
