# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

from ..types import (
    ACHPrenotification,
    ach_prenotification_list_params,
    ach_prenotification_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["ACHPrenotifications", "AsyncACHPrenotifications"]


class ACHPrenotifications(SyncAPIResource):
    def create(
        self,
        *,
        account_number: str,
        routing_number: str,
        addendum: str | NotGiven = NOT_GIVEN,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        credit_debit_indicator: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        individual_id: str | NotGiven = NOT_GIVEN,
        individual_name: str | NotGiven = NOT_GIVEN,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHPrenotification:
        """
        Create an ACH Prenotification

        Args:
          account_number: The account number for the destination account.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          addendum: Additional information that will be sent to the recipient.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: The data you choose to associate with the transfer.

          company_entry_description: The description of the transfer you wish to be shown to the recipient.

          company_name: The name by which the recipient knows you.

          credit_debit_indicator: Whether the Prenotification is for a future debit or credit.

              - `credit` - The Prenotification is for an anticipated credit.
              - `debit` - The Prenotification is for an anticipated debit.

          effective_date: The transfer effective date in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

          individual_id: Your identifer for the transfer recipient.

          individual_name: The name of the transfer recipient. This value is information and not verified
              by the recipient's bank.

          standard_entry_class_code: The Standard Entry Class (SEC) code to use for the ACH Prenotification.

              - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
              - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
              - `internet_initiated` - Internet Initiated (WEB).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/ach_prenotifications",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "routing_number": routing_number,
                    "addendum": addendum,
                    "company_descriptive_date": company_descriptive_date,
                    "company_discretionary_data": company_discretionary_data,
                    "company_entry_description": company_entry_description,
                    "company_name": company_name,
                    "credit_debit_indicator": credit_debit_indicator,
                    "effective_date": effective_date,
                    "individual_id": individual_id,
                    "individual_name": individual_name,
                    "standard_entry_class_code": standard_entry_class_code,
                },
                ach_prenotification_create_params.ACHPrenotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHPrenotification,
        )

    def retrieve(
        self,
        ach_prenotification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ACHPrenotification:
        """
        Retrieve an ACH Prenotification

        Args:
          ach_prenotification_id: The identifier of the ACH Prenotification to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/ach_prenotifications/{ach_prenotification_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACHPrenotification,
        )

    def list(
        self,
        *,
        created_at: ach_prenotification_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ACHPrenotification]:
        """
        List ACH Prenotifications

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
            "/ach_prenotifications",
            page=SyncPage[ACHPrenotification],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    ach_prenotification_list_params.ACHPrenotificationListParams,
                ),
            ),
            model=ACHPrenotification,
        )


class AsyncACHPrenotifications(AsyncAPIResource):
    async def create(
        self,
        *,
        account_number: str,
        routing_number: str,
        addendum: str | NotGiven = NOT_GIVEN,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        credit_debit_indicator: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date] | NotGiven = NOT_GIVEN,
        individual_id: str | NotGiven = NOT_GIVEN,
        individual_name: str | NotGiven = NOT_GIVEN,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHPrenotification:
        """
        Create an ACH Prenotification

        Args:
          account_number: The account number for the destination account.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          addendum: Additional information that will be sent to the recipient.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: The data you choose to associate with the transfer.

          company_entry_description: The description of the transfer you wish to be shown to the recipient.

          company_name: The name by which the recipient knows you.

          credit_debit_indicator: Whether the Prenotification is for a future debit or credit.

              - `credit` - The Prenotification is for an anticipated credit.
              - `debit` - The Prenotification is for an anticipated debit.

          effective_date: The transfer effective date in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

          individual_id: Your identifer for the transfer recipient.

          individual_name: The name of the transfer recipient. This value is information and not verified
              by the recipient's bank.

          standard_entry_class_code: The Standard Entry Class (SEC) code to use for the ACH Prenotification.

              - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
              - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
              - `internet_initiated` - Internet Initiated (WEB).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/ach_prenotifications",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "routing_number": routing_number,
                    "addendum": addendum,
                    "company_descriptive_date": company_descriptive_date,
                    "company_discretionary_data": company_discretionary_data,
                    "company_entry_description": company_entry_description,
                    "company_name": company_name,
                    "credit_debit_indicator": credit_debit_indicator,
                    "effective_date": effective_date,
                    "individual_id": individual_id,
                    "individual_name": individual_name,
                    "standard_entry_class_code": standard_entry_class_code,
                },
                ach_prenotification_create_params.ACHPrenotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHPrenotification,
        )

    async def retrieve(
        self,
        ach_prenotification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ACHPrenotification:
        """
        Retrieve an ACH Prenotification

        Args:
          ach_prenotification_id: The identifier of the ACH Prenotification to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/ach_prenotifications/{ach_prenotification_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACHPrenotification,
        )

    def list(
        self,
        *,
        created_at: ach_prenotification_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ACHPrenotification, AsyncPage[ACHPrenotification]]:
        """
        List ACH Prenotifications

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
            "/ach_prenotifications",
            page=AsyncPage[ACHPrenotification],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    ach_prenotification_list_params.ACHPrenotificationListParams,
                ),
            ),
            model=ACHPrenotification,
        )
