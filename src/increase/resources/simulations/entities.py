# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.entity import Entity
from ...types.simulations import entity_validation_params

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)

    def validation(
        self,
        entity_id: str,
        *,
        issues: Iterable[entity_validation_params.Issue],
        status: Literal["valid", "invalid", "pending"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Simulates setting an [Entity](#entities)'s validation under the managed
        compliance regime. Any existing managed compliance validation on the Entity will
        be marked as no longer current.

        Args:
          entity_id: The identifier of the Entity to set the validation on.

          issues: The issues to attach to the new managed compliance validation.

          status: The status to set on the new managed compliance validation.

              - `valid` - The submitted data is valid.
              - `invalid` - Additional information is required to validate the data.
              - `pending` - The submitted data is being validated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            path_template("/simulations/entities/{entity_id}/validation", entity_id=entity_id),
            body=maybe_transform(
                {
                    "issues": issues,
                    "status": status,
                },
                entity_validation_params.EntityValidationParams,
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


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)

    async def validation(
        self,
        entity_id: str,
        *,
        issues: Iterable[entity_validation_params.Issue],
        status: Literal["valid", "invalid", "pending"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Simulates setting an [Entity](#entities)'s validation under the managed
        compliance regime. Any existing managed compliance validation on the Entity will
        be marked as no longer current.

        Args:
          entity_id: The identifier of the Entity to set the validation on.

          issues: The issues to attach to the new managed compliance validation.

          status: The status to set on the new managed compliance validation.

              - `valid` - The submitted data is valid.
              - `invalid` - Additional information is required to validate the data.
              - `pending` - The submitted data is being validated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            path_template("/simulations/entities/{entity_id}/validation", entity_id=entity_id),
            body=await async_maybe_transform(
                {
                    "issues": issues,
                    "status": status,
                },
                entity_validation_params.EntityValidationParams,
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


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.validation = to_raw_response_wrapper(
            entities.validation,
        )


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.validation = async_to_raw_response_wrapper(
            entities.validation,
        )


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.validation = to_streamed_response_wrapper(
            entities.validation,
        )


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.validation = async_to_streamed_response_wrapper(
            entities.validation,
        )
