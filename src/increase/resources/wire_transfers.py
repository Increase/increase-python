# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import WireTransfer, wire_transfer_list_params, wire_transfer_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["WireTransfers", "AsyncWireTransfers"]


class WireTransfers(SyncAPIResource):
    def create(
        self,
        *,
        account_id: str,
        amount: int,
        beneficiary_name: str,
        message_to_recipient: str,
        account_number: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Create a Wire Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          amount: The transfer amount in cents.

          beneficiary_name: The beneficiary's name.

          message_to_recipient: The message that will show on the recipient's bank statement.

          account_number: The account number for the destination account.

          beneficiary_address_line1: The beneficiary's address line 1.

          beneficiary_address_line2: The beneficiary's address line 2.

          beneficiary_address_line3: The beneficiary's address line 3.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

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
            "/wire_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "beneficiary_name": beneficiary_name,
                    "message_to_recipient": message_to_recipient,
                    "account_number": account_number,
                    "beneficiary_address_line1": beneficiary_address_line1,
                    "beneficiary_address_line2": beneficiary_address_line2,
                    "beneficiary_address_line3": beneficiary_address_line3,
                    "external_account_id": external_account_id,
                    "require_approval": require_approval,
                    "routing_number": routing_number,
                    "unique_identifier": unique_identifier,
                },
                wire_transfer_create_params.WireTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    def retrieve(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> WireTransfer:
        """
        Retrieve a Wire Transfer

        Args:
          wire_transfer_id: The identifier of the Wire Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/wire_transfers/{wire_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
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
    ) -> SyncPage[WireTransfer]:
        """
        List Wire Transfers

        Args:
          account_id: Filter Wire Transfers to those belonging to the specified Account.

          cursor: Return the page of entries after this one.

          external_account_id: Filter Wire Transfers to those made to the specified External Account.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          unique_identifier: Filter Wire Transfers to the one with the specified unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/wire_transfers",
            page=SyncPage[WireTransfer],
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
                    wire_transfer_list_params.WireTransferListParams,
                ),
            ),
            model=WireTransfer,
        )

    def approve(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Approve a Wire Transfer

        Args:
          wire_transfer_id: The identifier of the Wire Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/wire_transfers/{wire_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    def cancel(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Cancel a pending Wire Transfer

        Args:
          wire_transfer_id: The identifier of the pending Wire Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/wire_transfers/{wire_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    def reverse(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Simulates the reversal of a [Wire Transfer](#wire-transfers) by the Federal
        Reserve due to error conditions. This will also create a
        [Transaction](#transaction) to account for the returned funds. This Wire
        Transfer must first have a `status` of `complete`.'

        Args:
          wire_transfer_id: The identifier of the Wire Transfer you wish to reverse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    def submit(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Simulates the submission of a [Wire Transfer](#wire-transfers) to the Federal
        Reserve. This transfer must first have a `status` of `pending_approval` or
        `pending_creating`.

        Args:
          wire_transfer_id: The identifier of the Wire Transfer you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )


class AsyncWireTransfers(AsyncAPIResource):
    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        beneficiary_name: str,
        message_to_recipient: str,
        account_number: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        unique_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Create a Wire Transfer

        Args:
          account_id: The identifier for the account that will send the transfer.

          amount: The transfer amount in cents.

          beneficiary_name: The beneficiary's name.

          message_to_recipient: The message that will show on the recipient's bank statement.

          account_number: The account number for the destination account.

          beneficiary_address_line1: The beneficiary's address line 1.

          beneficiary_address_line2: The beneficiary's address line 2.

          beneficiary_address_line3: The beneficiary's address line 3.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

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
            "/wire_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "beneficiary_name": beneficiary_name,
                    "message_to_recipient": message_to_recipient,
                    "account_number": account_number,
                    "beneficiary_address_line1": beneficiary_address_line1,
                    "beneficiary_address_line2": beneficiary_address_line2,
                    "beneficiary_address_line3": beneficiary_address_line3,
                    "external_account_id": external_account_id,
                    "require_approval": require_approval,
                    "routing_number": routing_number,
                    "unique_identifier": unique_identifier,
                },
                wire_transfer_create_params.WireTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    async def retrieve(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> WireTransfer:
        """
        Retrieve a Wire Transfer

        Args:
          wire_transfer_id: The identifier of the Wire Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/wire_transfers/{wire_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[WireTransfer, AsyncPage[WireTransfer]]:
        """
        List Wire Transfers

        Args:
          account_id: Filter Wire Transfers to those belonging to the specified Account.

          cursor: Return the page of entries after this one.

          external_account_id: Filter Wire Transfers to those made to the specified External Account.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          unique_identifier: Filter Wire Transfers to the one with the specified unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/wire_transfers",
            page=AsyncPage[WireTransfer],
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
                    wire_transfer_list_params.WireTransferListParams,
                ),
            ),
            model=WireTransfer,
        )

    async def approve(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Approve a Wire Transfer

        Args:
          wire_transfer_id: The identifier of the Wire Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/wire_transfers/{wire_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    async def cancel(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Cancel a pending Wire Transfer

        Args:
          wire_transfer_id: The identifier of the pending Wire Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/wire_transfers/{wire_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    async def reverse(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Simulates the reversal of a [Wire Transfer](#wire-transfers) by the Federal
        Reserve due to error conditions. This will also create a
        [Transaction](#transaction) to account for the returned funds. This Wire
        Transfer must first have a `status` of `complete`.'

        Args:
          wire_transfer_id: The identifier of the Wire Transfer you wish to reverse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    async def submit(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Simulates the submission of a [Wire Transfer](#wire-transfers) to the Federal
        Reserve. This transfer must first have a `status` of `pending_approval` or
        `pending_creating`.

        Args:
          wire_transfer_id: The identifier of the Wire Transfer you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )
