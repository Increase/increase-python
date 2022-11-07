# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload

from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._utils import required_args
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.wire_drawdown_request import WireDrawdownRequest
from ..types.wire_drawdown_request_list_params import WireDrawdownRequestListParams
from ..types.wire_drawdown_request_create_params import WireDrawdownRequestCreateParams

__all__ = ["WireDrawdownRequests", "AsyncWireDrawdownRequests"]


class WireDrawdownRequests(SyncAPIResource):
    @overload
    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        message_to_recipient: str,
        recipient_account_number: str,
        recipient_routing_number: str,
        recipient_name: str | NotGiven = NOT_GIVEN,
        recipient_address_line1: str | NotGiven = NOT_GIVEN,
        recipient_address_line2: str | NotGiven = NOT_GIVEN,
        recipient_address_line3: str | NotGiven = NOT_GIVEN,
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
    ) -> WireDrawdownRequest:
        """
        Args:
          account_number_id: The Account Number to which the recipient should send funds.

          amount: The amount requested from the recipient, in cents.

          message_to_recipient: A message the recipient will see as part of the request.

          recipient_account_number: The drawdown request's recipient's account number.

          recipient_routing_number: The drawdown request's recipient's routing number.

          recipient_name: The drawdown request's recipient's name.

          recipient_address_line1: Line 1 of the drawdown request's recipient's address.

          recipient_address_line2: Line 2 of the drawdown request's recipient's address.

          recipient_address_line3: Line 3 of the drawdown request's recipient's address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        body: WireDrawdownRequestCreateParams,
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
    ) -> WireDrawdownRequest:
        ...

    @required_args(
        ["body"],
        ["account_number_id", "amount", "message_to_recipient", "recipient_account_number", "recipient_routing_number"],
    )
    def create(
        self,
        body: WireDrawdownRequestCreateParams | None = None,
        *,
        account_number_id: str | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
        message_to_recipient: str | NotGiven = NOT_GIVEN,
        recipient_account_number: str | NotGiven = NOT_GIVEN,
        recipient_routing_number: str | NotGiven = NOT_GIVEN,
        recipient_name: str | NotGiven = NOT_GIVEN,
        recipient_address_line1: str | NotGiven = NOT_GIVEN,
        recipient_address_line2: str | NotGiven = NOT_GIVEN,
        recipient_address_line3: str | NotGiven = NOT_GIVEN,
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
    ) -> WireDrawdownRequest:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_number_id: The Account Number to which the recipient should send funds.

          amount: The amount requested from the recipient, in cents.

          message_to_recipient: A message the recipient will see as part of the request.

          recipient_account_number: The drawdown request's recipient's account number.

          recipient_routing_number: The drawdown request's recipient's routing number.

          recipient_name: The drawdown request's recipient's name.

          recipient_address_line1: Line 1 of the drawdown request's recipient's address.

          recipient_address_line2: Line 2 of the drawdown request's recipient's address.

          recipient_address_line3: Line 3 of the drawdown request's recipient's address.

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
            # with the standard WireDrawdownRequestCreateParams type.
            body = cast(
                Any,
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "message_to_recipient": message_to_recipient,
                    "recipient_account_number": recipient_account_number,
                    "recipient_routing_number": recipient_routing_number,
                    "recipient_name": recipient_name,
                    "recipient_address_line1": recipient_address_line1,
                    "recipient_address_line2": recipient_address_line2,
                    "recipient_address_line3": recipient_address_line3,
                },
            )

        return self._post(
            "/wire_drawdown_requests",
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
            cast_to=WireDrawdownRequest,
        )

    def retrieve(
        self,
        wire_drawdown_request_id: str,
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
    ) -> WireDrawdownRequest:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/wire_drawdown_requests/{wire_drawdown_request_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=WireDrawdownRequest,
        )

    @overload
    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[WireDrawdownRequest]:
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
        query: WireDrawdownRequestListParams = {},
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
    ) -> SyncPage[WireDrawdownRequest]:
        ...

    def list(
        self,
        query: WireDrawdownRequestListParams | None = None,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[WireDrawdownRequest]:
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
            # with the standard WireDrawdownRequestListParams type.
            query = cast(
                Any,
                {
                    "cursor": cursor,
                    "limit": limit,
                },
            )

        return self._get_api_list(
            "/wire_drawdown_requests",
            page=SyncPage[WireDrawdownRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=WireDrawdownRequest,
        )


class AsyncWireDrawdownRequests(AsyncAPIResource):
    @overload
    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        message_to_recipient: str,
        recipient_account_number: str,
        recipient_routing_number: str,
        recipient_name: str | NotGiven = NOT_GIVEN,
        recipient_address_line1: str | NotGiven = NOT_GIVEN,
        recipient_address_line2: str | NotGiven = NOT_GIVEN,
        recipient_address_line3: str | NotGiven = NOT_GIVEN,
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
    ) -> WireDrawdownRequest:
        """
        Args:
          account_number_id: The Account Number to which the recipient should send funds.

          amount: The amount requested from the recipient, in cents.

          message_to_recipient: A message the recipient will see as part of the request.

          recipient_account_number: The drawdown request's recipient's account number.

          recipient_routing_number: The drawdown request's recipient's routing number.

          recipient_name: The drawdown request's recipient's name.

          recipient_address_line1: Line 1 of the drawdown request's recipient's address.

          recipient_address_line2: Line 2 of the drawdown request's recipient's address.

          recipient_address_line3: Line 3 of the drawdown request's recipient's address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        body: WireDrawdownRequestCreateParams,
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
    ) -> WireDrawdownRequest:
        ...

    @required_args(
        ["body"],
        ["account_number_id", "amount", "message_to_recipient", "recipient_account_number", "recipient_routing_number"],
    )
    async def create(
        self,
        body: WireDrawdownRequestCreateParams | None = None,
        *,
        account_number_id: str | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
        message_to_recipient: str | NotGiven = NOT_GIVEN,
        recipient_account_number: str | NotGiven = NOT_GIVEN,
        recipient_routing_number: str | NotGiven = NOT_GIVEN,
        recipient_name: str | NotGiven = NOT_GIVEN,
        recipient_address_line1: str | NotGiven = NOT_GIVEN,
        recipient_address_line2: str | NotGiven = NOT_GIVEN,
        recipient_address_line3: str | NotGiven = NOT_GIVEN,
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
    ) -> WireDrawdownRequest:
        """
        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_number_id: The Account Number to which the recipient should send funds.

          amount: The amount requested from the recipient, in cents.

          message_to_recipient: A message the recipient will see as part of the request.

          recipient_account_number: The drawdown request's recipient's account number.

          recipient_routing_number: The drawdown request's recipient's routing number.

          recipient_name: The drawdown request's recipient's name.

          recipient_address_line1: Line 1 of the drawdown request's recipient's address.

          recipient_address_line2: Line 2 of the drawdown request's recipient's address.

          recipient_address_line3: Line 3 of the drawdown request's recipient's address.

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
            # with the standard WireDrawdownRequestCreateParams type.
            body = cast(
                Any,
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "message_to_recipient": message_to_recipient,
                    "recipient_account_number": recipient_account_number,
                    "recipient_routing_number": recipient_routing_number,
                    "recipient_name": recipient_name,
                    "recipient_address_line1": recipient_address_line1,
                    "recipient_address_line2": recipient_address_line2,
                    "recipient_address_line3": recipient_address_line3,
                },
            )

        return await self._post(
            "/wire_drawdown_requests",
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
            cast_to=WireDrawdownRequest,
        )

    async def retrieve(
        self,
        wire_drawdown_request_id: str,
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
    ) -> WireDrawdownRequest:
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/wire_drawdown_requests/{wire_drawdown_request_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=WireDrawdownRequest,
        )

    @overload
    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[WireDrawdownRequest, AsyncPage[WireDrawdownRequest]]:
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
        query: WireDrawdownRequestListParams = {},
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
    ) -> AsyncPaginator[WireDrawdownRequest, AsyncPage[WireDrawdownRequest]]:
        ...

    def list(
        self,
        query: WireDrawdownRequestListParams | None = None,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[WireDrawdownRequest, AsyncPage[WireDrawdownRequest]]:
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
            # with the standard WireDrawdownRequestListParams type.
            query = cast(
                Any,
                {
                    "cursor": cursor,
                    "limit": limit,
                },
            )

        return self._get_api_list(
            "/wire_drawdown_requests",
            page=AsyncPage[WireDrawdownRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=WireDrawdownRequest,
        )
