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
from ...types.checkbook import Checkbook

__all__ = ["CheckbooksResource", "AsyncCheckbooksResource"]


class CheckbooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckbooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CheckbooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckbooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CheckbooksResourceWithStreamingResponse(self)

    def mail(
        self,
        checkbook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Checkbook:
        """
        Simulates the mailing of a [Checkbook](#checkbooks), which happens periodically
        throughout the day in production but can be sped up in sandbox. This Checkbook
        must have a `status` of `pending_submission` or `pending_mailing`.

        Args:
          checkbook_id: The identifier of the Checkbook you wish to mail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not checkbook_id:
            raise ValueError(f"Expected a non-empty value for `checkbook_id` but received {checkbook_id!r}")
        return self._post(
            path_template("/simulations/checkbooks/{checkbook_id}/mail", checkbook_id=checkbook_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Checkbook,
        )


class AsyncCheckbooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckbooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckbooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckbooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCheckbooksResourceWithStreamingResponse(self)

    async def mail(
        self,
        checkbook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Checkbook:
        """
        Simulates the mailing of a [Checkbook](#checkbooks), which happens periodically
        throughout the day in production but can be sped up in sandbox. This Checkbook
        must have a `status` of `pending_submission` or `pending_mailing`.

        Args:
          checkbook_id: The identifier of the Checkbook you wish to mail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not checkbook_id:
            raise ValueError(f"Expected a non-empty value for `checkbook_id` but received {checkbook_id!r}")
        return await self._post(
            path_template("/simulations/checkbooks/{checkbook_id}/mail", checkbook_id=checkbook_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Checkbook,
        )


class CheckbooksResourceWithRawResponse:
    def __init__(self, checkbooks: CheckbooksResource) -> None:
        self._checkbooks = checkbooks

        self.mail = to_raw_response_wrapper(
            checkbooks.mail,
        )


class AsyncCheckbooksResourceWithRawResponse:
    def __init__(self, checkbooks: AsyncCheckbooksResource) -> None:
        self._checkbooks = checkbooks

        self.mail = async_to_raw_response_wrapper(
            checkbooks.mail,
        )


class CheckbooksResourceWithStreamingResponse:
    def __init__(self, checkbooks: CheckbooksResource) -> None:
        self._checkbooks = checkbooks

        self.mail = to_streamed_response_wrapper(
            checkbooks.mail,
        )


class AsyncCheckbooksResourceWithStreamingResponse:
    def __init__(self, checkbooks: AsyncCheckbooksResource) -> None:
        self._checkbooks = checkbooks

        self.mail = async_to_streamed_response_wrapper(
            checkbooks.mail,
        )
