# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..types import (
    InboundACHTransfer,
    inbound_ach_transfer_list_params,
    inbound_ach_transfer_transfer_return_params,
    inbound_ach_transfer_notification_of_change_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["InboundACHTransfers", "AsyncInboundACHTransfers"]


class InboundACHTransfers(SyncAPIResource):
    def retrieve(
        self,
        inbound_ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> InboundACHTransfer:
        """
        Retrieve an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer to get details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundACHTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: inbound_ach_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["pending", "declined", "accepted", "returned"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InboundACHTransfer]:
        """
        List Inbound ACH Transfers

        Args:
          account_id: Filter Inbound ACH Tranfers to ones belonging to the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          status: Filter Inbound ACH Transfers to those with the specified status.

              - `pending` - The Inbound ACH Transfer is awaiting action, will transition
                automatically if no action is taken.
              - `declined` - The Inbound ACH Transfer has been declined.
              - `accepted` - The Inbound ACH Transfer is accepted.
              - `returned` - The Inbound ACH Transfer has been returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_ach_transfers",
            page=SyncPage[InboundACHTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    inbound_ach_transfer_list_params.InboundACHTransferListParams,
                ),
            ),
            model=InboundACHTransfer,
        )

    def decline(
        self,
        inbound_ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """
        Decline an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer to decline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/decline",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundACHTransfer,
        )

    def notification_of_change(
        self,
        inbound_ach_transfer_id: str,
        *,
        updated_account_number: str | NotGiven = NOT_GIVEN,
        updated_routing_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """
        Create a notification of change for an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer for which to create a notification of
              change.

          updated_account_number: The updated account number to send in the notification of change.

          updated_routing_number: The updated routing number to send in the notification of change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/notification_of_change",
            body=maybe_transform(
                {
                    "updated_account_number": updated_account_number,
                    "updated_routing_number": updated_routing_number,
                },
                inbound_ach_transfer_notification_of_change_params.InboundACHTransferNotificationOfChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundACHTransfer,
        )

    def transfer_return(
        self,
        inbound_ach_transfer_id: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """
        Return an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer to return to the originating
              financial institution.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/transfer_return",
            body=maybe_transform(
                {"reason": reason}, inbound_ach_transfer_transfer_return_params.InboundACHTransferTransferReturnParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundACHTransfer,
        )


class AsyncInboundACHTransfers(AsyncAPIResource):
    async def retrieve(
        self,
        inbound_ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> InboundACHTransfer:
        """
        Retrieve an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer to get details for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundACHTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: inbound_ach_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["pending", "declined", "accepted", "returned"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InboundACHTransfer, AsyncPage[InboundACHTransfer]]:
        """
        List Inbound ACH Transfers

        Args:
          account_id: Filter Inbound ACH Tranfers to ones belonging to the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          status: Filter Inbound ACH Transfers to those with the specified status.

              - `pending` - The Inbound ACH Transfer is awaiting action, will transition
                automatically if no action is taken.
              - `declined` - The Inbound ACH Transfer has been declined.
              - `accepted` - The Inbound ACH Transfer is accepted.
              - `returned` - The Inbound ACH Transfer has been returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_ach_transfers",
            page=AsyncPage[InboundACHTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    inbound_ach_transfer_list_params.InboundACHTransferListParams,
                ),
            ),
            model=InboundACHTransfer,
        )

    async def decline(
        self,
        inbound_ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """
        Decline an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer to decline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/decline",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundACHTransfer,
        )

    async def notification_of_change(
        self,
        inbound_ach_transfer_id: str,
        *,
        updated_account_number: str | NotGiven = NOT_GIVEN,
        updated_routing_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """
        Create a notification of change for an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer for which to create a notification of
              change.

          updated_account_number: The updated account number to send in the notification of change.

          updated_routing_number: The updated routing number to send in the notification of change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/notification_of_change",
            body=maybe_transform(
                {
                    "updated_account_number": updated_account_number,
                    "updated_routing_number": updated_routing_number,
                },
                inbound_ach_transfer_notification_of_change_params.InboundACHTransferNotificationOfChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundACHTransfer,
        )

    async def transfer_return(
        self,
        inbound_ach_transfer_id: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """
        Return an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer to return to the originating
              financial institution.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/transfer_return",
            body=maybe_transform(
                {"reason": reason}, inbound_ach_transfer_transfer_return_params.InboundACHTransferTransferReturnParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundACHTransfer,
        )
