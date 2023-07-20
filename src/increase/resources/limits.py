# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..types import Limit, limit_list_params, limit_create_params, limit_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Limits", "AsyncLimits"]


class Limits(SyncAPIResource):
    def create(
        self,
        *,
        metric: Literal["count", "volume"],
        model_id: str,
        value: int,
        interval: Literal["transaction", "day", "week", "month", "year", "all_time"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Limit:
        """
        Create a Limit

        Args:
          metric: The metric for the limit.

              - `count` - The maximum number of debits allowed.
              - `volume` - The maximum volume of debits allowed in the minor unit of the
                model's currency.

          model_id: The identifier of the Account, Account Number, or Card you wish to associate the
              limit with.

          value: The value to test the limit against.

          interval: The interval for the metric. Required if `metric` is `count` or `volume`.

              - `transaction` - Enforce the limit per-transaction.
              - `day` - Enforce the limit based on the previous 24 hour period.
              - `week` - Enforce the limit based on the previous seven days.
              - `month` - Enforce the limit based on the previous month, going back to the
                current day in the previous month, or as close as possible given month length
                differences.
              - `year` - Enforce the limit based on the previous year.
              - `all_time` - Enforce the limit for all time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/limits",
            body=maybe_transform(
                {
                    "metric": metric,
                    "model_id": model_id,
                    "value": value,
                    "interval": interval,
                },
                limit_create_params.LimitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Limit:
        """
        Retrieve a Limit

        Args:
          limit_id: The identifier of the Limit to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/limits/{limit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Limit:
        """
        Update a Limit

        Args:
          limit_id: The limit to update.

          status: The status to update the limit with.

              - `inactive` - Disable the limit temporarily.
              - `active` - Activate the limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/limits/{limit_id}",
            body=maybe_transform({"status": status}, limit_update_params.LimitUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Limit]:
        """
        List Limits

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          model_id: The model to retrieve limits for.

          status: The status to retrieve limits for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/limits",
            page=SyncPage[Limit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "model_id": model_id,
                        "status": status,
                    },
                    limit_list_params.LimitListParams,
                ),
            ),
            model=Limit,
        )


class AsyncLimits(AsyncAPIResource):
    async def create(
        self,
        *,
        metric: Literal["count", "volume"],
        model_id: str,
        value: int,
        interval: Literal["transaction", "day", "week", "month", "year", "all_time"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Limit:
        """
        Create a Limit

        Args:
          metric: The metric for the limit.

              - `count` - The maximum number of debits allowed.
              - `volume` - The maximum volume of debits allowed in the minor unit of the
                model's currency.

          model_id: The identifier of the Account, Account Number, or Card you wish to associate the
              limit with.

          value: The value to test the limit against.

          interval: The interval for the metric. Required if `metric` is `count` or `volume`.

              - `transaction` - Enforce the limit per-transaction.
              - `day` - Enforce the limit based on the previous 24 hour period.
              - `week` - Enforce the limit based on the previous seven days.
              - `month` - Enforce the limit based on the previous month, going back to the
                current day in the previous month, or as close as possible given month length
                differences.
              - `year` - Enforce the limit based on the previous year.
              - `all_time` - Enforce the limit for all time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/limits",
            body=maybe_transform(
                {
                    "metric": metric,
                    "model_id": model_id,
                    "value": value,
                    "interval": interval,
                },
                limit_create_params.LimitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Limit:
        """
        Retrieve a Limit

        Args:
          limit_id: The identifier of the Limit to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/limits/{limit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Limit:
        """
        Update a Limit

        Args:
          limit_id: The limit to update.

          status: The status to update the limit with.

              - `inactive` - Disable the limit temporarily.
              - `active` - Activate the limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/limits/{limit_id}",
            body=maybe_transform({"status": status}, limit_update_params.LimitUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Limit, AsyncPage[Limit]]:
        """
        List Limits

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          model_id: The model to retrieve limits for.

          status: The status to retrieve limits for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/limits",
            page=AsyncPage[Limit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "model_id": model_id,
                        "status": status,
                    },
                    limit_list_params.LimitListParams,
                ),
            ),
            model=Limit,
        )
