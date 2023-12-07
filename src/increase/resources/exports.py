# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING
from typing_extensions import Literal

import httpx

from ..types import Export, export_list_params, export_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import Increase, AsyncIncrease

__all__ = ["Exports", "AsyncExports"]


class Exports(SyncAPIResource):
    with_raw_response: ExportsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = ExportsWithRawResponse(self)

    def create(
        self,
        *,
        category: Literal[
            "account_statement_ofx", "transaction_csv", "balance_csv", "bookkeeping_account_balance_csv", "entity_csv"
        ],
        account_statement_ofx: export_create_params.AccountStatementOfx | NotGiven = NOT_GIVEN,
        balance_csv: export_create_params.BalanceCsv | NotGiven = NOT_GIVEN,
        bookkeeping_account_balance_csv: export_create_params.BookkeepingAccountBalanceCsv | NotGiven = NOT_GIVEN,
        entity_csv: export_create_params.EntityCsv | NotGiven = NOT_GIVEN,
        transaction_csv: export_create_params.TransactionCsv | NotGiven = NOT_GIVEN,
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
              - `transaction_csv` - Export a CSV of all transactions for a given time range.
              - `balance_csv` - Export a CSV of account balances for the dates in a given
                range.
              - `bookkeeping_account_balance_csv` - Export a CSV of bookkeeping account
                balances for the dates in a given range.
              - `entity_csv` - Export a CSV of entities with a given status.

          account_statement_ofx: Options for the created export. Required if `category` is equal to
              `account_statement_ofx`.

          balance_csv: Options for the created export. Required if `category` is equal to
              `balance_csv`.

          bookkeeping_account_balance_csv: Options for the created export. Required if `category` is equal to
              `bookkeeping_account_balance_csv`.

          entity_csv: Options for the created export. Required if `category` is equal to `entity_csv`.

          transaction_csv: Options for the created export. Required if `category` is equal to
              `transaction_csv`.

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
                    "account_statement_ofx": account_statement_ofx,
                    "balance_csv": balance_csv,
                    "bookkeeping_account_balance_csv": bookkeeping_account_balance_csv,
                    "entity_csv": entity_csv,
                    "transaction_csv": transaction_csv,
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
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
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
                        "cursor": cursor,
                        "limit": limit,
                    },
                    export_list_params.ExportListParams,
                ),
            ),
            model=Export,
        )


class AsyncExports(AsyncAPIResource):
    with_raw_response: AsyncExportsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncExportsWithRawResponse(self)

    async def create(
        self,
        *,
        category: Literal[
            "account_statement_ofx", "transaction_csv", "balance_csv", "bookkeeping_account_balance_csv", "entity_csv"
        ],
        account_statement_ofx: export_create_params.AccountStatementOfx | NotGiven = NOT_GIVEN,
        balance_csv: export_create_params.BalanceCsv | NotGiven = NOT_GIVEN,
        bookkeeping_account_balance_csv: export_create_params.BookkeepingAccountBalanceCsv | NotGiven = NOT_GIVEN,
        entity_csv: export_create_params.EntityCsv | NotGiven = NOT_GIVEN,
        transaction_csv: export_create_params.TransactionCsv | NotGiven = NOT_GIVEN,
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
              - `transaction_csv` - Export a CSV of all transactions for a given time range.
              - `balance_csv` - Export a CSV of account balances for the dates in a given
                range.
              - `bookkeeping_account_balance_csv` - Export a CSV of bookkeeping account
                balances for the dates in a given range.
              - `entity_csv` - Export a CSV of entities with a given status.

          account_statement_ofx: Options for the created export. Required if `category` is equal to
              `account_statement_ofx`.

          balance_csv: Options for the created export. Required if `category` is equal to
              `balance_csv`.

          bookkeeping_account_balance_csv: Options for the created export. Required if `category` is equal to
              `bookkeeping_account_balance_csv`.

          entity_csv: Options for the created export. Required if `category` is equal to `entity_csv`.

          transaction_csv: Options for the created export. Required if `category` is equal to
              `transaction_csv`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/exports",
            body=maybe_transform(
                {
                    "category": category,
                    "account_statement_ofx": account_statement_ofx,
                    "balance_csv": balance_csv,
                    "bookkeeping_account_balance_csv": bookkeeping_account_balance_csv,
                    "entity_csv": entity_csv,
                    "transaction_csv": transaction_csv,
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
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
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
                        "cursor": cursor,
                        "limit": limit,
                    },
                    export_list_params.ExportListParams,
                ),
            ),
            model=Export,
        )


class ExportsWithRawResponse:
    def __init__(self, exports: Exports) -> None:
        self.create = to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            exports.retrieve,
        )
        self.list = to_raw_response_wrapper(
            exports.list,
        )


class AsyncExportsWithRawResponse:
    def __init__(self, exports: AsyncExports) -> None:
        self.create = async_to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            exports.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            exports.list,
        )
