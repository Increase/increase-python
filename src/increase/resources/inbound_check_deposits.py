# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import inbound_check_deposit_list_params
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
from ..types.inbound_check_deposit import InboundCheckDeposit

__all__ = ["InboundCheckDeposits", "AsyncInboundCheckDeposits"]


class InboundCheckDeposits(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundCheckDepositsWithRawResponse:
        return InboundCheckDepositsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundCheckDepositsWithStreamingResponse:
        return InboundCheckDepositsWithStreamingResponse(self)

    def retrieve(
        self,
        inbound_check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundCheckDeposit:
        """
        Retrieve an Inbound Check Deposit

        Args:
          inbound_check_deposit_id: The identifier of the Inbound Check Deposit to get details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_check_deposit_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_check_deposit_id` but received {inbound_check_deposit_id!r}"
            )
        return self._get(
            f"/inbound_check_deposits/{inbound_check_deposit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundCheckDeposit,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        check_transfer_id: str | NotGiven = NOT_GIVEN,
        created_at: inbound_check_deposit_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InboundCheckDeposit]:
        """
        List Inbound Check Deposits

        Args:
          account_id: Filter Inbound Check Deposits to those belonging to the specified Account.

          check_transfer_id: Filter Inbound Check Deposits to those belonging to the specified Check
              Transfer.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_check_deposits",
            page=SyncPage[InboundCheckDeposit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "check_transfer_id": check_transfer_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    inbound_check_deposit_list_params.InboundCheckDepositListParams,
                ),
            ),
            model=InboundCheckDeposit,
        )

    def decline(
        self,
        inbound_check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundCheckDeposit:
        """
        Decline an Inbound Check Deposit

        Args:
          inbound_check_deposit_id: The identifier of the Inbound Check Deposit to decline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not inbound_check_deposit_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_check_deposit_id` but received {inbound_check_deposit_id!r}"
            )
        return self._post(
            f"/inbound_check_deposits/{inbound_check_deposit_id}/decline",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundCheckDeposit,
        )


class AsyncInboundCheckDeposits(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundCheckDepositsWithRawResponse:
        return AsyncInboundCheckDepositsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundCheckDepositsWithStreamingResponse:
        return AsyncInboundCheckDepositsWithStreamingResponse(self)

    async def retrieve(
        self,
        inbound_check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundCheckDeposit:
        """
        Retrieve an Inbound Check Deposit

        Args:
          inbound_check_deposit_id: The identifier of the Inbound Check Deposit to get details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_check_deposit_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_check_deposit_id` but received {inbound_check_deposit_id!r}"
            )
        return await self._get(
            f"/inbound_check_deposits/{inbound_check_deposit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundCheckDeposit,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        check_transfer_id: str | NotGiven = NOT_GIVEN,
        created_at: inbound_check_deposit_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InboundCheckDeposit, AsyncPage[InboundCheckDeposit]]:
        """
        List Inbound Check Deposits

        Args:
          account_id: Filter Inbound Check Deposits to those belonging to the specified Account.

          check_transfer_id: Filter Inbound Check Deposits to those belonging to the specified Check
              Transfer.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_check_deposits",
            page=AsyncPage[InboundCheckDeposit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "check_transfer_id": check_transfer_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    inbound_check_deposit_list_params.InboundCheckDepositListParams,
                ),
            ),
            model=InboundCheckDeposit,
        )

    async def decline(
        self,
        inbound_check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundCheckDeposit:
        """
        Decline an Inbound Check Deposit

        Args:
          inbound_check_deposit_id: The identifier of the Inbound Check Deposit to decline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not inbound_check_deposit_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_check_deposit_id` but received {inbound_check_deposit_id!r}"
            )
        return await self._post(
            f"/inbound_check_deposits/{inbound_check_deposit_id}/decline",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundCheckDeposit,
        )


class InboundCheckDepositsWithRawResponse:
    def __init__(self, inbound_check_deposits: InboundCheckDeposits) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            inbound_check_deposits.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            inbound_check_deposits.list,
        )
        self.decline = _legacy_response.to_raw_response_wrapper(
            inbound_check_deposits.decline,
        )


class AsyncInboundCheckDepositsWithRawResponse:
    def __init__(self, inbound_check_deposits: AsyncInboundCheckDeposits) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            inbound_check_deposits.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            inbound_check_deposits.list,
        )
        self.decline = _legacy_response.async_to_raw_response_wrapper(
            inbound_check_deposits.decline,
        )


class InboundCheckDepositsWithStreamingResponse:
    def __init__(self, inbound_check_deposits: InboundCheckDeposits) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.retrieve = to_streamed_response_wrapper(
            inbound_check_deposits.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inbound_check_deposits.list,
        )
        self.decline = to_streamed_response_wrapper(
            inbound_check_deposits.decline,
        )


class AsyncInboundCheckDepositsWithStreamingResponse:
    def __init__(self, inbound_check_deposits: AsyncInboundCheckDeposits) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.retrieve = async_to_streamed_response_wrapper(
            inbound_check_deposits.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_check_deposits.list,
        )
        self.decline = async_to_streamed_response_wrapper(
            inbound_check_deposits.decline,
        )
