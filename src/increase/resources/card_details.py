# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import card_detail_update_params, card_detail_create_details_iframe_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.card_details import CardDetails
from ..types.card_iframe_url import CardIframeURL

__all__ = ["CardDetailsResource", "AsyncCardDetailsResource"]


class CardDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardDetailsResourceWithStreamingResponse(self)

    def update(
        self,
        card_id: str,
        *,
        pin: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardDetails:
        """
        Update a Card's PIN

        Args:
          card_id: The card identifier.

          pin: The 4-digit PIN for the card, for use with ATMs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._patch(
            f"/cards/{card_id}/details",
            body=maybe_transform({"pin": pin}, card_detail_update_params.CardDetailUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDetails,
        )

    def create_details_iframe(
        self,
        card_id: str,
        *,
        physical_card_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardIframeURL:
        """Create an iframe URL for a Card to display the card details.

        More details about
        styling and usage can be found in the
        [documentation](/documentation/embedded-card-component).

        Args:
          card_id: The identifier of the Card to retrieve details for.

          physical_card_id: The identifier of the Physical Card to retrieve details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._post(
            f"/cards/{card_id}/create_details_iframe",
            body=maybe_transform(
                {"physical_card_id": physical_card_id},
                card_detail_create_details_iframe_params.CardDetailCreateDetailsIframeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardIframeURL,
        )

    def details(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardDetails:
        """
        Sensitive details for a Card include the primary account number, expiry, card
        verification code, and PIN.

        Args:
          card_id: The identifier of the Card to retrieve details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            f"/cards/{card_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDetails,
        )


class AsyncCardDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardDetailsResourceWithStreamingResponse(self)

    async def update(
        self,
        card_id: str,
        *,
        pin: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardDetails:
        """
        Update a Card's PIN

        Args:
          card_id: The card identifier.

          pin: The 4-digit PIN for the card, for use with ATMs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._patch(
            f"/cards/{card_id}/details",
            body=await async_maybe_transform({"pin": pin}, card_detail_update_params.CardDetailUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDetails,
        )

    async def create_details_iframe(
        self,
        card_id: str,
        *,
        physical_card_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardIframeURL:
        """Create an iframe URL for a Card to display the card details.

        More details about
        styling and usage can be found in the
        [documentation](/documentation/embedded-card-component).

        Args:
          card_id: The identifier of the Card to retrieve details for.

          physical_card_id: The identifier of the Physical Card to retrieve details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._post(
            f"/cards/{card_id}/create_details_iframe",
            body=await async_maybe_transform(
                {"physical_card_id": physical_card_id},
                card_detail_create_details_iframe_params.CardDetailCreateDetailsIframeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardIframeURL,
        )

    async def details(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardDetails:
        """
        Sensitive details for a Card include the primary account number, expiry, card
        verification code, and PIN.

        Args:
          card_id: The identifier of the Card to retrieve details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            f"/cards/{card_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDetails,
        )


class CardDetailsResourceWithRawResponse:
    def __init__(self, card_details: CardDetailsResource) -> None:
        self._card_details = card_details

        self.update = to_raw_response_wrapper(
            card_details.update,
        )
        self.create_details_iframe = to_raw_response_wrapper(
            card_details.create_details_iframe,
        )
        self.details = to_raw_response_wrapper(
            card_details.details,
        )


class AsyncCardDetailsResourceWithRawResponse:
    def __init__(self, card_details: AsyncCardDetailsResource) -> None:
        self._card_details = card_details

        self.update = async_to_raw_response_wrapper(
            card_details.update,
        )
        self.create_details_iframe = async_to_raw_response_wrapper(
            card_details.create_details_iframe,
        )
        self.details = async_to_raw_response_wrapper(
            card_details.details,
        )


class CardDetailsResourceWithStreamingResponse:
    def __init__(self, card_details: CardDetailsResource) -> None:
        self._card_details = card_details

        self.update = to_streamed_response_wrapper(
            card_details.update,
        )
        self.create_details_iframe = to_streamed_response_wrapper(
            card_details.create_details_iframe,
        )
        self.details = to_streamed_response_wrapper(
            card_details.details,
        )


class AsyncCardDetailsResourceWithStreamingResponse:
    def __init__(self, card_details: AsyncCardDetailsResource) -> None:
        self._card_details = card_details

        self.update = async_to_streamed_response_wrapper(
            card_details.update,
        )
        self.create_details_iframe = async_to_streamed_response_wrapper(
            card_details.create_details_iframe,
        )
        self.details = async_to_streamed_response_wrapper(
            card_details.details,
        )
