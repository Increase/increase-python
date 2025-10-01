# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import card_dispute_action_params
from ...types.card_dispute import CardDispute

__all__ = ["CardDisputesResource", "AsyncCardDisputesResource"]


class CardDisputesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardDisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardDisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardDisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardDisputesResourceWithStreamingResponse(self)

    def action(
        self,
        card_dispute_id: str,
        *,
        network: Literal["visa"],
        visa: card_dispute_action_params.Visa | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        After a [Card Dispute](#card-disputes) is created in production, the dispute
        will initially be in a `pending_user_submission_reviewing` state. Since no
        review or further action happens in sandbox, this endpoint simulates moving a
        Card Dispute through its various states.

        Args:
          card_dispute_id: The dispute you would like to action.

          network: The network of the Card Dispute. Details specific to the network are required
              under the sub-object with the same identifier as the network.

              - `visa` - Visa

          visa: The Visa-specific parameters for the taking action on the dispute. Required if
              and only if `network` is `visa`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_dispute_id:
            raise ValueError(f"Expected a non-empty value for `card_dispute_id` but received {card_dispute_id!r}")
        return self._post(
            f"/simulations/card_disputes/{card_dispute_id}/action",
            body=maybe_transform(
                {
                    "network": network,
                    "visa": visa,
                },
                card_dispute_action_params.CardDisputeActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )


class AsyncCardDisputesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardDisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardDisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardDisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardDisputesResourceWithStreamingResponse(self)

    async def action(
        self,
        card_dispute_id: str,
        *,
        network: Literal["visa"],
        visa: card_dispute_action_params.Visa | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        After a [Card Dispute](#card-disputes) is created in production, the dispute
        will initially be in a `pending_user_submission_reviewing` state. Since no
        review or further action happens in sandbox, this endpoint simulates moving a
        Card Dispute through its various states.

        Args:
          card_dispute_id: The dispute you would like to action.

          network: The network of the Card Dispute. Details specific to the network are required
              under the sub-object with the same identifier as the network.

              - `visa` - Visa

          visa: The Visa-specific parameters for the taking action on the dispute. Required if
              and only if `network` is `visa`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_dispute_id:
            raise ValueError(f"Expected a non-empty value for `card_dispute_id` but received {card_dispute_id!r}")
        return await self._post(
            f"/simulations/card_disputes/{card_dispute_id}/action",
            body=await async_maybe_transform(
                {
                    "network": network,
                    "visa": visa,
                },
                card_dispute_action_params.CardDisputeActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )


class CardDisputesResourceWithRawResponse:
    def __init__(self, card_disputes: CardDisputesResource) -> None:
        self._card_disputes = card_disputes

        self.action = to_raw_response_wrapper(
            card_disputes.action,
        )


class AsyncCardDisputesResourceWithRawResponse:
    def __init__(self, card_disputes: AsyncCardDisputesResource) -> None:
        self._card_disputes = card_disputes

        self.action = async_to_raw_response_wrapper(
            card_disputes.action,
        )


class CardDisputesResourceWithStreamingResponse:
    def __init__(self, card_disputes: CardDisputesResource) -> None:
        self._card_disputes = card_disputes

        self.action = to_streamed_response_wrapper(
            card_disputes.action,
        )


class AsyncCardDisputesResourceWithStreamingResponse:
    def __init__(self, card_disputes: AsyncCardDisputesResource) -> None:
        self._card_disputes = card_disputes

        self.action = async_to_streamed_response_wrapper(
            card_disputes.action,
        )
