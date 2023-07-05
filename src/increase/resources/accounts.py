# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..types import (
    Account,
    account_list_params,
    account_create_params,
    account_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    def create(
        self,
        *,
        name: str,
        entity_id: str | NotGiven = NOT_GIVEN,
        informational_entity_id: str | NotGiven = NOT_GIVEN,
        program_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Account:
        """
        Create an Account

        Args:
          name: The name you choose for the Account.

          entity_id: The identifier for the Entity that will own the Account.

          informational_entity_id: The identifier of an Entity that, while not owning the Account, is associated
              with its activity. Its relationship to your group must be `informational`.

          program_id: The identifier for the Program that this Account falls under. Required if you
              operate more than one Program.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "entity_id": entity_id,
                    "informational_entity_id": informational_entity_id,
                    "program_id": program_id,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Account,
        )

    def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Retrieve an Account

        Args:
          account_id: The identifier of the Account to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def update(
        self,
        account_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Account:
        """
        Update an Account

        Args:
          account_id: The identifier of the Account to update.

          name: The new name of the Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/accounts/{account_id}",
            body=maybe_transform({"name": name}, account_update_params.AccountUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        created_at: account_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        informational_entity_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Account]:
        """
        List Accounts

        Args:
          cursor: Return the page of entries after this one.

          entity_id: Filter Accounts for those belonging to the specified Entity.

          informational_entity_id: Filter Accounts for those belonging to the specified Entity as informational.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          status: Filter Accounts for those with the specified status.

              - `open` - Open Accounts that are ready to use.
              - `closed` - Closed Accounts on which no new activity can occur.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounts",
            page=SyncPage[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "entity_id": entity_id,
                        "informational_entity_id": informational_entity_id,
                        "limit": limit,
                        "status": status,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=Account,
        )

    def close(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Account:
        """
        Close an Account

        Args:
          account_id: The identifier of the Account to close.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/accounts/{account_id}/close",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Account,
        )


class AsyncAccounts(AsyncAPIResource):
    async def create(
        self,
        *,
        name: str,
        entity_id: str | NotGiven = NOT_GIVEN,
        informational_entity_id: str | NotGiven = NOT_GIVEN,
        program_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Account:
        """
        Create an Account

        Args:
          name: The name you choose for the Account.

          entity_id: The identifier for the Entity that will own the Account.

          informational_entity_id: The identifier of an Entity that, while not owning the Account, is associated
              with its activity. Its relationship to your group must be `informational`.

          program_id: The identifier for the Program that this Account falls under. Required if you
              operate more than one Program.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "entity_id": entity_id,
                    "informational_entity_id": informational_entity_id,
                    "program_id": program_id,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Account,
        )

    async def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Retrieve an Account

        Args:
          account_id: The identifier of the Account to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def update(
        self,
        account_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Account:
        """
        Update an Account

        Args:
          account_id: The identifier of the Account to update.

          name: The new name of the Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/accounts/{account_id}",
            body=maybe_transform({"name": name}, account_update_params.AccountUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        created_at: account_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        informational_entity_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Account, AsyncPage[Account]]:
        """
        List Accounts

        Args:
          cursor: Return the page of entries after this one.

          entity_id: Filter Accounts for those belonging to the specified Entity.

          informational_entity_id: Filter Accounts for those belonging to the specified Entity as informational.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          status: Filter Accounts for those with the specified status.

              - `open` - Open Accounts that are ready to use.
              - `closed` - Closed Accounts on which no new activity can occur.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounts",
            page=AsyncPage[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "entity_id": entity_id,
                        "informational_entity_id": informational_entity_id,
                        "limit": limit,
                        "status": status,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=Account,
        )

    async def close(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Account:
        """
        Close an Account

        Args:
          account_id: The identifier of the Account to close.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/accounts/{account_id}/close",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Account,
        )
