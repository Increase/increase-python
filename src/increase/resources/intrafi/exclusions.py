# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.intrafi import (
    IntrafiExclusion,
    exclusion_list_params,
    exclusion_create_params,
)

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["Exclusions", "AsyncExclusions"]


class Exclusions(SyncAPIResource):
    with_raw_response: ExclusionsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = ExclusionsWithRawResponse(self)

    def create(
        self,
        *,
        bank_name: str,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> IntrafiExclusion:
        """
        Create an IntraFi Exclusion

        Args:
          bank_name: The name of the financial institution to be excluded.

          entity_id: The identifier of the Entity whose deposits will be excluded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/intrafi_exclusions",
            body=maybe_transform(
                {
                    "bank_name": bank_name,
                    "entity_id": entity_id,
                },
                exclusion_create_params.ExclusionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=IntrafiExclusion,
        )

    def retrieve(
        self,
        intrafi_exclusion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntrafiExclusion:
        """
        Get an IntraFi Exclusion

        Args:
          intrafi_exclusion_id: The identifier of the IntraFi Exclusion to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/intrafi_exclusions/{intrafi_exclusion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntrafiExclusion,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[IntrafiExclusion]:
        """
        List IntraFi Exclusions.

        Args:
          cursor: Return the page of entries after this one.

          entity_id: Filter IntraFi Exclusions for those belonging to the specified Entity.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/intrafi_exclusions",
            page=SyncPage[IntrafiExclusion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "entity_id": entity_id,
                        "limit": limit,
                    },
                    exclusion_list_params.ExclusionListParams,
                ),
            ),
            model=IntrafiExclusion,
        )

    def archive(
        self,
        intrafi_exclusion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> IntrafiExclusion:
        """
        Archive an IntraFi Exclusion

        Args:
          intrafi_exclusion_id: The identifier of the IntraFi Exclusion request to archive. It may take 5
              business days for an exclusion removal to be processed. Removing an exclusion
              does not guarantee that funds will be swept to the previously-excluded bank.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/intrafi_exclusions/{intrafi_exclusion_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=IntrafiExclusion,
        )


class AsyncExclusions(AsyncAPIResource):
    with_raw_response: AsyncExclusionsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncExclusionsWithRawResponse(self)

    async def create(
        self,
        *,
        bank_name: str,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> IntrafiExclusion:
        """
        Create an IntraFi Exclusion

        Args:
          bank_name: The name of the financial institution to be excluded.

          entity_id: The identifier of the Entity whose deposits will be excluded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/intrafi_exclusions",
            body=maybe_transform(
                {
                    "bank_name": bank_name,
                    "entity_id": entity_id,
                },
                exclusion_create_params.ExclusionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=IntrafiExclusion,
        )

    async def retrieve(
        self,
        intrafi_exclusion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntrafiExclusion:
        """
        Get an IntraFi Exclusion

        Args:
          intrafi_exclusion_id: The identifier of the IntraFi Exclusion to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/intrafi_exclusions/{intrafi_exclusion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntrafiExclusion,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IntrafiExclusion, AsyncPage[IntrafiExclusion]]:
        """
        List IntraFi Exclusions.

        Args:
          cursor: Return the page of entries after this one.

          entity_id: Filter IntraFi Exclusions for those belonging to the specified Entity.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/intrafi_exclusions",
            page=AsyncPage[IntrafiExclusion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "entity_id": entity_id,
                        "limit": limit,
                    },
                    exclusion_list_params.ExclusionListParams,
                ),
            ),
            model=IntrafiExclusion,
        )

    async def archive(
        self,
        intrafi_exclusion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> IntrafiExclusion:
        """
        Archive an IntraFi Exclusion

        Args:
          intrafi_exclusion_id: The identifier of the IntraFi Exclusion request to archive. It may take 5
              business days for an exclusion removal to be processed. Removing an exclusion
              does not guarantee that funds will be swept to the previously-excluded bank.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/intrafi_exclusions/{intrafi_exclusion_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=IntrafiExclusion,
        )


class ExclusionsWithRawResponse:
    def __init__(self, exclusions: Exclusions) -> None:
        self.create = to_raw_response_wrapper(
            exclusions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            exclusions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            exclusions.list,
        )
        self.archive = to_raw_response_wrapper(
            exclusions.archive,
        )


class AsyncExclusionsWithRawResponse:
    def __init__(self, exclusions: AsyncExclusions) -> None:
        self.create = async_to_raw_response_wrapper(
            exclusions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            exclusions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            exclusions.list,
        )
        self.archive = async_to_raw_response_wrapper(
            exclusions.archive,
        )
