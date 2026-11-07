# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import checkbook_list_params, checkbook_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.checkbook import Checkbook

__all__ = ["CheckbooksResource", "AsyncCheckbooksResource"]


class CheckbooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckbooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CheckbooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckbooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CheckbooksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        mailing_address: checkbook_create_params.MailingAddress,
        payer: Iterable[checkbook_create_params.Payer],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Checkbook:
        """
        Create a Checkbook

        Args:
          account_number_id: The identifier of the Account Number that the checks will draw from. The Account
              Number must be active.

          mailing_address: The destination address that the Checkbook will be mailed to.

          payer: The payer of the checks. This will be printed on the top-left corner of each
              check. This should be an array of up to 4 elements, each of which represents a
              line of the payer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/checkbooks",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "mailing_address": mailing_address,
                    "payer": payer,
                },
                checkbook_create_params.CheckbookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Checkbook,
        )

    def retrieve(
        self,
        checkbook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Checkbook:
        """
        Retrieve a Checkbook

        Args:
          checkbook_id: The identifier of the Checkbook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not checkbook_id:
            raise ValueError(f"Expected a non-empty value for `checkbook_id` but received {checkbook_id!r}")
        return self._get(
            path_template("/checkbooks/{checkbook_id}", checkbook_id=checkbook_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Checkbook,
        )

    def list(
        self,
        *,
        account_number_id: str | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: checkbook_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Checkbook]:
        """
        List Checkbooks

        Args:
          account_number_id: Filter Checkbooks to those attached to the specified Account Number.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

              Defaults to `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/checkbooks",
            page=SyncPage[Checkbook],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_number_id": account_number_id,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    checkbook_list_params.CheckbookListParams,
                ),
            ),
            model=Checkbook,
        )

    def stop(
        self,
        checkbook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Checkbook:
        """Stop a Checkbook.

        Stopping a Checkbook stops all of its checks that have not yet
        been deposited.

        Args:
          checkbook_id: The identifier of the Checkbook to stop.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not checkbook_id:
            raise ValueError(f"Expected a non-empty value for `checkbook_id` but received {checkbook_id!r}")
        return self._post(
            path_template("/checkbooks/{checkbook_id}/stop", checkbook_id=checkbook_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Checkbook,
        )


class AsyncCheckbooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckbooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckbooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckbooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCheckbooksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        mailing_address: checkbook_create_params.MailingAddress,
        payer: Iterable[checkbook_create_params.Payer],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Checkbook:
        """
        Create a Checkbook

        Args:
          account_number_id: The identifier of the Account Number that the checks will draw from. The Account
              Number must be active.

          mailing_address: The destination address that the Checkbook will be mailed to.

          payer: The payer of the checks. This will be printed on the top-left corner of each
              check. This should be an array of up to 4 elements, each of which represents a
              line of the payer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/checkbooks",
            body=await async_maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "mailing_address": mailing_address,
                    "payer": payer,
                },
                checkbook_create_params.CheckbookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Checkbook,
        )

    async def retrieve(
        self,
        checkbook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Checkbook:
        """
        Retrieve a Checkbook

        Args:
          checkbook_id: The identifier of the Checkbook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not checkbook_id:
            raise ValueError(f"Expected a non-empty value for `checkbook_id` but received {checkbook_id!r}")
        return await self._get(
            path_template("/checkbooks/{checkbook_id}", checkbook_id=checkbook_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Checkbook,
        )

    def list(
        self,
        *,
        account_number_id: str | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: checkbook_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Checkbook, AsyncPage[Checkbook]]:
        """
        List Checkbooks

        Args:
          account_number_id: Filter Checkbooks to those attached to the specified Account Number.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

              Defaults to `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/checkbooks",
            page=AsyncPage[Checkbook],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_number_id": account_number_id,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    checkbook_list_params.CheckbookListParams,
                ),
            ),
            model=Checkbook,
        )

    async def stop(
        self,
        checkbook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Checkbook:
        """Stop a Checkbook.

        Stopping a Checkbook stops all of its checks that have not yet
        been deposited.

        Args:
          checkbook_id: The identifier of the Checkbook to stop.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not checkbook_id:
            raise ValueError(f"Expected a non-empty value for `checkbook_id` but received {checkbook_id!r}")
        return await self._post(
            path_template("/checkbooks/{checkbook_id}/stop", checkbook_id=checkbook_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Checkbook,
        )


class CheckbooksResourceWithRawResponse:
    def __init__(self, checkbooks: CheckbooksResource) -> None:
        self._checkbooks = checkbooks

        self.create = to_raw_response_wrapper(
            checkbooks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            checkbooks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            checkbooks.list,
        )
        self.stop = to_raw_response_wrapper(
            checkbooks.stop,
        )


class AsyncCheckbooksResourceWithRawResponse:
    def __init__(self, checkbooks: AsyncCheckbooksResource) -> None:
        self._checkbooks = checkbooks

        self.create = async_to_raw_response_wrapper(
            checkbooks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            checkbooks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            checkbooks.list,
        )
        self.stop = async_to_raw_response_wrapper(
            checkbooks.stop,
        )


class CheckbooksResourceWithStreamingResponse:
    def __init__(self, checkbooks: CheckbooksResource) -> None:
        self._checkbooks = checkbooks

        self.create = to_streamed_response_wrapper(
            checkbooks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            checkbooks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            checkbooks.list,
        )
        self.stop = to_streamed_response_wrapper(
            checkbooks.stop,
        )


class AsyncCheckbooksResourceWithStreamingResponse:
    def __init__(self, checkbooks: AsyncCheckbooksResource) -> None:
        self._checkbooks = checkbooks

        self.create = async_to_streamed_response_wrapper(
            checkbooks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            checkbooks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            checkbooks.list,
        )
        self.stop = async_to_streamed_response_wrapper(
            checkbooks.stop,
        )
