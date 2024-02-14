# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import CheckDeposit, check_deposit_list_params, check_deposit_create_params
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

__all__ = ["CheckDeposits", "AsyncCheckDeposits"]


class CheckDeposits(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckDepositsWithRawResponse:
        return CheckDepositsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckDepositsWithStreamingResponse:
        return CheckDepositsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        back_image_file_id: str,
        currency: str,
        front_image_file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckDeposit:
        """
        Create a Check Deposit

        Args:
          account_id: The identifier for the Account to deposit the check in.

          amount: The deposit amount in the minor unit of the account currency. For dollars, for
              example, this is cents.

          back_image_file_id: The File containing the check's back image.

          currency: The currency to use for the deposit.

          front_image_file_id: The File containing the check's front image.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/check_deposits",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "back_image_file_id": back_image_file_id,
                    "currency": currency,
                    "front_image_file_id": front_image_file_id,
                },
                check_deposit_create_params.CheckDepositCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckDeposit,
        )

    def retrieve(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckDeposit:
        """
        Retrieve a Check Deposit

        Args:
          check_deposit_id: The identifier of the Check Deposit to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return self._get(
            f"/check_deposits/{check_deposit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckDeposit,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: check_deposit_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CheckDeposit]:
        """
        List Check Deposits

        Args:
          account_id: Filter Check Deposits to those belonging to the specified Account.

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
            "/check_deposits",
            page=SyncPage[CheckDeposit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    check_deposit_list_params.CheckDepositListParams,
                ),
            ),
            model=CheckDeposit,
        )


class AsyncCheckDeposits(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckDepositsWithRawResponse:
        return AsyncCheckDepositsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckDepositsWithStreamingResponse:
        return AsyncCheckDepositsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        back_image_file_id: str,
        currency: str,
        front_image_file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CheckDeposit:
        """
        Create a Check Deposit

        Args:
          account_id: The identifier for the Account to deposit the check in.

          amount: The deposit amount in the minor unit of the account currency. For dollars, for
              example, this is cents.

          back_image_file_id: The File containing the check's back image.

          currency: The currency to use for the deposit.

          front_image_file_id: The File containing the check's front image.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/check_deposits",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "back_image_file_id": back_image_file_id,
                    "currency": currency,
                    "front_image_file_id": front_image_file_id,
                },
                check_deposit_create_params.CheckDepositCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckDeposit,
        )

    async def retrieve(
        self,
        check_deposit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckDeposit:
        """
        Retrieve a Check Deposit

        Args:
          check_deposit_id: The identifier of the Check Deposit to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not check_deposit_id:
            raise ValueError(f"Expected a non-empty value for `check_deposit_id` but received {check_deposit_id!r}")
        return await self._get(
            f"/check_deposits/{check_deposit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckDeposit,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: check_deposit_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CheckDeposit, AsyncPage[CheckDeposit]]:
        """
        List Check Deposits

        Args:
          account_id: Filter Check Deposits to those belonging to the specified Account.

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
            "/check_deposits",
            page=AsyncPage[CheckDeposit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    check_deposit_list_params.CheckDepositListParams,
                ),
            ),
            model=CheckDeposit,
        )


class CheckDepositsWithRawResponse:
    def __init__(self, check_deposits: CheckDeposits) -> None:
        self._check_deposits = check_deposits

        self.create = _legacy_response.to_raw_response_wrapper(
            check_deposits.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            check_deposits.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            check_deposits.list,
        )


class AsyncCheckDepositsWithRawResponse:
    def __init__(self, check_deposits: AsyncCheckDeposits) -> None:
        self._check_deposits = check_deposits

        self.create = _legacy_response.async_to_raw_response_wrapper(
            check_deposits.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            check_deposits.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            check_deposits.list,
        )


class CheckDepositsWithStreamingResponse:
    def __init__(self, check_deposits: CheckDeposits) -> None:
        self._check_deposits = check_deposits

        self.create = to_streamed_response_wrapper(
            check_deposits.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            check_deposits.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            check_deposits.list,
        )


class AsyncCheckDepositsWithStreamingResponse:
    def __init__(self, check_deposits: AsyncCheckDeposits) -> None:
        self._check_deposits = check_deposits

        self.create = async_to_streamed_response_wrapper(
            check_deposits.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            check_deposits.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            check_deposits.list,
        )
