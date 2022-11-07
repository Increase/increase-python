# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload

from ..types import check_transfer_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._utils import required_args
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.check_transfer import CheckTransfer
from ..types.check_transfer_list_params import CheckTransferListParams
from ..types.check_transfer_create_params import CheckTransferCreateParams

__all__ = ["CheckTransfers", "AsyncCheckTransfers"]


class CheckTransfers(SyncAPIResource):
    @overload
    def create(
        self,
        *,
        account_id: str,
        address_line1: str,
        address_line2: str | NotGiven = NOT_GIVEN,
        address_city: str,
        address_state: str,
        address_zip: str,
        amount: int,
        message: str,
        recipient_name: str,
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
    ) -> CheckTransfer:
        """
        Args:
          account_id: The identifier for the account that will send the transfer.

          address_line1: The street address of the check's destination.

          address_line2: The second line of the address of the check's destination.

          address_city: The city of the check's destination.

          address_state: The state of the check's destination.

          address_zip: The postal code of the check's destination.

          amount: The transfer amount in cents.

          message: The descriptor that will be printed on the check.

          recipient_name: The name that will be printed on the check.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        body: CheckTransferCreateParams,
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
    ) -> CheckTransfer:
        ...

    @required_args(
        ["body"],
        [
            "account_id",
            "address_line1",
            "address_city",
            "address_state",
            "address_zip",
            "amount",
            "message",
            "recipient_name",
        ],
    )
    def create(
        self,
        body: CheckTransferCreateParams | None = None,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        address_line1: str | NotGiven = NOT_GIVEN,
        address_line2: str | NotGiven = NOT_GIVEN,
        address_city: str | NotGiven = NOT_GIVEN,
        address_state: str | NotGiven = NOT_GIVEN,
        address_zip: str | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        recipient_name: str | NotGiven = NOT_GIVEN,
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
    ) -> CheckTransfer:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_id: The identifier for the account that will send the transfer.

          address_line1: The street address of the check's destination.

          address_line2: The second line of the address of the check's destination.

          address_city: The city of the check's destination.

          address_state: The state of the check's destination.

          address_zip: The postal code of the check's destination.

          amount: The transfer amount in cents.

          message: The descriptor that will be printed on the check.

          recipient_name: The name that will be printed on the check.

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
            # with the standard CheckTransferCreateParams type.
            body = cast(
                Any,
                {
                    "account_id": account_id,
                    "address_line1": address_line1,
                    "address_line2": address_line2,
                    "address_city": address_city,
                    "address_state": address_state,
                    "address_zip": address_zip,
                    "amount": amount,
                    "message": message,
                    "recipient_name": recipient_name,
                },
            )

        return self._post(
            "/check_transfers",
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
            cast_to=CheckTransfer,
        )

    def retrieve(
        self,
        check_transfer_id: str,
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
    ) -> CheckTransfer:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/check_transfers/{check_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=CheckTransfer,
        )

    @overload
    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: check_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[CheckTransfer]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Check Transfers to those that originated from the specified Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: CheckTransferListParams = {},
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
    ) -> SyncPage[CheckTransfer]:
        ...

    def list(
        self,
        query: CheckTransferListParams | None = None,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: check_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[CheckTransfer]:
        """
        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Check Transfers to those that originated from the specified Account.

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
            # with the standard CheckTransferListParams type.
            query = cast(
                Any,
                {
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "created_at": created_at,
                },
            )

        return self._get_api_list(
            "/check_transfers",
            page=SyncPage[CheckTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=CheckTransfer,
        )

    def stop_payment(
        self,
        check_transfer_id: str,
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
    ) -> CheckTransfer:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=CheckTransfer,
        )


class AsyncCheckTransfers(AsyncAPIResource):
    @overload
    async def create(
        self,
        *,
        account_id: str,
        address_line1: str,
        address_line2: str | NotGiven = NOT_GIVEN,
        address_city: str,
        address_state: str,
        address_zip: str,
        amount: int,
        message: str,
        recipient_name: str,
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
    ) -> CheckTransfer:
        """
        Args:
          account_id: The identifier for the account that will send the transfer.

          address_line1: The street address of the check's destination.

          address_line2: The second line of the address of the check's destination.

          address_city: The city of the check's destination.

          address_state: The state of the check's destination.

          address_zip: The postal code of the check's destination.

          amount: The transfer amount in cents.

          message: The descriptor that will be printed on the check.

          recipient_name: The name that will be printed on the check.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        body: CheckTransferCreateParams,
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
    ) -> CheckTransfer:
        ...

    @required_args(
        ["body"],
        [
            "account_id",
            "address_line1",
            "address_city",
            "address_state",
            "address_zip",
            "amount",
            "message",
            "recipient_name",
        ],
    )
    async def create(
        self,
        body: CheckTransferCreateParams | None = None,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        address_line1: str | NotGiven = NOT_GIVEN,
        address_line2: str | NotGiven = NOT_GIVEN,
        address_city: str | NotGiven = NOT_GIVEN,
        address_state: str | NotGiven = NOT_GIVEN,
        address_zip: str | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        recipient_name: str | NotGiven = NOT_GIVEN,
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
    ) -> CheckTransfer:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_id: The identifier for the account that will send the transfer.

          address_line1: The street address of the check's destination.

          address_line2: The second line of the address of the check's destination.

          address_city: The city of the check's destination.

          address_state: The state of the check's destination.

          address_zip: The postal code of the check's destination.

          amount: The transfer amount in cents.

          message: The descriptor that will be printed on the check.

          recipient_name: The name that will be printed on the check.

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
            # with the standard CheckTransferCreateParams type.
            body = cast(
                Any,
                {
                    "account_id": account_id,
                    "address_line1": address_line1,
                    "address_line2": address_line2,
                    "address_city": address_city,
                    "address_state": address_state,
                    "address_zip": address_zip,
                    "amount": amount,
                    "message": message,
                    "recipient_name": recipient_name,
                },
            )

        return await self._post(
            "/check_transfers",
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
            cast_to=CheckTransfer,
        )

    async def retrieve(
        self,
        check_transfer_id: str,
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
    ) -> CheckTransfer:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/check_transfers/{check_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=CheckTransfer,
        )

    @overload
    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: check_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[CheckTransfer, AsyncPage[CheckTransfer]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Check Transfers to those that originated from the specified Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: CheckTransferListParams = {},
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
    ) -> AsyncPaginator[CheckTransfer, AsyncPage[CheckTransfer]]:
        ...

    def list(
        self,
        query: CheckTransferListParams | None = None,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: check_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[CheckTransfer, AsyncPage[CheckTransfer]]:
        """
        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Check Transfers to those that originated from the specified Account.

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
            # with the standard CheckTransferListParams type.
            query = cast(
                Any,
                {
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "created_at": created_at,
                },
            )

        return self._get_api_list(
            "/check_transfers",
            page=AsyncPage[CheckTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=CheckTransfer,
        )

    async def stop_payment(
        self,
        check_transfer_id: str,
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
    ) -> CheckTransfer:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._post(
            f"/check_transfers/{check_transfer_id}/stop_payment",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=CheckTransfer,
        )
