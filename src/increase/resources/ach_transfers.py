# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import ach_transfer_list_params, ach_transfer_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
        account_number: str | Omit = omit,
        addenda: ach_transfer_create_params.Addenda | Omit = omit,
        company_descriptive_date: str | Omit = omit,
        company_discretionary_data: str | Omit = omit,
        company_entry_description: str | Omit = omit,
        company_name: str | Omit = omit,
        destination_account_holder: Literal["business", "individual", "unknown"] | Omit = omit,
        external_account_id: str | Omit = omit,
        funding: Literal["checking", "savings", "loan", "general_ledger"] | Omit = omit,
        individual_id: str | Omit = omit,
        individual_name: str | Omit = omit,
        preferred_effective_date: ach_transfer_create_params.PreferredEffectiveDate | Omit = omit,
        require_approval: bool | Omit = omit,
        routing_number: str | Omit = omit,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit",
            "corporate_trade_exchange",
            "prearranged_payments_and_deposit",
            "internet_initiated",
        ]
        | Omit = omit,
        transaction_timing: Literal["synchronous", "asynchronous"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          account_number: The receiver's account number. For credit transfers (positive `amount`) this is
              the account that funds will be sent to. For debit transfers (negative `amount`)
              this is the account that funds will be pulled from.

          addenda: Additional information passed through to the receiving bank with the transfer.
              Most ACH transfers do not need this. Only set this if your recipient has asked
              for addendum data, typically unstructured remittance information. Corporate
              Trade Exchange (CTX) flows can carry structured X12 remittance advice instead.

          company_descriptive_date: A description of the transfer date (typically `YYMMDD`), sent in the company
              batch header. This value is informational and does not affect funds movement,
              settlement timing, or returns. Only set this if your recipient has asked for it.

          company_discretionary_data: Custom data sent in the company batch header. This value is informational and
              does not affect funds movement, settlement timing, or returns. Most ACH
              transfers do not need this. Only set this if your recipient has asked for it.

          company_entry_description: A short description sent in the company batch header. Most receivers do not
              surface this. Only set this if your recipient has asked for a specific value or
              if Nacha mandates one for your Standard Entry Class (SEC) code and use case. For
              example, Prearranged Payment and Deposit (PPD) payroll credits must use
              `PAYROLL`, and reversals must use `REVERSAL`.

          company_name: The name by which the recipient knows you, sent in the company batch header. We
              recommend setting this on every transfer; if you do not, we fall back to the ACH
              company name configured on your account.

          destination_account_holder: The type of entity that owns the receiver's account.

              - `business` - The External Account is owned by a business.
              - `individual` - The External Account is owned by an individual.
              - `unknown` - It's unknown what kind of entity owns the External Account.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number`, `routing_number`, and `funding` must be absent.

          funding: The type of the receiver's bank account.

              - `checking` - A checking account.
              - `savings` - A savings account.
              - `loan` - A loan account used in a lender-borrower relationship. Uncommon.
              - `general_ledger` - A bank's general ledger. Uncommon.

          individual_id: Your internal identifier for the transfer recipient. This value is informational
              and not verified by the recipient's bank. Most callers can leave this unset.

          individual_name: The name of the transfer recipient. This value is informational and not verified
              by the recipient's bank.

          preferred_effective_date: Configuration for how the effective date of the transfer will be set. This
              determines same-day vs future-dated settlement timing. If not set, defaults to a
              `settlement_schedule` of `same_day`. If set, exactly one of the child attributes
              must be set.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) of the
              receiver's bank.

          standard_entry_class_code: The
              [Standard Entry Class (SEC) code](/documentation/ach-standard-entry-class-codes)
              to use for the transfer. If not provided, the default is
              `corporate_credit_or_debit`.

              - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD) is used for
                business-to-business payments.
              - `corporate_trade_exchange` - Corporate Trade Exchange (CTX) allows for
                including extensive remittance information with business-to-business payments.
              - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD)
                is used for credits or debits originated by an organization to a consumer,
                such as payroll direct deposits.
              - `internet_initiated` - Internet Initiated (WEB) is used for consumer payments
                initiated or authorized via the Internet. Debits can only be initiated by
                non-consumers to debit a consumer’s account. Credits can only be used for
                consumer to consumer transactions.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/ach_transfers/{ach_transfer_id}", ach_transfer_id=ach_transfer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACHTransfer,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: ach_transfer_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        external_account_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: ach_transfer_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/ach_transfers/{ach_transfer_id}/approve", ach_transfer_id=ach_transfer_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/ach_transfers/{ach_transfer_id}/cancel", ach_transfer_id=ach_transfer_id),
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
        account_number: str | Omit = omit,
        addenda: ach_transfer_create_params.Addenda | Omit = omit,
        company_descriptive_date: str | Omit = omit,
        company_discretionary_data: str | Omit = omit,
        company_entry_description: str | Omit = omit,
        company_name: str | Omit = omit,
        destination_account_holder: Literal["business", "individual", "unknown"] | Omit = omit,
        external_account_id: str | Omit = omit,
        funding: Literal["checking", "savings", "loan", "general_ledger"] | Omit = omit,
        individual_id: str | Omit = omit,
        individual_name: str | Omit = omit,
        preferred_effective_date: ach_transfer_create_params.PreferredEffectiveDate | Omit = omit,
        require_approval: bool | Omit = omit,
        routing_number: str | Omit = omit,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit",
            "corporate_trade_exchange",
            "prearranged_payments_and_deposit",
            "internet_initiated",
        ]
        | Omit = omit,
        transaction_timing: Literal["synchronous", "asynchronous"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          account_number: The receiver's account number. For credit transfers (positive `amount`) this is
              the account that funds will be sent to. For debit transfers (negative `amount`)
              this is the account that funds will be pulled from.

          addenda: Additional information passed through to the receiving bank with the transfer.
              Most ACH transfers do not need this. Only set this if your recipient has asked
              for addendum data, typically unstructured remittance information. Corporate
              Trade Exchange (CTX) flows can carry structured X12 remittance advice instead.

          company_descriptive_date: A description of the transfer date (typically `YYMMDD`), sent in the company
              batch header. This value is informational and does not affect funds movement,
              settlement timing, or returns. Only set this if your recipient has asked for it.

          company_discretionary_data: Custom data sent in the company batch header. This value is informational and
              does not affect funds movement, settlement timing, or returns. Most ACH
              transfers do not need this. Only set this if your recipient has asked for it.

          company_entry_description: A short description sent in the company batch header. Most receivers do not
              surface this. Only set this if your recipient has asked for a specific value or
              if Nacha mandates one for your Standard Entry Class (SEC) code and use case. For
              example, Prearranged Payment and Deposit (PPD) payroll credits must use
              `PAYROLL`, and reversals must use `REVERSAL`.

          company_name: The name by which the recipient knows you, sent in the company batch header. We
              recommend setting this on every transfer; if you do not, we fall back to the ACH
              company name configured on your account.

          destination_account_holder: The type of entity that owns the receiver's account.

              - `business` - The External Account is owned by a business.
              - `individual` - The External Account is owned by an individual.
              - `unknown` - It's unknown what kind of entity owns the External Account.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number`, `routing_number`, and `funding` must be absent.

          funding: The type of the receiver's bank account.

              - `checking` - A checking account.
              - `savings` - A savings account.
              - `loan` - A loan account used in a lender-borrower relationship. Uncommon.
              - `general_ledger` - A bank's general ledger. Uncommon.

          individual_id: Your internal identifier for the transfer recipient. This value is informational
              and not verified by the recipient's bank. Most callers can leave this unset.

          individual_name: The name of the transfer recipient. This value is informational and not verified
              by the recipient's bank.

          preferred_effective_date: Configuration for how the effective date of the transfer will be set. This
              determines same-day vs future-dated settlement timing. If not set, defaults to a
              `settlement_schedule` of `same_day`. If set, exactly one of the child attributes
              must be set.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) of the
              receiver's bank.

          standard_entry_class_code: The
              [Standard Entry Class (SEC) code](/documentation/ach-standard-entry-class-codes)
              to use for the transfer. If not provided, the default is
              `corporate_credit_or_debit`.

              - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD) is used for
                business-to-business payments.
              - `corporate_trade_exchange` - Corporate Trade Exchange (CTX) allows for
                including extensive remittance information with business-to-business payments.
              - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD)
                is used for credits or debits originated by an organization to a consumer,
                such as payroll direct deposits.
              - `internet_initiated` - Internet Initiated (WEB) is used for consumer payments
                initiated or authorized via the Internet. Debits can only be initiated by
                non-consumers to debit a consumer’s account. Credits can only be used for
                consumer to consumer transactions.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/ach_transfers/{ach_transfer_id}", ach_transfer_id=ach_transfer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACHTransfer,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: ach_transfer_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        external_account_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: ach_transfer_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/ach_transfers/{ach_transfer_id}/approve", ach_transfer_id=ach_transfer_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/ach_transfers/{ach_transfer_id}/cancel", ach_transfer_id=ach_transfer_id),
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
