# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    ExternalAccount,
    external_account_list_params,
    external_account_create_params,
    external_account_update_params,
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

__all__ = ["ExternalAccounts", "AsyncExternalAccounts"]


class ExternalAccounts(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalAccountsWithRawResponse:
        return ExternalAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalAccountsWithStreamingResponse:
        return ExternalAccountsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number: str,
        description: str,
        routing_number: str,
        funding: Literal["checking", "savings", "other"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        Create an External Account

        Args:
          account_number: The account number for the destination account.

          description: The name you choose for the Account.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          funding: The type of the destination account. Defaults to `checking`.

              - `checking` - A checking account.
              - `savings` - A savings account.
              - `other` - A different type of account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/external_accounts",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "description": description,
                    "routing_number": routing_number,
                    "funding": funding,
                },
                external_account_create_params.ExternalAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalAccount,
        )

    def retrieve(
        self,
        external_account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAccount:
        """
        Retrieve an External Account

        Args:
          external_account_id: The identifier of the External Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        return self._get(
            f"/external_accounts/{external_account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAccount,
        )

    def update(
        self,
        external_account_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "archived"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        Update an External Account

        Args:
          external_account_id: The external account identifier.

          description: The description you choose to give the external account.

          status: The status of the External Account.

              - `active` - The External Account is active.
              - `archived` - The External Account is archived and won't appear in the
                dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        return self._patch(
            f"/external_accounts/{external_account_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "status": status,
                },
                external_account_update_params.ExternalAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalAccount,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        status: external_account_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ExternalAccount]:
        """
        List External Accounts

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          routing_number: Filter External Accounts to those with the specified Routing Number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/external_accounts",
            page=SyncPage[ExternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "routing_number": routing_number,
                        "status": status,
                    },
                    external_account_list_params.ExternalAccountListParams,
                ),
            ),
            model=ExternalAccount,
        )


class AsyncExternalAccounts(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalAccountsWithRawResponse:
        return AsyncExternalAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalAccountsWithStreamingResponse:
        return AsyncExternalAccountsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number: str,
        description: str,
        routing_number: str,
        funding: Literal["checking", "savings", "other"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        Create an External Account

        Args:
          account_number: The account number for the destination account.

          description: The name you choose for the Account.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          funding: The type of the destination account. Defaults to `checking`.

              - `checking` - A checking account.
              - `savings` - A savings account.
              - `other` - A different type of account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/external_accounts",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "description": description,
                    "routing_number": routing_number,
                    "funding": funding,
                },
                external_account_create_params.ExternalAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalAccount,
        )

    async def retrieve(
        self,
        external_account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalAccount:
        """
        Retrieve an External Account

        Args:
          external_account_id: The identifier of the External Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        return await self._get(
            f"/external_accounts/{external_account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAccount,
        )

    async def update(
        self,
        external_account_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "archived"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        Update an External Account

        Args:
          external_account_id: The external account identifier.

          description: The description you choose to give the external account.

          status: The status of the External Account.

              - `active` - The External Account is active.
              - `archived` - The External Account is archived and won't appear in the
                dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        return await self._patch(
            f"/external_accounts/{external_account_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "status": status,
                },
                external_account_update_params.ExternalAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalAccount,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        status: external_account_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ExternalAccount, AsyncPage[ExternalAccount]]:
        """
        List External Accounts

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          routing_number: Filter External Accounts to those with the specified Routing Number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/external_accounts",
            page=AsyncPage[ExternalAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "routing_number": routing_number,
                        "status": status,
                    },
                    external_account_list_params.ExternalAccountListParams,
                ),
            ),
            model=ExternalAccount,
        )


class ExternalAccountsWithRawResponse:
    def __init__(self, external_accounts: ExternalAccounts) -> None:
        self._external_accounts = external_accounts

        self.create = _legacy_response.to_raw_response_wrapper(
            external_accounts.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            external_accounts.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            external_accounts.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            external_accounts.list,
        )


class AsyncExternalAccountsWithRawResponse:
    def __init__(self, external_accounts: AsyncExternalAccounts) -> None:
        self._external_accounts = external_accounts

        self.create = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            external_accounts.list,
        )


class ExternalAccountsWithStreamingResponse:
    def __init__(self, external_accounts: ExternalAccounts) -> None:
        self._external_accounts = external_accounts

        self.create = to_streamed_response_wrapper(
            external_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            external_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            external_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            external_accounts.list,
        )


class AsyncExternalAccountsWithStreamingResponse:
    def __init__(self, external_accounts: AsyncExternalAccounts) -> None:
        self._external_accounts = external_accounts

        self.create = async_to_streamed_response_wrapper(
            external_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            external_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            external_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            external_accounts.list,
        )
