# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import PhysicalCard
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.simulations import physical_card_shipment_advance_params

__all__ = ["PhysicalCards", "AsyncPhysicalCards"]


class PhysicalCards(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhysicalCardsWithRawResponse:
        return PhysicalCardsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhysicalCardsWithStreamingResponse:
        return PhysicalCardsWithStreamingResponse(self)

    def shipment_advance(
        self,
        physical_card_id: str,
        *,
        shipment_status: Literal["pending", "canceled", "submitted", "acknowledged", "rejected", "shipped", "returned"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCard:
        """
        This endpoint allows you to simulate advancing the shipment status of a Physical
        Card, to simulate e.g., that a physical card was attempted shipped but then
        failed delivery.

        Args:
          physical_card_id: The Physical Card you would like to action.

          shipment_status: The shipment status to move the Physical Card to.

              - `pending` - The physical card has not yet been shipped.
              - `canceled` - The physical card shipment was canceled prior to submission.
              - `submitted` - The physical card shipment has been submitted to the card
                fulfillment provider.
              - `acknowledged` - The physical card shipment has been acknowledged by the card
                fulfillment provider and will be processed in their next batch.
              - `rejected` - The physical card shipment was rejected by the card printer due
                to an error.
              - `shipped` - The physical card has been shipped.
              - `returned` - The physical card shipment was returned to the sender and
                destroyed by the production facility.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_card_id:
            raise ValueError(f"Expected a non-empty value for `physical_card_id` but received {physical_card_id!r}")
        return self._post(
            f"/simulations/physical_cards/{physical_card_id}/shipment_advance",
            body=maybe_transform(
                {"shipment_status": shipment_status},
                physical_card_shipment_advance_params.PhysicalCardShipmentAdvanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCard,
        )


class AsyncPhysicalCards(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhysicalCardsWithRawResponse:
        return AsyncPhysicalCardsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhysicalCardsWithStreamingResponse:
        return AsyncPhysicalCardsWithStreamingResponse(self)

    async def shipment_advance(
        self,
        physical_card_id: str,
        *,
        shipment_status: Literal["pending", "canceled", "submitted", "acknowledged", "rejected", "shipped", "returned"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCard:
        """
        This endpoint allows you to simulate advancing the shipment status of a Physical
        Card, to simulate e.g., that a physical card was attempted shipped but then
        failed delivery.

        Args:
          physical_card_id: The Physical Card you would like to action.

          shipment_status: The shipment status to move the Physical Card to.

              - `pending` - The physical card has not yet been shipped.
              - `canceled` - The physical card shipment was canceled prior to submission.
              - `submitted` - The physical card shipment has been submitted to the card
                fulfillment provider.
              - `acknowledged` - The physical card shipment has been acknowledged by the card
                fulfillment provider and will be processed in their next batch.
              - `rejected` - The physical card shipment was rejected by the card printer due
                to an error.
              - `shipped` - The physical card has been shipped.
              - `returned` - The physical card shipment was returned to the sender and
                destroyed by the production facility.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_card_id:
            raise ValueError(f"Expected a non-empty value for `physical_card_id` but received {physical_card_id!r}")
        return await self._post(
            f"/simulations/physical_cards/{physical_card_id}/shipment_advance",
            body=maybe_transform(
                {"shipment_status": shipment_status},
                physical_card_shipment_advance_params.PhysicalCardShipmentAdvanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCard,
        )


class PhysicalCardsWithRawResponse:
    def __init__(self, physical_cards: PhysicalCards) -> None:
        self._physical_cards = physical_cards

        self.shipment_advance = _legacy_response.to_raw_response_wrapper(
            physical_cards.shipment_advance,
        )


class AsyncPhysicalCardsWithRawResponse:
    def __init__(self, physical_cards: AsyncPhysicalCards) -> None:
        self._physical_cards = physical_cards

        self.shipment_advance = _legacy_response.async_to_raw_response_wrapper(
            physical_cards.shipment_advance,
        )


class PhysicalCardsWithStreamingResponse:
    def __init__(self, physical_cards: PhysicalCards) -> None:
        self._physical_cards = physical_cards

        self.shipment_advance = to_streamed_response_wrapper(
            physical_cards.shipment_advance,
        )


class AsyncPhysicalCardsWithStreamingResponse:
    def __init__(self, physical_cards: AsyncPhysicalCards) -> None:
        self._physical_cards = physical_cards

        self.shipment_advance = async_to_streamed_response_wrapper(
            physical_cards.shipment_advance,
        )
