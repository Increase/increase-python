# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import physical_check_batch_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.physical_check_batch import PhysicalCheckBatch

__all__ = ["PhysicalCheckBatchesResource", "AsyncPhysicalCheckBatchesResource"]


class PhysicalCheckBatchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhysicalCheckBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return PhysicalCheckBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhysicalCheckBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return PhysicalCheckBatchesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        mailing_address: physical_check_batch_create_params.MailingAddress,
        return_address: physical_check_batch_create_params.ReturnAddress,
        shipping_method: Literal["usps_first_class", "fedex_overnight"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PhysicalCheckBatch:
        """
        Create a Physical Check Batch

        Args:
          mailing_address: Details for where the parcel will be mailed.

          return_address: Details for where the parcel should return if it is unable to be delivered.

          shipping_method: How to ship the batch.

              - `usps_first_class` - USPS First Class
              - `fedex_overnight` - FedEx Overnight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/physical_check_batches",
            body=maybe_transform(
                {
                    "mailing_address": mailing_address,
                    "return_address": return_address,
                    "shipping_method": shipping_method,
                },
                physical_check_batch_create_params.PhysicalCheckBatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCheckBatch,
        )

    def cancel(
        self,
        physical_check_batch_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PhysicalCheckBatch:
        """
        Cancel a pending Physical Check Batch, which cancels all of its related checks.

        Args:
          physical_check_batch_id: The identifier of the pending Physical Check Batch to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_check_batch_id:
            raise ValueError(
                f"Expected a non-empty value for `physical_check_batch_id` but received {physical_check_batch_id!r}"
            )
        return self._post(
            path_template(
                "/physical_check_batches/{physical_check_batch_id}/cancel",
                physical_check_batch_id=physical_check_batch_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCheckBatch,
        )

    def complete(
        self,
        physical_check_batch_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PhysicalCheckBatch:
        """
        Completing a Physical Check Batch closes it to new Physical Checks and begins
        the process of printing and mailing it.

        Args:
          physical_check_batch_id: The identifier of the Physical Check Batch to complete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_check_batch_id:
            raise ValueError(
                f"Expected a non-empty value for `physical_check_batch_id` but received {physical_check_batch_id!r}"
            )
        return self._post(
            path_template(
                "/physical_check_batches/{physical_check_batch_id}/complete",
                physical_check_batch_id=physical_check_batch_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCheckBatch,
        )


class AsyncPhysicalCheckBatchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhysicalCheckBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhysicalCheckBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhysicalCheckBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncPhysicalCheckBatchesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        mailing_address: physical_check_batch_create_params.MailingAddress,
        return_address: physical_check_batch_create_params.ReturnAddress,
        shipping_method: Literal["usps_first_class", "fedex_overnight"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PhysicalCheckBatch:
        """
        Create a Physical Check Batch

        Args:
          mailing_address: Details for where the parcel will be mailed.

          return_address: Details for where the parcel should return if it is unable to be delivered.

          shipping_method: How to ship the batch.

              - `usps_first_class` - USPS First Class
              - `fedex_overnight` - FedEx Overnight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/physical_check_batches",
            body=await async_maybe_transform(
                {
                    "mailing_address": mailing_address,
                    "return_address": return_address,
                    "shipping_method": shipping_method,
                },
                physical_check_batch_create_params.PhysicalCheckBatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCheckBatch,
        )

    async def cancel(
        self,
        physical_check_batch_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PhysicalCheckBatch:
        """
        Cancel a pending Physical Check Batch, which cancels all of its related checks.

        Args:
          physical_check_batch_id: The identifier of the pending Physical Check Batch to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_check_batch_id:
            raise ValueError(
                f"Expected a non-empty value for `physical_check_batch_id` but received {physical_check_batch_id!r}"
            )
        return await self._post(
            path_template(
                "/physical_check_batches/{physical_check_batch_id}/cancel",
                physical_check_batch_id=physical_check_batch_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCheckBatch,
        )

    async def complete(
        self,
        physical_check_batch_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PhysicalCheckBatch:
        """
        Completing a Physical Check Batch closes it to new Physical Checks and begins
        the process of printing and mailing it.

        Args:
          physical_check_batch_id: The identifier of the Physical Check Batch to complete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not physical_check_batch_id:
            raise ValueError(
                f"Expected a non-empty value for `physical_check_batch_id` but received {physical_check_batch_id!r}"
            )
        return await self._post(
            path_template(
                "/physical_check_batches/{physical_check_batch_id}/complete",
                physical_check_batch_id=physical_check_batch_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PhysicalCheckBatch,
        )


class PhysicalCheckBatchesResourceWithRawResponse:
    def __init__(self, physical_check_batches: PhysicalCheckBatchesResource) -> None:
        self._physical_check_batches = physical_check_batches

        self.create = to_raw_response_wrapper(
            physical_check_batches.create,
        )
        self.cancel = to_raw_response_wrapper(
            physical_check_batches.cancel,
        )
        self.complete = to_raw_response_wrapper(
            physical_check_batches.complete,
        )


class AsyncPhysicalCheckBatchesResourceWithRawResponse:
    def __init__(self, physical_check_batches: AsyncPhysicalCheckBatchesResource) -> None:
        self._physical_check_batches = physical_check_batches

        self.create = async_to_raw_response_wrapper(
            physical_check_batches.create,
        )
        self.cancel = async_to_raw_response_wrapper(
            physical_check_batches.cancel,
        )
        self.complete = async_to_raw_response_wrapper(
            physical_check_batches.complete,
        )


class PhysicalCheckBatchesResourceWithStreamingResponse:
    def __init__(self, physical_check_batches: PhysicalCheckBatchesResource) -> None:
        self._physical_check_batches = physical_check_batches

        self.create = to_streamed_response_wrapper(
            physical_check_batches.create,
        )
        self.cancel = to_streamed_response_wrapper(
            physical_check_batches.cancel,
        )
        self.complete = to_streamed_response_wrapper(
            physical_check_batches.complete,
        )


class AsyncPhysicalCheckBatchesResourceWithStreamingResponse:
    def __init__(self, physical_check_batches: AsyncPhysicalCheckBatchesResource) -> None:
        self._physical_check_batches = physical_check_batches

        self.create = async_to_streamed_response_wrapper(
            physical_check_batches.create,
        )
        self.cancel = async_to_streamed_response_wrapper(
            physical_check_batches.cancel,
        )
        self.complete = async_to_streamed_response_wrapper(
            physical_check_batches.complete,
        )
