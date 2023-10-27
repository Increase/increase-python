# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ...types import AccountStatement
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.simulations import account_statement_create_params

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["AccountStatements", "AsyncAccountStatements"]


class AccountStatements(SyncAPIResource):
    with_raw_response: AccountStatementsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = AccountStatementsWithRawResponse(self)

    def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountStatement:
        """
        Simulates an [Account Statement](#account-statements) being created for an
        account. In production, Account Statements are generated once per month.

        Args:
          account_id: The identifier of the Account the statement is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/account_statements",
            body=maybe_transform(
                {"account_id": account_id}, account_statement_create_params.AccountStatementCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountStatement,
        )


class AsyncAccountStatements(AsyncAPIResource):
    with_raw_response: AsyncAccountStatementsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncAccountStatementsWithRawResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountStatement:
        """
        Simulates an [Account Statement](#account-statements) being created for an
        account. In production, Account Statements are generated once per month.

        Args:
          account_id: The identifier of the Account the statement is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/account_statements",
            body=maybe_transform(
                {"account_id": account_id}, account_statement_create_params.AccountStatementCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountStatement,
        )


class AccountStatementsWithRawResponse:
    def __init__(self, account_statements: AccountStatements) -> None:
        self.create = to_raw_response_wrapper(
            account_statements.create,
        )


class AsyncAccountStatementsWithRawResponse:
    def __init__(self, account_statements: AsyncAccountStatements) -> None:
        self.create = async_to_raw_response_wrapper(
            account_statements.create,
        )
