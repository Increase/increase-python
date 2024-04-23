# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import (
    physical_card_profile_list_params,
    physical_card_profile_clone_params,
    physical_card_profile_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.physical_card_profile import PhysicalCardProfile

__all__ = ["PhysicalCardProfiles", "AsyncPhysicalCardProfiles"]


class PhysicalCardProfiles(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhysicalCardProfilesWithRawResponse:
        return PhysicalCardProfilesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhysicalCardProfilesWithStreamingResponse:
        return PhysicalCardProfilesWithStreamingResponse(self)

    def create(
        self,
        *,
        carrier_image_file_id: str,
        contact_phone: str,
        description: str,
        front_image_file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCardProfile:
        """
        Create a Physical Card Profile

        Args:
          carrier_image_file_id: The identifier of the File containing the physical card's carrier image.

          contact_phone: A phone number the user can contact to receive support for their card.

          description: A description you can use to identify the Card Profile.

          front_image_file_id: The identifier of the File containing the physical card's front image.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/physical_card_profiles",
            body=maybe_transform(
                {
                    "carrier_image_file_id": carrier_image_file_id,
                    "contact_phone": contact_phone,
                    "description": description,
                    "front_image_file_id": front_image_file_id,
                },
                physical_card_profile_create_params.PhysicalCardProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCardProfile,
        )

    def retrieve(
        self,
        physical_card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhysicalCardProfile:
        """
        Retrieve a Card Profile

        Args:
          physical_card_profile_id: The identifier of the Card Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not physical_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `physical_card_profile_id` but received {physical_card_profile_id!r}"
            )
        return self._get(
            f"/physical_card_profiles/{physical_card_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhysicalCardProfile,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: physical_card_profile_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PhysicalCardProfile]:
        """
        List Physical Card Profiles

        Args:
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
            "/physical_card_profiles",
            page=SyncPage[PhysicalCardProfile],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    physical_card_profile_list_params.PhysicalCardProfileListParams,
                ),
            ),
            model=PhysicalCardProfile,
        )

    def archive(
        self,
        physical_card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCardProfile:
        """
        Archive a Physical Card Profile

        Args:
          physical_card_profile_id: The identifier of the Physical Card Profile to archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `physical_card_profile_id` but received {physical_card_profile_id!r}"
            )
        return self._post(
            f"/physical_card_profiles/{physical_card_profile_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCardProfile,
        )

    def clone(
        self,
        physical_card_profile_id: str,
        *,
        carrier_image_file_id: str | NotGiven = NOT_GIVEN,
        contact_phone: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        front_image_file_id: str | NotGiven = NOT_GIVEN,
        front_text: physical_card_profile_clone_params.FrontText | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCardProfile:
        """
        Clone a Physical Card Profile

        Args:
          physical_card_profile_id: The identifier of the Physical Card Profile to clone.

          carrier_image_file_id: The identifier of the File containing the physical card's carrier image.

          contact_phone: A phone number the user can contact to receive support for their card.

          description: A description you can use to identify the Card Profile.

          front_image_file_id: The identifier of the File containing the physical card's front image.

          front_text: Text printed on the front of the card. Reach out to
              [support@increase.com](mailto:support@increase.com) for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `physical_card_profile_id` but received {physical_card_profile_id!r}"
            )
        return self._post(
            f"/physical_card_profiles/{physical_card_profile_id}/clone",
            body=maybe_transform(
                {
                    "carrier_image_file_id": carrier_image_file_id,
                    "contact_phone": contact_phone,
                    "description": description,
                    "front_image_file_id": front_image_file_id,
                    "front_text": front_text,
                },
                physical_card_profile_clone_params.PhysicalCardProfileCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCardProfile,
        )


class AsyncPhysicalCardProfiles(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhysicalCardProfilesWithRawResponse:
        return AsyncPhysicalCardProfilesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhysicalCardProfilesWithStreamingResponse:
        return AsyncPhysicalCardProfilesWithStreamingResponse(self)

    async def create(
        self,
        *,
        carrier_image_file_id: str,
        contact_phone: str,
        description: str,
        front_image_file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCardProfile:
        """
        Create a Physical Card Profile

        Args:
          carrier_image_file_id: The identifier of the File containing the physical card's carrier image.

          contact_phone: A phone number the user can contact to receive support for their card.

          description: A description you can use to identify the Card Profile.

          front_image_file_id: The identifier of the File containing the physical card's front image.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/physical_card_profiles",
            body=await async_maybe_transform(
                {
                    "carrier_image_file_id": carrier_image_file_id,
                    "contact_phone": contact_phone,
                    "description": description,
                    "front_image_file_id": front_image_file_id,
                },
                physical_card_profile_create_params.PhysicalCardProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCardProfile,
        )

    async def retrieve(
        self,
        physical_card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhysicalCardProfile:
        """
        Retrieve a Card Profile

        Args:
          physical_card_profile_id: The identifier of the Card Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not physical_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `physical_card_profile_id` but received {physical_card_profile_id!r}"
            )
        return await self._get(
            f"/physical_card_profiles/{physical_card_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhysicalCardProfile,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: physical_card_profile_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PhysicalCardProfile, AsyncPage[PhysicalCardProfile]]:
        """
        List Physical Card Profiles

        Args:
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
            "/physical_card_profiles",
            page=AsyncPage[PhysicalCardProfile],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    physical_card_profile_list_params.PhysicalCardProfileListParams,
                ),
            ),
            model=PhysicalCardProfile,
        )

    async def archive(
        self,
        physical_card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCardProfile:
        """
        Archive a Physical Card Profile

        Args:
          physical_card_profile_id: The identifier of the Physical Card Profile to archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `physical_card_profile_id` but received {physical_card_profile_id!r}"
            )
        return await self._post(
            f"/physical_card_profiles/{physical_card_profile_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCardProfile,
        )

    async def clone(
        self,
        physical_card_profile_id: str,
        *,
        carrier_image_file_id: str | NotGiven = NOT_GIVEN,
        contact_phone: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        front_image_file_id: str | NotGiven = NOT_GIVEN,
        front_text: physical_card_profile_clone_params.FrontText | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PhysicalCardProfile:
        """
        Clone a Physical Card Profile

        Args:
          physical_card_profile_id: The identifier of the Physical Card Profile to clone.

          carrier_image_file_id: The identifier of the File containing the physical card's carrier image.

          contact_phone: A phone number the user can contact to receive support for their card.

          description: A description you can use to identify the Card Profile.

          front_image_file_id: The identifier of the File containing the physical card's front image.

          front_text: Text printed on the front of the card. Reach out to
              [support@increase.com](mailto:support@increase.com) for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `physical_card_profile_id` but received {physical_card_profile_id!r}"
            )
        return await self._post(
            f"/physical_card_profiles/{physical_card_profile_id}/clone",
            body=await async_maybe_transform(
                {
                    "carrier_image_file_id": carrier_image_file_id,
                    "contact_phone": contact_phone,
                    "description": description,
                    "front_image_file_id": front_image_file_id,
                    "front_text": front_text,
                },
                physical_card_profile_clone_params.PhysicalCardProfileCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCardProfile,
        )


class PhysicalCardProfilesWithRawResponse:
    def __init__(self, physical_card_profiles: PhysicalCardProfiles) -> None:
        self._physical_card_profiles = physical_card_profiles

        self.create = _legacy_response.to_raw_response_wrapper(
            physical_card_profiles.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            physical_card_profiles.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            physical_card_profiles.list,
        )
        self.archive = _legacy_response.to_raw_response_wrapper(
            physical_card_profiles.archive,
        )
        self.clone = _legacy_response.to_raw_response_wrapper(
            physical_card_profiles.clone,
        )


class AsyncPhysicalCardProfilesWithRawResponse:
    def __init__(self, physical_card_profiles: AsyncPhysicalCardProfiles) -> None:
        self._physical_card_profiles = physical_card_profiles

        self.create = _legacy_response.async_to_raw_response_wrapper(
            physical_card_profiles.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            physical_card_profiles.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            physical_card_profiles.list,
        )
        self.archive = _legacy_response.async_to_raw_response_wrapper(
            physical_card_profiles.archive,
        )
        self.clone = _legacy_response.async_to_raw_response_wrapper(
            physical_card_profiles.clone,
        )


class PhysicalCardProfilesWithStreamingResponse:
    def __init__(self, physical_card_profiles: PhysicalCardProfiles) -> None:
        self._physical_card_profiles = physical_card_profiles

        self.create = to_streamed_response_wrapper(
            physical_card_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            physical_card_profiles.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            physical_card_profiles.list,
        )
        self.archive = to_streamed_response_wrapper(
            physical_card_profiles.archive,
        )
        self.clone = to_streamed_response_wrapper(
            physical_card_profiles.clone,
        )


class AsyncPhysicalCardProfilesWithStreamingResponse:
    def __init__(self, physical_card_profiles: AsyncPhysicalCardProfiles) -> None:
        self._physical_card_profiles = physical_card_profiles

        self.create = async_to_streamed_response_wrapper(
            physical_card_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            physical_card_profiles.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            physical_card_profiles.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            physical_card_profiles.archive,
        )
        self.clone = async_to_streamed_response_wrapper(
            physical_card_profiles.clone,
        )
