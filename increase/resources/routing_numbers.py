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
from ..pagination import AsyncPage, SyncPage
from ..types.routing_number import RoutingNumber
from ..types import routing_number_list_params
from ..types.routing_number_list_params import RoutingNumberListParams

__all__ = ["RoutingNumbers", "AsyncRoutingNumbers"]

class RoutingNumbers(SyncAPIResource):

    @overload
    def list(self,
    *,
    cursor: str | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    routing_number: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    # deprecated options params
    headers: Union[Headers, NotGiven] = NOT_GIVEN,
    max_retries: Union[int, NotGiven] = NOT_GIVEN,
    timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,) -> SyncPage[RoutingNumber]:
        """
        You can use this API to confirm if a routing number is valid, such as when a
        user is providing you with bank account details. Since routing numbers uniquely
        identify a bank, this will always return 0 or 1 entry. In Sandbox, the only
        valid routing number for this method is 110000000.

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          routing_number: Filter financial institutions by routing number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(self,
    query: RoutingNumberListParams,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    # deprecated options params
    headers: Union[Headers, NotGiven] = NOT_GIVEN,
    max_retries: Union[int, NotGiven] = NOT_GIVEN,
    timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,) -> SyncPage[RoutingNumber]:
        """
        You can use this API to confirm if a routing number is valid, such as when a
        user is providing you with bank account details. Since routing numbers uniquely
        identify a bank, this will always return 0 or 1 entry. In Sandbox, the only
        valid routing number for this method is 110000000.
        """
        ...

    @required_args(["query"], ["routing_number"])
    def list(self,
    query: RoutingNumberListParams | None = None,
    *,
    cursor: str | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    routing_number: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    # deprecated options params
    headers: Union[Headers, NotGiven] = NOT_GIVEN,
    max_retries: Union[int, NotGiven] = NOT_GIVEN,
    timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,) -> SyncPage[RoutingNumber]:
        """
        You can use this API to confirm if a routing number is valid, such as when a
        user is providing you with bank account details. Since routing numbers uniquely
        identify a bank, this will always return 0 or 1 entry. In Sandbox, the only
        valid routing number for this method is 110000000.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          routing_number: Filter financial institutions by routing number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
          warnings.warn(
            "Passing parameters as a dictionary is deprecated and will be removed in the future",
            DeprecationWarning,
            stacklevel=2,
          )
        else:
          # cast to Any is required because the NotGiven types make this expression incompatible
          # with the standard RoutingNumberListParams type.
          query = cast(Any, {
            "cursor": cursor,
            "limit": limit,
            "routing_number": routing_number,
        })

        return self._get_api_list(
            "/routing_numbers",
            page = SyncPage[RoutingNumber],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, headers=headers, max_retries=max_retries, timeout=timeout, query=query),
            model = RoutingNumber,
        )

class AsyncRoutingNumbers(AsyncAPIResource):

    @overload
    def list(self,
    *,
    cursor: str | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    routing_number: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    # deprecated options params
    headers: Union[Headers, NotGiven] = NOT_GIVEN,
    max_retries: Union[int, NotGiven] = NOT_GIVEN,
    timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,) -> AsyncPaginator[RoutingNumber, AsyncPage[RoutingNumber]]:
        """
        You can use this API to confirm if a routing number is valid, such as when a
        user is providing you with bank account details. Since routing numbers uniquely
        identify a bank, this will always return 0 or 1 entry. In Sandbox, the only
        valid routing number for this method is 110000000.

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          routing_number: Filter financial institutions by routing number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(self,
    query: RoutingNumberListParams,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    # deprecated options params
    headers: Union[Headers, NotGiven] = NOT_GIVEN,
    max_retries: Union[int, NotGiven] = NOT_GIVEN,
    timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,) -> AsyncPaginator[RoutingNumber, AsyncPage[RoutingNumber]]:
        """
        You can use this API to confirm if a routing number is valid, such as when a
        user is providing you with bank account details. Since routing numbers uniquely
        identify a bank, this will always return 0 or 1 entry. In Sandbox, the only
        valid routing number for this method is 110000000.
        """
        ...

    @required_args(["query"], ["routing_number"])
    def list(self,
    query: RoutingNumberListParams | None = None,
    *,
    cursor: str | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    routing_number: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    # deprecated options params
    headers: Union[Headers, NotGiven] = NOT_GIVEN,
    max_retries: Union[int, NotGiven] = NOT_GIVEN,
    timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,) -> AsyncPaginator[RoutingNumber, AsyncPage[RoutingNumber]]:
        """
        You can use this API to confirm if a routing number is valid, such as when a
        user is providing you with bank account details. Since routing numbers uniquely
        identify a bank, this will always return 0 or 1 entry. In Sandbox, the only
        valid routing number for this method is 110000000.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          routing_number: Filter financial institutions by routing number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
          warnings.warn(
            "Passing parameters as a dictionary is deprecated and will be removed in the future",
            DeprecationWarning,
            stacklevel=2,
          )
        else:
          # cast to Any is required because the NotGiven types make this expression incompatible
          # with the standard RoutingNumberListParams type.
          query = cast(Any, {
            "cursor": cursor,
            "limit": limit,
            "routing_number": routing_number,
        })

        return self._get_api_list(
            "/routing_numbers",
            page = AsyncPage[RoutingNumber],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, headers=headers, max_retries=max_retries, timeout=timeout, query=query),
            model = RoutingNumber,
        )