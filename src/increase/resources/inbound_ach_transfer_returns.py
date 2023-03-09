# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..types import (
    InboundACHTransferReturn,
    inbound_ach_transfer_return_list_params,
    inbound_ach_transfer_return_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["InboundACHTransferReturns", "AsyncInboundACHTransferReturns"]


class InboundACHTransferReturns(SyncAPIResource):
    def create(
        self,
        *,
        reason: Literal[
            "authorization_revoked_by_customer",
            "payment_stopped",
            "customer_advised_unauthorized_improper_ineligible_or_incomplete",
            "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
            "beneficiary_or_account_holder_deceased",
            "credit_entry_refused_by_receiver",
            "duplicate_entry",
            "corporate_customer_advised_not_authorized",
        ],
        transaction_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InboundACHTransferReturn:
        """
        Create an ACH Return

        Args:
          reason: The reason why this transfer will be returned. The most usual return codes are
              `payment_stopped` for debits and `credit_entry_refused_by_receiver` for credits.

          transaction_id: The transaction identifier of the Inbound ACH Transfer to return to the
              originating financial institution.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/inbound_ach_transfer_returns",
            body=maybe_transform(
                {
                    "transaction_id": transaction_id,
                    "reason": reason,
                },
                inbound_ach_transfer_return_create_params.InboundACHTransferReturnCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InboundACHTransferReturn,
        )

    def retrieve(
        self,
        inbound_ach_transfer_return_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InboundACHTransferReturn:
        """Retrieve an Inbound ACH Transfer Return"""
        return self._get(
            f"/inbound_ach_transfer_returns/{inbound_ach_transfer_return_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InboundACHTransferReturn,
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
    ) -> SyncPage[InboundACHTransferReturn]:
        """
        List Inbound ACH Transfer Returns

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/inbound_ach_transfer_returns",
            page=SyncPage[InboundACHTransferReturn],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    inbound_ach_transfer_return_list_params.InboundACHTransferReturnListParams,
                ),
            ),
            model=InboundACHTransferReturn,
        )


class AsyncInboundACHTransferReturns(AsyncAPIResource):
    async def create(
        self,
        *,
        reason: Literal[
            "authorization_revoked_by_customer",
            "payment_stopped",
            "customer_advised_unauthorized_improper_ineligible_or_incomplete",
            "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
            "beneficiary_or_account_holder_deceased",
            "credit_entry_refused_by_receiver",
            "duplicate_entry",
            "corporate_customer_advised_not_authorized",
        ],
        transaction_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InboundACHTransferReturn:
        """
        Create an ACH Return

        Args:
          reason: The reason why this transfer will be returned. The most usual return codes are
              `payment_stopped` for debits and `credit_entry_refused_by_receiver` for credits.

          transaction_id: The transaction identifier of the Inbound ACH Transfer to return to the
              originating financial institution.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/inbound_ach_transfer_returns",
            body=maybe_transform(
                {
                    "transaction_id": transaction_id,
                    "reason": reason,
                },
                inbound_ach_transfer_return_create_params.InboundACHTransferReturnCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InboundACHTransferReturn,
        )

    async def retrieve(
        self,
        inbound_ach_transfer_return_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InboundACHTransferReturn:
        """Retrieve an Inbound ACH Transfer Return"""
        return await self._get(
            f"/inbound_ach_transfer_returns/{inbound_ach_transfer_return_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InboundACHTransferReturn,
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
    ) -> AsyncPaginator[InboundACHTransferReturn, AsyncPage[InboundACHTransferReturn]]:
        """
        List Inbound ACH Transfer Returns

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/inbound_ach_transfer_returns",
            page=AsyncPage[InboundACHTransferReturn],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    inbound_ach_transfer_return_list_params.InboundACHTransferReturnListParams,
                ),
            ),
            model=InboundACHTransferReturn,
        )
