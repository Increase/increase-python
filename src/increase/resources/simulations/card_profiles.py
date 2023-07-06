# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import CardProfile
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

__all__ = ["CardProfiles", "AsyncCardProfiles"]


class CardProfiles(SyncAPIResource):
    def approve(
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
    async def approve(
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
