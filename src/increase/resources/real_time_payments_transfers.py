# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import (
    RealTimePaymentsTransfer,
    real_time_payments_transfer_list_params,
    real_time_payments_transfer_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["RealTimePaymentsTransfers", "AsyncRealTimePaymentsTransfers"]


class RealTimePaymentsTransfers(SyncAPIResource):
    def create(
        self,
        *,
        amount: int,
        creditor_name: str,
        remittance_information: str,
        source_account_number_id: str,
        destination_account_number: str | NotGiven = NOT_GIVEN,
        destination_routing_number: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsTransfer:
        """
        Create a Real Time Payments Transfer

        Args:
          amount: The transfer amount in USD cents. For Real Time Payments transfers, must be
              positive.

          creditor_name: The name of the transfer's recipient.

          remittance_information: Unstructured information that will show on the recipient's bank statement.

          source_account_number_id: The identifier of the Account Number from which to send the transfer.

          destination_account_number: The destination account number.

          destination_routing_number: The destination American Bankers' Association (ABA) Routing Transit Number
              (RTN).

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `destination_account_number` and `destination_routing_number` must be
              absent.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          unique_identifier: A unique identifier you choose for the transfer. Reusing this identifer for
              another transfer will result in an error. You can query for the transfer
              associated with this identifier using the List endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/real_time_payments_transfers",
            body=maybe_transform(
                {
                    "amount": amount,
                    "creditor_name": creditor_name,
                    "remittance_information": remittance_information,
                    "source_account_number_id": source_account_number_id,
                    "destination_account_number": destination_account_number,
                    "destination_routing_number": destination_routing_number,
                    "external_account_id": external_account_id,
                    "require_approval": require_approval,
                    "unique_identifier": unique_identifier,
                },
                real_time_payments_transfer_create_params.RealTimePaymentsTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimePaymentsTransfer,
        )

    def retrieve(
        self,
        real_time_payments_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RealTimePaymentsTransfer:
        """
        Retrieve a Real Time Payments Transfer

        Args:
          real_time_payments_transfer_id: The identifier of the Real Time Payments Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/real_time_payments_transfers/{real_time_payments_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealTimePaymentsTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: real_time_payments_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[RealTimePaymentsTransfer]:
        """
        List Real Time Payments Transfers

        Args:
          account_id: Filter Real Time Payments Transfers to those belonging to the specified Account.

          cursor: Return the page of entries after this one.

          external_account_id: Filter Real Time Payments Transfers to those made to the specified External
              Account.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          unique_identifier: Filter ACH Transfers to the one with the specified unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/real_time_payments_transfers",
            page=SyncPage[RealTimePaymentsTransfer],
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
                        "external_account_id": external_account_id,
                        "limit": limit,
                        "unique_identifier": unique_identifier,
                    },
                    real_time_payments_transfer_list_params.RealTimePaymentsTransferListParams,
                ),
            ),
            model=RealTimePaymentsTransfer,
        )


class AsyncRealTimePaymentsTransfers(AsyncAPIResource):
    async def create(
        self,
        *,
        amount: int,
        creditor_name: str,
        remittance_information: str,
        source_account_number_id: str,
        destination_account_number: str | NotGiven = NOT_GIVEN,
        destination_routing_number: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsTransfer:
        """
        Create a Real Time Payments Transfer

        Args:
          amount: The transfer amount in USD cents. For Real Time Payments transfers, must be
              positive.

          creditor_name: The name of the transfer's recipient.

          remittance_information: Unstructured information that will show on the recipient's bank statement.

          source_account_number_id: The identifier of the Account Number from which to send the transfer.

          destination_account_number: The destination account number.

          destination_routing_number: The destination American Bankers' Association (ABA) Routing Transit Number
              (RTN).

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `destination_account_number` and `destination_routing_number` must be
              absent.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          unique_identifier: A unique identifier you choose for the transfer. Reusing this identifer for
              another transfer will result in an error. You can query for the transfer
              associated with this identifier using the List endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/real_time_payments_transfers",
            body=maybe_transform(
                {
                    "amount": amount,
                    "creditor_name": creditor_name,
                    "remittance_information": remittance_information,
                    "source_account_number_id": source_account_number_id,
                    "destination_account_number": destination_account_number,
                    "destination_routing_number": destination_routing_number,
                    "external_account_id": external_account_id,
                    "require_approval": require_approval,
                    "unique_identifier": unique_identifier,
                },
                real_time_payments_transfer_create_params.RealTimePaymentsTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimePaymentsTransfer,
        )

    async def retrieve(
        self,
        real_time_payments_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RealTimePaymentsTransfer:
        """
        Retrieve a Real Time Payments Transfer

        Args:
          real_time_payments_transfer_id: The identifier of the Real Time Payments Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/real_time_payments_transfers/{real_time_payments_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealTimePaymentsTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: real_time_payments_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RealTimePaymentsTransfer, AsyncPage[RealTimePaymentsTransfer]]:
        """
        List Real Time Payments Transfers

        Args:
          account_id: Filter Real Time Payments Transfers to those belonging to the specified Account.

          cursor: Return the page of entries after this one.

          external_account_id: Filter Real Time Payments Transfers to those made to the specified External
              Account.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          unique_identifier: Filter ACH Transfers to the one with the specified unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/real_time_payments_transfers",
            page=AsyncPage[RealTimePaymentsTransfer],
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
                        "external_account_id": external_account_id,
                        "limit": limit,
                        "unique_identifier": unique_identifier,
                    },
                    real_time_payments_transfer_list_params.RealTimePaymentsTransferListParams,
                ),
            ),
            model=RealTimePaymentsTransfer,
        )
