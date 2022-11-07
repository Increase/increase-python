# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload

from ..types import wire_transfer_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._utils import required_args
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.wire_transfer import WireTransfer
from ..types.wire_transfer_list_params import WireTransferListParams
from ..types.wire_transfer_create_params import WireTransferCreateParams

__all__ = ["WireTransfers", "AsyncWireTransfers"]


class WireTransfers(SyncAPIResource):
    @overload
    def create(
        self,
        *,
        account_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        amount: int,
        message_to_recipient: str,
        beneficiary_name: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
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
    ) -> WireTransfer:
        """
        Args:
          account_id: The identifier for the account that will send the transfer.

          account_number: The account number for the destination account.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          amount: The transfer amount in cents.

          message_to_recipient: The message that will show on the recipient's bank statement.

          beneficiary_name: The beneficiary's name.

          beneficiary_address_line1: The beneficiary's address line 1.

          beneficiary_address_line2: The beneficiary's address line 2.

          beneficiary_address_line3: The beneficiary's address line 3.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        body: WireTransferCreateParams,
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
    ) -> WireTransfer:
        ...

    @required_args(["body"], ["account_id", "amount", "message_to_recipient"])
    def create(
        self,
        body: WireTransferCreateParams | None = None,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        account_number: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
        message_to_recipient: str | NotGiven = NOT_GIVEN,
        beneficiary_name: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
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
    ) -> WireTransfer:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_id: The identifier for the account that will send the transfer.

          account_number: The account number for the destination account.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          amount: The transfer amount in cents.

          message_to_recipient: The message that will show on the recipient's bank statement.

          beneficiary_name: The beneficiary's name.

          beneficiary_address_line1: The beneficiary's address line 1.

          beneficiary_address_line2: The beneficiary's address line 2.

          beneficiary_address_line3: The beneficiary's address line 3.

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
            # with the standard WireTransferCreateParams type.
            body = cast(
                Any,
                {
                    "account_id": account_id,
                    "account_number": account_number,
                    "routing_number": routing_number,
                    "external_account_id": external_account_id,
                    "amount": amount,
                    "message_to_recipient": message_to_recipient,
                    "beneficiary_name": beneficiary_name,
                    "beneficiary_address_line1": beneficiary_address_line1,
                    "beneficiary_address_line2": beneficiary_address_line2,
                    "beneficiary_address_line3": beneficiary_address_line3,
                },
            )

        return self._post(
            "/wire_transfers",
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/wire_transfers/{wire_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=WireTransfer,
        )

    @overload
    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        created_at: wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[WireTransfer]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Wire Transfers to those belonging to the specified Account.

          external_account_id: Filter Wire Transfers to those made to the specified External Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: WireTransferListParams = {},
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
    ) -> SyncPage[WireTransfer]:
        ...

    def list(
        self,
        query: WireTransferListParams | None = None,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        created_at: wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[WireTransfer]:
        """
        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Wire Transfers to those belonging to the specified Account.

          external_account_id: Filter Wire Transfers to those made to the specified External Account.

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
            # with the standard WireTransferListParams type.
            query = cast(
                Any,
                {
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "external_account_id": external_account_id,
                    "created_at": created_at,
                },
            )

        return self._get_api_list(
            "/wire_transfers",
            page=SyncPage[WireTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=WireTransfer,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        """
        Simulates the reversal of an Wire Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `complete`.
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        """Simulates the submission of a Wire Transfer to the Federal Reserve.

        This
        transfer must first have a `status` of `pending_approval` or `pending_creating`.
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=WireTransfer,
        )


class AsyncWireTransfers(AsyncAPIResource):
    @overload
    async def create(
        self,
        *,
        account_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        amount: int,
        message_to_recipient: str,
        beneficiary_name: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
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
    ) -> WireTransfer:
        """
        Args:
          account_id: The identifier for the account that will send the transfer.

          account_number: The account number for the destination account.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          amount: The transfer amount in cents.

          message_to_recipient: The message that will show on the recipient's bank statement.

          beneficiary_name: The beneficiary's name.

          beneficiary_address_line1: The beneficiary's address line 1.

          beneficiary_address_line2: The beneficiary's address line 2.

          beneficiary_address_line3: The beneficiary's address line 3.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        body: WireTransferCreateParams,
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
    ) -> WireTransfer:
        ...

    @required_args(["body"], ["account_id", "amount", "message_to_recipient"])
    async def create(
        self,
        body: WireTransferCreateParams | None = None,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        account_number: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
        message_to_recipient: str | NotGiven = NOT_GIVEN,
        beneficiary_name: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
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
    ) -> WireTransfer:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_id: The identifier for the account that will send the transfer.

          account_number: The account number for the destination account.

          routing_number: The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
              destination account.

          external_account_id: The ID of an External Account to initiate a transfer to. If this parameter is
              provided, `account_number` and `routing_number` must be absent.

          amount: The transfer amount in cents.

          message_to_recipient: The message that will show on the recipient's bank statement.

          beneficiary_name: The beneficiary's name.

          beneficiary_address_line1: The beneficiary's address line 1.

          beneficiary_address_line2: The beneficiary's address line 2.

          beneficiary_address_line3: The beneficiary's address line 3.

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
            # with the standard WireTransferCreateParams type.
            body = cast(
                Any,
                {
                    "account_id": account_id,
                    "account_number": account_number,
                    "routing_number": routing_number,
                    "external_account_id": external_account_id,
                    "amount": amount,
                    "message_to_recipient": message_to_recipient,
                    "beneficiary_name": beneficiary_name,
                    "beneficiary_address_line1": beneficiary_address_line1,
                    "beneficiary_address_line2": beneficiary_address_line2,
                    "beneficiary_address_line3": beneficiary_address_line3,
                },
            )

        return await self._post(
            "/wire_transfers",
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/wire_transfers/{wire_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=WireTransfer,
        )

    @overload
    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        created_at: wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[WireTransfer, AsyncPage[WireTransfer]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Wire Transfers to those belonging to the specified Account.

          external_account_id: Filter Wire Transfers to those made to the specified External Account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def list(
        self,
        query: WireTransferListParams = {},
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
    ) -> AsyncPaginator[WireTransfer, AsyncPage[WireTransfer]]:
        ...

    def list(
        self,
        query: WireTransferListParams | None = None,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        external_account_id: str | NotGiven = NOT_GIVEN,
        created_at: wire_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[WireTransfer, AsyncPage[WireTransfer]]:
        """
        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Wire Transfers to those belonging to the specified Account.

          external_account_id: Filter Wire Transfers to those made to the specified External Account.

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
            # with the standard WireTransferListParams type.
            query = cast(
                Any,
                {
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "external_account_id": external_account_id,
                    "created_at": created_at,
                },
            )

        return self._get_api_list(
            "/wire_transfers",
            page=AsyncPage[WireTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=WireTransfer,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        """
        Simulates the reversal of an Wire Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `complete`.
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> WireTransfer:
        """Simulates the submission of a Wire Transfer to the Federal Reserve.

        This
        transfer must first have a `status` of `pending_approval` or `pending_creating`.
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=WireTransfer,
        )
