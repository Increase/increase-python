# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import intrafi_account_enrollment_list_params, intrafi_account_enrollment_create_params
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
from ..types.intrafi_account_enrollment import IntrafiAccountEnrollment

__all__ = ["IntrafiAccountEnrollmentsResource", "AsyncIntrafiAccountEnrollmentsResource"]


class IntrafiAccountEnrollmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntrafiAccountEnrollmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return IntrafiAccountEnrollmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntrafiAccountEnrollmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return IntrafiAccountEnrollmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        email_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> IntrafiAccountEnrollment:
        """
        Enroll an account in the IntraFi deposit sweep network

        Args:
          account_id: The identifier for the account to be added to IntraFi.

          email_address: The contact email for the account owner, to be shared with IntraFi.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/intrafi_account_enrollments",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "email_address": email_address,
                },
                intrafi_account_enrollment_create_params.IntrafiAccountEnrollmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=IntrafiAccountEnrollment,
        )

    def retrieve(
        self,
        intrafi_account_enrollment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntrafiAccountEnrollment:
        """
        Get an IntraFi Account Enrollment

        Args:
          intrafi_account_enrollment_id: The identifier of the IntraFi Account Enrollment to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not intrafi_account_enrollment_id:
            raise ValueError(
                f"Expected a non-empty value for `intrafi_account_enrollment_id` but received {intrafi_account_enrollment_id!r}"
            )
        return self._get(
            f"/intrafi_account_enrollments/{intrafi_account_enrollment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntrafiAccountEnrollment,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: intrafi_account_enrollment_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[IntrafiAccountEnrollment]:
        """
        List IntraFi Account Enrollments

        Args:
          account_id: Filter IntraFi Account Enrollments to the one belonging to an account.

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
            "/intrafi_account_enrollments",
            page=SyncPage[IntrafiAccountEnrollment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    intrafi_account_enrollment_list_params.IntrafiAccountEnrollmentListParams,
                ),
            ),
            model=IntrafiAccountEnrollment,
        )

    def unenroll(
        self,
        intrafi_account_enrollment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> IntrafiAccountEnrollment:
        """
        Unenroll an account from IntraFi

        Args:
          intrafi_account_enrollment_id: The Identifier of the IntraFi Account Enrollment to remove from IntraFi.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not intrafi_account_enrollment_id:
            raise ValueError(
                f"Expected a non-empty value for `intrafi_account_enrollment_id` but received {intrafi_account_enrollment_id!r}"
            )
        return self._post(
            f"/intrafi_account_enrollments/{intrafi_account_enrollment_id}/unenroll",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=IntrafiAccountEnrollment,
        )


class AsyncIntrafiAccountEnrollmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntrafiAccountEnrollmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntrafiAccountEnrollmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntrafiAccountEnrollmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncIntrafiAccountEnrollmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        email_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> IntrafiAccountEnrollment:
        """
        Enroll an account in the IntraFi deposit sweep network

        Args:
          account_id: The identifier for the account to be added to IntraFi.

          email_address: The contact email for the account owner, to be shared with IntraFi.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/intrafi_account_enrollments",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "email_address": email_address,
                },
                intrafi_account_enrollment_create_params.IntrafiAccountEnrollmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=IntrafiAccountEnrollment,
        )

    async def retrieve(
        self,
        intrafi_account_enrollment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntrafiAccountEnrollment:
        """
        Get an IntraFi Account Enrollment

        Args:
          intrafi_account_enrollment_id: The identifier of the IntraFi Account Enrollment to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not intrafi_account_enrollment_id:
            raise ValueError(
                f"Expected a non-empty value for `intrafi_account_enrollment_id` but received {intrafi_account_enrollment_id!r}"
            )
        return await self._get(
            f"/intrafi_account_enrollments/{intrafi_account_enrollment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntrafiAccountEnrollment,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: intrafi_account_enrollment_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IntrafiAccountEnrollment, AsyncPage[IntrafiAccountEnrollment]]:
        """
        List IntraFi Account Enrollments

        Args:
          account_id: Filter IntraFi Account Enrollments to the one belonging to an account.

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
            "/intrafi_account_enrollments",
            page=AsyncPage[IntrafiAccountEnrollment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    intrafi_account_enrollment_list_params.IntrafiAccountEnrollmentListParams,
                ),
            ),
            model=IntrafiAccountEnrollment,
        )

    async def unenroll(
        self,
        intrafi_account_enrollment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> IntrafiAccountEnrollment:
        """
        Unenroll an account from IntraFi

        Args:
          intrafi_account_enrollment_id: The Identifier of the IntraFi Account Enrollment to remove from IntraFi.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not intrafi_account_enrollment_id:
            raise ValueError(
                f"Expected a non-empty value for `intrafi_account_enrollment_id` but received {intrafi_account_enrollment_id!r}"
            )
        return await self._post(
            f"/intrafi_account_enrollments/{intrafi_account_enrollment_id}/unenroll",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=IntrafiAccountEnrollment,
        )


class IntrafiAccountEnrollmentsResourceWithRawResponse:
    def __init__(self, intrafi_account_enrollments: IntrafiAccountEnrollmentsResource) -> None:
        self._intrafi_account_enrollments = intrafi_account_enrollments

        self.create = to_raw_response_wrapper(
            intrafi_account_enrollments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            intrafi_account_enrollments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            intrafi_account_enrollments.list,
        )
        self.unenroll = to_raw_response_wrapper(
            intrafi_account_enrollments.unenroll,
        )


class AsyncIntrafiAccountEnrollmentsResourceWithRawResponse:
    def __init__(self, intrafi_account_enrollments: AsyncIntrafiAccountEnrollmentsResource) -> None:
        self._intrafi_account_enrollments = intrafi_account_enrollments

        self.create = async_to_raw_response_wrapper(
            intrafi_account_enrollments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            intrafi_account_enrollments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            intrafi_account_enrollments.list,
        )
        self.unenroll = async_to_raw_response_wrapper(
            intrafi_account_enrollments.unenroll,
        )


class IntrafiAccountEnrollmentsResourceWithStreamingResponse:
    def __init__(self, intrafi_account_enrollments: IntrafiAccountEnrollmentsResource) -> None:
        self._intrafi_account_enrollments = intrafi_account_enrollments

        self.create = to_streamed_response_wrapper(
            intrafi_account_enrollments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            intrafi_account_enrollments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            intrafi_account_enrollments.list,
        )
        self.unenroll = to_streamed_response_wrapper(
            intrafi_account_enrollments.unenroll,
        )


class AsyncIntrafiAccountEnrollmentsResourceWithStreamingResponse:
    def __init__(self, intrafi_account_enrollments: AsyncIntrafiAccountEnrollmentsResource) -> None:
        self._intrafi_account_enrollments = intrafi_account_enrollments

        self.create = async_to_streamed_response_wrapper(
            intrafi_account_enrollments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            intrafi_account_enrollments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            intrafi_account_enrollments.list,
        )
        self.unenroll = async_to_streamed_response_wrapper(
            intrafi_account_enrollments.unenroll,
        )
