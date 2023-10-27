# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..types import CardProfile, card_profile_list_params, card_profile_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import Increase, AsyncIncrease

__all__ = ["CardProfiles", "AsyncCardProfiles"]


class CardProfiles(SyncAPIResource):
    with_raw_response: CardProfilesWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = CardProfilesWithRawResponse(self)

    def create(
        self,
        *,
        description: str,
        digital_wallets: card_profile_create_params.DigitalWallets,
        physical_cards: card_profile_create_params.PhysicalCards | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardProfile:
        """
        Create a Card Profile

        Args:
          description: A description you can use to identify the Card Profile.

          digital_wallets: How Cards should appear in digital wallets such as Apple Pay. Different wallets
              will use these values to render card artwork appropriately for their app.

          physical_cards: How physical cards should be designed and shipped.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/card_profiles",
            body=maybe_transform(
                {
                    "description": description,
                    "digital_wallets": digital_wallets,
                    "physical_cards": physical_cards,
                },
                card_profile_create_params.CardProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardProfile,
        )

    def retrieve(
        self,
        card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CardProfile:
        """
        Retrieve a Card Profile

        Args:
          card_profile_id: The identifier of the Card Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/card_profiles/{card_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProfile,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        physical_cards_status: card_profile_list_params.PhysicalCardsStatus | NotGiven = NOT_GIVEN,
        status: card_profile_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CardProfile]:
        """
        List Card Profiles

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_profiles",
            page=SyncPage[CardProfile],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "physical_cards_status": physical_cards_status,
                        "status": status,
                    },
                    card_profile_list_params.CardProfileListParams,
                ),
            ),
            model=CardProfile,
        )

    def archive(
        self,
        card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardProfile:
        """
        Archive an Card Profile

        Args:
          card_profile_id: The identifier of the Card Profile to archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/card_profiles/{card_profile_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardProfile,
        )


class AsyncCardProfiles(AsyncAPIResource):
    with_raw_response: AsyncCardProfilesWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCardProfilesWithRawResponse(self)

    async def create(
        self,
        *,
        description: str,
        digital_wallets: card_profile_create_params.DigitalWallets,
        physical_cards: card_profile_create_params.PhysicalCards | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardProfile:
        """
        Create a Card Profile

        Args:
          description: A description you can use to identify the Card Profile.

          digital_wallets: How Cards should appear in digital wallets such as Apple Pay. Different wallets
              will use these values to render card artwork appropriately for their app.

          physical_cards: How physical cards should be designed and shipped.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/card_profiles",
            body=maybe_transform(
                {
                    "description": description,
                    "digital_wallets": digital_wallets,
                    "physical_cards": physical_cards,
                },
                card_profile_create_params.CardProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardProfile,
        )

    async def retrieve(
        self,
        card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CardProfile:
        """
        Retrieve a Card Profile

        Args:
          card_profile_id: The identifier of the Card Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/card_profiles/{card_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProfile,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        physical_cards_status: card_profile_list_params.PhysicalCardsStatus | NotGiven = NOT_GIVEN,
        status: card_profile_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CardProfile, AsyncPage[CardProfile]]:
        """
        List Card Profiles

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_profiles",
            page=AsyncPage[CardProfile],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "physical_cards_status": physical_cards_status,
                        "status": status,
                    },
                    card_profile_list_params.CardProfileListParams,
                ),
            ),
            model=CardProfile,
        )

    async def archive(
        self,
        card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardProfile:
        """
        Archive an Card Profile

        Args:
          card_profile_id: The identifier of the Card Profile to archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/card_profiles/{card_profile_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardProfile,
        )


class CardProfilesWithRawResponse:
    def __init__(self, card_profiles: CardProfiles) -> None:
        self.create = to_raw_response_wrapper(
            card_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            card_profiles.retrieve,
        )
        self.list = to_raw_response_wrapper(
            card_profiles.list,
        )
        self.archive = to_raw_response_wrapper(
            card_profiles.archive,
        )


class AsyncCardProfilesWithRawResponse:
    def __init__(self, card_profiles: AsyncCardProfiles) -> None:
        self.create = async_to_raw_response_wrapper(
            card_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            card_profiles.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            card_profiles.list,
        )
        self.archive = async_to_raw_response_wrapper(
            card_profiles.archive,
        )
