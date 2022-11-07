# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload

from ..._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from ..._utils import required_args
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.wire_transfer_simulation import WireTransferSimulation
from ...types.simulations.wire_transfer_create_inbound_params import (
    WireTransferCreateInboundParams,
)

__all__ = ["WireTransfers", "AsyncWireTransfers"]


class WireTransfers(SyncAPIResource):
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
    ) -> WireTransferSimulation:
        """
        Simulates an inbound Wire transfer to your account.

        Args:
          account_number_id: The identifier of the Account Number the inbound Wire Transfer is for.

          amount: The transfer amount in cents. Must be positive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create_inbound(
        self,
        body: WireTransferCreateInboundParams,
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
    ) -> WireTransferSimulation:
        """Simulates an inbound Wire transfer to your account."""
        ...

    @required_args(["body"], ["account_number_id", "amount"])
    def create_inbound(
        self,
        body: WireTransferCreateInboundParams | None = None,
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
    ) -> WireTransferSimulation:
        """
        Simulates an inbound Wire transfer to your account.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_number_id: The identifier of the Account Number the inbound Wire Transfer is for.

          amount: The transfer amount in cents. Must be positive.

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
            # with the standard WireTransferCreateInboundParams type.
            body = cast(
                Any,
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                },
            )

        return self._post(
            "/simulations/inbound_wire_transfers",
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
            cast_to=WireTransferSimulation,
        )


class AsyncWireTransfers(AsyncAPIResource):
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
    ) -> WireTransferSimulation:
        """
        Simulates an inbound Wire transfer to your account.

        Args:
          account_number_id: The identifier of the Account Number the inbound Wire Transfer is for.

          amount: The transfer amount in cents. Must be positive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create_inbound(
        self,
        body: WireTransferCreateInboundParams,
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
    ) -> WireTransferSimulation:
        """Simulates an inbound Wire transfer to your account."""
        ...

    @required_args(["body"], ["account_number_id", "amount"])
    async def create_inbound(
        self,
        body: WireTransferCreateInboundParams | None = None,
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
    ) -> WireTransferSimulation:
        """
        Simulates an inbound Wire transfer to your account.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_number_id: The identifier of the Account Number the inbound Wire Transfer is for.

          amount: The transfer amount in cents. Must be positive.

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
            # with the standard WireTransferCreateInboundParams type.
            body = cast(
                Any,
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                },
            )

        return await self._post(
            "/simulations/inbound_wire_transfers",
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
            cast_to=WireTransferSimulation,
        )
