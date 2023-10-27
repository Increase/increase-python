# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING
from typing_extensions import Literal

from ..types import (
    AccountNumber,
    account_number_list_params,
    account_number_create_params,
    account_number_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import Increase, AsyncIncrease

__all__ = ["AccountNumbers", "AsyncAccountNumbers"]


class AccountNumbers(SyncAPIResource):
    with_raw_response: AccountNumbersWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = AccountNumbersWithRawResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        inbound_ach: account_number_create_params.InboundACH | NotGiven = NOT_GIVEN,
        inbound_checks: account_number_create_params.InboundChecks | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountNumber:
        """
        Create an Account Number

        Args:
          account_id: The Account the Account Number should belong to.

          name: The name you choose for the Account Number.

          inbound_ach: Options related to how this Account Number should handle inbound ACH transfers.

          inbound_checks: Options related to how this Account Number should handle inbound check
              withdrawls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/account_numbers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "inbound_ach": inbound_ach,
                    "inbound_checks": inbound_checks,
                },
                account_number_create_params.AccountNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountNumber,
        )

    def retrieve(
        self,
        account_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AccountNumber:
        """
        Retrieve an Account Number

        Args:
          account_number_id: The identifier of the Account Number to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/account_numbers/{account_number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountNumber,
        )

    def update(
        self,
        account_number_id: str,
        *,
        inbound_ach: account_number_update_params.InboundACH | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountNumber:
        """
        Update an Account Number

        Args:
          account_number_id: The identifier of the Account Number.

          inbound_ach: Options related to how this Account Number handles inbound ACH transfers.

          name: The name you choose for the Account Number.

          status: This indicates if transfers can be made to the Account Number.

              - `active` - The account number is active.
              - `disabled` - The account number is temporarily disabled.
              - `canceled` - The account number is permanently disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/account_numbers/{account_number_id}",
            body=maybe_transform(
                {
                    "inbound_ach": inbound_ach,
                    "name": name,
                    "status": status,
                },
                account_number_update_params.AccountNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountNumber,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: account_number_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[AccountNumber]:
        """
        List Account Numbers

        Args:
          account_id: Filter Account Numbers to those belonging to the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          status: The status to retrieve Account Numbers for.

              - `active` - The account number is active.
              - `disabled` - The account number is temporarily disabled.
              - `canceled` - The account number is permanently disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/account_numbers",
            page=SyncPage[AccountNumber],
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
                    account_number_list_params.AccountNumberListParams,
                ),
            ),
            model=AccountNumber,
        )


class AsyncAccountNumbers(AsyncAPIResource):
    with_raw_response: AsyncAccountNumbersWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncAccountNumbersWithRawResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        inbound_ach: account_number_create_params.InboundACH | NotGiven = NOT_GIVEN,
        inbound_checks: account_number_create_params.InboundChecks | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountNumber:
        """
        Create an Account Number

        Args:
          account_id: The Account the Account Number should belong to.

          name: The name you choose for the Account Number.

          inbound_ach: Options related to how this Account Number should handle inbound ACH transfers.

          inbound_checks: Options related to how this Account Number should handle inbound check
              withdrawls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/account_numbers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "inbound_ach": inbound_ach,
                    "inbound_checks": inbound_checks,
                },
                account_number_create_params.AccountNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountNumber,
        )

    async def retrieve(
        self,
        account_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AccountNumber:
        """
        Retrieve an Account Number

        Args:
          account_number_id: The identifier of the Account Number to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/account_numbers/{account_number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountNumber,
        )

    async def update(
        self,
        account_number_id: str,
        *,
        inbound_ach: account_number_update_params.InboundACH | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountNumber:
        """
        Update an Account Number

        Args:
          account_number_id: The identifier of the Account Number.

          inbound_ach: Options related to how this Account Number handles inbound ACH transfers.

          name: The name you choose for the Account Number.

          status: This indicates if transfers can be made to the Account Number.

              - `active` - The account number is active.
              - `disabled` - The account number is temporarily disabled.
              - `canceled` - The account number is permanently disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/account_numbers/{account_number_id}",
            body=maybe_transform(
                {
                    "inbound_ach": inbound_ach,
                    "name": name,
                    "status": status,
                },
                account_number_update_params.AccountNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountNumber,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: account_number_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "disabled", "canceled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AccountNumber, AsyncPage[AccountNumber]]:
        """
        List Account Numbers

        Args:
          account_id: Filter Account Numbers to those belonging to the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          status: The status to retrieve Account Numbers for.

              - `active` - The account number is active.
              - `disabled` - The account number is temporarily disabled.
              - `canceled` - The account number is permanently disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/account_numbers",
            page=AsyncPage[AccountNumber],
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
                    account_number_list_params.AccountNumberListParams,
                ),
            ),
            model=AccountNumber,
        )


class AccountNumbersWithRawResponse:
    def __init__(self, account_numbers: AccountNumbers) -> None:
        self.create = to_raw_response_wrapper(
            account_numbers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            account_numbers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            account_numbers.update,
        )
        self.list = to_raw_response_wrapper(
            account_numbers.list,
        )


class AsyncAccountNumbersWithRawResponse:
    def __init__(self, account_numbers: AsyncAccountNumbers) -> None:
        self.create = async_to_raw_response_wrapper(
            account_numbers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            account_numbers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            account_numbers.update,
        )
        self.list = async_to_raw_response_wrapper(
            account_numbers.list,
        )
