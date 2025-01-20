# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import (
    proof_of_authorization_request_submission_list_params,
    proof_of_authorization_request_submission_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ..types.proof_of_authorization_request_submission import ProofOfAuthorizationRequestSubmission

__all__ = ["ProofOfAuthorizationRequestSubmissionsResource", "AsyncProofOfAuthorizationRequestSubmissionsResource"]


class ProofOfAuthorizationRequestSubmissionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProofOfAuthorizationRequestSubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return ProofOfAuthorizationRequestSubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProofOfAuthorizationRequestSubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return ProofOfAuthorizationRequestSubmissionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        authorization_terms: str,
        authorized_at: Union[str, datetime],
        authorizer_email: str,
        authorizer_name: str,
        customer_has_been_offboarded: bool,
        proof_of_authorization_request_id: str,
        validated_account_ownership_via_credential: bool,
        validated_account_ownership_with_account_statement: bool,
        validated_account_ownership_with_microdeposit: bool,
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

          customer_has_been_offboarded: Whether the customer has been offboarded or suspended.

          proof_of_authorization_request_id: ID of the proof of authorization request.

          validated_account_ownership_via_credential: Whether the account ownership was validated via credential (e.g. Plaid).

          validated_account_ownership_with_account_statement: Whether the account ownership was validated with an account statement.

          validated_account_ownership_with_microdeposit: Whether the account ownership was validated with a microdeposit.

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
                    "customer_has_been_offboarded": customer_has_been_offboarded,
                    "proof_of_authorization_request_id": proof_of_authorization_request_id,
                    "validated_account_ownership_via_credential": validated_account_ownership_via_credential,
                    "validated_account_ownership_with_account_statement": validated_account_ownership_with_account_statement,
                    "validated_account_ownership_with_microdeposit": validated_account_ownership_with_microdeposit,
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
        idempotency_key: str | NotGiven = NOT_GIVEN,
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

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

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
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "proof_of_authorization_request_id": proof_of_authorization_request_id,
                    },
                    proof_of_authorization_request_submission_list_params.ProofOfAuthorizationRequestSubmissionListParams,
                ),
            ),
            model=ProofOfAuthorizationRequestSubmission,
        )


class AsyncProofOfAuthorizationRequestSubmissionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProofOfAuthorizationRequestSubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProofOfAuthorizationRequestSubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProofOfAuthorizationRequestSubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncProofOfAuthorizationRequestSubmissionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        authorization_terms: str,
        authorized_at: Union[str, datetime],
        authorizer_email: str,
        authorizer_name: str,
        customer_has_been_offboarded: bool,
        proof_of_authorization_request_id: str,
        validated_account_ownership_via_credential: bool,
        validated_account_ownership_with_account_statement: bool,
        validated_account_ownership_with_microdeposit: bool,
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

          customer_has_been_offboarded: Whether the customer has been offboarded or suspended.

          proof_of_authorization_request_id: ID of the proof of authorization request.

          validated_account_ownership_via_credential: Whether the account ownership was validated via credential (e.g. Plaid).

          validated_account_ownership_with_account_statement: Whether the account ownership was validated with an account statement.

          validated_account_ownership_with_microdeposit: Whether the account ownership was validated with a microdeposit.

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
            body=await async_maybe_transform(
                {
                    "authorization_terms": authorization_terms,
                    "authorized_at": authorized_at,
                    "authorizer_email": authorizer_email,
                    "authorizer_name": authorizer_name,
                    "customer_has_been_offboarded": customer_has_been_offboarded,
                    "proof_of_authorization_request_id": proof_of_authorization_request_id,
                    "validated_account_ownership_via_credential": validated_account_ownership_via_credential,
                    "validated_account_ownership_with_account_statement": validated_account_ownership_with_account_statement,
                    "validated_account_ownership_with_microdeposit": validated_account_ownership_with_microdeposit,
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
        idempotency_key: str | NotGiven = NOT_GIVEN,
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

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

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
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "proof_of_authorization_request_id": proof_of_authorization_request_id,
                    },
                    proof_of_authorization_request_submission_list_params.ProofOfAuthorizationRequestSubmissionListParams,
                ),
            ),
            model=ProofOfAuthorizationRequestSubmission,
        )


class ProofOfAuthorizationRequestSubmissionsResourceWithRawResponse:
    def __init__(
        self, proof_of_authorization_request_submissions: ProofOfAuthorizationRequestSubmissionsResource
    ) -> None:
        self._proof_of_authorization_request_submissions = proof_of_authorization_request_submissions

        self.create = to_raw_response_wrapper(
            proof_of_authorization_request_submissions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            proof_of_authorization_request_submissions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            proof_of_authorization_request_submissions.list,
        )


class AsyncProofOfAuthorizationRequestSubmissionsResourceWithRawResponse:
    def __init__(
        self, proof_of_authorization_request_submissions: AsyncProofOfAuthorizationRequestSubmissionsResource
    ) -> None:
        self._proof_of_authorization_request_submissions = proof_of_authorization_request_submissions

        self.create = async_to_raw_response_wrapper(
            proof_of_authorization_request_submissions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            proof_of_authorization_request_submissions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            proof_of_authorization_request_submissions.list,
        )


class ProofOfAuthorizationRequestSubmissionsResourceWithStreamingResponse:
    def __init__(
        self, proof_of_authorization_request_submissions: ProofOfAuthorizationRequestSubmissionsResource
    ) -> None:
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


class AsyncProofOfAuthorizationRequestSubmissionsResourceWithStreamingResponse:
    def __init__(
        self, proof_of_authorization_request_submissions: AsyncProofOfAuthorizationRequestSubmissionsResource
    ) -> None:
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
