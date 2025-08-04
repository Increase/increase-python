# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import ach_transfer_list_params, ach_transfer_create_params
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
from ..types.ach_transfer import ACHTransfer

__all__ = ["ACHTransfersResource", "AsyncACHTransfersResource"]


class ACHTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ACHTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return ACHTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ACHTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return ACHTransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        statement_descriptor: str,
        account_number: str | NotGiven = NOT_GIVEN,
        addenda: ach_transfer_create_params.Addenda | NotGiven = NOT_GIVEN,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        destination_account_holder: Literal["business", "individual", "unknown"] | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        funding: Literal["checking", "savings", "general_ledger"] | NotGiven = NOT_GIVEN,
        individual_id: str | NotGiven = NOT_GIVEN,
        individual_name: str | NotGiven = NOT_GIVEN,
        preferred_effective_date: ach_transfer_create_params.PreferredEffectiveDate | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit",
            "corporate_trade_exchange",
            "prearranged_payments_and_deposit",
            "internet_initiated",
        ]
        | NotGiven = NOT_GIVEN,
        transaction_timing: Literal["synchronous", "asynchronous"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransfer:
        """
        Create an ACH Transfer

        Args:
          account_id: The Increase identifier for the account that will send the transfer.

          amount: The transfer amount in USD cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          statement_descriptor: A description you choose to give the transfer. This will be saved with the
              transfer details, displayed in the dashboard, and returned by the API. If
              `individual_name` and `company_name` are not explicitly set by this API, the
              `statement_descriptor` will be sent in those fields to the receiving bank to
              help the customer recognize the transfer. You are highly encouraged to pass
              `individual_name` and `company_name` instead of relying on this fallback.

          account_number: The account number for the destination account.

          addenda: Additional information that will be sent to the recipient. This is included in
              the transfer data sent to the receiving bank.

          company_descriptive_date: The description of the date of the transfer, usually in the format `YYMMDD`.
              This is included in the transfer data sent to the receiving bank.

          company_discretionary_data: The data you choose to associate with the transfer. This is included in the
              transfer data sent to the receiving bank.

          company_entry_description: A description of the transfer. This is included in the transfer data sent to the
              receiving bank.

          company_name: The name by which the recipient knows you. This is included in the transfer data
              sent to the receiving bank.

          destination_account_holder: The type of entity that owns the account to which the ACH Transfer is being
              sent.

              - `business` - The External Account is owned by a business.
              - `individual` - The External Account is owned by an individual.
              - `unknown` - It's unknown what kind of entity owns the External Account.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number`, `routing_number`, and `funding` must be absent.

          funding: The type of the account to which the transfer will be sent.

              - `checking` - A checking account.
              - `savings` - A savings account.
              - `general_ledger` - A bank's general ledger. Uncommon.

          individual_id: Your identifier for the transfer recipient.

          individual_name: The name of the transfer recipient. This value is informational and not verified
              by the recipient's bank.

          preferred_effective_date: Configuration for how the effective date of the transfer will be set. This
              determines same-day vs future-dated settlement timing. If not set, defaults to a
              `settlement_schedule` of `same_day`. If set, exactly one of the child attributes
              must be set.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          standard_entry_class_code: The Standard Entry Class (SEC) code to use for the transfer.

              - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
              - `corporate_trade_exchange` - Corporate Trade Exchange (CTX).
              - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
              - `internet_initiated` - Internet Initiated (WEB).

          transaction_timing: The timing of the transaction.

              - `synchronous` - A Transaction will be created immediately.
              - `asynchronous` - A Transaction will be created when the funds settle at the
                Federal Reserve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/ach_transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "statement_descriptor": statement_descriptor,
                    "account_number": account_number,
                    "addenda": addenda,
                    "company_descriptive_date": company_descriptive_date,
                    "company_discretionary_data": company_discretionary_data,
                    "company_entry_description": company_entry_description,
                    "company_name": company_name,
                    "destination_account_holder": destination_account_holder,
                    "external_account_id": external_account_id,
                    "funding": funding,
                    "individual_id": individual_id,
                    "individual_name": individual_name,
                    "preferred_effective_date": preferred_effective_date,
                    "require_approval": require_approval,
                    "routing_number": routing_number,
                    "standard_entry_class_code": standard_entry_class_code,
                    "transaction_timing": transaction_timing,
                },
                ach_transfer_create_params.ACHTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransfer,
        )

    def retrieve(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACHTransfer:
        """
        Retrieve an ACH Transfer

        Args:
          ach_transfer_id: The identifier of the ACH Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ach_transfer_id:
            raise ValueError(f"Expected a non-empty value for `ach_transfer_id` but received {ach_transfer_id!r}")
        return self._get(
            f"/ach_transfers/{ach_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACHTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: ach_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: ach_transfer_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ACHTransfer]:
        """
        List ACH Transfers

        Args:
          account_id: Filter ACH Transfers to those that originated from the specified Account.

          cursor: Return the page of entries after this one.

          external_account_id: Filter ACH Transfers to those made to the specified External Account.

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
            "/ach_transfers",
            page=SyncPage[ACHTransfer],
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
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    ach_transfer_list_params.ACHTransferListParams,
                ),
            ),
            model=ACHTransfer,
        )

    def approve(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransfer:
        """
        Approves an ACH Transfer in a pending_approval state.

        Args:
          ach_transfer_id: The identifier of the ACH Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not ach_transfer_id:
            raise ValueError(f"Expected a non-empty value for `ach_transfer_id` but received {ach_transfer_id!r}")
        return self._post(
            f"/ach_transfers/{ach_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransfer,
        )

    def cancel(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransfer:
        """
        Cancels an ACH Transfer in a pending_approval state.

        Args:
          ach_transfer_id: The identifier of the pending ACH Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not ach_transfer_id:
            raise ValueError(f"Expected a non-empty value for `ach_transfer_id` but received {ach_transfer_id!r}")
        return self._post(
            f"/ach_transfers/{ach_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransfer,
        )


class AsyncACHTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncACHTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncACHTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncACHTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncACHTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        statement_descriptor: str,
        account_number: str | NotGiven = NOT_GIVEN,
        addenda: ach_transfer_create_params.Addenda | NotGiven = NOT_GIVEN,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        destination_account_holder: Literal["business", "individual", "unknown"] | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        funding: Literal["checking", "savings", "general_ledger"] | NotGiven = NOT_GIVEN,
        individual_id: str | NotGiven = NOT_GIVEN,
        individual_name: str | NotGiven = NOT_GIVEN,
        preferred_effective_date: ach_transfer_create_params.PreferredEffectiveDate | NotGiven = NOT_GIVEN,
        require_approval: bool | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit",
            "corporate_trade_exchange",
            "prearranged_payments_and_deposit",
            "internet_initiated",
        ]
        | NotGiven = NOT_GIVEN,
        transaction_timing: Literal["synchronous", "asynchronous"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransfer:
        """
        Create an ACH Transfer

        Args:
          account_id: The Increase identifier for the account that will send the transfer.

          amount: The transfer amount in USD cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          statement_descriptor: A description you choose to give the transfer. This will be saved with the
              transfer details, displayed in the dashboard, and returned by the API. If
              `individual_name` and `company_name` are not explicitly set by this API, the
              `statement_descriptor` will be sent in those fields to the receiving bank to
              help the customer recognize the transfer. You are highly encouraged to pass
              `individual_name` and `company_name` instead of relying on this fallback.

          account_number: The account number for the destination account.

          addenda: Additional information that will be sent to the recipient. This is included in
              the transfer data sent to the receiving bank.

          company_descriptive_date: The description of the date of the transfer, usually in the format `YYMMDD`.
              This is included in the transfer data sent to the receiving bank.

          company_discretionary_data: The data you choose to associate with the transfer. This is included in the
              transfer data sent to the receiving bank.

          company_entry_description: A description of the transfer. This is included in the transfer data sent to the
              receiving bank.

          company_name: The name by which the recipient knows you. This is included in the transfer data
              sent to the receiving bank.

          destination_account_holder: The type of entity that owns the account to which the ACH Transfer is being
              sent.

              - `business` - The External Account is owned by a business.
              - `individual` - The External Account is owned by an individual.
              - `unknown` - It's unknown what kind of entity owns the External Account.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number`, `routing_number`, and `funding` must be absent.

          funding: The type of the account to which the transfer will be sent.

              - `checking` - A checking account.
              - `savings` - A savings account.
              - `general_ledger` - A bank's general ledger. Uncommon.

          individual_id: Your identifier for the transfer recipient.

          individual_name: The name of the transfer recipient. This value is informational and not verified
              by the recipient's bank.

          preferred_effective_date: Configuration for how the effective date of the transfer will be set. This
              determines same-day vs future-dated settlement timing. If not set, defaults to a
              `settlement_schedule` of `same_day`. If set, exactly one of the child attributes
              must be set.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          standard_entry_class_code: The Standard Entry Class (SEC) code to use for the transfer.

              - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
              - `corporate_trade_exchange` - Corporate Trade Exchange (CTX).
              - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
              - `internet_initiated` - Internet Initiated (WEB).

          transaction_timing: The timing of the transaction.

              - `synchronous` - A Transaction will be created immediately.
              - `asynchronous` - A Transaction will be created when the funds settle at the
                Federal Reserve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/ach_transfers",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "statement_descriptor": statement_descriptor,
                    "account_number": account_number,
                    "addenda": addenda,
                    "company_descriptive_date": company_descriptive_date,
                    "company_discretionary_data": company_discretionary_data,
                    "company_entry_description": company_entry_description,
                    "company_name": company_name,
                    "destination_account_holder": destination_account_holder,
                    "external_account_id": external_account_id,
                    "funding": funding,
                    "individual_id": individual_id,
                    "individual_name": individual_name,
                    "preferred_effective_date": preferred_effective_date,
                    "require_approval": require_approval,
                    "routing_number": routing_number,
                    "standard_entry_class_code": standard_entry_class_code,
                    "transaction_timing": transaction_timing,
                },
                ach_transfer_create_params.ACHTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransfer,
        )

    async def retrieve(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACHTransfer:
        """
        Retrieve an ACH Transfer

        Args:
          ach_transfer_id: The identifier of the ACH Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ach_transfer_id:
            raise ValueError(f"Expected a non-empty value for `ach_transfer_id` but received {ach_transfer_id!r}")
        return await self._get(
            f"/ach_transfers/{ach_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACHTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: ach_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: ach_transfer_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ACHTransfer, AsyncPage[ACHTransfer]]:
        """
        List ACH Transfers

        Args:
          account_id: Filter ACH Transfers to those that originated from the specified Account.

          cursor: Return the page of entries after this one.

          external_account_id: Filter ACH Transfers to those made to the specified External Account.

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
            "/ach_transfers",
            page=AsyncPage[ACHTransfer],
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
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    ach_transfer_list_params.ACHTransferListParams,
                ),
            ),
            model=ACHTransfer,
        )

    async def approve(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransfer:
        """
        Approves an ACH Transfer in a pending_approval state.

        Args:
          ach_transfer_id: The identifier of the ACH Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not ach_transfer_id:
            raise ValueError(f"Expected a non-empty value for `ach_transfer_id` but received {ach_transfer_id!r}")
        return await self._post(
            f"/ach_transfers/{ach_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransfer,
        )

    async def cancel(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransfer:
        """
        Cancels an ACH Transfer in a pending_approval state.

        Args:
          ach_transfer_id: The identifier of the pending ACH Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not ach_transfer_id:
            raise ValueError(f"Expected a non-empty value for `ach_transfer_id` but received {ach_transfer_id!r}")
        return await self._post(
            f"/ach_transfers/{ach_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransfer,
        )


class ACHTransfersResourceWithRawResponse:
    def __init__(self, ach_transfers: ACHTransfersResource) -> None:
        self._ach_transfers = ach_transfers

        self.create = to_raw_response_wrapper(
            ach_transfers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ach_transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            ach_transfers.list,
        )
        self.approve = to_raw_response_wrapper(
            ach_transfers.approve,
        )
        self.cancel = to_raw_response_wrapper(
            ach_transfers.cancel,
        )


class AsyncACHTransfersResourceWithRawResponse:
    def __init__(self, ach_transfers: AsyncACHTransfersResource) -> None:
        self._ach_transfers = ach_transfers

        self.create = async_to_raw_response_wrapper(
            ach_transfers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ach_transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            ach_transfers.list,
        )
        self.approve = async_to_raw_response_wrapper(
            ach_transfers.approve,
        )
        self.cancel = async_to_raw_response_wrapper(
            ach_transfers.cancel,
        )


class ACHTransfersResourceWithStreamingResponse:
    def __init__(self, ach_transfers: ACHTransfersResource) -> None:
        self._ach_transfers = ach_transfers

        self.create = to_streamed_response_wrapper(
            ach_transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ach_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            ach_transfers.list,
        )
        self.approve = to_streamed_response_wrapper(
            ach_transfers.approve,
        )
        self.cancel = to_streamed_response_wrapper(
            ach_transfers.cancel,
        )


class AsyncACHTransfersResourceWithStreamingResponse:
    def __init__(self, ach_transfers: AsyncACHTransfersResource) -> None:
        self._ach_transfers = ach_transfers

        self.create = async_to_streamed_response_wrapper(
            ach_transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ach_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            ach_transfers.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            ach_transfers.approve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            ach_transfers.cancel,
        )
