# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    BookkeepingAccount,
    BookkeepingBalanceLookup,
    bookkeeping_account_list_params,
    bookkeeping_account_create_params,
    bookkeeping_account_update_params,
    bookkeeping_account_balance_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import Increase, AsyncIncrease

__all__ = ["BookkeepingAccounts", "AsyncBookkeepingAccounts"]


class BookkeepingAccounts(SyncAPIResource):
    with_raw_response: BookkeepingAccountsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = BookkeepingAccountsWithRawResponse(self)

    def create(
        self,
        *,
        name: str,
        account_id: str | NotGiven = NOT_GIVEN,
        compliance_category: Literal["commingled_cash", "customer_balance"] | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BookkeepingAccount:
        """
        Create a Bookkeeping Account

        Args:
          name: The name you choose for the account.

          account_id: The entity, if `compliance_category` is `commingled_cash`.

          compliance_category: The account compliance category.

              - `commingled_cash` - A cash in an commingled Increase Account.
              - `customer_balance` - A customer balance.

          entity_id: The entity, if `compliance_category` is `customer_balance`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/bookkeeping_accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "account_id": account_id,
                    "compliance_category": compliance_category,
                    "entity_id": entity_id,
                },
                bookkeeping_account_create_params.BookkeepingAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BookkeepingAccount,
        )

    def update(
        self,
        bookkeeping_account_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BookkeepingAccount:
        """
        Update a Bookkeeping Account

        Args:
          bookkeeping_account_id: The bookkeeping account you would like to update.

          name: The name you choose for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/bookkeeping_accounts/{bookkeeping_account_id}",
            body=maybe_transform({"name": name}, bookkeeping_account_update_params.BookkeepingAccountUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BookkeepingAccount,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[BookkeepingAccount]:
        """
        List Bookkeeping Accounts

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
            "/bookkeeping_accounts",
            page=SyncPage[BookkeepingAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    bookkeeping_account_list_params.BookkeepingAccountListParams,
                ),
            ),
            model=BookkeepingAccount,
        )

    def balance(
        self,
        bookkeeping_account_id: str,
        *,
        at_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookkeepingBalanceLookup:
        """
        Retrieve a Bookkeeping Account Balance

        Args:
          bookkeeping_account_id: The identifier of the Bookkeeping Account to retrieve.

          at_time: The moment to query the balance at. If not set, returns the current balances.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/bookkeeping_accounts/{bookkeeping_account_id}/balance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"at_time": at_time}, bookkeeping_account_balance_params.BookkeepingAccountBalanceParams
                ),
            ),
            cast_to=BookkeepingBalanceLookup,
        )


class AsyncBookkeepingAccounts(AsyncAPIResource):
    with_raw_response: AsyncBookkeepingAccountsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncBookkeepingAccountsWithRawResponse(self)

    async def create(
        self,
        *,
        name: str,
        account_id: str | NotGiven = NOT_GIVEN,
        compliance_category: Literal["commingled_cash", "customer_balance"] | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BookkeepingAccount:
        """
        Create a Bookkeeping Account

        Args:
          name: The name you choose for the account.

          account_id: The entity, if `compliance_category` is `commingled_cash`.

          compliance_category: The account compliance category.

              - `commingled_cash` - A cash in an commingled Increase Account.
              - `customer_balance` - A customer balance.

          entity_id: The entity, if `compliance_category` is `customer_balance`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/bookkeeping_accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "account_id": account_id,
                    "compliance_category": compliance_category,
                    "entity_id": entity_id,
                },
                bookkeeping_account_create_params.BookkeepingAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BookkeepingAccount,
        )

    async def update(
        self,
        bookkeeping_account_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BookkeepingAccount:
        """
        Update a Bookkeeping Account

        Args:
          bookkeeping_account_id: The bookkeeping account you would like to update.

          name: The name you choose for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/bookkeeping_accounts/{bookkeeping_account_id}",
            body=maybe_transform({"name": name}, bookkeeping_account_update_params.BookkeepingAccountUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BookkeepingAccount,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BookkeepingAccount, AsyncPage[BookkeepingAccount]]:
        """
        List Bookkeeping Accounts

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
            "/bookkeeping_accounts",
            page=AsyncPage[BookkeepingAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    bookkeeping_account_list_params.BookkeepingAccountListParams,
                ),
            ),
            model=BookkeepingAccount,
        )

    async def balance(
        self,
        bookkeeping_account_id: str,
        *,
        at_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookkeepingBalanceLookup:
        """
        Retrieve a Bookkeeping Account Balance

        Args:
          bookkeeping_account_id: The identifier of the Bookkeeping Account to retrieve.

          at_time: The moment to query the balance at. If not set, returns the current balances.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/bookkeeping_accounts/{bookkeeping_account_id}/balance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"at_time": at_time}, bookkeeping_account_balance_params.BookkeepingAccountBalanceParams
                ),
            ),
            cast_to=BookkeepingBalanceLookup,
        )


class BookkeepingAccountsWithRawResponse:
    def __init__(self, bookkeeping_accounts: BookkeepingAccounts) -> None:
        self.create = to_raw_response_wrapper(
            bookkeeping_accounts.create,
        )
        self.update = to_raw_response_wrapper(
            bookkeeping_accounts.update,
        )
        self.list = to_raw_response_wrapper(
            bookkeeping_accounts.list,
        )
        self.balance = to_raw_response_wrapper(
            bookkeeping_accounts.balance,
        )


class AsyncBookkeepingAccountsWithRawResponse:
    def __init__(self, bookkeeping_accounts: AsyncBookkeepingAccounts) -> None:
        self.create = async_to_raw_response_wrapper(
            bookkeeping_accounts.create,
        )
        self.update = async_to_raw_response_wrapper(
            bookkeeping_accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            bookkeeping_accounts.list,
        )
        self.balance = async_to_raw_response_wrapper(
            bookkeeping_accounts.balance,
        )
