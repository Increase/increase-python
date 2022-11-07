# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.limit import Limit
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Limits", "AsyncLimits"]


class Limits(SyncAPIResource):
    def create(
        self,
        *,
        metric: Literal["count", "volume"],
        interval: Literal["transaction", "day", "week", "month", "year", "all_time"] | NotGiven = NOT_GIVEN,
        model_id: str,
        value: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Limit:
        """
        Args:
          metric: The metric for the limit.

          interval: The interval for the metric. Required if `metric` is `count` or `volume`.

          model_id: The identifier of the Account or Account Number you wish to associate the limit
              with.

          value: The value to test the limit against.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/limits",
            body={
                "metric": metric,
                "interval": interval,
                "model_id": model_id,
                "value": value,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Limit,
        )

    def retrieve(
        self,
        limit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Limit:
        return self._get(
            f"/limits/{limit_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Limit,
        )

    def update(
        self,
        limit_id: str,
        *,
        status: Literal["inactive", "active"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Limit:
        """
        Args:
          status: The status to update the limit with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/limits/{limit_id}",
            body={"status": status},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Limit,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        model_id: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[Limit]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          model_id: The model to retrieve limits for.

          status: The status to retrieve limits for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/limits",
            page=SyncPage[Limit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "model_id": model_id,
                    "status": status,
                },
            ),
            model=Limit,
        )


class AsyncLimits(AsyncAPIResource):
    async def create(
        self,
        *,
        metric: Literal["count", "volume"],
        interval: Literal["transaction", "day", "week", "month", "year", "all_time"] | NotGiven = NOT_GIVEN,
        model_id: str,
        value: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Limit:
        """
        Args:
          metric: The metric for the limit.

          interval: The interval for the metric. Required if `metric` is `count` or `volume`.

          model_id: The identifier of the Account or Account Number you wish to associate the limit
              with.

          value: The value to test the limit against.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/limits",
            body={
                "metric": metric,
                "interval": interval,
                "model_id": model_id,
                "value": value,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Limit,
        )

    async def retrieve(
        self,
        limit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Limit:
        return await self._get(
            f"/limits/{limit_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Limit,
        )

    async def update(
        self,
        limit_id: str,
        *,
        status: Literal["inactive", "active"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Limit:
        """
        Args:
          status: The status to update the limit with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/limits/{limit_id}",
            body={"status": status},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Limit,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        model_id: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[Limit, AsyncPage[Limit]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          model_id: The model to retrieve limits for.

          status: The status to retrieve limits for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/limits",
            page=AsyncPage[Limit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "model_id": model_id,
                    "status": status,
                },
            ),
            model=Limit,
        )
