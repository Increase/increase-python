# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import datetime

from ..types import BookkeepingEntrySet, bookkeeping_entry_set_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["BookkeepingEntrySets", "AsyncBookkeepingEntrySets"]


class BookkeepingEntrySets(SyncAPIResource):
    def create(
        self,
        *,
        entries: List[bookkeeping_entry_set_create_params.Entry],
        date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BookkeepingEntrySet:
        """
        Create a Bookkeeping Entry Set

        Args:
          entries: The bookkeeping entries.

          date: The date of the transaction. If `transaction_id` is provided, this must match
              the `created_at` field on that resource.

          transaction_id: The identifier of the Transaction related to this entry set, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/bookkeeping_entry_sets",
            body=maybe_transform(
                {
                    "entries": entries,
                    "date": date,
                    "transaction_id": transaction_id,
                },
                bookkeeping_entry_set_create_params.BookkeepingEntrySetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BookkeepingEntrySet,
        )


class AsyncBookkeepingEntrySets(AsyncAPIResource):
    async def create(
        self,
        *,
        entries: List[bookkeeping_entry_set_create_params.Entry],
        date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BookkeepingEntrySet:
        """
        Create a Bookkeeping Entry Set

        Args:
          entries: The bookkeeping entries.

          date: The date of the transaction. If `transaction_id` is provided, this must match
              the `created_at` field on that resource.

          transaction_id: The identifier of the Transaction related to this entry set, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/bookkeeping_entry_sets",
            body=maybe_transform(
                {
                    "entries": entries,
                    "date": date,
                    "transaction_id": transaction_id,
                },
                bookkeeping_entry_set_create_params.BookkeepingEntrySetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BookkeepingEntrySet,
        )
