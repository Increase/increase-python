# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import lockbox_list_params, lockbox_create_params, lockbox_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.lockbox import Lockbox

__all__ = ["LockboxesResource", "AsyncLockboxesResource"]


class LockboxesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LockboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return LockboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LockboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return LockboxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        recipient_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Lockbox:
        """
        Create a Lockbox

        Args:
          account_id: The Account checks sent to this Lockbox should be deposited into.

          description: The description you choose for the Lockbox, for display purposes.

          recipient_name: The name of the recipient that will receive mail at this location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/lockboxes",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "description": description,
                    "recipient_name": recipient_name,
                },
                lockbox_create_params.LockboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Lockbox,
        )

    def retrieve(
        self,
        lockbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Lockbox:
        """
        Retrieve a Lockbox

        Args:
          lockbox_id: The identifier of the Lockbox to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lockbox_id:
            raise ValueError(f"Expected a non-empty value for `lockbox_id` but received {lockbox_id!r}")
        return self._get(
            f"/lockboxes/{lockbox_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lockbox,
        )

    def update(
        self,
        lockbox_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        recipient_name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Lockbox:
        """
        Update a Lockbox

        Args:
          lockbox_id: The identifier of the Lockbox.

          description: The description you choose for the Lockbox.

          recipient_name: The recipient name you choose for the Lockbox.

          status: This indicates if checks can be sent to the Lockbox.

              - `active` - This Lockbox is active. Checks mailed to it will be deposited
                automatically.
              - `inactive` - This Lockbox is inactive. Checks mailed to it will not be
                deposited.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not lockbox_id:
            raise ValueError(f"Expected a non-empty value for `lockbox_id` but received {lockbox_id!r}")
        return self._patch(
            f"/lockboxes/{lockbox_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "recipient_name": recipient_name,
                    "status": status,
                },
                lockbox_update_params.LockboxUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Lockbox,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: lockbox_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Lockbox]:
        """
        List Lockboxes

        Args:
          account_id: Filter Lockboxes to those associated with the provided Account.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/lockboxes",
            page=SyncPage[Lockbox],
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
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    lockbox_list_params.LockboxListParams,
                ),
            ),
            model=Lockbox,
        )


class AsyncLockboxesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLockboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLockboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLockboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncLockboxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        recipient_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Lockbox:
        """
        Create a Lockbox

        Args:
          account_id: The Account checks sent to this Lockbox should be deposited into.

          description: The description you choose for the Lockbox, for display purposes.

          recipient_name: The name of the recipient that will receive mail at this location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/lockboxes",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "description": description,
                    "recipient_name": recipient_name,
                },
                lockbox_create_params.LockboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Lockbox,
        )

    async def retrieve(
        self,
        lockbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Lockbox:
        """
        Retrieve a Lockbox

        Args:
          lockbox_id: The identifier of the Lockbox to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lockbox_id:
            raise ValueError(f"Expected a non-empty value for `lockbox_id` but received {lockbox_id!r}")
        return await self._get(
            f"/lockboxes/{lockbox_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lockbox,
        )

    async def update(
        self,
        lockbox_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        recipient_name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Lockbox:
        """
        Update a Lockbox

        Args:
          lockbox_id: The identifier of the Lockbox.

          description: The description you choose for the Lockbox.

          recipient_name: The recipient name you choose for the Lockbox.

          status: This indicates if checks can be sent to the Lockbox.

              - `active` - This Lockbox is active. Checks mailed to it will be deposited
                automatically.
              - `inactive` - This Lockbox is inactive. Checks mailed to it will not be
                deposited.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not lockbox_id:
            raise ValueError(f"Expected a non-empty value for `lockbox_id` but received {lockbox_id!r}")
        return await self._patch(
            f"/lockboxes/{lockbox_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "recipient_name": recipient_name,
                    "status": status,
                },
                lockbox_update_params.LockboxUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Lockbox,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: lockbox_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Lockbox, AsyncPage[Lockbox]]:
        """
        List Lockboxes

        Args:
          account_id: Filter Lockboxes to those associated with the provided Account.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/lockboxes",
            page=AsyncPage[Lockbox],
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
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    lockbox_list_params.LockboxListParams,
                ),
            ),
            model=Lockbox,
        )


class LockboxesResourceWithRawResponse:
    def __init__(self, lockboxes: LockboxesResource) -> None:
        self._lockboxes = lockboxes

        self.create = to_raw_response_wrapper(
            lockboxes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            lockboxes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            lockboxes.update,
        )
        self.list = to_raw_response_wrapper(
            lockboxes.list,
        )


class AsyncLockboxesResourceWithRawResponse:
    def __init__(self, lockboxes: AsyncLockboxesResource) -> None:
        self._lockboxes = lockboxes

        self.create = async_to_raw_response_wrapper(
            lockboxes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            lockboxes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            lockboxes.update,
        )
        self.list = async_to_raw_response_wrapper(
            lockboxes.list,
        )


class LockboxesResourceWithStreamingResponse:
    def __init__(self, lockboxes: LockboxesResource) -> None:
        self._lockboxes = lockboxes

        self.create = to_streamed_response_wrapper(
            lockboxes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            lockboxes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            lockboxes.update,
        )
        self.list = to_streamed_response_wrapper(
            lockboxes.list,
        )


class AsyncLockboxesResourceWithStreamingResponse:
    def __init__(self, lockboxes: AsyncLockboxesResource) -> None:
        self._lockboxes = lockboxes

        self.create = async_to_streamed_response_wrapper(
            lockboxes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            lockboxes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            lockboxes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            lockboxes.list,
        )
