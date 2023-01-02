# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..types import ach_transfer_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ach_transfer import ACHTransfer

__all__ = ["ACHTransfers", "AsyncACHTransfers"]


class ACHTransfers(SyncAPIResource):
    def create(
        self,
        *,
        account_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        addendum: str | NotGiven = NOT_GIVEN,
        amount: int,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        funding: Literal["checking", "savings"] | NotGiven = NOT_GIVEN,
        individual_id: str | NotGiven = NOT_GIVEN,
        individual_name: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
        ]
        | NotGiven = NOT_GIVEN,
        statement_descriptor: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ACHTransfer:
        """
        Args:
          account_id: The identifier for the account that will send the transfer.

          account_number: The account number for the destination account.

          addendum: Additional information that will be sent to the recipient.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: The data you choose to associate with the transfer.

          company_entry_description: The description of the transfer you wish to be shown to the recipient.

          company_name: The name by which the recipient knows you.

          effective_date: The transfer effective date in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number`, `routing_number`, and `funding` must be absent.

          funding: The type of the account to which the transfer will be sent.

          individual_id: Your identifer for the transfer recipient.

          individual_name: The name of the transfer recipient. This value is information and not verified
              by the recipient's bank.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          standard_entry_class_code: The Standard Entry Class (SEC) code to use for the transfer.

          statement_descriptor: The description you choose to give the transfer. This will be shown to the
              recipient.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/ach_transfers",
            body={
                "account_id": account_id,
                "account_number": account_number,
                "addendum": addendum,
                "amount": amount,
                "company_descriptive_date": company_descriptive_date,
                "company_discretionary_data": company_discretionary_data,
                "company_entry_description": company_entry_description,
                "company_name": company_name,
                "effective_date": effective_date,
                "external_account_id": external_account_id,
                "funding": funding,
                "individual_id": individual_id,
                "individual_name": individual_name,
                "routing_number": routing_number,
                "standard_entry_class_code": standard_entry_class_code,
                "statement_descriptor": statement_descriptor,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> ACHTransfer:
        return self._get(
            f"/ach_transfers/{ach_transfer_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ACHTransfer,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        created_at: ach_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[ACHTransfer]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter ACH Transfers to those that originated from the specified Account.

          external_account_id: Filter ACH Transfers to those made to the specified External Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/ach_transfers",
            page=SyncPage[ACHTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "external_account_id": external_account_id,
                    "created_at": created_at,
                },
            ),
            model=ACHTransfer,
        )


class AsyncACHTransfers(AsyncAPIResource):
    async def create(
        self,
        *,
        account_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        addendum: str | NotGiven = NOT_GIVEN,
        amount: int,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        funding: Literal["checking", "savings"] | NotGiven = NOT_GIVEN,
        individual_id: str | NotGiven = NOT_GIVEN,
        individual_name: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
        ]
        | NotGiven = NOT_GIVEN,
        statement_descriptor: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ACHTransfer:
        """
        Args:
          account_id: The identifier for the account that will send the transfer.

          account_number: The account number for the destination account.

          addendum: Additional information that will be sent to the recipient.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: The data you choose to associate with the transfer.

          company_entry_description: The description of the transfer you wish to be shown to the recipient.

          company_name: The name by which the recipient knows you.

          effective_date: The transfer effective date in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number`, `routing_number`, and `funding` must be absent.

          funding: The type of the account to which the transfer will be sent.

          individual_id: Your identifer for the transfer recipient.

          individual_name: The name of the transfer recipient. This value is information and not verified
              by the recipient's bank.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          standard_entry_class_code: The Standard Entry Class (SEC) code to use for the transfer.

          statement_descriptor: The description you choose to give the transfer. This will be shown to the
              recipient.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/ach_transfers",
            body={
                "account_id": account_id,
                "account_number": account_number,
                "addendum": addendum,
                "amount": amount,
                "company_descriptive_date": company_descriptive_date,
                "company_discretionary_data": company_discretionary_data,
                "company_entry_description": company_entry_description,
                "company_name": company_name,
                "effective_date": effective_date,
                "external_account_id": external_account_id,
                "funding": funding,
                "individual_id": individual_id,
                "individual_name": individual_name,
                "routing_number": routing_number,
                "standard_entry_class_code": standard_entry_class_code,
                "statement_descriptor": statement_descriptor,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> ACHTransfer:
        return await self._get(
            f"/ach_transfers/{ach_transfer_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=ACHTransfer,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        created_at: ach_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[ACHTransfer, AsyncPage[ACHTransfer]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter ACH Transfers to those that originated from the specified Account.

          external_account_id: Filter ACH Transfers to those made to the specified External Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/ach_transfers",
            page=AsyncPage[ACHTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "external_account_id": external_account_id,
                    "created_at": created_at,
                },
            ),
            model=ACHTransfer,
        )
