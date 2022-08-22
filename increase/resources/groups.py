# File generated from our OpenAPI spec by Stainless.

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.group import Group
from .._base_client import make_request_options

__all__ = ["Groups", "AsyncGroups"]


class Groups(SyncAPIResource):
    def retrieve_details(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Group:
        """Returns details for the currently authenticated Group."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            "/groups/current",
            options=options,
            cast_to=Group,
        )


class AsyncGroups(AsyncAPIResource):
    async def retrieve_details(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Group:
        """Returns details for the currently authenticated Group."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            "/groups/current",
            options=options,
            cast_to=Group,
        )
