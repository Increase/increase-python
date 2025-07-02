# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    inbound_ach_transfer_list_params,
    inbound_ach_transfer_decline_params,
    inbound_ach_transfer_transfer_return_params,
    inbound_ach_transfer_create_notification_of_change_params,
)
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
from ..types.inbound_ach_transfer import InboundACHTransfer

__all__ = ["InboundACHTransfersResource", "AsyncInboundACHTransfersResource"]


class InboundACHTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundACHTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundACHTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundACHTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundACHTransfersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        inbound_ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not inbound_ach_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_ach_transfer_id` but received {inbound_ach_transfer_id!r}"
            )
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
        account_number_id: str | NotGiven = NOT_GIVEN,
        created_at: inbound_ach_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: inbound_ach_transfer_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InboundACHTransfer]:
        """
        List Inbound ACH Transfers

        Args:
          account_id: Filter Inbound ACH Transfers to ones belonging to the specified Account.

          account_number_id: Filter Inbound ACH Transfers to ones belonging to the specified Account Number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

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
                        "account_number_id": account_number_id,
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

    def create_notification_of_change(
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not inbound_ach_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_ach_transfer_id` but received {inbound_ach_transfer_id!r}"
            )
        return self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/create_notification_of_change",
            body=maybe_transform(
                {
                    "updated_account_number": updated_account_number,
                    "updated_routing_number": updated_routing_number,
                },
                inbound_ach_transfer_create_notification_of_change_params.InboundACHTransferCreateNotificationOfChangeParams,
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

    def decline(
        self,
        inbound_ach_transfer_id: str,
        *,
        reason: Literal[
            "insufficient_funds",
            "returned_per_odfi_request",
            "authorization_revoked_by_customer",
            "payment_stopped",
            "customer_advised_unauthorized_improper_ineligible_or_incomplete",
            "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
            "beneficiary_or_account_holder_deceased",
            "credit_entry_refused_by_receiver",
            "duplicate_entry",
            "corporate_customer_advised_not_authorized",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """
        Decline an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer to decline.

          reason: The reason why this transfer will be returned. If this parameter is unset, the
              return codes will be `payment_stopped` for debits and
              `credit_entry_refused_by_receiver` for credits.

              - `insufficient_funds` - The customer's account has insufficient funds. This
                reason is only allowed for debits. The Nacha return code is R01.
              - `returned_per_odfi_request` - The originating financial institution asked for
                this transfer to be returned. The receiving bank is complying with the
                request. The Nacha return code is R06.
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
        if not inbound_ach_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_ach_transfer_id` but received {inbound_ach_transfer_id!r}"
            )
        return self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/decline",
            body=maybe_transform(
                {"reason": reason}, inbound_ach_transfer_decline_params.InboundACHTransferDeclineParams
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
            "insufficient_funds",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """
        Return an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer to return to the originating
              financial institution.

          reason: The reason why this transfer will be returned. The most usual return codes are
              `payment_stopped` for debits and `credit_entry_refused_by_receiver` for credits.

              - `insufficient_funds` - The customer's account has insufficient funds. This
                reason is only allowed for debits. The Nacha return code is R01.
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
        if not inbound_ach_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_ach_transfer_id` but received {inbound_ach_transfer_id!r}"
            )
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


class AsyncInboundACHTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundACHTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundACHTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundACHTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundACHTransfersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        inbound_ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not inbound_ach_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_ach_transfer_id` but received {inbound_ach_transfer_id!r}"
            )
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
        account_number_id: str | NotGiven = NOT_GIVEN,
        created_at: inbound_ach_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: inbound_ach_transfer_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InboundACHTransfer, AsyncPage[InboundACHTransfer]]:
        """
        List Inbound ACH Transfers

        Args:
          account_id: Filter Inbound ACH Transfers to ones belonging to the specified Account.

          account_number_id: Filter Inbound ACH Transfers to ones belonging to the specified Account Number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

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
                        "account_number_id": account_number_id,
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

    async def create_notification_of_change(
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if not inbound_ach_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_ach_transfer_id` but received {inbound_ach_transfer_id!r}"
            )
        return await self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/create_notification_of_change",
            body=await async_maybe_transform(
                {
                    "updated_account_number": updated_account_number,
                    "updated_routing_number": updated_routing_number,
                },
                inbound_ach_transfer_create_notification_of_change_params.InboundACHTransferCreateNotificationOfChangeParams,
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

    async def decline(
        self,
        inbound_ach_transfer_id: str,
        *,
        reason: Literal[
            "insufficient_funds",
            "returned_per_odfi_request",
            "authorization_revoked_by_customer",
            "payment_stopped",
            "customer_advised_unauthorized_improper_ineligible_or_incomplete",
            "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
            "beneficiary_or_account_holder_deceased",
            "credit_entry_refused_by_receiver",
            "duplicate_entry",
            "corporate_customer_advised_not_authorized",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """
        Decline an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer to decline.

          reason: The reason why this transfer will be returned. If this parameter is unset, the
              return codes will be `payment_stopped` for debits and
              `credit_entry_refused_by_receiver` for credits.

              - `insufficient_funds` - The customer's account has insufficient funds. This
                reason is only allowed for debits. The Nacha return code is R01.
              - `returned_per_odfi_request` - The originating financial institution asked for
                this transfer to be returned. The receiving bank is complying with the
                request. The Nacha return code is R06.
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
        if not inbound_ach_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_ach_transfer_id` but received {inbound_ach_transfer_id!r}"
            )
        return await self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/decline",
            body=await async_maybe_transform(
                {"reason": reason}, inbound_ach_transfer_decline_params.InboundACHTransferDeclineParams
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
            "insufficient_funds",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """
        Return an Inbound ACH Transfer

        Args:
          inbound_ach_transfer_id: The identifier of the Inbound ACH Transfer to return to the originating
              financial institution.

          reason: The reason why this transfer will be returned. The most usual return codes are
              `payment_stopped` for debits and `credit_entry_refused_by_receiver` for credits.

              - `insufficient_funds` - The customer's account has insufficient funds. This
                reason is only allowed for debits. The Nacha return code is R01.
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
        if not inbound_ach_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_ach_transfer_id` but received {inbound_ach_transfer_id!r}"
            )
        return await self._post(
            f"/inbound_ach_transfers/{inbound_ach_transfer_id}/transfer_return",
            body=await async_maybe_transform(
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


class InboundACHTransfersResourceWithRawResponse:
    def __init__(self, inbound_ach_transfers: InboundACHTransfersResource) -> None:
        self._inbound_ach_transfers = inbound_ach_transfers

        self.retrieve = to_raw_response_wrapper(
            inbound_ach_transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inbound_ach_transfers.list,
        )
        self.create_notification_of_change = to_raw_response_wrapper(
            inbound_ach_transfers.create_notification_of_change,
        )
        self.decline = to_raw_response_wrapper(
            inbound_ach_transfers.decline,
        )
        self.transfer_return = to_raw_response_wrapper(
            inbound_ach_transfers.transfer_return,
        )


class AsyncInboundACHTransfersResourceWithRawResponse:
    def __init__(self, inbound_ach_transfers: AsyncInboundACHTransfersResource) -> None:
        self._inbound_ach_transfers = inbound_ach_transfers

        self.retrieve = async_to_raw_response_wrapper(
            inbound_ach_transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inbound_ach_transfers.list,
        )
        self.create_notification_of_change = async_to_raw_response_wrapper(
            inbound_ach_transfers.create_notification_of_change,
        )
        self.decline = async_to_raw_response_wrapper(
            inbound_ach_transfers.decline,
        )
        self.transfer_return = async_to_raw_response_wrapper(
            inbound_ach_transfers.transfer_return,
        )


class InboundACHTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_ach_transfers: InboundACHTransfersResource) -> None:
        self._inbound_ach_transfers = inbound_ach_transfers

        self.retrieve = to_streamed_response_wrapper(
            inbound_ach_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inbound_ach_transfers.list,
        )
        self.create_notification_of_change = to_streamed_response_wrapper(
            inbound_ach_transfers.create_notification_of_change,
        )
        self.decline = to_streamed_response_wrapper(
            inbound_ach_transfers.decline,
        )
        self.transfer_return = to_streamed_response_wrapper(
            inbound_ach_transfers.transfer_return,
        )


class AsyncInboundACHTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_ach_transfers: AsyncInboundACHTransfersResource) -> None:
        self._inbound_ach_transfers = inbound_ach_transfers

        self.retrieve = async_to_streamed_response_wrapper(
            inbound_ach_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_ach_transfers.list,
        )
        self.create_notification_of_change = async_to_streamed_response_wrapper(
            inbound_ach_transfers.create_notification_of_change,
        )
        self.decline = async_to_streamed_response_wrapper(
            inbound_ach_transfers.decline,
        )
        self.transfer_return = async_to_streamed_response_wrapper(
            inbound_ach_transfers.transfer_return,
        )
