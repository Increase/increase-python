# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.intrafi import IntrafiAccountEnrollment, account_enrollment_list_params, account_enrollment_create_params

__all__ = ["AccountEnrollments", "AsyncAccountEnrollments"]


class AccountEnrollments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountEnrollmentsWithRawResponse:
        return AccountEnrollmentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountEnrollmentsWithStreamingResponse:
        return AccountEnrollmentsWithStreamingResponse(self)

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
        Enroll an account in the IntraFi deposit sweep network.

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
                account_enrollment_create_params.AccountEnrollmentCreateParams,
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
        limit: int | NotGiven = NOT_GIVEN,
        status: account_enrollment_list_params.Status | NotGiven = NOT_GIVEN,
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
                        "limit": limit,
                        "status": status,
                    },
                    account_enrollment_list_params.AccountEnrollmentListParams,
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
        Unenroll an account from IntraFi.

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


class AsyncAccountEnrollments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountEnrollmentsWithRawResponse:
        return AsyncAccountEnrollmentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountEnrollmentsWithStreamingResponse:
        return AsyncAccountEnrollmentsWithStreamingResponse(self)

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
        Enroll an account in the IntraFi deposit sweep network.

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
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "email_address": email_address,
                },
                account_enrollment_create_params.AccountEnrollmentCreateParams,
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
        limit: int | NotGiven = NOT_GIVEN,
        status: account_enrollment_list_params.Status | NotGiven = NOT_GIVEN,
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
                        "limit": limit,
                        "status": status,
                    },
                    account_enrollment_list_params.AccountEnrollmentListParams,
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
        Unenroll an account from IntraFi.

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


class AccountEnrollmentsWithRawResponse:
    def __init__(self, account_enrollments: AccountEnrollments) -> None:
        self._account_enrollments = account_enrollments

        self.create = _legacy_response.to_raw_response_wrapper(
            account_enrollments.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            account_enrollments.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            account_enrollments.list,
        )
        self.unenroll = _legacy_response.to_raw_response_wrapper(
            account_enrollments.unenroll,
        )


class AsyncAccountEnrollmentsWithRawResponse:
    def __init__(self, account_enrollments: AsyncAccountEnrollments) -> None:
        self._account_enrollments = account_enrollments

        self.create = _legacy_response.async_to_raw_response_wrapper(
            account_enrollments.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            account_enrollments.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            account_enrollments.list,
        )
        self.unenroll = _legacy_response.async_to_raw_response_wrapper(
            account_enrollments.unenroll,
        )


class AccountEnrollmentsWithStreamingResponse:
    def __init__(self, account_enrollments: AccountEnrollments) -> None:
        self._account_enrollments = account_enrollments

        self.create = to_streamed_response_wrapper(
            account_enrollments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            account_enrollments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            account_enrollments.list,
        )
        self.unenroll = to_streamed_response_wrapper(
            account_enrollments.unenroll,
        )


class AsyncAccountEnrollmentsWithStreamingResponse:
    def __init__(self, account_enrollments: AsyncAccountEnrollments) -> None:
        self._account_enrollments = account_enrollments

        self.create = async_to_streamed_response_wrapper(
            account_enrollments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            account_enrollments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            account_enrollments.list,
        )
        self.unenroll = async_to_streamed_response_wrapper(
            account_enrollments.unenroll,
        )
