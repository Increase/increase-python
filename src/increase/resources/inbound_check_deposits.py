# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import inbound_check_deposit_list_params, inbound_check_deposit_return_params
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
from ..types.inbound_check_deposit import InboundCheckDeposit

__all__ = ["InboundCheckDepositsResource", "AsyncInboundCheckDepositsResource"]


class InboundCheckDepositsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundCheckDepositsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundCheckDepositsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundCheckDepositsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundCheckDepositsResourceWithStreamingResponse(self)

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

    def return_(
        self,
        inbound_check_deposit_id: str,
        *,
        reason: Literal[
            "altered_or_fictitious",
            "not_authorized",
            "duplicate_presentment",
            "endorsement_missing",
            "endorsement_irregular",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundCheckDeposit:
        """
        Return an Inbound Check Deposit

        Args:
          inbound_check_deposit_id: The identifier of the Inbound Check Deposit to return.

          reason: The reason to return the Inbound Check Deposit.

              - `altered_or_fictitious` - The check was altered or fictitious.
              - `not_authorized` - The check was not authorized.
              - `duplicate_presentment` - The check was a duplicate presentment.
              - `endorsement_missing` - The check was not endorsed.
              - `endorsement_irregular` - The check was not endorsed by the payee.

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
            f"/inbound_check_deposits/{inbound_check_deposit_id}/return",
            body=maybe_transform(
                {"reason": reason}, inbound_check_deposit_return_params.InboundCheckDepositReturnParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundCheckDeposit,
        )


class AsyncInboundCheckDepositsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundCheckDepositsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundCheckDepositsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundCheckDepositsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundCheckDepositsResourceWithStreamingResponse(self)

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

    async def return_(
        self,
        inbound_check_deposit_id: str,
        *,
        reason: Literal[
            "altered_or_fictitious",
            "not_authorized",
            "duplicate_presentment",
            "endorsement_missing",
            "endorsement_irregular",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundCheckDeposit:
        """
        Return an Inbound Check Deposit

        Args:
          inbound_check_deposit_id: The identifier of the Inbound Check Deposit to return.

          reason: The reason to return the Inbound Check Deposit.

              - `altered_or_fictitious` - The check was altered or fictitious.
              - `not_authorized` - The check was not authorized.
              - `duplicate_presentment` - The check was a duplicate presentment.
              - `endorsement_missing` - The check was not endorsed.
              - `endorsement_irregular` - The check was not endorsed by the payee.

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
            f"/inbound_check_deposits/{inbound_check_deposit_id}/return",
            body=await async_maybe_transform(
                {"reason": reason}, inbound_check_deposit_return_params.InboundCheckDepositReturnParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundCheckDeposit,
        )


class InboundCheckDepositsResourceWithRawResponse:
    def __init__(self, inbound_check_deposits: InboundCheckDepositsResource) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.retrieve = to_raw_response_wrapper(
            inbound_check_deposits.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inbound_check_deposits.list,
        )
        self.decline = to_raw_response_wrapper(
            inbound_check_deposits.decline,
        )
        self.return_ = to_raw_response_wrapper(
            inbound_check_deposits.return_,
        )


class AsyncInboundCheckDepositsResourceWithRawResponse:
    def __init__(self, inbound_check_deposits: AsyncInboundCheckDepositsResource) -> None:
        self._inbound_check_deposits = inbound_check_deposits

        self.retrieve = async_to_raw_response_wrapper(
            inbound_check_deposits.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inbound_check_deposits.list,
        )
        self.decline = async_to_raw_response_wrapper(
            inbound_check_deposits.decline,
        )
        self.return_ = async_to_raw_response_wrapper(
            inbound_check_deposits.return_,
        )


class InboundCheckDepositsResourceWithStreamingResponse:
    def __init__(self, inbound_check_deposits: InboundCheckDepositsResource) -> None:
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
        self.return_ = to_streamed_response_wrapper(
            inbound_check_deposits.return_,
        )


class AsyncInboundCheckDepositsResourceWithStreamingResponse:
    def __init__(self, inbound_check_deposits: AsyncInboundCheckDepositsResource) -> None:
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
        self.return_ = async_to_streamed_response_wrapper(
            inbound_check_deposits.return_,
        )
