# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..types import Group
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Increase, AsyncIncrease

__all__ = ["Groups", "AsyncGroups"]


class Groups(SyncAPIResource):
    with_raw_response: GroupsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = GroupsWithRawResponse(self)

    def retrieve_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Group:
        """Returns details for the currently authenticated Group."""
        return self._get(
            "/groups/current",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )


class AsyncGroups(AsyncAPIResource):
    with_raw_response: AsyncGroupsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncGroupsWithRawResponse(self)

    async def retrieve_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Group:
        """Returns details for the currently authenticated Group."""
        return await self._get(
            "/groups/current",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )


class GroupsWithRawResponse:
    def __init__(self, groups: Groups) -> None:
        self.retrieve_details = to_raw_response_wrapper(
            groups.retrieve_details,
        )


class AsyncGroupsWithRawResponse:
    def __init__(self, groups: AsyncGroups) -> None:
        self.retrieve_details = async_to_raw_response_wrapper(
            groups.retrieve_details,
        )
