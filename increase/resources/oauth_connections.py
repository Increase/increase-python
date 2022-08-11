# File generated from our OpenAPI spec by Stainless.

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.oauth_connection import *
from ..types.oauth_connection_list_params import OauthConnectionListParams

__all__ = ["OauthConnections", "AsyncOauthConnections"]


class OauthConnections(SyncAPIResource):
    def retrieve(
        self,
        oauth_connection_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> OauthConnection:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/oauth_connections/{oauth_connection_id}",
            options=options,
            cast_to=OauthConnection,
        )

    def list(
        self,
        query: OauthConnectionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[OauthConnection]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/oauth_connections",
            page=SyncPage[OauthConnection],
            options=options,
            model=OauthConnection,
        )


class AsyncOauthConnections(AsyncAPIResource):
    async def retrieve(
        self,
        oauth_connection_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> OauthConnection:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/oauth_connections/{oauth_connection_id}",
            options=options,
            cast_to=OauthConnection,
        )

    def list(
        self,
        query: OauthConnectionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[OauthConnection, AsyncPage[OauthConnection]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/oauth_connections",
            page=AsyncPage[OauthConnection],
            options=options,
            model=OauthConnection,
        )
