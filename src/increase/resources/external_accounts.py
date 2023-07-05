# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..types import (
    ExternalAccount,
    external_account_list_params,
    external_account_create_params,
    external_account_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["ExternalAccounts", "AsyncExternalAccounts"]


class ExternalAccounts(SyncAPIResource):
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        Update an External Account

        Args:
          external_account_id: The external account identifier.

          description: The description you choose to give the external account.

          status: The status of the External Account.

              - `active` - The External Acccount is active.
              - `archived` - The External Account is archived and won't appear in the
                dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
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
        status: external_account_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ExternalAccount]:
        """
        List External Accounts

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
                        "status": status,
                    },
                    external_account_list_params.ExternalAccountListParams,
                ),
            ),
            model=ExternalAccount,
        )


class AsyncExternalAccounts(AsyncAPIResource):
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalAccount:
        """
        Update an External Account

        Args:
          external_account_id: The external account identifier.

          description: The description you choose to give the external account.

          status: The status of the External Account.

              - `active` - The External Acccount is active.
              - `archived` - The External Account is archived and won't appear in the
                dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
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
        status: external_account_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ExternalAccount, AsyncPage[ExternalAccount]]:
        """
        List External Accounts

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
                        "status": status,
                    },
                    external_account_list_params.ExternalAccountListParams,
                ),
            ),
            model=ExternalAccount,
        )
