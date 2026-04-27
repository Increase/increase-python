# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import lockbox_recipient_list_params, lockbox_recipient_create_params, lockbox_recipient_update_params
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
from ..types.lockbox_recipient import LockboxRecipient

__all__ = ["LockboxRecipientsResource", "AsyncLockboxRecipientsResource"]


class LockboxRecipientsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LockboxRecipientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return LockboxRecipientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LockboxRecipientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return LockboxRecipientsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        lockbox_address_id: str,
        description: str | Omit = omit,
        recipient_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LockboxRecipient:
        """
        Create a Lockbox Recipient

        Args:
          account_id: The Account that checks sent to this Lockbox Recipient should be deposited into.

          lockbox_address_id: The Lockbox Address where this Lockbox Recipient may receive mail.

          description: The description you choose for the Lockbox Recipient.

          recipient_name: The name of the Lockbox Recipient

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/lockbox_recipients",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "lockbox_address_id": lockbox_address_id,
                    "description": description,
                    "recipient_name": recipient_name,
                },
                lockbox_recipient_create_params.LockboxRecipientCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LockboxRecipient,
        )

    def retrieve(
        self,
        lockbox_recipient_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LockboxRecipient:
        """
        Retrieve a Lockbox Recipient

        Args:
          lockbox_recipient_id: The identifier of the Lockbox Recipient to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lockbox_recipient_id:
            raise ValueError(
                f"Expected a non-empty value for `lockbox_recipient_id` but received {lockbox_recipient_id!r}"
            )
        return self._get(
            path_template("/lockbox_recipients/{lockbox_recipient_id}", lockbox_recipient_id=lockbox_recipient_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LockboxRecipient,
        )

    def update(
        self,
        lockbox_recipient_id: str,
        *,
        description: str | Omit = omit,
        recipient_name: str | Omit = omit,
        status: Literal["active", "disabled", "canceled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LockboxRecipient:
        """
        Update a Lockbox Recipient

        Args:
          lockbox_recipient_id: The identifier of the Lockbox Recipient.

          description: The description you choose for the Lockbox Recipient.

          recipient_name: The name of the Lockbox Recipient.

          status: The status of the Lockbox Recipient.

              - `active` - This Lockbox Recipient is active.
              - `disabled` - This Lockbox Recipient is disabled. Checks mailed to this Lockbox
                Recipient will be rejected.
              - `canceled` - This Lockbox Recipient is canceled and cannot be modified. Checks
                mailed to this Lockbox Recipient will be rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not lockbox_recipient_id:
            raise ValueError(
                f"Expected a non-empty value for `lockbox_recipient_id` but received {lockbox_recipient_id!r}"
            )
        return self._patch(
            path_template("/lockbox_recipients/{lockbox_recipient_id}", lockbox_recipient_id=lockbox_recipient_id),
            body=maybe_transform(
                {
                    "description": description,
                    "recipient_name": recipient_name,
                    "status": status,
                },
                lockbox_recipient_update_params.LockboxRecipientUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LockboxRecipient,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: lockbox_recipient_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        lockbox_address_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[LockboxRecipient]:
        """
        List Lockbox Recipients

        Args:
          account_id: Filter Lockbox Recipients to those associated with the provided Account.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          lockbox_address_id: Filter Lockbox Recipients to those associated with the provided Lockbox Address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/lockbox_recipients",
            page=SyncPage[LockboxRecipient],
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
                        "lockbox_address_id": lockbox_address_id,
                    },
                    lockbox_recipient_list_params.LockboxRecipientListParams,
                ),
            ),
            model=LockboxRecipient,
        )


class AsyncLockboxRecipientsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLockboxRecipientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLockboxRecipientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLockboxRecipientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncLockboxRecipientsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        lockbox_address_id: str,
        description: str | Omit = omit,
        recipient_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LockboxRecipient:
        """
        Create a Lockbox Recipient

        Args:
          account_id: The Account that checks sent to this Lockbox Recipient should be deposited into.

          lockbox_address_id: The Lockbox Address where this Lockbox Recipient may receive mail.

          description: The description you choose for the Lockbox Recipient.

          recipient_name: The name of the Lockbox Recipient

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/lockbox_recipients",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "lockbox_address_id": lockbox_address_id,
                    "description": description,
                    "recipient_name": recipient_name,
                },
                lockbox_recipient_create_params.LockboxRecipientCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LockboxRecipient,
        )

    async def retrieve(
        self,
        lockbox_recipient_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LockboxRecipient:
        """
        Retrieve a Lockbox Recipient

        Args:
          lockbox_recipient_id: The identifier of the Lockbox Recipient to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not lockbox_recipient_id:
            raise ValueError(
                f"Expected a non-empty value for `lockbox_recipient_id` but received {lockbox_recipient_id!r}"
            )
        return await self._get(
            path_template("/lockbox_recipients/{lockbox_recipient_id}", lockbox_recipient_id=lockbox_recipient_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LockboxRecipient,
        )

    async def update(
        self,
        lockbox_recipient_id: str,
        *,
        description: str | Omit = omit,
        recipient_name: str | Omit = omit,
        status: Literal["active", "disabled", "canceled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LockboxRecipient:
        """
        Update a Lockbox Recipient

        Args:
          lockbox_recipient_id: The identifier of the Lockbox Recipient.

          description: The description you choose for the Lockbox Recipient.

          recipient_name: The name of the Lockbox Recipient.

          status: The status of the Lockbox Recipient.

              - `active` - This Lockbox Recipient is active.
              - `disabled` - This Lockbox Recipient is disabled. Checks mailed to this Lockbox
                Recipient will be rejected.
              - `canceled` - This Lockbox Recipient is canceled and cannot be modified. Checks
                mailed to this Lockbox Recipient will be rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not lockbox_recipient_id:
            raise ValueError(
                f"Expected a non-empty value for `lockbox_recipient_id` but received {lockbox_recipient_id!r}"
            )
        return await self._patch(
            path_template("/lockbox_recipients/{lockbox_recipient_id}", lockbox_recipient_id=lockbox_recipient_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "recipient_name": recipient_name,
                    "status": status,
                },
                lockbox_recipient_update_params.LockboxRecipientUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LockboxRecipient,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_at: lockbox_recipient_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        lockbox_address_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LockboxRecipient, AsyncPage[LockboxRecipient]]:
        """
        List Lockbox Recipients

        Args:
          account_id: Filter Lockbox Recipients to those associated with the provided Account.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          lockbox_address_id: Filter Lockbox Recipients to those associated with the provided Lockbox Address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/lockbox_recipients",
            page=AsyncPage[LockboxRecipient],
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
                        "lockbox_address_id": lockbox_address_id,
                    },
                    lockbox_recipient_list_params.LockboxRecipientListParams,
                ),
            ),
            model=LockboxRecipient,
        )


class LockboxRecipientsResourceWithRawResponse:
    def __init__(self, lockbox_recipients: LockboxRecipientsResource) -> None:
        self._lockbox_recipients = lockbox_recipients

        self.create = to_raw_response_wrapper(
            lockbox_recipients.create,
        )
        self.retrieve = to_raw_response_wrapper(
            lockbox_recipients.retrieve,
        )
        self.update = to_raw_response_wrapper(
            lockbox_recipients.update,
        )
        self.list = to_raw_response_wrapper(
            lockbox_recipients.list,
        )


class AsyncLockboxRecipientsResourceWithRawResponse:
    def __init__(self, lockbox_recipients: AsyncLockboxRecipientsResource) -> None:
        self._lockbox_recipients = lockbox_recipients

        self.create = async_to_raw_response_wrapper(
            lockbox_recipients.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            lockbox_recipients.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            lockbox_recipients.update,
        )
        self.list = async_to_raw_response_wrapper(
            lockbox_recipients.list,
        )


class LockboxRecipientsResourceWithStreamingResponse:
    def __init__(self, lockbox_recipients: LockboxRecipientsResource) -> None:
        self._lockbox_recipients = lockbox_recipients

        self.create = to_streamed_response_wrapper(
            lockbox_recipients.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            lockbox_recipients.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            lockbox_recipients.update,
        )
        self.list = to_streamed_response_wrapper(
            lockbox_recipients.list,
        )


class AsyncLockboxRecipientsResourceWithStreamingResponse:
    def __init__(self, lockbox_recipients: AsyncLockboxRecipientsResource) -> None:
        self._lockbox_recipients = lockbox_recipients

        self.create = async_to_streamed_response_wrapper(
            lockbox_recipients.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            lockbox_recipients.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            lockbox_recipients.update,
        )
        self.list = async_to_streamed_response_wrapper(
            lockbox_recipients.list,
        )
