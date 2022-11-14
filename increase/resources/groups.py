# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal

from .._utils import extract_files, maybe_transform, required_args, deprecated_positional_args, deepcopy_minimal
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, UnknownResponse, FileTypes
from .._base_client import AsyncPaginator, make_request_options, strip_not_given
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import SyncAPIClient, AsyncAPIClient
from ..types import shared_params

from ..types.group import Group

__all__ = ["Groups", "AsyncGroups"]

class Groups(SyncAPIResource):

    def retrieve_details(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    # deprecated options params
    headers: Union[Headers, NotGiven] = NOT_GIVEN,
    max_retries: Union[int, NotGiven] = NOT_GIVEN,
    timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    query: Optional[Query] = None,) -> Group:
        """Returns details for the currently authenticated Group."""
        if query is not None:
          warnings.warn(
            "The `query` argument is deprecated. Please use `extra_query` instead",
            DeprecationWarning,
            stacklevel=3,
        )

        return self._get(
            "/groups/current",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, headers=headers, max_retries=max_retries, timeout=timeout, query=query),
            cast_to = Group,
        )

class AsyncGroups(AsyncAPIResource):

    async def retrieve_details(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    # deprecated options params
    headers: Union[Headers, NotGiven] = NOT_GIVEN,
    max_retries: Union[int, NotGiven] = NOT_GIVEN,
    timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    query: Optional[Query] = None,) -> Group:
        """Returns details for the currently authenticated Group."""
        if query is not None:
          warnings.warn(
            "The `query` argument is deprecated. Please use `extra_query` instead",
            DeprecationWarning,
            stacklevel=3,
        )

        return await self._get(
            "/groups/current",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, headers=headers, max_retries=max_retries, timeout=timeout, query=query),
            cast_to = Group,
        )