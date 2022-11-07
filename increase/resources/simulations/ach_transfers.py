# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload

from ..._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from ..._utils import required_args
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.ach_transfer import ACHTransfer
from ...types.simulations.ach_transfer_simulation import ACHTransferSimulation
from ...types.simulations.ach_transfer_create_inbound_params import (
    ACHTransferCreateInboundParams,
)

__all__ = ["ACHTransfers", "AsyncACHTransfers"]


class ACHTransfers(SyncAPIResource):
    @overload
    def create_inbound(
        self,
        *,
        account_number_id: str,
        amount: int,
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
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        The transfer may be either a
        credit or a debit depending on if the `amount` is positive or negative. This
        will result in either a Transaction or a Declined Transaction depending on if
        the transfer is allowed.

        Args:
          account_number_id: The identifier of the Account Number the inbound ACH Transfer is for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create_inbound(
        self,
        body: ACHTransferCreateInboundParams,
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
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        The transfer may be either a
        credit or a debit depending on if the `amount` is positive or negative. This
        will result in either a Transaction or a Declined Transaction depending on if
        the transfer is allowed.
        """
        ...

    @required_args(["body"], ["account_number_id", "amount"])
    def create_inbound(
        self,
        body: ACHTransferCreateInboundParams | None = None,
        *,
        account_number_id: str | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
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
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        The transfer may be either a
        credit or a debit depending on if the `amount` is positive or negative. This
        will result in either a Transaction or a Declined Transaction depending on if
        the transfer is allowed.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_number_id: The identifier of the Account Number the inbound ACH Transfer is for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

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
            # with the standard ACHTransferCreateInboundParams type.
            body = cast(
                Any,
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                },
            )

        return self._post(
            "/simulations/inbound_ach_transfers",
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
            cast_to=ACHTransferSimulation,
        )

    def return_(
        self,
        ach_transfer_id: str,
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
    ) -> ACHTransfer:
        """
        Simulates the return of an ACH Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `submitted`.
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/return",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=ACHTransfer,
        )

    def submit(
        self,
        ach_transfer_id: str,
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
    ) -> ACHTransfer:
        """Simulates the submission of an ACH Transfer to the Federal Reserve.

        This
        transfer must first have a `status` of `pending_approval` or
        `pending_submission`.
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=ACHTransfer,
        )


class AsyncACHTransfers(AsyncAPIResource):
    @overload
    async def create_inbound(
        self,
        *,
        account_number_id: str,
        amount: int,
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
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        The transfer may be either a
        credit or a debit depending on if the `amount` is positive or negative. This
        will result in either a Transaction or a Declined Transaction depending on if
        the transfer is allowed.

        Args:
          account_number_id: The identifier of the Account Number the inbound ACH Transfer is for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create_inbound(
        self,
        body: ACHTransferCreateInboundParams,
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
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        The transfer may be either a
        credit or a debit depending on if the `amount` is positive or negative. This
        will result in either a Transaction or a Declined Transaction depending on if
        the transfer is allowed.
        """
        ...

    @required_args(["body"], ["account_number_id", "amount"])
    async def create_inbound(
        self,
        body: ACHTransferCreateInboundParams | None = None,
        *,
        account_number_id: str | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
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
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        The transfer may be either a
        credit or a debit depending on if the `amount` is positive or negative. This
        will result in either a Transaction or a Declined Transaction depending on if
        the transfer is allowed.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_number_id: The identifier of the Account Number the inbound ACH Transfer is for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

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
            # with the standard ACHTransferCreateInboundParams type.
            body = cast(
                Any,
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                },
            )

        return await self._post(
            "/simulations/inbound_ach_transfers",
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
            cast_to=ACHTransferSimulation,
        )

    async def return_(
        self,
        ach_transfer_id: str,
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
    ) -> ACHTransfer:
        """
        Simulates the return of an ACH Transfer by the Federal Reserve due to error
        conditions. This will also create a Transaction to account for the returned
        funds. This transfer must first have a `status` of `submitted`.
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/return",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=ACHTransfer,
        )

    async def submit(
        self,
        ach_transfer_id: str,
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
    ) -> ACHTransfer:
        """Simulates the submission of an ACH Transfer to the Federal Reserve.

        This
        transfer must first have a `status` of `pending_approval` or
        `pending_submission`.
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=ACHTransfer,
        )
