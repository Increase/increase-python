# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import export_list_params, export_create_params
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
from ..types.export import Export

__all__ = ["ExportsResource", "AsyncExportsResource"]


class ExportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return ExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return ExportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        category: Literal[
            "account_statement_ofx",
            "account_statement_bai2",
            "transaction_csv",
            "balance_csv",
            "bookkeeping_account_balance_csv",
            "entity_csv",
            "vendor_csv",
        ],
        account_statement_bai2: export_create_params.AccountStatementBai2 | NotGiven = NOT_GIVEN,
        account_statement_ofx: export_create_params.AccountStatementOfx | NotGiven = NOT_GIVEN,
        balance_csv: export_create_params.BalanceCsv | NotGiven = NOT_GIVEN,
        bookkeeping_account_balance_csv: export_create_params.BookkeepingAccountBalanceCsv | NotGiven = NOT_GIVEN,
        entity_csv: export_create_params.EntityCsv | NotGiven = NOT_GIVEN,
        transaction_csv: export_create_params.TransactionCsv | NotGiven = NOT_GIVEN,
        vendor_csv: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Export:
        """
        Create an Export

        Args:
          category: The type of Export to create.

              - `account_statement_ofx` - Export an Open Financial Exchange (OFX) file of
                transactions and balances for a given time range and Account.
              - `account_statement_bai2` - Export a BAI2 file of transactions and balances for
                a given date and optional Account.
              - `transaction_csv` - Export a CSV of all transactions for a given time range.
              - `balance_csv` - Export a CSV of account balances for the dates in a given
                range.
              - `bookkeeping_account_balance_csv` - Export a CSV of bookkeeping account
                balances for the dates in a given range.
              - `entity_csv` - Export a CSV of entities with a given status.
              - `vendor_csv` - Export a CSV of vendors added to the third-party risk
                management dashboard.

          account_statement_bai2: Options for the created export. Required if `category` is equal to
              `account_statement_bai2`.

          account_statement_ofx: Options for the created export. Required if `category` is equal to
              `account_statement_ofx`.

          balance_csv: Options for the created export. Required if `category` is equal to
              `balance_csv`.

          bookkeeping_account_balance_csv: Options for the created export. Required if `category` is equal to
              `bookkeeping_account_balance_csv`.

          entity_csv: Options for the created export. Required if `category` is equal to `entity_csv`.

          transaction_csv: Options for the created export. Required if `category` is equal to
              `transaction_csv`.

          vendor_csv: Options for the created export. Required if `category` is equal to `vendor_csv`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/exports",
            body=maybe_transform(
                {
                    "category": category,
                    "account_statement_bai2": account_statement_bai2,
                    "account_statement_ofx": account_statement_ofx,
                    "balance_csv": balance_csv,
                    "bookkeeping_account_balance_csv": bookkeeping_account_balance_csv,
                    "entity_csv": entity_csv,
                    "transaction_csv": transaction_csv,
                    "vendor_csv": vendor_csv,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Export,
        )

    def retrieve(
        self,
        export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Export:
        """
        Retrieve an Export

        Args:
          export_id: The identifier of the Export to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return self._get(
            f"/exports/{export_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Export,
        )

    def list(
        self,
        *,
        category: export_list_params.Category | NotGiven = NOT_GIVEN,
        created_at: export_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: export_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Export]:
        """
        List Exports

        Args:
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
            "/exports",
            page=SyncPage[Export],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    export_list_params.ExportListParams,
                ),
            ),
            model=Export,
        )


class AsyncExportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncExportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        category: Literal[
            "account_statement_ofx",
            "account_statement_bai2",
            "transaction_csv",
            "balance_csv",
            "bookkeeping_account_balance_csv",
            "entity_csv",
            "vendor_csv",
        ],
        account_statement_bai2: export_create_params.AccountStatementBai2 | NotGiven = NOT_GIVEN,
        account_statement_ofx: export_create_params.AccountStatementOfx | NotGiven = NOT_GIVEN,
        balance_csv: export_create_params.BalanceCsv | NotGiven = NOT_GIVEN,
        bookkeeping_account_balance_csv: export_create_params.BookkeepingAccountBalanceCsv | NotGiven = NOT_GIVEN,
        entity_csv: export_create_params.EntityCsv | NotGiven = NOT_GIVEN,
        transaction_csv: export_create_params.TransactionCsv | NotGiven = NOT_GIVEN,
        vendor_csv: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Export:
        """
        Create an Export

        Args:
          category: The type of Export to create.

              - `account_statement_ofx` - Export an Open Financial Exchange (OFX) file of
                transactions and balances for a given time range and Account.
              - `account_statement_bai2` - Export a BAI2 file of transactions and balances for
                a given date and optional Account.
              - `transaction_csv` - Export a CSV of all transactions for a given time range.
              - `balance_csv` - Export a CSV of account balances for the dates in a given
                range.
              - `bookkeeping_account_balance_csv` - Export a CSV of bookkeeping account
                balances for the dates in a given range.
              - `entity_csv` - Export a CSV of entities with a given status.
              - `vendor_csv` - Export a CSV of vendors added to the third-party risk
                management dashboard.

          account_statement_bai2: Options for the created export. Required if `category` is equal to
              `account_statement_bai2`.

          account_statement_ofx: Options for the created export. Required if `category` is equal to
              `account_statement_ofx`.

          balance_csv: Options for the created export. Required if `category` is equal to
              `balance_csv`.

          bookkeeping_account_balance_csv: Options for the created export. Required if `category` is equal to
              `bookkeeping_account_balance_csv`.

          entity_csv: Options for the created export. Required if `category` is equal to `entity_csv`.

          transaction_csv: Options for the created export. Required if `category` is equal to
              `transaction_csv`.

          vendor_csv: Options for the created export. Required if `category` is equal to `vendor_csv`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/exports",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "account_statement_bai2": account_statement_bai2,
                    "account_statement_ofx": account_statement_ofx,
                    "balance_csv": balance_csv,
                    "bookkeeping_account_balance_csv": bookkeeping_account_balance_csv,
                    "entity_csv": entity_csv,
                    "transaction_csv": transaction_csv,
                    "vendor_csv": vendor_csv,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Export,
        )

    async def retrieve(
        self,
        export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Export:
        """
        Retrieve an Export

        Args:
          export_id: The identifier of the Export to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return await self._get(
            f"/exports/{export_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Export,
        )

    def list(
        self,
        *,
        category: export_list_params.Category | NotGiven = NOT_GIVEN,
        created_at: export_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: export_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Export, AsyncPage[Export]]:
        """
        List Exports

        Args:
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
            "/exports",
            page=AsyncPage[Export],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    export_list_params.ExportListParams,
                ),
            ),
            model=Export,
        )


class ExportsResourceWithRawResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            exports.retrieve,
        )
        self.list = to_raw_response_wrapper(
            exports.list,
        )


class AsyncExportsResourceWithRawResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            exports.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            exports.list,
        )


class ExportsResourceWithStreamingResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            exports.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            exports.list,
        )


class AsyncExportsResourceWithStreamingResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            exports.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            exports.list,
        )
