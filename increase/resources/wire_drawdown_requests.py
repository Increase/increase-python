# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.wire_drawdown_request import WireDrawdownRequest

__all__ = ["WireDrawdownRequests", "AsyncWireDrawdownRequests"]


class WireDrawdownRequests(SyncAPIResource):
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
        return self._post(
            "/wire_drawdown_requests",
            body={
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
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> WireDrawdownRequest:
        return self._get(
            f"/wire_drawdown_requests/{wire_drawdown_request_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=WireDrawdownRequest,
        )

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
        return self._get_api_list(
            "/wire_drawdown_requests",
            page=SyncPage[WireDrawdownRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                },
            ),
            model=WireDrawdownRequest,
        )


class AsyncWireDrawdownRequests(AsyncAPIResource):
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
        return await self._post(
            "/wire_drawdown_requests",
            body={
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
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> WireDrawdownRequest:
        return await self._get(
            f"/wire_drawdown_requests/{wire_drawdown_request_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=WireDrawdownRequest,
        )

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
        return self._get_api_list(
            "/wire_drawdown_requests",
            page=AsyncPage[WireDrawdownRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                },
            ),
            model=WireDrawdownRequest,
        )
