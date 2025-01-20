# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import proof_of_authorization_request_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
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
from ..types.proof_of_authorization_request import ProofOfAuthorizationRequest

__all__ = ["ProofOfAuthorizationRequestsResource", "AsyncProofOfAuthorizationRequestsResource"]


class ProofOfAuthorizationRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProofOfAuthorizationRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return ProofOfAuthorizationRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProofOfAuthorizationRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return ProofOfAuthorizationRequestsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        proof_of_authorization_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProofOfAuthorizationRequest:
        """
        Retrieve a Proof of Authorization Request

        Args:
          proof_of_authorization_request_id: The identifier of the Proof of Authorization Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proof_of_authorization_request_id:
            raise ValueError(
                f"Expected a non-empty value for `proof_of_authorization_request_id` but received {proof_of_authorization_request_id!r}"
            )
        return self._get(
            f"/proof_of_authorization_requests/{proof_of_authorization_request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProofOfAuthorizationRequest,
        )

    def list(
        self,
        *,
        created_at: proof_of_authorization_request_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ProofOfAuthorizationRequest]:
        """
        List Proof of Authorization Requests

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
            "/proof_of_authorization_requests",
            page=SyncPage[ProofOfAuthorizationRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    proof_of_authorization_request_list_params.ProofOfAuthorizationRequestListParams,
                ),
            ),
            model=ProofOfAuthorizationRequest,
        )


class AsyncProofOfAuthorizationRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProofOfAuthorizationRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProofOfAuthorizationRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProofOfAuthorizationRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncProofOfAuthorizationRequestsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        proof_of_authorization_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProofOfAuthorizationRequest:
        """
        Retrieve a Proof of Authorization Request

        Args:
          proof_of_authorization_request_id: The identifier of the Proof of Authorization Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proof_of_authorization_request_id:
            raise ValueError(
                f"Expected a non-empty value for `proof_of_authorization_request_id` but received {proof_of_authorization_request_id!r}"
            )
        return await self._get(
            f"/proof_of_authorization_requests/{proof_of_authorization_request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProofOfAuthorizationRequest,
        )

    def list(
        self,
        *,
        created_at: proof_of_authorization_request_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ProofOfAuthorizationRequest, AsyncPage[ProofOfAuthorizationRequest]]:
        """
        List Proof of Authorization Requests

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
            "/proof_of_authorization_requests",
            page=AsyncPage[ProofOfAuthorizationRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    proof_of_authorization_request_list_params.ProofOfAuthorizationRequestListParams,
                ),
            ),
            model=ProofOfAuthorizationRequest,
        )


class ProofOfAuthorizationRequestsResourceWithRawResponse:
    def __init__(self, proof_of_authorization_requests: ProofOfAuthorizationRequestsResource) -> None:
        self._proof_of_authorization_requests = proof_of_authorization_requests

        self.retrieve = to_raw_response_wrapper(
            proof_of_authorization_requests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            proof_of_authorization_requests.list,
        )


class AsyncProofOfAuthorizationRequestsResourceWithRawResponse:
    def __init__(self, proof_of_authorization_requests: AsyncProofOfAuthorizationRequestsResource) -> None:
        self._proof_of_authorization_requests = proof_of_authorization_requests

        self.retrieve = async_to_raw_response_wrapper(
            proof_of_authorization_requests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            proof_of_authorization_requests.list,
        )


class ProofOfAuthorizationRequestsResourceWithStreamingResponse:
    def __init__(self, proof_of_authorization_requests: ProofOfAuthorizationRequestsResource) -> None:
        self._proof_of_authorization_requests = proof_of_authorization_requests

        self.retrieve = to_streamed_response_wrapper(
            proof_of_authorization_requests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            proof_of_authorization_requests.list,
        )


class AsyncProofOfAuthorizationRequestsResourceWithStreamingResponse:
    def __init__(self, proof_of_authorization_requests: AsyncProofOfAuthorizationRequestsResource) -> None:
        self._proof_of_authorization_requests = proof_of_authorization_requests

        self.retrieve = async_to_streamed_response_wrapper(
            proof_of_authorization_requests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            proof_of_authorization_requests.list,
        )
