# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    digital_card_profile_list_params,
    digital_card_profile_clone_params,
    digital_card_profile_create_params,
)
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
from ..types.digital_card_profile import DigitalCardProfile

__all__ = ["DigitalCardProfilesResource", "AsyncDigitalCardProfilesResource"]


class DigitalCardProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DigitalCardProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return DigitalCardProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DigitalCardProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return DigitalCardProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        app_icon_file_id: str,
        background_image_file_id: str,
        card_description: str,
        description: str,
        issuer_name: str,
        contact_email: str | NotGiven = NOT_GIVEN,
        contact_phone: str | NotGiven = NOT_GIVEN,
        contact_website: str | NotGiven = NOT_GIVEN,
        text_color: digital_card_profile_create_params.TextColor | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DigitalCardProfile:
        """
        Create a Digital Card Profile

        Args:
          app_icon_file_id: The identifier of the File containing the card's icon image.

          background_image_file_id: The identifier of the File containing the card's front image.

          card_description: A user-facing description for the card itself.

          description: A description you can use to identify the Card Profile.

          issuer_name: A user-facing description for whoever is issuing the card.

          contact_email: An email address the user can contact to receive support for their card.

          contact_phone: A phone number the user can contact to receive support for their card.

          contact_website: A website the user can visit to view and receive support for their card.

          text_color: The Card's text color, specified as an RGB triple. The default is white.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/digital_card_profiles",
            body=maybe_transform(
                {
                    "app_icon_file_id": app_icon_file_id,
                    "background_image_file_id": background_image_file_id,
                    "card_description": card_description,
                    "description": description,
                    "issuer_name": issuer_name,
                    "contact_email": contact_email,
                    "contact_phone": contact_phone,
                    "contact_website": contact_website,
                    "text_color": text_color,
                },
                digital_card_profile_create_params.DigitalCardProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DigitalCardProfile,
        )

    def retrieve(
        self,
        digital_card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DigitalCardProfile:
        """
        Retrieve a Digital Card Profile

        Args:
          digital_card_profile_id: The identifier of the Digital Card Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not digital_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `digital_card_profile_id` but received {digital_card_profile_id!r}"
            )
        return self._get(
            f"/digital_card_profiles/{digital_card_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DigitalCardProfile,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: digital_card_profile_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[DigitalCardProfile]:
        """
        List Card Profiles

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
            "/digital_card_profiles",
            page=SyncPage[DigitalCardProfile],
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
                    digital_card_profile_list_params.DigitalCardProfileListParams,
                ),
            ),
            model=DigitalCardProfile,
        )

    def archive(
        self,
        digital_card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DigitalCardProfile:
        """
        Archive a Digital Card Profile

        Args:
          digital_card_profile_id: The identifier of the Digital Card Profile to archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not digital_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `digital_card_profile_id` but received {digital_card_profile_id!r}"
            )
        return self._post(
            f"/digital_card_profiles/{digital_card_profile_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DigitalCardProfile,
        )

    def clone(
        self,
        digital_card_profile_id: str,
        *,
        app_icon_file_id: str | NotGiven = NOT_GIVEN,
        background_image_file_id: str | NotGiven = NOT_GIVEN,
        card_description: str | NotGiven = NOT_GIVEN,
        contact_email: str | NotGiven = NOT_GIVEN,
        contact_phone: str | NotGiven = NOT_GIVEN,
        contact_website: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        issuer_name: str | NotGiven = NOT_GIVEN,
        text_color: digital_card_profile_clone_params.TextColor | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DigitalCardProfile:
        """
        Clones a Digital Card Profile

        Args:
          digital_card_profile_id: The identifier of the Digital Card Profile to clone.

          app_icon_file_id: The identifier of the File containing the card's icon image.

          background_image_file_id: The identifier of the File containing the card's front image.

          card_description: A user-facing description for the card itself.

          contact_email: An email address the user can contact to receive support for their card.

          contact_phone: A phone number the user can contact to receive support for their card.

          contact_website: A website the user can visit to view and receive support for their card.

          description: A description you can use to identify the Card Profile.

          issuer_name: A user-facing description for whoever is issuing the card.

          text_color: The Card's text color, specified as an RGB triple. The default is white.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not digital_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `digital_card_profile_id` but received {digital_card_profile_id!r}"
            )
        return self._post(
            f"/digital_card_profiles/{digital_card_profile_id}/clone",
            body=maybe_transform(
                {
                    "app_icon_file_id": app_icon_file_id,
                    "background_image_file_id": background_image_file_id,
                    "card_description": card_description,
                    "contact_email": contact_email,
                    "contact_phone": contact_phone,
                    "contact_website": contact_website,
                    "description": description,
                    "issuer_name": issuer_name,
                    "text_color": text_color,
                },
                digital_card_profile_clone_params.DigitalCardProfileCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DigitalCardProfile,
        )


class AsyncDigitalCardProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDigitalCardProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDigitalCardProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDigitalCardProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncDigitalCardProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        app_icon_file_id: str,
        background_image_file_id: str,
        card_description: str,
        description: str,
        issuer_name: str,
        contact_email: str | NotGiven = NOT_GIVEN,
        contact_phone: str | NotGiven = NOT_GIVEN,
        contact_website: str | NotGiven = NOT_GIVEN,
        text_color: digital_card_profile_create_params.TextColor | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DigitalCardProfile:
        """
        Create a Digital Card Profile

        Args:
          app_icon_file_id: The identifier of the File containing the card's icon image.

          background_image_file_id: The identifier of the File containing the card's front image.

          card_description: A user-facing description for the card itself.

          description: A description you can use to identify the Card Profile.

          issuer_name: A user-facing description for whoever is issuing the card.

          contact_email: An email address the user can contact to receive support for their card.

          contact_phone: A phone number the user can contact to receive support for their card.

          contact_website: A website the user can visit to view and receive support for their card.

          text_color: The Card's text color, specified as an RGB triple. The default is white.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/digital_card_profiles",
            body=await async_maybe_transform(
                {
                    "app_icon_file_id": app_icon_file_id,
                    "background_image_file_id": background_image_file_id,
                    "card_description": card_description,
                    "description": description,
                    "issuer_name": issuer_name,
                    "contact_email": contact_email,
                    "contact_phone": contact_phone,
                    "contact_website": contact_website,
                    "text_color": text_color,
                },
                digital_card_profile_create_params.DigitalCardProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DigitalCardProfile,
        )

    async def retrieve(
        self,
        digital_card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DigitalCardProfile:
        """
        Retrieve a Digital Card Profile

        Args:
          digital_card_profile_id: The identifier of the Digital Card Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not digital_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `digital_card_profile_id` but received {digital_card_profile_id!r}"
            )
        return await self._get(
            f"/digital_card_profiles/{digital_card_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DigitalCardProfile,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: digital_card_profile_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DigitalCardProfile, AsyncPage[DigitalCardProfile]]:
        """
        List Card Profiles

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
            "/digital_card_profiles",
            page=AsyncPage[DigitalCardProfile],
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
                    digital_card_profile_list_params.DigitalCardProfileListParams,
                ),
            ),
            model=DigitalCardProfile,
        )

    async def archive(
        self,
        digital_card_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DigitalCardProfile:
        """
        Archive a Digital Card Profile

        Args:
          digital_card_profile_id: The identifier of the Digital Card Profile to archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not digital_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `digital_card_profile_id` but received {digital_card_profile_id!r}"
            )
        return await self._post(
            f"/digital_card_profiles/{digital_card_profile_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DigitalCardProfile,
        )

    async def clone(
        self,
        digital_card_profile_id: str,
        *,
        app_icon_file_id: str | NotGiven = NOT_GIVEN,
        background_image_file_id: str | NotGiven = NOT_GIVEN,
        card_description: str | NotGiven = NOT_GIVEN,
        contact_email: str | NotGiven = NOT_GIVEN,
        contact_phone: str | NotGiven = NOT_GIVEN,
        contact_website: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        issuer_name: str | NotGiven = NOT_GIVEN,
        text_color: digital_card_profile_clone_params.TextColor | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DigitalCardProfile:
        """
        Clones a Digital Card Profile

        Args:
          digital_card_profile_id: The identifier of the Digital Card Profile to clone.

          app_icon_file_id: The identifier of the File containing the card's icon image.

          background_image_file_id: The identifier of the File containing the card's front image.

          card_description: A user-facing description for the card itself.

          contact_email: An email address the user can contact to receive support for their card.

          contact_phone: A phone number the user can contact to receive support for their card.

          contact_website: A website the user can visit to view and receive support for their card.

          description: A description you can use to identify the Card Profile.

          issuer_name: A user-facing description for whoever is issuing the card.

          text_color: The Card's text color, specified as an RGB triple. The default is white.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not digital_card_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `digital_card_profile_id` but received {digital_card_profile_id!r}"
            )
        return await self._post(
            f"/digital_card_profiles/{digital_card_profile_id}/clone",
            body=await async_maybe_transform(
                {
                    "app_icon_file_id": app_icon_file_id,
                    "background_image_file_id": background_image_file_id,
                    "card_description": card_description,
                    "contact_email": contact_email,
                    "contact_phone": contact_phone,
                    "contact_website": contact_website,
                    "description": description,
                    "issuer_name": issuer_name,
                    "text_color": text_color,
                },
                digital_card_profile_clone_params.DigitalCardProfileCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DigitalCardProfile,
        )


class DigitalCardProfilesResourceWithRawResponse:
    def __init__(self, digital_card_profiles: DigitalCardProfilesResource) -> None:
        self._digital_card_profiles = digital_card_profiles

        self.create = to_raw_response_wrapper(
            digital_card_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            digital_card_profiles.retrieve,
        )
        self.list = to_raw_response_wrapper(
            digital_card_profiles.list,
        )
        self.archive = to_raw_response_wrapper(
            digital_card_profiles.archive,
        )
        self.clone = to_raw_response_wrapper(
            digital_card_profiles.clone,
        )


class AsyncDigitalCardProfilesResourceWithRawResponse:
    def __init__(self, digital_card_profiles: AsyncDigitalCardProfilesResource) -> None:
        self._digital_card_profiles = digital_card_profiles

        self.create = async_to_raw_response_wrapper(
            digital_card_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            digital_card_profiles.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            digital_card_profiles.list,
        )
        self.archive = async_to_raw_response_wrapper(
            digital_card_profiles.archive,
        )
        self.clone = async_to_raw_response_wrapper(
            digital_card_profiles.clone,
        )


class DigitalCardProfilesResourceWithStreamingResponse:
    def __init__(self, digital_card_profiles: DigitalCardProfilesResource) -> None:
        self._digital_card_profiles = digital_card_profiles

        self.create = to_streamed_response_wrapper(
            digital_card_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            digital_card_profiles.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            digital_card_profiles.list,
        )
        self.archive = to_streamed_response_wrapper(
            digital_card_profiles.archive,
        )
        self.clone = to_streamed_response_wrapper(
            digital_card_profiles.clone,
        )


class AsyncDigitalCardProfilesResourceWithStreamingResponse:
    def __init__(self, digital_card_profiles: AsyncDigitalCardProfilesResource) -> None:
        self._digital_card_profiles = digital_card_profiles

        self.create = async_to_streamed_response_wrapper(
            digital_card_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            digital_card_profiles.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            digital_card_profiles.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            digital_card_profiles.archive,
        )
        self.clone = async_to_streamed_response_wrapper(
            digital_card_profiles.clone,
        )
