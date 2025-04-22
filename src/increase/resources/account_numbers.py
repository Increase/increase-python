# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import account_number_list_params, account_number_create_params, account_number_update_params
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
from ..types.account_number import AccountNumber

__all__ = ["AccountNumbersResource", "AsyncAccountNumbersResource"]


class AccountNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AccountNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AccountNumbersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        inbound_ach: account_number_create_params.InboundACH | NotGiven = NOT_GIVEN,
        inbound_checks: account_number_create_params.InboundChecks | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountNumber:
        """
        Create an Account Number

        Args:
          account_id: The Account the Account Number should belong to.

          name: The name you choose for the Account Number.

          inbound_ach: Options related to how this Account Number should handle inbound ACH transfers.

          inbound_checks: Options related to how this Account Number should handle inbound check
              withdrawals.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/account_numbers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "inbound_ach": inbound_ach,
                    "inbound_checks": inbound_checks,
                },
                account_number_create_params.AccountNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountNumber,
        )

    def retrieve(
        self,
        account_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountNumber:
        """
        Retrieve an Account Number

        Args:
          account_number_id: The identifier of the Account Number to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_number_id:
            raise ValueError(f"Expected a non-empty value for `account_number_id` but received {account_number_id!r}")
        return self._get(
            f"/account_numbers/{account_number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountNumber,
        )

    def update(
        self,
        account_number_id: str,
        *,
        inbound_ach: account_number_update_params.InboundACH | NotGiven = NOT_GIVEN,
        inbound_checks: account_number_update_params.InboundChecks | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountNumber:
        """
        Update an Account Number

        Args:
          account_number_id: The identifier of the Account Number.

          inbound_ach: Options related to how this Account Number handles inbound ACH transfers.

          inbound_checks: Options related to how this Account Number should handle inbound check
              withdrawals.

          name: The name you choose for the Account Number.

          status: This indicates if transfers can be made to the Account Number.

              - `active` - The account number is active.
              - `disabled` - The account number is temporarily disabled.
              - `canceled` - The account number is permanently disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not account_number_id:
            raise ValueError(f"Expected a non-empty value for `account_number_id` but received {account_number_id!r}")
        return self._patch(
            f"/account_numbers/{account_number_id}",
            body=maybe_transform(
                {
                    "inbound_ach": inbound_ach,
                    "inbound_checks": inbound_checks,
                    "name": name,
                    "status": status,
                },
                account_number_update_params.AccountNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountNumber,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        ach_debit_status: account_number_list_params.ACHDebitStatus | NotGiven = NOT_GIVEN,
        created_at: account_number_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: account_number_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[AccountNumber]:
        """
        List Account Numbers

        Args:
          account_id: Filter Account Numbers to those belonging to the specified Account.

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
            "/account_numbers",
            page=SyncPage[AccountNumber],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "ach_debit_status": ach_debit_status,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    account_number_list_params.AccountNumberListParams,
                ),
            ),
            model=AccountNumber,
        )


class AsyncAccountNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncAccountNumbersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        inbound_ach: account_number_create_params.InboundACH | NotGiven = NOT_GIVEN,
        inbound_checks: account_number_create_params.InboundChecks | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountNumber:
        """
        Create an Account Number

        Args:
          account_id: The Account the Account Number should belong to.

          name: The name you choose for the Account Number.

          inbound_ach: Options related to how this Account Number should handle inbound ACH transfers.

          inbound_checks: Options related to how this Account Number should handle inbound check
              withdrawals.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/account_numbers",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "inbound_ach": inbound_ach,
                    "inbound_checks": inbound_checks,
                },
                account_number_create_params.AccountNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountNumber,
        )

    async def retrieve(
        self,
        account_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountNumber:
        """
        Retrieve an Account Number

        Args:
          account_number_id: The identifier of the Account Number to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_number_id:
            raise ValueError(f"Expected a non-empty value for `account_number_id` but received {account_number_id!r}")
        return await self._get(
            f"/account_numbers/{account_number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountNumber,
        )

    async def update(
        self,
        account_number_id: str,
        *,
        inbound_ach: account_number_update_params.InboundACH | NotGiven = NOT_GIVEN,
        inbound_checks: account_number_update_params.InboundChecks | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountNumber:
        """
        Update an Account Number

        Args:
          account_number_id: The identifier of the Account Number.

          inbound_ach: Options related to how this Account Number handles inbound ACH transfers.

          inbound_checks: Options related to how this Account Number should handle inbound check
              withdrawals.

          name: The name you choose for the Account Number.

          status: This indicates if transfers can be made to the Account Number.

              - `active` - The account number is active.
              - `disabled` - The account number is temporarily disabled.
              - `canceled` - The account number is permanently disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not account_number_id:
            raise ValueError(f"Expected a non-empty value for `account_number_id` but received {account_number_id!r}")
        return await self._patch(
            f"/account_numbers/{account_number_id}",
            body=await async_maybe_transform(
                {
                    "inbound_ach": inbound_ach,
                    "inbound_checks": inbound_checks,
                    "name": name,
                    "status": status,
                },
                account_number_update_params.AccountNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountNumber,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        ach_debit_status: account_number_list_params.ACHDebitStatus | NotGiven = NOT_GIVEN,
        created_at: account_number_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: account_number_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AccountNumber, AsyncPage[AccountNumber]]:
        """
        List Account Numbers

        Args:
          account_id: Filter Account Numbers to those belonging to the specified Account.

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
            "/account_numbers",
            page=AsyncPage[AccountNumber],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "ach_debit_status": ach_debit_status,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    account_number_list_params.AccountNumberListParams,
                ),
            ),
            model=AccountNumber,
        )


class AccountNumbersResourceWithRawResponse:
    def __init__(self, account_numbers: AccountNumbersResource) -> None:
        self._account_numbers = account_numbers

        self.create = to_raw_response_wrapper(
            account_numbers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            account_numbers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            account_numbers.update,
        )
        self.list = to_raw_response_wrapper(
            account_numbers.list,
        )


class AsyncAccountNumbersResourceWithRawResponse:
    def __init__(self, account_numbers: AsyncAccountNumbersResource) -> None:
        self._account_numbers = account_numbers

        self.create = async_to_raw_response_wrapper(
            account_numbers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            account_numbers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            account_numbers.update,
        )
        self.list = async_to_raw_response_wrapper(
            account_numbers.list,
        )


class AccountNumbersResourceWithStreamingResponse:
    def __init__(self, account_numbers: AccountNumbersResource) -> None:
        self._account_numbers = account_numbers

        self.create = to_streamed_response_wrapper(
            account_numbers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            account_numbers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            account_numbers.update,
        )
        self.list = to_streamed_response_wrapper(
            account_numbers.list,
        )


class AsyncAccountNumbersResourceWithStreamingResponse:
    def __init__(self, account_numbers: AsyncAccountNumbersResource) -> None:
        self._account_numbers = account_numbers

        self.create = async_to_streamed_response_wrapper(
            account_numbers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            account_numbers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            account_numbers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            account_numbers.list,
        )
