# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ach_prenotification import *
from ..types.ach_prenotification_list_params import ACHPrenotificationListParams
from ..types.ach_prenotification_create_params import ACHPrenotificationCreateParams

__all__ = ["ACHPrenotifications", "AsyncACHPrenotifications"]


class ACHPrenotifications(SyncAPIResource):
    def create(
        self,
        body: ACHPrenotificationCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> ACHPrenotification:
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/ach_prenotifications",
            body=body,
            options=options,
            cast_to=ACHPrenotification,
        )

    def retrieve(
        self,
        ach_prenotification_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> ACHPrenotification:
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/ach_prenotifications/{ach_prenotification_id}",
            options=options,
            cast_to=ACHPrenotification,
        )

    def list(
        self,
        query: ACHPrenotificationListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ACHPrenotification]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/ach_prenotifications",
            page=SyncPage[ACHPrenotification],
            query=query,
            options=options,
            model=ACHPrenotification,
        )


class AsyncACHPrenotifications(AsyncAPIResource):
    async def create(
        self,
        body: ACHPrenotificationCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> ACHPrenotification:
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/ach_prenotifications",
            body=body,
            options=options,
            cast_to=ACHPrenotification,
        )

    async def retrieve(
        self,
        ach_prenotification_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> ACHPrenotification:
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/ach_prenotifications/{ach_prenotification_id}",
            options=options,
            cast_to=ACHPrenotification,
        )

    def list(
        self,
        query: ACHPrenotificationListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ACHPrenotification, AsyncPage[ACHPrenotification]]:
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/ach_prenotifications",
            page=AsyncPage[ACHPrenotification],
            query=query,
            options=options,
            model=ACHPrenotification,
        )
