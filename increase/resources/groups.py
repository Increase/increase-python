# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.group import *
from .._base_client import make_request_options

__all__ = ["Groups", "AsyncGroups"]


class Groups(SyncAPIResource):
    def retrieve_details(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Group:
        """Returns details for the currently authenticated Group."""
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> Group:
        """Returns details for the currently authenticated Group."""
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            "/groups/current",
            options=options,
            cast_to=Group,
        )
