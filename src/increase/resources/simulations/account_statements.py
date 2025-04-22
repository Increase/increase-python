# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import account_statement_create_params
from ...types.account_statement import AccountStatement

__all__ = ["AccountStatementsResource", "AsyncAccountStatementsResource"]


class AccountStatementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountStatementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AccountStatementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountStatementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AccountStatementsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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


class AsyncAccountStatementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountStatementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountStatementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountStatementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncAccountStatementsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            body=await async_maybe_transform(
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


class AccountStatementsResourceWithRawResponse:
    def __init__(self, account_statements: AccountStatementsResource) -> None:
        self._account_statements = account_statements

        self.create = to_raw_response_wrapper(
            account_statements.create,
        )


class AsyncAccountStatementsResourceWithRawResponse:
    def __init__(self, account_statements: AsyncAccountStatementsResource) -> None:
        self._account_statements = account_statements

        self.create = async_to_raw_response_wrapper(
            account_statements.create,
        )


class AccountStatementsResourceWithStreamingResponse:
    def __init__(self, account_statements: AccountStatementsResource) -> None:
        self._account_statements = account_statements

        self.create = to_streamed_response_wrapper(
            account_statements.create,
        )


class AsyncAccountStatementsResourceWithStreamingResponse:
    def __init__(self, account_statements: AsyncAccountStatementsResource) -> None:
        self._account_statements = account_statements

        self.create = async_to_streamed_response_wrapper(
            account_statements.create,
        )
