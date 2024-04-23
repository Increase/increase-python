# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.entity import Entity
from ...types.entities import industry_code_create_params

__all__ = ["IndustryCode", "AsyncIndustryCode"]


class IndustryCode(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndustryCodeWithRawResponse:
        return IndustryCodeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndustryCodeWithStreamingResponse:
        return IndustryCodeWithStreamingResponse(self)

    def create(
        self,
        entity_id: str,
        *,
        industry_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update the industry code for a corporate Entity

        Args:
          entity_id: The identifier of the Entity to update. This endpoint only accepts `corporation`
              entities.

          industry_code: The North American Industry Classification System (NAICS) code for the
              corporation's primary line of business. This is a number, like `5132` for
              `Software Publishers`. A full list of classification codes is available
              [here](https://increase.com/documentation/data-dictionary#north-american-industry-classification-system-codes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/industry_code",
            body=maybe_transform(
                {"industry_code": industry_code}, industry_code_create_params.IndustryCodeCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )


class AsyncIndustryCode(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndustryCodeWithRawResponse:
        return AsyncIndustryCodeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndustryCodeWithStreamingResponse:
        return AsyncIndustryCodeWithStreamingResponse(self)

    async def create(
        self,
        entity_id: str,
        *,
        industry_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update the industry code for a corporate Entity

        Args:
          entity_id: The identifier of the Entity to update. This endpoint only accepts `corporation`
              entities.

          industry_code: The North American Industry Classification System (NAICS) code for the
              corporation's primary line of business. This is a number, like `5132` for
              `Software Publishers`. A full list of classification codes is available
              [here](https://increase.com/documentation/data-dictionary#north-american-industry-classification-system-codes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/industry_code",
            body=await async_maybe_transform(
                {"industry_code": industry_code}, industry_code_create_params.IndustryCodeCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )


class IndustryCodeWithRawResponse:
    def __init__(self, industry_code: IndustryCode) -> None:
        self._industry_code = industry_code

        self.create = _legacy_response.to_raw_response_wrapper(
            industry_code.create,
        )


class AsyncIndustryCodeWithRawResponse:
    def __init__(self, industry_code: AsyncIndustryCode) -> None:
        self._industry_code = industry_code

        self.create = _legacy_response.async_to_raw_response_wrapper(
            industry_code.create,
        )


class IndustryCodeWithStreamingResponse:
    def __init__(self, industry_code: IndustryCode) -> None:
        self._industry_code = industry_code

        self.create = to_streamed_response_wrapper(
            industry_code.create,
        )


class AsyncIndustryCodeWithStreamingResponse:
    def __init__(self, industry_code: AsyncIndustryCode) -> None:
        self._industry_code = industry_code

        self.create = async_to_streamed_response_wrapper(
            industry_code.create,
        )
