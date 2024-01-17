# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import CardDispute
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.simulations import card_dispute_action_params

__all__ = ["CardDisputes", "AsyncCardDisputes"]


class CardDisputes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardDisputesWithRawResponse:
        return CardDisputesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardDisputesWithStreamingResponse:
        return CardDisputesWithStreamingResponse(self)

    def action(
        self,
        card_dispute_id: str,
        *,
        status: Literal["accepted", "rejected"],
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

              - `accepted` - The Card Dispute has been accepted and your funds have been
                returned.
              - `rejected` - The Card Dispute has been rejected.

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


class AsyncCardDisputes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardDisputesWithRawResponse:
        return AsyncCardDisputesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardDisputesWithStreamingResponse:
        return AsyncCardDisputesWithStreamingResponse(self)

    async def action(
        self,
        card_dispute_id: str,
        *,
        status: Literal["accepted", "rejected"],
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

              - `accepted` - The Card Dispute has been accepted and your funds have been
                returned.
              - `rejected` - The Card Dispute has been rejected.

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


class CardDisputesWithRawResponse:
    def __init__(self, card_disputes: CardDisputes) -> None:
        self._card_disputes = card_disputes

        self.action = _legacy_response.to_raw_response_wrapper(
            card_disputes.action,
        )


class AsyncCardDisputesWithRawResponse:
    def __init__(self, card_disputes: AsyncCardDisputes) -> None:
        self._card_disputes = card_disputes

        self.action = _legacy_response.async_to_raw_response_wrapper(
            card_disputes.action,
        )


class CardDisputesWithStreamingResponse:
    def __init__(self, card_disputes: CardDisputes) -> None:
        self._card_disputes = card_disputes

        self.action = to_streamed_response_wrapper(
            card_disputes.action,
        )


class AsyncCardDisputesWithStreamingResponse:
    def __init__(self, card_disputes: AsyncCardDisputes) -> None:
        self._card_disputes = card_disputes

        self.action = async_to_streamed_response_wrapper(
            card_disputes.action,
        )
