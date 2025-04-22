# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import physical_card_list_params, physical_card_create_params, physical_card_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.physical_card import PhysicalCard

__all__ = ["PhysicalCardsResource", "AsyncPhysicalCardsResource"]


class PhysicalCardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhysicalCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return PhysicalCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhysicalCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return PhysicalCardsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        card_id: str,
        cardholder: physical_card_create_params.Cardholder,
        shipment: physical_card_create_params.Shipment,
        physical_card_profile_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCard:
        """
        Create a Physical Card

        Args:
          card_id: The underlying card representing this physical card.

          cardholder: Details about the cardholder, as it will appear on the physical card.

          shipment: The details used to ship this physical card.

          physical_card_profile_id: The physical card profile to use for this physical card. The latest default
              physical card profile will be used if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/physical_cards",
            body=maybe_transform(
                {
                    "card_id": card_id,
                    "cardholder": cardholder,
                    "shipment": shipment,
                    "physical_card_profile_id": physical_card_profile_id,
                },
                physical_card_create_params.PhysicalCardCreateParams,
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

    def retrieve(
        self,
        physical_card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhysicalCard:
        """
        Retrieve a Physical Card

        Args:
          physical_card_id: The identifier of the Physical Card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not physical_card_id:
            raise ValueError(f"Expected a non-empty value for `physical_card_id` but received {physical_card_id!r}")
        return self._get(
            f"/physical_cards/{physical_card_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhysicalCard,
        )

    def update(
        self,
        physical_card_id: str,
        *,
        status: Literal["active", "disabled", "canceled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCard:
        """
        Update a Physical Card

        Args:
          physical_card_id: The Physical Card identifier.

          status: The status to update the Physical Card to.

              - `active` - The physical card is active.
              - `disabled` - The physical card is temporarily disabled.
              - `canceled` - The physical card is permanently canceled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_card_id:
            raise ValueError(f"Expected a non-empty value for `physical_card_id` but received {physical_card_id!r}")
        return self._patch(
            f"/physical_cards/{physical_card_id}",
            body=maybe_transform({"status": status}, physical_card_update_params.PhysicalCardUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCard,
        )

    def list(
        self,
        *,
        card_id: str | NotGiven = NOT_GIVEN,
        created_at: physical_card_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PhysicalCard]:
        """
        List Physical Cards

        Args:
          card_id: Filter Physical Cards to ones belonging to the specified Card.

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
            "/physical_cards",
            page=SyncPage[PhysicalCard],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "card_id": card_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    physical_card_list_params.PhysicalCardListParams,
                ),
            ),
            model=PhysicalCard,
        )


class AsyncPhysicalCardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhysicalCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhysicalCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhysicalCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncPhysicalCardsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        card_id: str,
        cardholder: physical_card_create_params.Cardholder,
        shipment: physical_card_create_params.Shipment,
        physical_card_profile_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCard:
        """
        Create a Physical Card

        Args:
          card_id: The underlying card representing this physical card.

          cardholder: Details about the cardholder, as it will appear on the physical card.

          shipment: The details used to ship this physical card.

          physical_card_profile_id: The physical card profile to use for this physical card. The latest default
              physical card profile will be used if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/physical_cards",
            body=await async_maybe_transform(
                {
                    "card_id": card_id,
                    "cardholder": cardholder,
                    "shipment": shipment,
                    "physical_card_profile_id": physical_card_profile_id,
                },
                physical_card_create_params.PhysicalCardCreateParams,
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

    async def retrieve(
        self,
        physical_card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhysicalCard:
        """
        Retrieve a Physical Card

        Args:
          physical_card_id: The identifier of the Physical Card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not physical_card_id:
            raise ValueError(f"Expected a non-empty value for `physical_card_id` but received {physical_card_id!r}")
        return await self._get(
            f"/physical_cards/{physical_card_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhysicalCard,
        )

    async def update(
        self,
        physical_card_id: str,
        *,
        status: Literal["active", "disabled", "canceled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCard:
        """
        Update a Physical Card

        Args:
          physical_card_id: The Physical Card identifier.

          status: The status to update the Physical Card to.

              - `active` - The physical card is active.
              - `disabled` - The physical card is temporarily disabled.
              - `canceled` - The physical card is permanently canceled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_card_id:
            raise ValueError(f"Expected a non-empty value for `physical_card_id` but received {physical_card_id!r}")
        return await self._patch(
            f"/physical_cards/{physical_card_id}",
            body=await async_maybe_transform({"status": status}, physical_card_update_params.PhysicalCardUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCard,
        )

    def list(
        self,
        *,
        card_id: str | NotGiven = NOT_GIVEN,
        created_at: physical_card_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PhysicalCard, AsyncPage[PhysicalCard]]:
        """
        List Physical Cards

        Args:
          card_id: Filter Physical Cards to ones belonging to the specified Card.

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
            "/physical_cards",
            page=AsyncPage[PhysicalCard],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "card_id": card_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    physical_card_list_params.PhysicalCardListParams,
                ),
            ),
            model=PhysicalCard,
        )


class PhysicalCardsResourceWithRawResponse:
    def __init__(self, physical_cards: PhysicalCardsResource) -> None:
        self._physical_cards = physical_cards

        self.create = to_raw_response_wrapper(
            physical_cards.create,
        )
        self.retrieve = to_raw_response_wrapper(
            physical_cards.retrieve,
        )
        self.update = to_raw_response_wrapper(
            physical_cards.update,
        )
        self.list = to_raw_response_wrapper(
            physical_cards.list,
        )


class AsyncPhysicalCardsResourceWithRawResponse:
    def __init__(self, physical_cards: AsyncPhysicalCardsResource) -> None:
        self._physical_cards = physical_cards

        self.create = async_to_raw_response_wrapper(
            physical_cards.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            physical_cards.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            physical_cards.update,
        )
        self.list = async_to_raw_response_wrapper(
            physical_cards.list,
        )


class PhysicalCardsResourceWithStreamingResponse:
    def __init__(self, physical_cards: PhysicalCardsResource) -> None:
        self._physical_cards = physical_cards

        self.create = to_streamed_response_wrapper(
            physical_cards.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            physical_cards.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            physical_cards.update,
        )
        self.list = to_streamed_response_wrapper(
            physical_cards.list,
        )


class AsyncPhysicalCardsResourceWithStreamingResponse:
    def __init__(self, physical_cards: AsyncPhysicalCardsResource) -> None:
        self._physical_cards = physical_cards

        self.create = async_to_streamed_response_wrapper(
            physical_cards.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            physical_cards.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            physical_cards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            physical_cards.list,
        )
