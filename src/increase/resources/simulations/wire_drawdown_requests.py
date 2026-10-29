# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import wire_drawdown_request_refuse_params
from ...types.wire_drawdown_request import WireDrawdownRequest

__all__ = ["WireDrawdownRequestsResource", "AsyncWireDrawdownRequestsResource"]


class WireDrawdownRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WireDrawdownRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return WireDrawdownRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WireDrawdownRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return WireDrawdownRequestsResourceWithStreamingResponse(self)

    def refuse(
        self,
        wire_drawdown_request_id: str,
        *,
        refusal_reason_additional_information: str | Omit = omit,
        refusal_reason_code: Literal[
            "invalid_debtor_account_number",
            "transaction_forbidden",
            "unsuccessful_direct_debit",
            "inconsistent_with_end_customer",
            "narrative",
            "other",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WireDrawdownRequest:
        """
        Simulates a Wire Drawdown Request being refused by the debtor.

        Args:
          wire_drawdown_request_id: The identifier of the Wire Drawdown Request you wish to refuse.

          refusal_reason_additional_information: Additional information about the refusal that the simulated refusal will have.

          refusal_reason_code: The reason code that the simulated refusal will have.

              - `invalid_debtor_account_number` - The debtor's account number is invalid or
                missing. Corresponds to the Fedwire reason code `AC02`.
              - `transaction_forbidden` - The debtor account does not allow drawdown requests.
                Corresponds to the Fedwire reason code `AG01`.
              - `unsuccessful_direct_debit` - The debtor account cannot be debited for a
                generic reason. Corresponds to the Fedwire reason code `AG07`.
              - `inconsistent_with_end_customer` - The debtor's identification is inconsistent
                with the debtor account number. Corresponds to the Fedwire reason code `BE01`.
              - `narrative` - The reason is provided as narrative information in the
                additional information field. Corresponds to the Fedwire reason code `NARR`.
              - `other` - Some other error or issue has occurred.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `wire_drawdown_request_id` but received {wire_drawdown_request_id!r}"
            )
        return self._post(
            path_template(
                "/simulations/wire_drawdown_requests/{wire_drawdown_request_id}/refuse",
                wire_drawdown_request_id=wire_drawdown_request_id,
            ),
            body=maybe_transform(
                {
                    "refusal_reason_additional_information": refusal_reason_additional_information,
                    "refusal_reason_code": refusal_reason_code,
                },
                wire_drawdown_request_refuse_params.WireDrawdownRequestRefuseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireDrawdownRequest,
        )

    def submit(
        self,
        wire_drawdown_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WireDrawdownRequest:
        """
        Simulates a Wire Drawdown Request being submitted to Fedwire.

        Args:
          wire_drawdown_request_id: The identifier of the Wire Drawdown Request you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `wire_drawdown_request_id` but received {wire_drawdown_request_id!r}"
            )
        return self._post(
            path_template(
                "/simulations/wire_drawdown_requests/{wire_drawdown_request_id}/submit",
                wire_drawdown_request_id=wire_drawdown_request_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireDrawdownRequest,
        )


class AsyncWireDrawdownRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWireDrawdownRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWireDrawdownRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWireDrawdownRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncWireDrawdownRequestsResourceWithStreamingResponse(self)

    async def refuse(
        self,
        wire_drawdown_request_id: str,
        *,
        refusal_reason_additional_information: str | Omit = omit,
        refusal_reason_code: Literal[
            "invalid_debtor_account_number",
            "transaction_forbidden",
            "unsuccessful_direct_debit",
            "inconsistent_with_end_customer",
            "narrative",
            "other",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WireDrawdownRequest:
        """
        Simulates a Wire Drawdown Request being refused by the debtor.

        Args:
          wire_drawdown_request_id: The identifier of the Wire Drawdown Request you wish to refuse.

          refusal_reason_additional_information: Additional information about the refusal that the simulated refusal will have.

          refusal_reason_code: The reason code that the simulated refusal will have.

              - `invalid_debtor_account_number` - The debtor's account number is invalid or
                missing. Corresponds to the Fedwire reason code `AC02`.
              - `transaction_forbidden` - The debtor account does not allow drawdown requests.
                Corresponds to the Fedwire reason code `AG01`.
              - `unsuccessful_direct_debit` - The debtor account cannot be debited for a
                generic reason. Corresponds to the Fedwire reason code `AG07`.
              - `inconsistent_with_end_customer` - The debtor's identification is inconsistent
                with the debtor account number. Corresponds to the Fedwire reason code `BE01`.
              - `narrative` - The reason is provided as narrative information in the
                additional information field. Corresponds to the Fedwire reason code `NARR`.
              - `other` - Some other error or issue has occurred.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `wire_drawdown_request_id` but received {wire_drawdown_request_id!r}"
            )
        return await self._post(
            path_template(
                "/simulations/wire_drawdown_requests/{wire_drawdown_request_id}/refuse",
                wire_drawdown_request_id=wire_drawdown_request_id,
            ),
            body=await async_maybe_transform(
                {
                    "refusal_reason_additional_information": refusal_reason_additional_information,
                    "refusal_reason_code": refusal_reason_code,
                },
                wire_drawdown_request_refuse_params.WireDrawdownRequestRefuseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireDrawdownRequest,
        )

    async def submit(
        self,
        wire_drawdown_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WireDrawdownRequest:
        """
        Simulates a Wire Drawdown Request being submitted to Fedwire.

        Args:
          wire_drawdown_request_id: The identifier of the Wire Drawdown Request you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `wire_drawdown_request_id` but received {wire_drawdown_request_id!r}"
            )
        return await self._post(
            path_template(
                "/simulations/wire_drawdown_requests/{wire_drawdown_request_id}/submit",
                wire_drawdown_request_id=wire_drawdown_request_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireDrawdownRequest,
        )


class WireDrawdownRequestsResourceWithRawResponse:
    def __init__(self, wire_drawdown_requests: WireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.refuse = to_raw_response_wrapper(
            wire_drawdown_requests.refuse,
        )
        self.submit = to_raw_response_wrapper(
            wire_drawdown_requests.submit,
        )


class AsyncWireDrawdownRequestsResourceWithRawResponse:
    def __init__(self, wire_drawdown_requests: AsyncWireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.refuse = async_to_raw_response_wrapper(
            wire_drawdown_requests.refuse,
        )
        self.submit = async_to_raw_response_wrapper(
            wire_drawdown_requests.submit,
        )


class WireDrawdownRequestsResourceWithStreamingResponse:
    def __init__(self, wire_drawdown_requests: WireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.refuse = to_streamed_response_wrapper(
            wire_drawdown_requests.refuse,
        )
        self.submit = to_streamed_response_wrapper(
            wire_drawdown_requests.submit,
        )


class AsyncWireDrawdownRequestsResourceWithStreamingResponse:
    def __init__(self, wire_drawdown_requests: AsyncWireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.refuse = async_to_streamed_response_wrapper(
            wire_drawdown_requests.refuse,
        )
        self.submit = async_to_streamed_response_wrapper(
            wire_drawdown_requests.submit,
        )
