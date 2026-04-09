# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import entity_onboarding_session_list_params, entity_onboarding_session_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.entity_onboarding_session import EntityOnboardingSession

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

    def create(
        self,
        *,
        program_id: str,
        redirect_url: str,
        entity_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EntityOnboardingSession:
        """
        Create an Entity Onboarding Session

        Args:
          program_id: The identifier of the Program the Entity will be onboarded to.

          redirect_url: The URL to redirect the customer to after they complete the onboarding form. The
              redirect will include `entity_onboarding_session_id` and `entity_id` query
              parameters.

          entity_id: The identifier of an existing Entity to associate with the onboarding session.
              If provided, the onboarding form will display any outstanding tasks required to
              complete the Entity's onboarding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/entity_onboarding_sessions",
            body=maybe_transform(
                {
                    "program_id": program_id,
                    "redirect_url": redirect_url,
                    "entity_id": entity_id,
                },
                entity_onboarding_session_create_params.EntityOnboardingSessionCreateParams,
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

    def retrieve(
        self,
        entity_onboarding_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityOnboardingSession:
        """
        Retrieve an Entity Onboarding Session

        Args:
          entity_onboarding_session_id: The identifier of the Entity Onboarding Session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_onboarding_session_id:
            raise ValueError(
                f"Expected a non-empty value for `entity_onboarding_session_id` but received {entity_onboarding_session_id!r}"
            )
        return self._get(
            path_template(
                "/entity_onboarding_sessions/{entity_onboarding_session_id}",
                entity_onboarding_session_id=entity_onboarding_session_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityOnboardingSession,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: entity_onboarding_session_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[EntityOnboardingSession]:
        """
        List Entity Onboarding Session

        Args:
          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/entity_onboarding_sessions",
            page=SyncPage[EntityOnboardingSession],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    entity_onboarding_session_list_params.EntityOnboardingSessionListParams,
                ),
            ),
            model=EntityOnboardingSession,
        )

    def expire(
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
        Expire an Entity Onboarding Session

        Args:
          entity_onboarding_session_id: The identifier of the Entity Onboarding Session to expire.

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
                "/entity_onboarding_sessions/{entity_onboarding_session_id}/expire",
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

    async def create(
        self,
        *,
        program_id: str,
        redirect_url: str,
        entity_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EntityOnboardingSession:
        """
        Create an Entity Onboarding Session

        Args:
          program_id: The identifier of the Program the Entity will be onboarded to.

          redirect_url: The URL to redirect the customer to after they complete the onboarding form. The
              redirect will include `entity_onboarding_session_id` and `entity_id` query
              parameters.

          entity_id: The identifier of an existing Entity to associate with the onboarding session.
              If provided, the onboarding form will display any outstanding tasks required to
              complete the Entity's onboarding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/entity_onboarding_sessions",
            body=await async_maybe_transform(
                {
                    "program_id": program_id,
                    "redirect_url": redirect_url,
                    "entity_id": entity_id,
                },
                entity_onboarding_session_create_params.EntityOnboardingSessionCreateParams,
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

    async def retrieve(
        self,
        entity_onboarding_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityOnboardingSession:
        """
        Retrieve an Entity Onboarding Session

        Args:
          entity_onboarding_session_id: The identifier of the Entity Onboarding Session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_onboarding_session_id:
            raise ValueError(
                f"Expected a non-empty value for `entity_onboarding_session_id` but received {entity_onboarding_session_id!r}"
            )
        return await self._get(
            path_template(
                "/entity_onboarding_sessions/{entity_onboarding_session_id}",
                entity_onboarding_session_id=entity_onboarding_session_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityOnboardingSession,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: entity_onboarding_session_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EntityOnboardingSession, AsyncPage[EntityOnboardingSession]]:
        """
        List Entity Onboarding Session

        Args:
          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/entity_onboarding_sessions",
            page=AsyncPage[EntityOnboardingSession],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    entity_onboarding_session_list_params.EntityOnboardingSessionListParams,
                ),
            ),
            model=EntityOnboardingSession,
        )

    async def expire(
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
        Expire an Entity Onboarding Session

        Args:
          entity_onboarding_session_id: The identifier of the Entity Onboarding Session to expire.

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
                "/entity_onboarding_sessions/{entity_onboarding_session_id}/expire",
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

        self.create = to_raw_response_wrapper(
            entity_onboarding_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            entity_onboarding_sessions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            entity_onboarding_sessions.list,
        )
        self.expire = to_raw_response_wrapper(
            entity_onboarding_sessions.expire,
        )


class AsyncEntityOnboardingSessionsResourceWithRawResponse:
    def __init__(self, entity_onboarding_sessions: AsyncEntityOnboardingSessionsResource) -> None:
        self._entity_onboarding_sessions = entity_onboarding_sessions

        self.create = async_to_raw_response_wrapper(
            entity_onboarding_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            entity_onboarding_sessions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            entity_onboarding_sessions.list,
        )
        self.expire = async_to_raw_response_wrapper(
            entity_onboarding_sessions.expire,
        )


class EntityOnboardingSessionsResourceWithStreamingResponse:
    def __init__(self, entity_onboarding_sessions: EntityOnboardingSessionsResource) -> None:
        self._entity_onboarding_sessions = entity_onboarding_sessions

        self.create = to_streamed_response_wrapper(
            entity_onboarding_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            entity_onboarding_sessions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            entity_onboarding_sessions.list,
        )
        self.expire = to_streamed_response_wrapper(
            entity_onboarding_sessions.expire,
        )


class AsyncEntityOnboardingSessionsResourceWithStreamingResponse:
    def __init__(self, entity_onboarding_sessions: AsyncEntityOnboardingSessionsResource) -> None:
        self._entity_onboarding_sessions = entity_onboarding_sessions

        self.create = async_to_streamed_response_wrapper(
            entity_onboarding_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            entity_onboarding_sessions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            entity_onboarding_sessions.list,
        )
        self.expire = async_to_streamed_response_wrapper(
            entity_onboarding_sessions.expire,
        )
