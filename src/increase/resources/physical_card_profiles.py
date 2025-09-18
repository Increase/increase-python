# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    physical_card_profile_list_params,
    physical_card_profile_clone_params,
    physical_card_profile_create_params,
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
from .._base_client import AsyncPaginator, make_request_options
from ..types.physical_card_profile import PhysicalCardProfile

__all__ = ["PhysicalCardProfilesResource", "AsyncPhysicalCardProfilesResource"]


class PhysicalCardProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhysicalCardProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return PhysicalCardProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhysicalCardProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return PhysicalCardProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        carrier_image_file_id: str,
        contact_phone: str,
        description: str,
        front_image_file_id: str,
        program_id: str,
        back_color: Literal["black", "white"] | Omit = omit,
        card_stock_reference: str | Omit = omit,
        carrier_stock_reference: str | Omit = omit,
        front_color: Literal["black", "white"] | Omit = omit,
        front_text: physical_card_profile_create_params.FrontText | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PhysicalCardProfile:
        """
        Create a Physical Card Profile

        Args:
          carrier_image_file_id: The identifier of the File containing the physical card's carrier image.

          contact_phone: A phone number the user can contact to receive support for their card.

          description: A description you can use to identify the Card Profile.

          front_image_file_id: The identifier of the File containing the physical card's front image.

          program_id: The identifier for the Program that this Physical Card Profile falls under.

          back_color: The color of the text on the back of the card. Defaults to "black".

              - `black` - Black personalization color.
              - `white` - White personalization color.

          card_stock_reference: A reference ID provided by the fulfillment provider for the card stock used.
              Only used if you've ordered card stock separately.

          carrier_stock_reference: A reference ID provided by the fulfillment provider for the carrier stock used.
              Only used if you've ordered carrier stock separately.

          front_color: The color of the design on the front of the card. Defaults to "black".

              - `black` - Black personalization color.
              - `white` - White personalization color.

          front_text: Text printed on the front of the card. Reach out to
              [support@increase.com](mailto:support@increase.com) for more information.

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
                    "program_id": program_id,
                    "back_color": back_color,
                    "card_stock_reference": card_stock_reference,
                    "carrier_stock_reference": carrier_stock_reference,
                    "front_color": front_color,
                    "front_text": front_text,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: physical_card_profile_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        carrier_image_file_id: str | Omit = omit,
        contact_phone: str | Omit = omit,
        description: str | Omit = omit,
        front_image_file_id: str | Omit = omit,
        front_text: physical_card_profile_clone_params.FrontText | Omit = omit,
        program_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          program_id: The identifier of the Program to use for the cloned Physical Card Profile.

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
                    "program_id": program_id,
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


class AsyncPhysicalCardProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhysicalCardProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhysicalCardProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhysicalCardProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncPhysicalCardProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        carrier_image_file_id: str,
        contact_phone: str,
        description: str,
        front_image_file_id: str,
        program_id: str,
        back_color: Literal["black", "white"] | Omit = omit,
        card_stock_reference: str | Omit = omit,
        carrier_stock_reference: str | Omit = omit,
        front_color: Literal["black", "white"] | Omit = omit,
        front_text: physical_card_profile_create_params.FrontText | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PhysicalCardProfile:
        """
        Create a Physical Card Profile

        Args:
          carrier_image_file_id: The identifier of the File containing the physical card's carrier image.

          contact_phone: A phone number the user can contact to receive support for their card.

          description: A description you can use to identify the Card Profile.

          front_image_file_id: The identifier of the File containing the physical card's front image.

          program_id: The identifier for the Program that this Physical Card Profile falls under.

          back_color: The color of the text on the back of the card. Defaults to "black".

              - `black` - Black personalization color.
              - `white` - White personalization color.

          card_stock_reference: A reference ID provided by the fulfillment provider for the card stock used.
              Only used if you've ordered card stock separately.

          carrier_stock_reference: A reference ID provided by the fulfillment provider for the carrier stock used.
              Only used if you've ordered carrier stock separately.

          front_color: The color of the design on the front of the card. Defaults to "black".

              - `black` - Black personalization color.
              - `white` - White personalization color.

          front_text: Text printed on the front of the card. Reach out to
              [support@increase.com](mailto:support@increase.com) for more information.

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
                    "program_id": program_id,
                    "back_color": back_color,
                    "card_stock_reference": card_stock_reference,
                    "carrier_stock_reference": carrier_stock_reference,
                    "front_color": front_color,
                    "front_text": front_text,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: physical_card_profile_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        carrier_image_file_id: str | Omit = omit,
        contact_phone: str | Omit = omit,
        description: str | Omit = omit,
        front_image_file_id: str | Omit = omit,
        front_text: physical_card_profile_clone_params.FrontText | Omit = omit,
        program_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          program_id: The identifier of the Program to use for the cloned Physical Card Profile.

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
                    "program_id": program_id,
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


class PhysicalCardProfilesResourceWithRawResponse:
    def __init__(self, physical_card_profiles: PhysicalCardProfilesResource) -> None:
        self._physical_card_profiles = physical_card_profiles

        self.create = to_raw_response_wrapper(
            physical_card_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            physical_card_profiles.retrieve,
        )
        self.list = to_raw_response_wrapper(
            physical_card_profiles.list,
        )
        self.archive = to_raw_response_wrapper(
            physical_card_profiles.archive,
        )
        self.clone = to_raw_response_wrapper(
            physical_card_profiles.clone,
        )


class AsyncPhysicalCardProfilesResourceWithRawResponse:
    def __init__(self, physical_card_profiles: AsyncPhysicalCardProfilesResource) -> None:
        self._physical_card_profiles = physical_card_profiles

        self.create = async_to_raw_response_wrapper(
            physical_card_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            physical_card_profiles.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            physical_card_profiles.list,
        )
        self.archive = async_to_raw_response_wrapper(
            physical_card_profiles.archive,
        )
        self.clone = async_to_raw_response_wrapper(
            physical_card_profiles.clone,
        )


class PhysicalCardProfilesResourceWithStreamingResponse:
    def __init__(self, physical_card_profiles: PhysicalCardProfilesResource) -> None:
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


class AsyncPhysicalCardProfilesResourceWithStreamingResponse:
    def __init__(self, physical_card_profiles: AsyncPhysicalCardProfilesResource) -> None:
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
