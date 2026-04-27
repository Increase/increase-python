# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import lockbox_address_list_params, lockbox_address_create_params, lockbox_address_update_params
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
from ..types.lockbox_address import LockboxAddress

__all__ = ["LockboxAddressesResource", "AsyncLockboxAddressesResource"]


class LockboxAddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LockboxAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return LockboxAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LockboxAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return LockboxAddressesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LockboxAddress:
        """
        Create a Lockbox Address

        Args:
          description: The description you choose for the Lockbox Address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/lockbox_addresses",
            body=maybe_transform(
                {"description": description}, lockbox_address_create_params.LockboxAddressCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LockboxAddress,
        )

    def retrieve(
        self,
        lockbox_address_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LockboxAddress:
        """
        Retrieve a Lockbox Address

        Args:
          lockbox_address_id: The identifier of the Lockbox Address to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lockbox_address_id:
            raise ValueError(f"Expected a non-empty value for `lockbox_address_id` but received {lockbox_address_id!r}")
        return self._get(
            path_template("/lockbox_addresses/{lockbox_address_id}", lockbox_address_id=lockbox_address_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LockboxAddress,
        )

    def update(
        self,
        lockbox_address_id: str,
        *,
        description: str | Omit = omit,
        status: Literal["active", "disabled", "canceled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LockboxAddress:
        """
        Update a Lockbox Address

        Args:
          lockbox_address_id: The identifier of the Lockbox Address.

          description: The description you choose for the Lockbox Address.

          status: The status of the Lockbox Address.

              - `active` - This Lockbox Address is active.
              - `disabled` - This Lockbox Address is disabled.
              - `canceled` - This Lockbox Address is permanently disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not lockbox_address_id:
            raise ValueError(f"Expected a non-empty value for `lockbox_address_id` but received {lockbox_address_id!r}")
        return self._patch(
            path_template("/lockbox_addresses/{lockbox_address_id}", lockbox_address_id=lockbox_address_id),
            body=maybe_transform(
                {
                    "description": description,
                    "status": status,
                },
                lockbox_address_update_params.LockboxAddressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LockboxAddress,
        )

    def list(
        self,
        *,
        created_at: lockbox_address_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[LockboxAddress]:
        """
        List Lockbox Addresses

        Args:
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
            "/lockbox_addresses",
            page=SyncPage[LockboxAddress],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    lockbox_address_list_params.LockboxAddressListParams,
                ),
            ),
            model=LockboxAddress,
        )


class AsyncLockboxAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLockboxAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLockboxAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLockboxAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncLockboxAddressesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LockboxAddress:
        """
        Create a Lockbox Address

        Args:
          description: The description you choose for the Lockbox Address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/lockbox_addresses",
            body=await async_maybe_transform(
                {"description": description}, lockbox_address_create_params.LockboxAddressCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LockboxAddress,
        )

    async def retrieve(
        self,
        lockbox_address_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LockboxAddress:
        """
        Retrieve a Lockbox Address

        Args:
          lockbox_address_id: The identifier of the Lockbox Address to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lockbox_address_id:
            raise ValueError(f"Expected a non-empty value for `lockbox_address_id` but received {lockbox_address_id!r}")
        return await self._get(
            path_template("/lockbox_addresses/{lockbox_address_id}", lockbox_address_id=lockbox_address_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LockboxAddress,
        )

    async def update(
        self,
        lockbox_address_id: str,
        *,
        description: str | Omit = omit,
        status: Literal["active", "disabled", "canceled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LockboxAddress:
        """
        Update a Lockbox Address

        Args:
          lockbox_address_id: The identifier of the Lockbox Address.

          description: The description you choose for the Lockbox Address.

          status: The status of the Lockbox Address.

              - `active` - This Lockbox Address is active.
              - `disabled` - This Lockbox Address is disabled.
              - `canceled` - This Lockbox Address is permanently disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not lockbox_address_id:
            raise ValueError(f"Expected a non-empty value for `lockbox_address_id` but received {lockbox_address_id!r}")
        return await self._patch(
            path_template("/lockbox_addresses/{lockbox_address_id}", lockbox_address_id=lockbox_address_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "status": status,
                },
                lockbox_address_update_params.LockboxAddressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LockboxAddress,
        )

    def list(
        self,
        *,
        created_at: lockbox_address_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LockboxAddress, AsyncPage[LockboxAddress]]:
        """
        List Lockbox Addresses

        Args:
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
            "/lockbox_addresses",
            page=AsyncPage[LockboxAddress],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    lockbox_address_list_params.LockboxAddressListParams,
                ),
            ),
            model=LockboxAddress,
        )


class LockboxAddressesResourceWithRawResponse:
    def __init__(self, lockbox_addresses: LockboxAddressesResource) -> None:
        self._lockbox_addresses = lockbox_addresses

        self.create = to_raw_response_wrapper(
            lockbox_addresses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            lockbox_addresses.retrieve,
        )
        self.update = to_raw_response_wrapper(
            lockbox_addresses.update,
        )
        self.list = to_raw_response_wrapper(
            lockbox_addresses.list,
        )


class AsyncLockboxAddressesResourceWithRawResponse:
    def __init__(self, lockbox_addresses: AsyncLockboxAddressesResource) -> None:
        self._lockbox_addresses = lockbox_addresses

        self.create = async_to_raw_response_wrapper(
            lockbox_addresses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            lockbox_addresses.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            lockbox_addresses.update,
        )
        self.list = async_to_raw_response_wrapper(
            lockbox_addresses.list,
        )


class LockboxAddressesResourceWithStreamingResponse:
    def __init__(self, lockbox_addresses: LockboxAddressesResource) -> None:
        self._lockbox_addresses = lockbox_addresses

        self.create = to_streamed_response_wrapper(
            lockbox_addresses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            lockbox_addresses.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            lockbox_addresses.update,
        )
        self.list = to_streamed_response_wrapper(
            lockbox_addresses.list,
        )


class AsyncLockboxAddressesResourceWithStreamingResponse:
    def __init__(self, lockbox_addresses: AsyncLockboxAddressesResource) -> None:
        self._lockbox_addresses = lockbox_addresses

        self.create = async_to_streamed_response_wrapper(
            lockbox_addresses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            lockbox_addresses.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            lockbox_addresses.update,
        )
        self.list = async_to_streamed_response_wrapper(
            lockbox_addresses.list,
        )
