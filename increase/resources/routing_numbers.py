# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.routing_number import RoutingNumber
from ..types.routing_number_list_params import RoutingNumberListParams

__all__ = ["RoutingNumbers", "AsyncRoutingNumbers"]


class RoutingNumbers(SyncAPIResource):
    def list(
        self,
        query: RoutingNumberListParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[RoutingNumber]:
        """
        You can use this API to confirm if a routing number is valid, such as when a
        user is providing you with bank account details.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/routing_numbers",
            page=SyncPage[RoutingNumber],
            options=options,
            model=RoutingNumber,
        )


class AsyncRoutingNumbers(AsyncAPIResource):
    def list(
        self,
        query: RoutingNumberListParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[RoutingNumber, AsyncPage[RoutingNumber]]:
        """
        You can use this API to confirm if a routing number is valid, such as when a
        user is providing you with bank account details.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/routing_numbers",
            page=AsyncPage[RoutingNumber],
            options=options,
            model=RoutingNumber,
        )
