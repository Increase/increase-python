# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload
from typing_extensions import Literal

from ..types import ach_prenotification_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._utils import required_args
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.ach_prenotification import ACHPrenotification
from ..types.ach_prenotification_list_params import ACHPrenotificationListParams
from ..types.ach_prenotification_create_params import ACHPrenotificationCreateParams

__all__ = ["ACHPrenotifications", "AsyncACHPrenotifications"]


class ACHPrenotifications(SyncAPIResource):
    @overload
    def create(
        self,
        *,
        account_number: str,
        addendum: str | NotGiven = NOT_GIVEN,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        credit_debit_indicator: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        individual_id: str | NotGiven = NOT_GIVEN,
        individual_name: str | NotGiven = NOT_GIVEN,
        routing_number: str,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHPrenotification:
        """
        Args:
          account_number: The account number for the destination account.

          addendum: Additional information that will be sent to the recipient.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: The data you choose to associate with the transfer.

          company_entry_description: The description of the transfer you wish to be shown to the recipient.

          company_name: The name by which the recipient knows you.

          credit_debit_indicator: Whether the Prenotification is for a future debit or credit.

          effective_date: The transfer effective date in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

          individual_id: Your identifer for the transfer recipient.

          individual_name: The name of the transfer recipient. This value is information and not verified
              by the recipient's bank.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          standard_entry_class_code: The Standard Entry Class (SEC) code to use for the ACH Prenotification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        body: ACHPrenotificationCreateParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHPrenotification:
        ...

    @required_args(["body"], ["account_number", "routing_number"])
    def create(
        self,
        body: ACHPrenotificationCreateParams | None = None,
        *,
        account_number: str | NotGiven = NOT_GIVEN,
        addendum: str | NotGiven = NOT_GIVEN,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        credit_debit_indicator: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        individual_id: str | NotGiven = NOT_GIVEN,
        individual_name: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHPrenotification:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_number: The account number for the destination account.

          addendum: Additional information that will be sent to the recipient.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: The data you choose to associate with the transfer.

          company_entry_description: The description of the transfer you wish to be shown to the recipient.

          company_name: The name by which the recipient knows you.

          credit_debit_indicator: Whether the Prenotification is for a future debit or credit.

          effective_date: The transfer effective date in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

          individual_id: Your identifer for the transfer recipient.

          individual_name: The name of the transfer recipient. This value is information and not verified
              by the recipient's bank.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          standard_entry_class_code: The Standard Entry Class (SEC) code to use for the ACH Prenotification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard ACHPrenotificationCreateParams type.
            body = cast(
                Any,
                {
                    "account_number": account_number,
                    "addendum": addendum,
                    "company_descriptive_date": company_descriptive_date,
                    "company_discretionary_data": company_discretionary_data,
                    "company_entry_description": company_entry_description,
                    "company_name": company_name,
                    "credit_debit_indicator": credit_debit_indicator,
                    "effective_date": effective_date,
                    "individual_id": individual_id,
                    "individual_name": individual_name,
                    "routing_number": routing_number,
                    "standard_entry_class_code": standard_entry_class_code,
                },
            )

        return self._post(
            "/ach_prenotifications",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHPrenotification:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/ach_prenotifications/{ach_prenotification_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=ACHPrenotification,
        )

    @overload
    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        created_at: ach_prenotification_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ACHPrenotification]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: ACHPrenotificationListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ACHPrenotification]:
        ...

    def list(
        self,
        query: ACHPrenotificationListParams | None = None,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        created_at: ach_prenotification_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[ACHPrenotification]:
        """
        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard ACHPrenotificationListParams type.
            query = cast(
                Any,
                {
                    "cursor": cursor,
                    "limit": limit,
                    "created_at": created_at,
                },
            )

        return self._get_api_list(
            "/ach_prenotifications",
            page=SyncPage[ACHPrenotification],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=ACHPrenotification,
        )


class AsyncACHPrenotifications(AsyncAPIResource):
    @overload
    async def create(
        self,
        *,
        account_number: str,
        addendum: str | NotGiven = NOT_GIVEN,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        credit_debit_indicator: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        individual_id: str | NotGiven = NOT_GIVEN,
        individual_name: str | NotGiven = NOT_GIVEN,
        routing_number: str,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHPrenotification:
        """
        Args:
          account_number: The account number for the destination account.

          addendum: Additional information that will be sent to the recipient.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: The data you choose to associate with the transfer.

          company_entry_description: The description of the transfer you wish to be shown to the recipient.

          company_name: The name by which the recipient knows you.

          credit_debit_indicator: Whether the Prenotification is for a future debit or credit.

          effective_date: The transfer effective date in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

          individual_id: Your identifer for the transfer recipient.

          individual_name: The name of the transfer recipient. This value is information and not verified
              by the recipient's bank.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          standard_entry_class_code: The Standard Entry Class (SEC) code to use for the ACH Prenotification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        body: ACHPrenotificationCreateParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHPrenotification:
        ...

    @required_args(["body"], ["account_number", "routing_number"])
    async def create(
        self,
        body: ACHPrenotificationCreateParams | None = None,
        *,
        account_number: str | NotGiven = NOT_GIVEN,
        addendum: str | NotGiven = NOT_GIVEN,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        credit_debit_indicator: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        individual_id: str | NotGiven = NOT_GIVEN,
        individual_name: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHPrenotification:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_number: The account number for the destination account.

          addendum: Additional information that will be sent to the recipient.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: The data you choose to associate with the transfer.

          company_entry_description: The description of the transfer you wish to be shown to the recipient.

          company_name: The name by which the recipient knows you.

          credit_debit_indicator: Whether the Prenotification is for a future debit or credit.

          effective_date: The transfer effective date in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

          individual_id: Your identifer for the transfer recipient.

          individual_name: The name of the transfer recipient. This value is information and not verified
              by the recipient's bank.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          standard_entry_class_code: The Standard Entry Class (SEC) code to use for the ACH Prenotification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard ACHPrenotificationCreateParams type.
            body = cast(
                Any,
                {
                    "account_number": account_number,
                    "addendum": addendum,
                    "company_descriptive_date": company_descriptive_date,
                    "company_discretionary_data": company_discretionary_data,
                    "company_entry_description": company_entry_description,
                    "company_name": company_name,
                    "credit_debit_indicator": credit_debit_indicator,
                    "effective_date": effective_date,
                    "individual_id": individual_id,
                    "individual_name": individual_name,
                    "routing_number": routing_number,
                    "standard_entry_class_code": standard_entry_class_code,
                },
            )

        return await self._post(
            "/ach_prenotifications",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> ACHPrenotification:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/ach_prenotifications/{ach_prenotification_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=ACHPrenotification,
        )

    @overload
    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        created_at: ach_prenotification_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ACHPrenotification, AsyncPage[ACHPrenotification]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: ACHPrenotificationListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ACHPrenotification, AsyncPage[ACHPrenotification]]:
        ...

    def list(
        self,
        query: ACHPrenotificationListParams | None = None,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        created_at: ach_prenotification_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[ACHPrenotification, AsyncPage[ACHPrenotification]]:
        """
        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard ACHPrenotificationListParams type.
            query = cast(
                Any,
                {
                    "cursor": cursor,
                    "limit": limit,
                    "created_at": created_at,
                },
            )

        return self._get_api_list(
            "/ach_prenotifications",
            page=AsyncPage[ACHPrenotification],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=ACHPrenotification,
        )
