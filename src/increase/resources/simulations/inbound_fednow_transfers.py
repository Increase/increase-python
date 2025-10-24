# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import inbound_fednow_transfer_create_params
from ...types.inbound_fednow_transfer import InboundFednowTransfer

__all__ = ["InboundFednowTransfersResource", "AsyncInboundFednowTransfersResource"]


class InboundFednowTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundFednowTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundFednowTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundFednowTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundFednowTransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        debtor_account_number: str | Omit = omit,
        debtor_name: str | Omit = omit,
        debtor_routing_number: str | Omit = omit,
        unstructured_remittance_information: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> InboundFednowTransfer:
        """
        Simulates an [Inbound FedNow Transfer](#inbound-fednow-transfers) to your
        account.

        Args:
          account_number_id: The identifier of the Account Number the inbound FedNow Transfer is for.

          amount: The transfer amount in USD cents. Must be positive.

          debtor_account_number: The account number of the account that sent the transfer.

          debtor_name: The name provided by the sender of the transfer.

          debtor_routing_number: The routing number of the account that sent the transfer.

          unstructured_remittance_information: Additional information included with the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/inbound_fednow_transfers",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "debtor_account_number": debtor_account_number,
                    "debtor_name": debtor_name,
                    "debtor_routing_number": debtor_routing_number,
                    "unstructured_remittance_information": unstructured_remittance_information,
                },
                inbound_fednow_transfer_create_params.InboundFednowTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundFednowTransfer,
        )


class AsyncInboundFednowTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundFednowTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundFednowTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundFednowTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundFednowTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        debtor_account_number: str | Omit = omit,
        debtor_name: str | Omit = omit,
        debtor_routing_number: str | Omit = omit,
        unstructured_remittance_information: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> InboundFednowTransfer:
        """
        Simulates an [Inbound FedNow Transfer](#inbound-fednow-transfers) to your
        account.

        Args:
          account_number_id: The identifier of the Account Number the inbound FedNow Transfer is for.

          amount: The transfer amount in USD cents. Must be positive.

          debtor_account_number: The account number of the account that sent the transfer.

          debtor_name: The name provided by the sender of the transfer.

          debtor_routing_number: The routing number of the account that sent the transfer.

          unstructured_remittance_information: Additional information included with the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/inbound_fednow_transfers",
            body=await async_maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "debtor_account_number": debtor_account_number,
                    "debtor_name": debtor_name,
                    "debtor_routing_number": debtor_routing_number,
                    "unstructured_remittance_information": unstructured_remittance_information,
                },
                inbound_fednow_transfer_create_params.InboundFednowTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundFednowTransfer,
        )


class InboundFednowTransfersResourceWithRawResponse:
    def __init__(self, inbound_fednow_transfers: InboundFednowTransfersResource) -> None:
        self._inbound_fednow_transfers = inbound_fednow_transfers

        self.create = to_raw_response_wrapper(
            inbound_fednow_transfers.create,
        )


class AsyncInboundFednowTransfersResourceWithRawResponse:
    def __init__(self, inbound_fednow_transfers: AsyncInboundFednowTransfersResource) -> None:
        self._inbound_fednow_transfers = inbound_fednow_transfers

        self.create = async_to_raw_response_wrapper(
            inbound_fednow_transfers.create,
        )


class InboundFednowTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_fednow_transfers: InboundFednowTransfersResource) -> None:
        self._inbound_fednow_transfers = inbound_fednow_transfers

        self.create = to_streamed_response_wrapper(
            inbound_fednow_transfers.create,
        )


class AsyncInboundFednowTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_fednow_transfers: AsyncInboundFednowTransfersResource) -> None:
        self._inbound_fednow_transfers = inbound_fednow_transfers

        self.create = async_to_streamed_response_wrapper(
            inbound_fednow_transfers.create,
        )
