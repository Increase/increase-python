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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransferReturn:
        """
        Create an ACH Return

        Args:
          reason: The reason why this transfer will be returned. The most usual return codes are
              `payment_stopped` for debits and `credit_entry_refused_by_receiver` for credits.

              - `authorization_revoked_by_customer` - The customer no longer authorizes this
                transaction. The Nacha return code is R07.
              - `payment_stopped` - The customer asked for the payment to be stopped. This
                reason is only allowed for debits. The Nacha return code is R08.
              - `customer_advised_unauthorized_improper_ineligible_or_incomplete` - The
                customer advises that the debit was unauthorized. The Nacha return code is
                R10.
              - `representative_payee_deceased_or_unable_to_continue_in_that_capacity` - The
                payee is deceased. The Nacha return code is R14.
              - `beneficiary_or_account_holder_deceased` - The account holder is deceased. The
                Nacha return code is R15.
              - `credit_entry_refused_by_receiver` - The customer refused a credit entry. This
                reason is only allowed for credits. The Nacha return code is R23.
              - `duplicate_entry` - The account holder identified this transaction as a
                duplicate. The Nacha return code is R24.
              - `corporate_customer_advised_not_authorized` - The corporate customer no longer
                authorizes this transaction. The Nacha return code is R29.

          transaction_id: The transaction identifier of the Inbound ACH Transfer to return to the
              originating financial institution.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/inbound_ach_transfer_returns",
            body=maybe_transform(
                {
                    "reason": reason,
                    "transaction_id": transaction_id,
                },
                inbound_ach_transfer_return_create_params.InboundACHTransferReturnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> InboundACHTransferReturn:
        """
        Retrieve an Inbound ACH Transfer Return

        Args:
          inbound_ach_transfer_return_id: The identifier of the Inbound ACH Transfer Return to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/inbound_ach_transfer_returns/{inbound_ach_transfer_return_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_ach_transfer_returns",
            page=SyncPage[InboundACHTransferReturn],
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransferReturn:
        """
        Create an ACH Return

        Args:
          reason: The reason why this transfer will be returned. The most usual return codes are
              `payment_stopped` for debits and `credit_entry_refused_by_receiver` for credits.

              - `authorization_revoked_by_customer` - The customer no longer authorizes this
                transaction. The Nacha return code is R07.
              - `payment_stopped` - The customer asked for the payment to be stopped. This
                reason is only allowed for debits. The Nacha return code is R08.
              - `customer_advised_unauthorized_improper_ineligible_or_incomplete` - The
                customer advises that the debit was unauthorized. The Nacha return code is
                R10.
              - `representative_payee_deceased_or_unable_to_continue_in_that_capacity` - The
                payee is deceased. The Nacha return code is R14.
              - `beneficiary_or_account_holder_deceased` - The account holder is deceased. The
                Nacha return code is R15.
              - `credit_entry_refused_by_receiver` - The customer refused a credit entry. This
                reason is only allowed for credits. The Nacha return code is R23.
              - `duplicate_entry` - The account holder identified this transaction as a
                duplicate. The Nacha return code is R24.
              - `corporate_customer_advised_not_authorized` - The corporate customer no longer
                authorizes this transaction. The Nacha return code is R29.

          transaction_id: The transaction identifier of the Inbound ACH Transfer to return to the
              originating financial institution.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/inbound_ach_transfer_returns",
            body=maybe_transform(
                {
                    "reason": reason,
                    "transaction_id": transaction_id,
                },
                inbound_ach_transfer_return_create_params.InboundACHTransferReturnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> InboundACHTransferReturn:
        """
        Retrieve an Inbound ACH Transfer Return

        Args:
          inbound_ach_transfer_return_id: The identifier of the Inbound ACH Transfer Return to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/inbound_ach_transfer_returns/{inbound_ach_transfer_return_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_ach_transfer_returns",
            page=AsyncPage[InboundACHTransferReturn],
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
                    inbound_ach_transfer_return_list_params.InboundACHTransferReturnListParams,
                ),
            ),
            model=InboundACHTransferReturn,
        )
