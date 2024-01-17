# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from .. import _legacy_response
from ..types import (
    ProofOfAuthorizationRequestSubmission,
    proof_of_authorization_request_submission_list_params,
    proof_of_authorization_request_submission_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["ProofOfAuthorizationRequestSubmissions", "AsyncProofOfAuthorizationRequestSubmissions"]


class ProofOfAuthorizationRequestSubmissions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProofOfAuthorizationRequestSubmissionsWithRawResponse:
        return ProofOfAuthorizationRequestSubmissionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProofOfAuthorizationRequestSubmissionsWithStreamingResponse:
        return ProofOfAuthorizationRequestSubmissionsWithStreamingResponse(self)

    def create(
        self,
        *,
        authorization_terms: str,
        authorized_at: Union[str, datetime],
        authorizer_email: str,
        authorizer_name: str,
        proof_of_authorization_request_id: str,
        authorizer_company: str | NotGiven = NOT_GIVEN,
        authorizer_ip_address: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ProofOfAuthorizationRequestSubmission:
        """
        Submit Proof of Authorization

        Args:
          authorization_terms: Terms of authorization.

          authorized_at: Time of authorization.

          authorizer_email: Email of the authorizer.

          authorizer_name: Name of the authorizer.

          proof_of_authorization_request_id: ID of the proof of authorization request.

          authorizer_company: Company of the authorizer.

          authorizer_ip_address: IP address of the authorizer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/proof_of_authorization_request_submissions",
            body=maybe_transform(
                {
                    "authorization_terms": authorization_terms,
                    "authorized_at": authorized_at,
                    "authorizer_email": authorizer_email,
                    "authorizer_name": authorizer_name,
                    "proof_of_authorization_request_id": proof_of_authorization_request_id,
                    "authorizer_company": authorizer_company,
                    "authorizer_ip_address": authorizer_ip_address,
                },
                proof_of_authorization_request_submission_create_params.ProofOfAuthorizationRequestSubmissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ProofOfAuthorizationRequestSubmission,
        )

    def retrieve(
        self,
        proof_of_authorization_request_submission_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProofOfAuthorizationRequestSubmission:
        """
        Retrieve a Proof of Authorization Request Submission

        Args:
          proof_of_authorization_request_submission_id: The identifier of the Proof of Authorization Request Submission.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proof_of_authorization_request_submission_id:
            raise ValueError(
                f"Expected a non-empty value for `proof_of_authorization_request_submission_id` but received {proof_of_authorization_request_submission_id!r}"
            )
        return self._get(
            f"/proof_of_authorization_request_submissions/{proof_of_authorization_request_submission_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProofOfAuthorizationRequestSubmission,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        proof_of_authorization_request_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ProofOfAuthorizationRequestSubmission]:
        """
        List Proof of Authorization Request Submissions

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          proof_of_authorization_request_id: ID of the proof of authorization request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/proof_of_authorization_request_submissions",
            page=SyncPage[ProofOfAuthorizationRequestSubmission],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "proof_of_authorization_request_id": proof_of_authorization_request_id,
                    },
                    proof_of_authorization_request_submission_list_params.ProofOfAuthorizationRequestSubmissionListParams,
                ),
            ),
            model=ProofOfAuthorizationRequestSubmission,
        )


class AsyncProofOfAuthorizationRequestSubmissions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProofOfAuthorizationRequestSubmissionsWithRawResponse:
        return AsyncProofOfAuthorizationRequestSubmissionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProofOfAuthorizationRequestSubmissionsWithStreamingResponse:
        return AsyncProofOfAuthorizationRequestSubmissionsWithStreamingResponse(self)

    async def create(
        self,
        *,
        authorization_terms: str,
        authorized_at: Union[str, datetime],
        authorizer_email: str,
        authorizer_name: str,
        proof_of_authorization_request_id: str,
        authorizer_company: str | NotGiven = NOT_GIVEN,
        authorizer_ip_address: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ProofOfAuthorizationRequestSubmission:
        """
        Submit Proof of Authorization

        Args:
          authorization_terms: Terms of authorization.

          authorized_at: Time of authorization.

          authorizer_email: Email of the authorizer.

          authorizer_name: Name of the authorizer.

          proof_of_authorization_request_id: ID of the proof of authorization request.

          authorizer_company: Company of the authorizer.

          authorizer_ip_address: IP address of the authorizer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/proof_of_authorization_request_submissions",
            body=maybe_transform(
                {
                    "authorization_terms": authorization_terms,
                    "authorized_at": authorized_at,
                    "authorizer_email": authorizer_email,
                    "authorizer_name": authorizer_name,
                    "proof_of_authorization_request_id": proof_of_authorization_request_id,
                    "authorizer_company": authorizer_company,
                    "authorizer_ip_address": authorizer_ip_address,
                },
                proof_of_authorization_request_submission_create_params.ProofOfAuthorizationRequestSubmissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ProofOfAuthorizationRequestSubmission,
        )

    async def retrieve(
        self,
        proof_of_authorization_request_submission_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProofOfAuthorizationRequestSubmission:
        """
        Retrieve a Proof of Authorization Request Submission

        Args:
          proof_of_authorization_request_submission_id: The identifier of the Proof of Authorization Request Submission.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proof_of_authorization_request_submission_id:
            raise ValueError(
                f"Expected a non-empty value for `proof_of_authorization_request_submission_id` but received {proof_of_authorization_request_submission_id!r}"
            )
        return await self._get(
            f"/proof_of_authorization_request_submissions/{proof_of_authorization_request_submission_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProofOfAuthorizationRequestSubmission,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        proof_of_authorization_request_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ProofOfAuthorizationRequestSubmission, AsyncPage[ProofOfAuthorizationRequestSubmission]]:
        """
        List Proof of Authorization Request Submissions

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          proof_of_authorization_request_id: ID of the proof of authorization request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/proof_of_authorization_request_submissions",
            page=AsyncPage[ProofOfAuthorizationRequestSubmission],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "proof_of_authorization_request_id": proof_of_authorization_request_id,
                    },
                    proof_of_authorization_request_submission_list_params.ProofOfAuthorizationRequestSubmissionListParams,
                ),
            ),
            model=ProofOfAuthorizationRequestSubmission,
        )


class ProofOfAuthorizationRequestSubmissionsWithRawResponse:
    def __init__(self, proof_of_authorization_request_submissions: ProofOfAuthorizationRequestSubmissions) -> None:
        self._proof_of_authorization_request_submissions = proof_of_authorization_request_submissions

        self.create = _legacy_response.to_raw_response_wrapper(
            proof_of_authorization_request_submissions.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            proof_of_authorization_request_submissions.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            proof_of_authorization_request_submissions.list,
        )


class AsyncProofOfAuthorizationRequestSubmissionsWithRawResponse:
    def __init__(self, proof_of_authorization_request_submissions: AsyncProofOfAuthorizationRequestSubmissions) -> None:
        self._proof_of_authorization_request_submissions = proof_of_authorization_request_submissions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            proof_of_authorization_request_submissions.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            proof_of_authorization_request_submissions.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            proof_of_authorization_request_submissions.list,
        )


class ProofOfAuthorizationRequestSubmissionsWithStreamingResponse:
    def __init__(self, proof_of_authorization_request_submissions: ProofOfAuthorizationRequestSubmissions) -> None:
        self._proof_of_authorization_request_submissions = proof_of_authorization_request_submissions

        self.create = to_streamed_response_wrapper(
            proof_of_authorization_request_submissions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            proof_of_authorization_request_submissions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            proof_of_authorization_request_submissions.list,
        )


class AsyncProofOfAuthorizationRequestSubmissionsWithStreamingResponse:
    def __init__(self, proof_of_authorization_request_submissions: AsyncProofOfAuthorizationRequestSubmissions) -> None:
        self._proof_of_authorization_request_submissions = proof_of_authorization_request_submissions

        self.create = async_to_streamed_response_wrapper(
            proof_of_authorization_request_submissions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            proof_of_authorization_request_submissions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            proof_of_authorization_request_submissions.list,
        )
