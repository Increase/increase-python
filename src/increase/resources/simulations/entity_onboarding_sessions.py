# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.entity_onboarding_session import EntityOnboardingSession

__all__ = ["EntityOnboardingSessionsResource", "AsyncEntityOnboardingSessionsResource"]


class EntityOnboardingSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntityOnboardingSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return EntityOnboardingSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntityOnboardingSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return EntityOnboardingSessionsResourceWithStreamingResponse(self)

    def submit(
        self,
        entity_onboarding_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EntityOnboardingSession:
        """
        Simulates the submission of an
        [Entity Onboarding Session](#entity-onboarding-sessions). This session must have
        a `status` of `active`. After submission, the session will transition to
        `expired` and a new Entity will be created.

        Args:
          entity_onboarding_session_id: The identifier of the Entity Onboarding Session you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_onboarding_session_id:
            raise ValueError(
                f"Expected a non-empty value for `entity_onboarding_session_id` but received {entity_onboarding_session_id!r}"
            )
        return self._post(
            path_template(
                "/simulations/entity_onboarding_sessions/{entity_onboarding_session_id}/submit",
                entity_onboarding_session_id=entity_onboarding_session_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EntityOnboardingSession,
        )


class AsyncEntityOnboardingSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntityOnboardingSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntityOnboardingSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntityOnboardingSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncEntityOnboardingSessionsResourceWithStreamingResponse(self)

    async def submit(
        self,
        entity_onboarding_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EntityOnboardingSession:
        """
        Simulates the submission of an
        [Entity Onboarding Session](#entity-onboarding-sessions). This session must have
        a `status` of `active`. After submission, the session will transition to
        `expired` and a new Entity will be created.

        Args:
          entity_onboarding_session_id: The identifier of the Entity Onboarding Session you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_onboarding_session_id:
            raise ValueError(
                f"Expected a non-empty value for `entity_onboarding_session_id` but received {entity_onboarding_session_id!r}"
            )
        return await self._post(
            path_template(
                "/simulations/entity_onboarding_sessions/{entity_onboarding_session_id}/submit",
                entity_onboarding_session_id=entity_onboarding_session_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EntityOnboardingSession,
        )


class EntityOnboardingSessionsResourceWithRawResponse:
    def __init__(self, entity_onboarding_sessions: EntityOnboardingSessionsResource) -> None:
        self._entity_onboarding_sessions = entity_onboarding_sessions

        self.submit = to_raw_response_wrapper(
            entity_onboarding_sessions.submit,
        )


class AsyncEntityOnboardingSessionsResourceWithRawResponse:
    def __init__(self, entity_onboarding_sessions: AsyncEntityOnboardingSessionsResource) -> None:
        self._entity_onboarding_sessions = entity_onboarding_sessions

        self.submit = async_to_raw_response_wrapper(
            entity_onboarding_sessions.submit,
        )


class EntityOnboardingSessionsResourceWithStreamingResponse:
    def __init__(self, entity_onboarding_sessions: EntityOnboardingSessionsResource) -> None:
        self._entity_onboarding_sessions = entity_onboarding_sessions

        self.submit = to_streamed_response_wrapper(
            entity_onboarding_sessions.submit,
        )


class AsyncEntityOnboardingSessionsResourceWithStreamingResponse:
    def __init__(self, entity_onboarding_sessions: AsyncEntityOnboardingSessionsResource) -> None:
        self._entity_onboarding_sessions = entity_onboarding_sessions

        self.submit = async_to_streamed_response_wrapper(
            entity_onboarding_sessions.submit,
        )
