# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    card_list_params,
    card_create_params,
    card_update_params,
    card_update_pin_params,
    card_create_details_iframe_params,
)
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
from ..pagination import SyncPage, AsyncPage
from ..types.card import Card
from .._base_client import AsyncPaginator, make_request_options
from ..types.card_details import CardDetails
from ..types.card_iframe_url import CardIframeURL

__all__ = ["CardsResource", "AsyncCardsResource"]


class CardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        billing_address: card_create_params.BillingAddress | Omit = omit,
        description: str | Omit = omit,
        digital_wallet: card_create_params.DigitalWallet | Omit = omit,
        entity_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Card:
        """
        Create a Card

        Args:
          account_id: The Account the card should belong to.

          billing_address: The card's billing address.

          description: The description you choose to give the card.

          digital_wallet: The contact information used in the two-factor steps for digital wallet card
              creation. To add the card to a digital wallet, you may supply an email or phone
              number with this request. Otherwise, subscribe and then action a Real Time
              Decision with the category `digital_wallet_token_requested` or
              `digital_wallet_authentication_requested`.

          entity_id: The Entity the card belongs to. You only need to supply this in rare situations
              when the card is not for the Account holder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/cards",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "billing_address": billing_address,
                    "description": description,
                    "digital_wallet": digital_wallet,
                    "entity_id": entity_id,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )

    def retrieve(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """
        Retrieve a Card

        Args:
          card_id: The identifier of the Card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            f"/cards/{card_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def update(
        self,
        card_id: str,
        *,
        billing_address: card_update_params.BillingAddress | Omit = omit,
        description: str | Omit = omit,
        digital_wallet: card_update_params.DigitalWallet | Omit = omit,
        entity_id: str | Omit = omit,
        status: Literal["active", "disabled", "canceled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Card:
        """
        Update a Card

        Args:
          card_id: The card identifier.

          billing_address: The card's updated billing address.

          description: The description you choose to give the card.

          digital_wallet: The contact information used in the two-factor steps for digital wallet card
              creation. At least one field must be present to complete the digital wallet
              steps.

          entity_id: The Entity the card belongs to. You only need to supply this in rare situations
              when the card is not for the Account holder.

          status: The status to update the Card with.

              - `active` - The card is active.
              - `disabled` - The card is temporarily disabled.
              - `canceled` - The card is permanently canceled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._patch(
            f"/cards/{card_id}",
            body=maybe_transform(
                {
                    "billing_address": billing_address,
                    "description": description,
                    "digital_wallet": digital_wallet,
                    "entity_id": entity_id,
                    "status": status,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: card_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: card_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Card]:
        """
        List Cards

        Args:
          account_id: Filter Cards to ones belonging to the specified Account.

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
            "/cards",
            page=SyncPage[Card],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            model=Card,
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
          card_id: The identifier of the Card to create an iframe for.

          physical_card_id: The identifier of the Physical Card to create an iframe for. This will inform
              the appearance of the card rendered in the iframe.

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
                {"physical_card_id": physical_card_id}, card_create_details_iframe_params.CardCreateDetailsIframeParams
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

    def update_pin(
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
          card_id: The identifier of the Card to update the PIN for.

          pin: The 4-digit PIN for the card, for use with ATMs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._post(
            f"/cards/{card_id}/update_pin",
            body=maybe_transform({"pin": pin}, card_update_pin_params.CardUpdatePinParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDetails,
        )


class AsyncCardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        billing_address: card_create_params.BillingAddress | Omit = omit,
        description: str | Omit = omit,
        digital_wallet: card_create_params.DigitalWallet | Omit = omit,
        entity_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Card:
        """
        Create a Card

        Args:
          account_id: The Account the card should belong to.

          billing_address: The card's billing address.

          description: The description you choose to give the card.

          digital_wallet: The contact information used in the two-factor steps for digital wallet card
              creation. To add the card to a digital wallet, you may supply an email or phone
              number with this request. Otherwise, subscribe and then action a Real Time
              Decision with the category `digital_wallet_token_requested` or
              `digital_wallet_authentication_requested`.

          entity_id: The Entity the card belongs to. You only need to supply this in rare situations
              when the card is not for the Account holder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/cards",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "billing_address": billing_address,
                    "description": description,
                    "digital_wallet": digital_wallet,
                    "entity_id": entity_id,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )

    async def retrieve(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """
        Retrieve a Card

        Args:
          card_id: The identifier of the Card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            f"/cards/{card_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def update(
        self,
        card_id: str,
        *,
        billing_address: card_update_params.BillingAddress | Omit = omit,
        description: str | Omit = omit,
        digital_wallet: card_update_params.DigitalWallet | Omit = omit,
        entity_id: str | Omit = omit,
        status: Literal["active", "disabled", "canceled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Card:
        """
        Update a Card

        Args:
          card_id: The card identifier.

          billing_address: The card's updated billing address.

          description: The description you choose to give the card.

          digital_wallet: The contact information used in the two-factor steps for digital wallet card
              creation. At least one field must be present to complete the digital wallet
              steps.

          entity_id: The Entity the card belongs to. You only need to supply this in rare situations
              when the card is not for the Account holder.

          status: The status to update the Card with.

              - `active` - The card is active.
              - `disabled` - The card is temporarily disabled.
              - `canceled` - The card is permanently canceled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._patch(
            f"/cards/{card_id}",
            body=await async_maybe_transform(
                {
                    "billing_address": billing_address,
                    "description": description,
                    "digital_wallet": digital_wallet,
                    "entity_id": entity_id,
                    "status": status,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: card_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: card_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Card, AsyncPage[Card]]:
        """
        List Cards

        Args:
          account_id: Filter Cards to ones belonging to the specified Account.

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
            "/cards",
            page=AsyncPage[Card],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            model=Card,
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
          card_id: The identifier of the Card to create an iframe for.

          physical_card_id: The identifier of the Physical Card to create an iframe for. This will inform
              the appearance of the card rendered in the iframe.

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
                {"physical_card_id": physical_card_id}, card_create_details_iframe_params.CardCreateDetailsIframeParams
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

    async def update_pin(
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
          card_id: The identifier of the Card to update the PIN for.

          pin: The 4-digit PIN for the card, for use with ATMs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._post(
            f"/cards/{card_id}/update_pin",
            body=await async_maybe_transform({"pin": pin}, card_update_pin_params.CardUpdatePinParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDetails,
        )


class CardsResourceWithRawResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.create = to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = to_raw_response_wrapper(
            cards.update,
        )
        self.list = to_raw_response_wrapper(
            cards.list,
        )
        self.create_details_iframe = to_raw_response_wrapper(
            cards.create_details_iframe,
        )
        self.details = to_raw_response_wrapper(
            cards.details,
        )
        self.update_pin = to_raw_response_wrapper(
            cards.update_pin,
        )


class AsyncCardsResourceWithRawResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.create = async_to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            cards.update,
        )
        self.list = async_to_raw_response_wrapper(
            cards.list,
        )
        self.create_details_iframe = async_to_raw_response_wrapper(
            cards.create_details_iframe,
        )
        self.details = async_to_raw_response_wrapper(
            cards.details,
        )
        self.update_pin = async_to_raw_response_wrapper(
            cards.update_pin,
        )


class CardsResourceWithStreamingResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.create = to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            cards.update,
        )
        self.list = to_streamed_response_wrapper(
            cards.list,
        )
        self.create_details_iframe = to_streamed_response_wrapper(
            cards.create_details_iframe,
        )
        self.details = to_streamed_response_wrapper(
            cards.details,
        )
        self.update_pin = to_streamed_response_wrapper(
            cards.update_pin,
        )


class AsyncCardsResourceWithStreamingResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.create = async_to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            cards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cards.list,
        )
        self.create_details_iframe = async_to_streamed_response_wrapper(
            cards.create_details_iframe,
        )
        self.details = async_to_streamed_response_wrapper(
            cards.details,
        )
        self.update_pin = async_to_streamed_response_wrapper(
            cards.update_pin,
        )
