# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    AccountNumber,
    account_number_list_params,
    account_number_create_params,
    account_number_update_params,
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

__all__ = ["AccountNumbers", "AsyncAccountNumbers"]


class AccountNumbers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountNumbersWithRawResponse:
        return AccountNumbersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountNumbersWithStreamingResponse:
        return AccountNumbersWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        inbound_ach: account_number_create_params.InboundACH | NotGiven = NOT_GIVEN,
        inbound_checks: account_number_create_params.InboundChecks | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
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

          unique_identifier: A unique identifier you choose for the object. Reusing this identifier for
              another object will result in an error. You can query for the object associated
              with this identifier using the List endpoint.

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
                    "unique_identifier": unique_identifier,
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
        ach_debit_status: Literal["allowed", "blocked"] | NotGiven = NOT_GIVEN,
        created_at: account_number_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
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

          ach_debit_status: The ACH Debit status to retrieve Account Numbers for.

              - `allowed` - ACH Debits are allowed.
              - `blocked` - ACH Debits are blocked.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          status: The status to retrieve Account Numbers for.

              - `active` - The account number is active.
              - `disabled` - The account number is temporarily disabled.
              - `canceled` - The account number is permanently disabled.

          unique_identifier: Filter records to the one with the specified `unique_identifier`.

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
                        "limit": limit,
                        "status": status,
                        "unique_identifier": unique_identifier,
                    },
                    account_number_list_params.AccountNumberListParams,
                ),
            ),
            model=AccountNumber,
        )


class AsyncAccountNumbers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountNumbersWithRawResponse:
        return AsyncAccountNumbersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountNumbersWithStreamingResponse:
        return AsyncAccountNumbersWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        inbound_ach: account_number_create_params.InboundACH | NotGiven = NOT_GIVEN,
        inbound_checks: account_number_create_params.InboundChecks | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
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

          unique_identifier: A unique identifier you choose for the object. Reusing this identifier for
              another object will result in an error. You can query for the object associated
              with this identifier using the List endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/account_numbers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "inbound_ach": inbound_ach,
                    "inbound_checks": inbound_checks,
                    "unique_identifier": unique_identifier,
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
            body=maybe_transform(
                {
                    "inbound_ach": inbound_ach,
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
        ach_debit_status: Literal["allowed", "blocked"] | NotGiven = NOT_GIVEN,
        created_at: account_number_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
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

          ach_debit_status: The ACH Debit status to retrieve Account Numbers for.

              - `allowed` - ACH Debits are allowed.
              - `blocked` - ACH Debits are blocked.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          status: The status to retrieve Account Numbers for.

              - `active` - The account number is active.
              - `disabled` - The account number is temporarily disabled.
              - `canceled` - The account number is permanently disabled.

          unique_identifier: Filter records to the one with the specified `unique_identifier`.

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
                        "limit": limit,
                        "status": status,
                        "unique_identifier": unique_identifier,
                    },
                    account_number_list_params.AccountNumberListParams,
                ),
            ),
            model=AccountNumber,
        )


class AccountNumbersWithRawResponse:
    def __init__(self, account_numbers: AccountNumbers) -> None:
        self._account_numbers = account_numbers

        self.create = _legacy_response.to_raw_response_wrapper(
            account_numbers.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            account_numbers.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            account_numbers.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            account_numbers.list,
        )


class AsyncAccountNumbersWithRawResponse:
    def __init__(self, account_numbers: AsyncAccountNumbers) -> None:
        self._account_numbers = account_numbers

        self.create = _legacy_response.async_to_raw_response_wrapper(
            account_numbers.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            account_numbers.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            account_numbers.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            account_numbers.list,
        )


class AccountNumbersWithStreamingResponse:
    def __init__(self, account_numbers: AccountNumbers) -> None:
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


class AsyncAccountNumbersWithStreamingResponse:
    def __init__(self, account_numbers: AsyncAccountNumbers) -> None:
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
