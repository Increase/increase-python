# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ...types import CardProfile
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["CardProfiles", "AsyncCardProfiles"]


class CardProfiles(SyncAPIResource):
    with_raw_response: CardProfilesWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = CardProfilesWithRawResponse(self)

    def approve(
        self,
        card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardProfile:
        """
        After a [Card Profile](#card-profile) is created in production, the images will
        be uploaded to Visa within one day. Since Card Profiles are not uploaded to Visa
        in sandbox, this endpoint simulates that step. Invoking this simulation triggers
        the webhooks Increase sends when the Card Profile is approved and updates the
        status of the Card Profile.

        Args:
          card_profile_id: The card profile you would like to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/simulations/card_profiles/{card_profile_id}/approve",
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

    async def approve(
        self,
        card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardProfile:
        """
        After a [Card Profile](#card-profile) is created in production, the images will
        be uploaded to Visa within one day. Since Card Profiles are not uploaded to Visa
        in sandbox, this endpoint simulates that step. Invoking this simulation triggers
        the webhooks Increase sends when the Card Profile is approved and updates the
        status of the Card Profile.

        Args:
          card_profile_id: The card profile you would like to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/simulations/card_profiles/{card_profile_id}/approve",
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
        self.approve = to_raw_response_wrapper(
            card_profiles.approve,
        )


class AsyncCardProfilesWithRawResponse:
    def __init__(self, card_profiles: AsyncCardProfiles) -> None:
        self.approve = async_to_raw_response_wrapper(
            card_profiles.approve,
        )
