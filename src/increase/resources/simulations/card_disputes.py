# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
        status: Literal["pending_user_information", "accepted", "rejected", "lost", "won"],
        explanation: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        After a [Card Dispute](#card-disputes) is created in production, the dispute
        will be reviewed. Since no review happens in sandbox, this endpoint simulates
        moving a Card Dispute into a rejected or accepted state. A Card Dispute can only
        be actioned one time and must have a status of `pending_reviewing`.

        Args:
          card_dispute_id: The dispute you would like to action.

          status: The status to move the dispute to.

              - `pending_user_information` - Increase has requested more information related
                to the Card Dispute from you.
              - `accepted` - The Card Dispute has been accepted and your funds have been
                returned. The card dispute will eventually transition into `won` or `lost`
                depending on the outcome.
              - `rejected` - The Card Dispute has been rejected.
              - `lost` - The Card Dispute has been lost and funds previously credited from the
                acceptance have been debited.
              - `won` - The Card Dispute has been won and no further action can be taken.

          explanation: Why the dispute was rejected. Not required for accepting disputes.

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
                    "status": status,
                    "explanation": explanation,
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
        status: Literal["pending_user_information", "accepted", "rejected", "lost", "won"],
        explanation: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        After a [Card Dispute](#card-disputes) is created in production, the dispute
        will be reviewed. Since no review happens in sandbox, this endpoint simulates
        moving a Card Dispute into a rejected or accepted state. A Card Dispute can only
        be actioned one time and must have a status of `pending_reviewing`.

        Args:
          card_dispute_id: The dispute you would like to action.

          status: The status to move the dispute to.

              - `pending_user_information` - Increase has requested more information related
                to the Card Dispute from you.
              - `accepted` - The Card Dispute has been accepted and your funds have been
                returned. The card dispute will eventually transition into `won` or `lost`
                depending on the outcome.
              - `rejected` - The Card Dispute has been rejected.
              - `lost` - The Card Dispute has been lost and funds previously credited from the
                acceptance have been debited.
              - `won` - The Card Dispute has been won and no further action can be taken.

          explanation: Why the dispute was rejected. Not required for accepting disputes.

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
                    "status": status,
                    "explanation": explanation,
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
